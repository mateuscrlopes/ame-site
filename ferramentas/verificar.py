#!/usr/bin/env python3
"""
VERIFICAÇÃO AUTOMÁTICA DO SITE DA AME
=====================================
Confere as páginas HTML do repositório com os mesmos critérios usados na
revisão manual. É o "juiz" objetivo dos agentes revisor e corretor.

Como rodar (uma vez: pip install playwright && python -m playwright install chromium):
    python ferramentas/verificar.py              # todas as páginas
    python ferramentas/verificar.py doe inicio   # só algumas

Saída: relatório em Markdown (tela e ferramentas/relatorio-verificacao.md).
Código de saída 1 se houver algum problema CRÍTICO (útil no GitHub Actions).

O que é verificado
  CRÍTICO     conteúdo maior que a altura do bloco no Wix (fica cortado)
  CRÍTICO     rolagem horizontal (algo vaza para os lados)
  CRÍTICO     erro de JavaScript na página
  CRÍTICO     link relativo ou "#secao" sem data-rolar (mostra o endereço do GitHub)
  IMPORTANTE  sobra de mais de 200 px no bloco do Wix (espaço em branco)
  IMPORTANTE  botão ou link com menos de 44 px de altura no celular
  IMPORTANTE  imagem sem atributo alt
  MELHORIA    texto entre [colchetes] visível (pendência de conteúdo)
"""
import asyncio, json, re, sys, functools, threading, http.server, socketserver
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONFIG = json.loads((RAIZ / "ferramentas" / "alturas.json").read_text(encoding="utf-8"))["paginas"]
LARGURAS = {"computador": [980, 1280, 1440, 1920], "celular": [320]}  # o Wix monta o celular com 320 px e só amplia na tela
FOLGA_MAX = 200

def servidor():
    """Serve o repositório em http://127.0.0.1:PORTA para as páginas carregarem como no GitHub Pages."""
    class Silencioso(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    handler = functools.partial(Silencioso, directory=str(RAIZ))
    srv = socketserver.TCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]

MEDIR = r"""() => {
  const main = document.querySelector('main') || document.body;
  const altura = Math.ceil(main.getBoundingClientRect().height);
  const vaza = document.documentElement.scrollWidth > window.innerWidth + 1;
  const linksRuins = [...document.querySelectorAll('a[href]')].filter(a => {
    const h = a.getAttribute('href').trim();
    if (/^(https?:|mailto:|tel:)/i.test(h)) return false;
    if (h.startsWith('#') && (a.hasAttribute('data-rolar') || h === '#')) return false;
    return true;
  }).map(a => (a.textContent || '').trim().slice(0, 40) + ' → ' + a.getAttribute('href'));
  const pequenos = [...document.querySelectorAll('a, button')].filter(e => {
    const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && r.height < 44 && s.visibility !== 'hidden' && !e.closest('.faixa');
  }).map(e => (e.textContent || e.getAttribute('aria-label') || '').trim().slice(0, 30) + ' (' + Math.round(e.getBoundingClientRect().height) + ' px)');
  const semAlt = [...document.querySelectorAll('img')].filter(i => !i.hasAttribute('alt')).map(i => (i.getAttribute('src') || '').slice(-40));
  const texto = (document.body.innerText || '');
  const colchetes = [...new Set((texto.match(/\[[^\]\n]{2,60}\]/g) || []))];
  return {altura, vaza, linksRuins, pequenos, semAlt, colchetes};
}"""

