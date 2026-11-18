// ============================================================================
//  CÓDIGO DO VELO · POP-UP "CAMPANHA DE NATAL"
//  Onde colar: abra o pop-up "Campanha de Natal" no editor e cole este código
//  no painel de código do pop-up (apague o exemplo que vier).
//  O que faz: o botão "Quero apadrinhar" leva à página /natal; o X e o
//  "Agora não" fecham o pop-up.
// ============================================================================

import wixWindow from 'wix-window';
import wixLocation from 'wix-location';

$w.onReady(function () {
  $w('HtmlComponent').forEach(function (bloco) {
    bloco.onMessage(function (evento) {
      const dados = evento.data || {};
      if (dados.tipo === 'natal-abrir') {
        wixLocation.to('/natal');
        wixWindow.lightbox.close();
      } else if (dados.tipo === 'natal-fechar') {
        wixWindow.lightbox.close();
      }
    });
  });
});
