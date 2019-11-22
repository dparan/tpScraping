const testFolder = 'Corpus_detourage\\html';
const fs = require('fs');
const extractor = require('unfluff');

fs.readdir(testFolder, (err, files) => {
    files.forEach(file => {
        let data = fs.readFileSync(testFolder + '/' + file);
        let content = extractor(data);
        fs.writeFileSync('./uf/' + file, content.text, encoding="utf-8");
    });
});