async def verificar(nomes):
    from playwright.async_api import async_playwright
    srv, porta = servidor()
    problemas = []  # (gravidade, página, contexto, descrição)
    def add(g, p, c, d): problemas.append((g, p, c, d))
    async with async_playwright() as pw:
        nav = await pw.chromium.launch()
        for nome in nomes:
            cfg = CONFIG[nome]
            url = f"http://127.0.0.1:{porta}/{cfg['arquivo']}"
            for modo in ("computador", "celular"):
                alvo = cfg.get(modo)
                if alvo is None:
                    continue
                fixa = (cfg.get("largura_fixa") or {}).get(modo)
                larguras = [fixa] if fixa else LARGURAS[modo]
                for w in larguras:
                    altura_janela = alvo if fixa else 900
                    ctx = await nav.new_context(viewport={"width": w, "height": altura_janela},
                                                is_mobile=(modo == "celular"), has_touch=(modo == "celular"))
                    pg = await ctx.new_page()
                    erros = []
                    pg.on("pageerror", lambda e: erros.append(str(e)))
                    await pg.goto(url + ("?celular=0" if nome == "inicio" else ""))
                    await pg.wait_for_timeout(600)
                    m = await pg.evaluate(MEDIR)
                    c = f"{modo} {w}px"
                    if fixa:
                        m["altura"] = await pg.evaluate("Math.ceil(document.documentElement.scrollHeight)")
                    if m["altura"] > alvo:
                        add("CRÍTICO", nome, c, f"conteúdo tem {m['altura']} px e o bloco do Wix tem {alvo} px: o fim fica cortado")
                    elif alvo - m["altura"] > FOLGA_MAX and not fixa and not cfg.get("altura_variavel"):
                        add("IMPORTANTE", nome, c, f"sobram {alvo - m['altura']} px em branco no bloco (conteúdo {m['altura']} px, bloco {alvo} px)")
                    if m["vaza"]:
                        add("CRÍTICO", nome, c, "há rolagem horizontal (algo vaza para os lados)")
                    for e in erros[:3]:
                        add("CRÍTICO", nome, c, f"erro de JavaScript: {e[:120]}")
                    if w == larguras[0]:
                        for l in m["linksRuins"][:5]:
                            add("CRÍTICO", nome, modo, f"link que mostra o endereço do GitHub: {l}")
                        for i in m["semAlt"][:5]:
                            add("IMPORTANTE", nome, modo, f"imagem sem alt: …{i}")
                        if modo == "celular":
                            for b in m["pequenos"][:6]:
                                add("IMPORTANTE", nome, c, f"alvo de toque pequeno: {b}")
                        for t in m["colchetes"][:6]:
                            add("MELHORIA", nome, modo, f"pendência visível: {t}")
                    await ctx.close()
        await nav.close()
    srv.shutdown()
    return problemas

def relatorio(problemas, nomes):
    ordem = {"CRÍTICO": 0, "IMPORTANTE": 1, "MELHORIA": 2}
    vistos, linhas = set(), []
    for g, p, c, d in sorted(problemas, key=lambda x: (ordem[x[0]], x[1], x[2])):
        chave = (g, p, d)
        if chave in vistos and g != "CRÍTICO":
            continue
        vistos.add(chave)
        linhas.append(f"| {g} | {p} | {c} | {d} |")
    criticos = sum(1 for x in problemas if x[0] == "CRÍTICO")
    veredito = "✅ Pode publicar" if criticos == 0 else f"❌ Não publicar: {criticos} problema(s) crítico(s)"
    md = [f"# Verificação do site da AME", "", f"**{veredito}**", "",
          f"Páginas verificadas: {', '.join(nomes)}", ""]
    if linhas:
        md += ["| Gravidade | Página | Onde | Problema |", "|---|---|---|---|"] + linhas
    else:
        md += ["Nenhum problema encontrado."]
    md += ["", "_Não verificado aqui: o site publicado no Wix (altura real dos blocos, âncoras, menu do celular, código do Velo). Confira no celular de verdade._"]
    return "\n".join(md), criticos

if __name__ == "__main__":
    nomes = sys.argv[1:] or list(CONFIG)
    desconhecidas = [n for n in nomes if n not in CONFIG]
    if desconhecidas:
        sys.exit(f"Páginas desconhecidas: {desconhecidas}. Opções: {list(CONFIG)}")
    problemas = asyncio.run(verificar(nomes))
    texto, criticos = relatorio(problemas, nomes)
    (RAIZ / "ferramentas" / "relatorio-verificacao.md").write_text(texto, encoding="utf-8")
    print(texto)
    sys.exit(1 if criticos else 0)
