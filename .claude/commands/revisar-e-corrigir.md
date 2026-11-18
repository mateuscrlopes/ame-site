---
description: Revisa o site da AME com o agente revisor, corrige com o agente corretor e revisa de novo
argument-hint: [páginas, ex.: doe reforca-jacare — vazio = site inteiro]
---

Coordene a revisão e a correção do site da AME para: $ARGUMENTS (se vazio, todas as páginas).

1. Use o agente **revisor** para revisar o escopo e trazer a lista de problemas.
2. Mostre a lista para a pessoa e pergunte se pode corrigir tudo ou só parte. Itens que dependem
   de informação da equipe ou do editor do Wix não vão para o corretor.
3. Use o agente **corretor** para corrigir os itens aprovados, numa branch, e abrir o pull request.
4. Use o **revisor** de novo na branch corrigida. Se ainda houver problema CRÍTICO, volte ao passo 3
   (no máximo duas voltas; depois disso, explique o que travou).
5. Termine com um resumo: o que foi corrigido, o link do pull request, o que falta no Wix e o que
   depende da equipe. Lembre que nada vai ao ar até o pull request ser aprovado.
