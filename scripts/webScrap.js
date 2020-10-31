const fs = require('fs');
const cheerio = require('cheerio')
const got = require('got');

const url = 'https://docquery.fec.gov/cgi-bin/forms/C00703975/1379721/sa/ALL'

got(url).then(response =>{
    const $ = cheerio.load(response.body);
    console.log($('tbody').text())
}).catch(err=>{
    console.log("error");
})