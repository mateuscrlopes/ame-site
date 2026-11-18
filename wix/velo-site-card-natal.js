// ============================================================================
//  CÓDIGO DO VELO · CARD FLUTUANTE DA CAMPANHA DE NATAL (masterPage.js)
//  Roda em todas as páginas. Controla o card do canto (bloco com ID cardNatal):
//  - clique no card: vai para a página /natal;
//  - X do card: esconde o card até a pessoa fechar o navegador;
//  - não aparece na própria página /natal nem depois de FIM_DA_CAMPANHA.
//  O pop-up "Natal 2026" continua sendo aberto pelas configurações do Wix.
// ============================================================================

import wixLocation from 'wix-location';
import { session } from 'wix-storage';

// EDITAR: a partir desta data o card some sozinho
const FIM_DA_CAMPANHA = new Date('2026-12-26T00:00:00-03:00');

$w.onReady(function () {
  let card = null;
  try { card = $w('#cardNatal'); } catch (e) { card = null; }
  if (!card || typeof card.onMessage !== 'function') return;

  const campanhaAtiva = new Date() < FIM_DA_CAMPANHA;
  const naPaginaDoNatal = wixLocation.path[0] === 'natal';

  if (!campanhaAtiva || naPaginaDoNatal || session.getItem('natalCardFechado')) {
    card.collapse();
    return;
  }

  card.onMessage(function (evento) {
    const dados = evento.data || {};
    if (dados.tipo === 'natal-abrir') {
      wixLocation.to('/natal');
    } else if (dados.tipo === 'natal-fechar-card') {
      session.setItem('natalCardFechado', '1');
      card.collapse();
    }
  });
});
