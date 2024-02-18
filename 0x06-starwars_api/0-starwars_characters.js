#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body);
  const characters = data.characters;
  for (let i = 0; i < characters.length; i++) {
    const url = characters[i];
    request(url, (err, res, body) => {
      if (err) console.log(err);
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
