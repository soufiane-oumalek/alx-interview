#!/usr/bin/node

const request = require('request');

const fetchCharacterName = async (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, _, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

const fetchFilmCharacters = async (movieId) => {
  const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
  try {
    const filmData = await new Promise((resolve, reject) => {
      request(filmUrl, (err, _, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });
    const charactersURL = filmData.characters;
    const characterNames = await Promise.all(
      charactersURL.map(async (url) => {
        try {
          return await fetchCharacterName(url);
        } catch (error) {
          throw new Error(`Error fetching character: ${error}`);
        }
      })
    );
    return characterNames;
  } catch (error) {
    throw new Error(`Error fetching film data: ${error}`);
  }
};

const main = async () => {
  try {
    if (process.argv.length <= 2) {
      console.error('Please provide a movie ID as an argument.');
      process.exit(1);
    }
    const movieId = process.argv[2];
    const characterNames = await fetchFilmCharacters(movieId);
    console.log(characterNames.join('\n'));
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
};
