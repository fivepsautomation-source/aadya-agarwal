(function () {
  const textAttributes = ['alt', 'aria-label', 'placeholder', 'title'];
  const excludedElements = new Set(['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE', 'TEXTAREA', 'FOOTER']);
  const preservedNumberSelectors = '.conference-number, .featured-publication-index, footer, .site-footer, .preserve-numbers, [data-cms]';

  const tokenWords = ['FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH'];

  function removeNumbers(value) {
    const preserved = [];
    const protectedVal = value.replace(/\bClass\s+of\s+\d{4}\b/gi, (match) => {
      const idx = preserved.length;
      preserved.push(match);
      const token = tokenWords[idx] || `TOKEN_${idx}`;
      return `__PRESERVED_CLASS_${token}__`;
    });

    let cleaned = protectedVal
      .replace(/\s*[,;:|·•#]?\s*\d+(?:[.,:/\u2013\u2014-]\d+)*\+?(?:st|nd|rd|th)?/gi, ' ')
      .replace(/^[\s,;:|·•\u2013\u2014-]+|[\s,;:|·•\u2013\u2014-]+$/g, '')
      .replace(/\s+[\u2013\u2014-]\s*(?=[A-Za-z])/g, ' ')
      .replace(/\s+[,;:|·•\u2013\u2014-]+\s+/g, ' ')
      .replace(/\s{2,}/g, ' ');

    preserved.forEach((p, i) => {
      const token = tokenWords[i] || `TOKEN_${i}`;
      cleaned = cleaned.replace(`__PRESERVED_CLASS_${token}__`, p);
    });

    return cleaned;
  }

  function shouldSkip(element) {
    return excludedElements.has(element.tagName)
      || element.isContentEditable
      || (element.closest && element.closest(preservedNumberSelectors));
  }

  function processNode(node) {
    if (node.nodeType === Node.TEXT_NODE) {
      if (node.parentElement && !shouldSkip(node.parentElement)) {
        const cleaned = removeNumbers(node.nodeValue);
        if (cleaned !== node.nodeValue) node.nodeValue = cleaned;
      }
      return;
    }

    if (node.nodeType !== Node.ELEMENT_NODE || shouldSkip(node)) return;

    textAttributes.forEach(attribute => {
      if (node.hasAttribute(attribute)) {
        const value = node.getAttribute(attribute);
        const cleaned = removeNumbers(value);
        if (cleaned !== value) node.setAttribute(attribute, cleaned);
      }
    });

    node.childNodes.forEach(processNode);
  }

  function start() {
    if (document.title) document.title = removeNumbers(document.title);
    processNode(document.body);

    const observer = new MutationObserver(records => {
      records.forEach(record => {
        if (record.type === 'characterData') {
          processNode(record.target);
        } else if (record.type === 'attributes') {
          processNode(record.target);
        } else {
          record.addedNodes.forEach(processNode);
        }
      });
    });

    observer.observe(document.body, {
      subtree: true,
      childList: true,
      characterData: true,
      attributes: true,
      attributeFilter: textAttributes
    });
    observer.observe(document.head, {
      subtree: true,
      childList: true,
      characterData: true
    });
  }

  if (document.body) {
    start();
  } else {
    document.addEventListener('DOMContentLoaded', start, { once: true });
  }
})();
