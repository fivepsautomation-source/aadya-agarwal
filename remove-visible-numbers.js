(function () {
  const textAttributes = ['alt', 'aria-label', 'placeholder', 'title'];
  const excludedElements = new Set(['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE', 'TEXTAREA']);
  const preservedNumberSelectors = '.conference-number, .featured-publication-index';

  function removeNumbers(value) {
    return value
      .replace(/\s*[,;:|·•#]?\s*\d+(?:[.,:/\u2013\u2014-]\d+)*\+?(?:st|nd|rd|th)?/gi, ' ')
      .replace(/^[\s,;:|·•\u2013\u2014-]+|[\s,;:|·•\u2013\u2014-]+$/g, '')
      .replace(/\s+[\u2013\u2014-]\s*(?=[A-Za-z])/g, ' ')
      .replace(/\s+[,;:|·•\u2013\u2014-]+\s+/g, ' ')
      .replace(/\s{2,}/g, ' ');
  }

  function shouldSkip(element) {
    return excludedElements.has(element.tagName)
      || element.isContentEditable
      || element.closest(preservedNumberSelectors);
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
