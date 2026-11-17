# Site da AME · páginas em HTML

Páginas e blocos do site da **Associação Mais Educação** ([maiseducacao.org](https://www.maiseducacao.org)), hospedados no GitHub Pages e exibidos dentro do Wix.

## Como funciona

1. Cada página ou bloco é um arquivo `index.html` numa pasta deste repositório.
2. O GitHub Pages publica em `https://mateuscrlopes.github.io/ame-site/<pasta>/`.
3. No Wix (Editor clássico), a página recebe um elemento **Incorporar HTML** no modo **endereço do site**, apontando para esse link.
4. Para mudar algo no site, basta editar o arquivo aqui. O Wix mostra a versão nova sozinho, sem precisar colar código de novo.

O menu e o rodapé são os do próprio Wix e ficam fora destes arquivos.

## Mapa das páginas

| Pasta | O que é | Onde fica no Wix | Altura no Wix (computador / celular) |
|---|---|---|---|
| `inicio-celular/` | Página inicial inteira, só para o celular | Página inicial, bloco com ID `inicioCelular`, recolhido ao carregar | — / 7600 px |
| `reforca-jacare/` | Página do projeto Reforça Jacaré | `/reforca-jacare` | 2800 / 4200 px |
| `blocos/como-apoiar/` | Seção Como apoiar (Pix, QR Code, voluntariado, parceria) | Página inicial (computador) | 650 / 1550 px |
| `faixas/topo/` | Faixa animada abaixo do topo | Página inicial (computador) | 48 / 42 px |
| `faixas/apoio-impacto/` | Faixa entre Como apoiar e Nosso impacto | Página inicial (computador) | 48 / 42 px |
| `wix/velo-pagina.js` | Código do Velo (ponte de links) | Código de cada página que tem bloco com links | — |
| `marca/` | Logos e assinaturas dos projetos | — | — |

## Regras importantes

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

- Páginas de Pré-Vestibular, AME Qualifica, Atendimento Jurídico, Transparência e Política de privacidade.
- Dados entre colchetes: dias, horários, documentos de matrícula, carga horária, fonte e período dos números de impacto.
- Depoimentos reais (os atuais são de demonstração).
