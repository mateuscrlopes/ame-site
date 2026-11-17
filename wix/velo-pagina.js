// =========================================================================
//  CÓDIGO DO VELO · PONTE DE LINKS DOS BLOCOS HTML DA AME
//
//  POR QUE EXISTE: o Wix não deixa um bloco "Incorporar HTML" abrir links
//  (WhatsApp, Atados, outras páginas). O bloco pede, e este código abre.
//
//  COMO INSTALAR (uma vez em cada página que tem bloco com links):
//  1. Ative o Modo Dev no editor.
//  2. No painel de código da página (embaixo), apague o exemplo e cole tudo isto.
//  3. Salve e PUBLIQUE. Teste no site publicado (no editor ele não roda).
//
//  Não precisa descobrir o ID dos blocos: o código encontra sozinho todos
//  os blocos HTML da página. A única exceção é o bloco da página inicial
//  para celular: dê a ele o ID inicioCelular (painel Propriedades e eventos).
// =========================================================================

import wixLocation from 'wix-location';
import wixWindow from 'wix-window';

// Só abre endereços destes sites (segurança)
const PERMITIDOS = /^https:\/\/(wa\.me|api\.whatsapp\.com|(www\.)?atados\.com\.br|(www\.)?maiseducacao\.org|(www\.)?instagram\.com)(\/|$)/;

// Página inicial: bloco que só aparece no celular (ID definido no painel
// "Propriedades e eventos"). Em outras páginas, esta parte não faz nada.
const BLOCO_SO_CELULAR = '#inicioCelular';

$w.onReady(function () {
  try {
    const blocoCelular = $w(BLOCO_SO_CELULAR);
    if (blocoCelular && blocoCelular.expand) {
      if (wixWindow.formFactor === 'Mobile') blocoCelular.expand();
      else blocoCelular.collapse();
    }
  } catch (e) { /* esta página não tem o bloco do celular */ }

  const encontrados = $w('HtmlComponent');                      // todos os blocos HTML da página
  const blocos = Array.isArray(encontrados) ? encontrados : [encontrados];
  blocos.forEach(function (bloco) {
    bloco.onMessage(function (evento) {
      const dados = evento.data;
      if (!dados) return;
      // Rolar a página até um ponto do bloco
      if (dados.tipo === 'ame-rolar' && typeof dados.y === 'number') {
        bloco.postMessage({ tipo: 'ame-rolar-ok' });
        bloco.scrollTo().then(function () { return wixWindow.scrollBy(0, dados.y); });
        return;
      }
      // Abrir um link
      if (dados.tipo !== 'ame-abrir-link' || typeof dados.url !== 'string') return;
      if (!PERMITIDOS.test(dados.url)) return;
      bloco.postMessage({ tipo: 'ame-link-ok' });               // avisa o bloco que deu certo
      wixLocation.to(dados.url);
    });
  });
});
