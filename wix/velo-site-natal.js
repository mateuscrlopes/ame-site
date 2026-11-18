// ============================================================================
//  CÓDIGO DO VELO · CAMPANHA DE NATAL (código do SITE: masterPage.js)
//  Onde colar: no painel de código, abra "masterPage.js" (código que roda em
//  todas as páginas). Se já houver código lá, cole este no fim, sem apagar o
//  que existe. Se só houver o exemplo do Wix, pode substituir.
//
//  O que faz:
//  1. Abre o pop-up "Campanha de Natal" uma vez por visita, 2,5 s depois de
//     a página carregar (não abre na própria página /natal).
//  2. Controla o card flutuante (bloco com ID cardNatal): leva à página
//     /natal e, se a pessoa fechar, ele some até ela fechar o navegador.
//  3. Depois da data FIM_DA_CAMPANHA, o pop-up para de abrir e o card some.
//
//  ANTES DE COLAR: no pop-up "Campanha de Natal", em "Definir gatilhos",
//  desligue a abertura automática (quem abre agora é este código).
// ============================================================================

import wixWindow from 'wix-window';
import wixLocation from 'wix-location';
import { session } from 'wix-storage';

// EDITAR: último dia da campanha (o pop-up e o card somem a partir desta data)
const FIM_DA_CAMPANHA = new Date('2026-12-26T00:00:00-03:00');
// EDITAR: nome do pop-up no Wix
const NOME_DO_POPUP = 'Campanha de Natal';

$w.onReady(function () {
  const campanhaAtiva = new Date() < FIM_DA_CAMPANHA;
  const naPaginaDoNatal = wixLocation.path[0] === 'natal';

  // Card flutuante
  let card = null;
  try { card = $w('#cardNatal'); } catch (e) { card = null; }
  if (card) {
    if (!campanhaAtiva || naPaginaDoNatal || session.getItem('natalCardFechado')) {
      card.collapse();
    } else {
      card.onMessage(function (evento) {
        const dados = evento.data || {};
        if (dados.tipo === 'natal-abrir') wixLocation.to('/natal');
        if (dados.tipo === 'natal-fechar-card') {
          session.setItem('natalCardFechado', '1');
          card.collapse();
        }
      });
    }
  }

  // Pop-up: uma vez por visita
  if (campanhaAtiva && !naPaginaDoNatal && !session.getItem('natalPopupVisto')) {
    setTimeout(function () {
      session.setItem('natalPopupVisto', '1');
      wixWindow.openLightbox(NOME_DO_POPUP);
    }, 2500);
  }
});
