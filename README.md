# Site da AME · páginas em HTML

Páginas e blocos do site da **Associação Mais Educação** ([maiseducacao.org](https://www.maiseducacao.org)), hospedados no GitHub Pages e exibidos dentro do Wix.

## Como funciona

1. Cada página ou bloco é um arquivo `index.html` numa pasta deste repositório.
2. O GitHub Pages publica em `https://mateuscrlopes.github.io/ame-site/<pasta>/`.
3. No Wix (Editor clássico), a página recebe um elemento **Incorporar HTML** no modo **endereço do site**, apontando para esse link.
4. Para mudar algo no site, basta editar o arquivo aqui. O Wix mostra a versão nova sozinho, sem precisar colar código de novo.

O menu e o rodapé são os do próprio Wix e ficam fora destes arquivos.


## Trabalhando com o Claude Code (revisão e correção automáticas)

Abra esta pasta no Claude Code (Claude Desktop → Code, ou terminal) e use:

- **`/revisar-e-corrigir`** — o agente **revisor** confere o site, você aprova o que corrigir,
  o agente **corretor** corrige numa branch e abre um pull request, e o revisor confere de novo.
  Ex.: `/revisar-e-corrigir doe reforca-jacare` (vazio = site inteiro).
- **`python ferramentas/verificar.py`** — a verificação objetiva usada pelos dois agentes
  (alturas x blocos do Wix, nada vazando para os lados, erros, links que mostram o GitHub,
  alvos de toque no celular, imagens sem alt, pendências entre colchetes).
- **`ferramentas/alturas.json`** — alturas dos blocos no Wix. Mudou no Wix? Atualize aqui.
- **`CLAUDE.md`** — regras do repositório que o Claude Code lê sozinho.

Nada vai ao ar sem o pull request ser aprovado.

**Verificação automática no GitHub (a ativar):** `ferramentas/verificacao.yml` roda a verificação a cada
mudança e toda segunda-feira e, se algo crítico quebrar, abre um issue com o relatório. Para ativar,
mova o arquivo para `.github/workflows/` (peça ao Claude Code: "ative a verificação automática do GitHub").

## Mapa das páginas

| Pasta | O que é | Onde fica no Wix | Altura no Wix (computador / celular) |
|---|---|---|---|
| `inicio/` | Página inicial (computador). Em celulares, abre sozinha a versão de celular (`inicio-celular/`) | Página Início | 3100 (limite do Wix) / ver celular |
| `inicio-celular/` | Página inicial, versão de celular: topo, faixa, quem somos, projetos, como ajudar, impacto e contato | Aberta pela página inicial em celulares | — / 3350 px |
| `reforca-jacare/` | Página do projeto Reforça Jacaré | `/reforca-jacare` | 2800 / 3850 px |
| `pre-vestibular/` | Página do Pré-Vestibular AME | `/pre-vestibular` | 2600 / 3620 px |
| `ame-qualifica/` | Página do AME Qualifica | `/ame-qualifica` | 2650 / 3750 px |
| `atendimento-juridico/` | Página do Atendimento Jurídico AME (solicitação pelo Google Forms) | `/atendimento-juridico` | 2700 / 4000 px |
| `blocos/como-apoiar/` | Seção Como apoiar (Pix, QR Code, voluntariado, parceria) | Página inicial (computador) | 650 / 1550 px |
| `faixas/topo/` | Faixa animada abaixo do topo | Página inicial (computador) | 48 / 42 px |
| `faixas/apoio-impacto/` | Faixa entre Como apoiar e Nosso impacto | Página inicial (computador) | 48 / 42 px |
| `doe/` | Página de doação: Pix (chave, QR Code e copia e cola), transparência e outras formas de ajudar | `/doe` | 1450 / 2650 px |
| `links/` | Página de links da bio do Instagram (estilo Linktree): destaques, projetos, como ajudar e contato | `/links` (fora do menu) | 1430 / 1570 px |
| `prestacao-de-contas/` | Prestação de contas: 2023, 2024 e 2025 numa página só, com abas por ano | `/prestacao-de-contas` | 1450 / 1900 px |
| `natal/popup/` | Pop-up da campanha de Natal (dentro do pop-up do Wix) | Pop-up "Natal 2026" | 800 × 440 / 300 × 540 px |
| `natal/card/` | Card flutuante da campanha de Natal, no canto da tela | Todas as páginas, ID `cardNatal` | 320 × 104 / 300 × 92 px |
| `wix/velo-popup-natal.js` | Código do Velo do pop-up de Natal (fechar e ir para /natal) | Código do pop-up | — |
| `wix/velo-site-card-natal.js` | Código do Velo do site (masterPage.js) que está em uso: só controla o card de Natal (o pop-up abre pelas configurações do Wix) | masterPage.js | — |
| `wix/velo-site-natal.js` | Código do Velo do site (masterPage.js): abre o pop-up uma vez por visita e controla o card | masterPage.js | — |
| `wix/velo-pagina.js` | Código do Velo (ponte de links) | Código de cada página que tem bloco com links | — |
| `marca/` | Logos e assinaturas dos projetos | — | — |

## Regras importantes

- **Links que só rolam a página:** use o endereço do site no href e o id da seção em data-rolar, por exemplo `<a href="https://www.maiseducacao.org/#apoiar" data-rolar="apoiar">`. Assim, ao passar o mouse, aparece o endereço da AME, e não o do GitHub.

- **Limite do Wix:** no computador, um bloco incorporado não passa de 3100 px de altura. Páginas maiores que isso precisam ser divididas em partes (veja a página inicial).

- **Links e WhatsApp passam pela ponte do Velo.** O Wix não deixa um bloco incorporado abrir links sozinho. O bloco avisa a página, e o código `wix/velo-pagina.js` abre o link. Ele precisa estar colado no código de cada página que tem bloco com links (Modo Dev). No celular, o WhatsApp abre direto no aplicativo.
- **Comentários `EDITAR`.** Cada arquivo tem comentários indicando o que pode ser trocado. Textos entre colchetes `[ ]` são informações a confirmar.
- **Alturas fixas.** O bloco do Wix tem altura fixa. Se o conteúdo crescer, aumente a altura no editor (computador e celular separadamente).
- **Sem indexação.** As páginas têm `noindex`: quem deve aparecer no Google é o maiseducacao.org. Preencha o título e a descrição de SEO de cada página no próprio Wix.
- **Fotos.** Só imagens com autorização de uso, com cuidado redobrado com crianças e adolescentes (LGPD e ECA).
- **Dados pessoais.** Os formulários não guardam nada: montam a mensagem e abrem o WhatsApp da AME.

## Identidade visual

- Cores: roxo `#614998`, ameixa `#562568`, amarelo `#E8B950`, lilás `#E9DDF8`, creme `#FCF8F0`, grafite `#292530`.
- Projetos: Reforça Jacaré `#E8B950` (texto grafite), Pré-Vestibular `#3E64B0`, Qualifica `#BF5236`, Jurídico `#2E7D73`.
- Fonte: DM Sans. Títulos leves com a última palavra em negrito roxo, como na página inicial.
- Design System completo: https://claude.ai/artifact/3pNSzzgB74jfeiA44hAnMD

## Pendências

- Criar no Wix as páginas de Pré-Vestibular, AME Qualifica e Atendimento Jurídico (os arquivos já estão aqui).
- Política de privacidade.
- Prestação de contas: faltam novembro e dezembro de 2024, fevereiro a dezembro de 2025 e todo 2026. Para publicar um mês novo, veja as instruções no topo de `prestacao-de-contas/index.html`.
- AJA e Atendimento AME (apoio psicanalítico) estão inativos: as páginas antigas continuam ocultas no Wix.
- Dados entre colchetes: dias, horários, documentos de matrícula, carga horária, fonte e período dos números de impacto.
- Depoimentos reais (os atuais são de demonstração).
