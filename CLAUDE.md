# Site da AME · instruções para o Claude Code

Repositório das páginas do site da **Associação Mais Educação (AME)** — https://www.maiseducacao.org.
O Wix hospeda o site; este repositório (GitHub Pages) hospeda o HTML que aparece dentro dos blocos
"Incorporar HTML" do Wix. Tudo que for publicado aqui na branch `main` vai ao ar em ~1 minuto.

## Regras de ouro
1. **Os arquivos HTML deste repositório são a fonte oficial.** Edite-os diretamente. Não existe gerador.
2. **Nunca publique na `main` sem aprovação.** Trabalhe numa branch, abra um pull request e espere a
   pessoa responsável aprovar. Exceção: só se ela pedir explicitamente para publicar direto.
3. **Rode `python ferramentas/verificar.py` antes de propor qualquer mudança.** Nenhum problema
   CRÍTICO pode ficar. Se mudar a altura de uma página, atualize `ferramentas/alturas.json` e avise
   que a altura do bloco no Wix também precisa mudar (o Wix não ajusta sozinho).
4. **Fatos só da lista confirmada** (abaixo). Nada de números, datas ou histórias inventadas.
   Pendências ficam entre `[colchetes]`.
5. **Crianças e dados pessoais:** nada de fotos de crianças sem autorização dos responsáveis,
   nenhum dado pessoal em formulário aberto ou mensagem pública.

## Como as páginas funcionam
- Cada pasta (`inicio/`, `doe/`, `reforca-jacare/`…) tem um `index.html` autossuficiente (CSS e JS no arquivo).
- Comentários `EDITAR` marcam os pontos de edição. Mantenha-os.
- **Links:** todo link deve ter `href` com endereço completo. Links que só rolam a página usam
  `href="https://www.maiseducacao.org/<pagina>#secao"` + `data-rolar="secao"`. Nunca `href="#secao"` sozinho
  (mostra o endereço do GitHub ao passar o mouse).
- A **ponte de links** (bloco `<script>` com `AME_abrirLink`) pede ao código Velo do Wix
  (`wix/velo-pagina.js`) que abra os links. Não remova.
- **Celular:** `inicio/` abre `inicio-celular/` em aparelhos com tela de até 760 px. As demais páginas são responsivas.
- **Alturas dos blocos no Wix:** em `ferramentas/alturas.json`. No computador, o Wix recusa valores
  digitados acima de ~3100 px (arrastar a borda funciona).
- Páginas do GitHub têm `noindex`: o SEO fica nas configurações de cada página do Wix.

## Identidade
Cores: roxo #614998 · ameixa #562568 · amarelo #E8B950 · lilás #E9DDF8 · creme #FCF8F0 · grafite #292530.
Fonte DM Sans. Natal: #26114A, #C9A8FF e Fraunces itálico. Tom próximo, esperançoso, concreto.

## Fatos confirmados
- Associação Mais Educação (AME), Jacaré, Rio de Janeiro, desde 2022. CNPJ/Pix 57.125.059/0001-23.
- R. Conselheiro Mayrink, 339 · Jacaré · RJ · 20960-140. WhatsApp (21) 97718-0459. Instagram @amemaiseducacao.
- Reforça Jacaré (6 a 10 anos): mais de 80 crianças atendidas. AJA (inativo): mais de 10 jovens e adultos.
- AME Qualifica (cozinheiro, montador de móveis) e Pré-Vestibular: em breve. Jurídico: solicitações pelo Google Forms.
- Campanha de Natal 2026 até 26/12/2026 (/natal).
- Prestação de contas publicada: 2023 (fev.–dez.), 2024 (jan.–out.), 2025 (jan.). Não dizer "todo mês".

## O que este repositório NÃO controla (precisa do editor do Wix)
Altura dos blocos, âncoras (posições no computador e no celular), menus, SEO das páginas,
pop-ups e o código Velo colado em cada página. Quando uma mudança aqui exigir algo lá, diga exatamente o quê.

## Agentes
- `revisor` (somente leitura): verifica e devolve a lista de problemas.
- `corretor`: corrige, roda a verificação e prepara o pull request.
- Comando `/revisar-e-corrigir`: coordena os dois.
