const fs = require('fs');
const cheerio = require('cheerio')
const got = require('got');

const url = 'https://docquery.fec.gov/cgi-bin/forms/C00703975/1379721/sa/ALL'

got(url).then(response =>{
    const $ = cheerio.load(response.body);
    var blocks = $('tbody.tablebody reportTable');
    console.log(blocks.find('tr').length)
}).catch(err=>{
    console.log("error");
})