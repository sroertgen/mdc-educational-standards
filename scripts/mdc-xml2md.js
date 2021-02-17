const xpath = require('xpath');
const { DOMParser } = require('xmldom');
const fs = require('fs');

const myArgs = process.argv.slice(2);
const mdTargetFilename = 'docs/catalog.md';

function getXmlDoc() {
  const catFileName = myArgs[0];
  const xml = fs.readFileSync(catFileName, 'utf8');
  return new DOMParser().parseFromString(xml);
}

function getRootNode(xDoc) {
  return xpath.select('/MDCat', xDoc, true);
}

function getCatLabel(xDoc) {
  return xpath.select('string(//Label)', xDoc, true);
}

console.log('reading xml');
const catXDoc = getXmlDoc();
console.log('writing markdown');
let mdContent = `# IQB Metadatenkatalog "${getCatLabel(catXDoc)}"\n`;
const rootNode = getRootNode(catXDoc);
mdContent += `Version: ${rootNode.getAttribute('version')}\n`;

const mdNodes = xpath.select('//MDDef', catXDoc);
mdNodes.forEach(mdDefNode => {
  const firstLabelNode = xpath.select('Label', mdDefNode, true);
  const id = mdDefNode.getAttribute('id');
  const type = mdDefNode.getAttribute('type');
  mdContent += `## ${firstLabelNode.textContent}\nID: ${id}, Datentyp: ${type}\n`;
  xpath.select('Value', mdDefNode).forEach(valueNode => {
    let valueLabel = xpath.select('string(Label)', valueNode, true);
    valueLabel = valueLabel.replace(/\. /, '\\. ');
    let valueDescription = xpath.select('string(Description)', valueNode, true);
    if (valueDescription.length > 0) {
      valueDescription = ` - ${valueDescription}`;
    }
    mdContent += `* ${valueLabel}${valueDescription}\n`;
  });
});

fs.writeFileSync(mdTargetFilename, mdContent, 'utf8');
console.log('done.');
