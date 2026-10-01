# Country Information API

A Python command-line application that retrieves information about a country using the REST Countries API.

## Features

* Search for a country by name
* Display country name
* Display region
* Display continent
* Display population
* Display capital
* Display currency
* Display languages
* Handles API and connection errors

## Technologies Used

* Python
* Requests
* REST API
* JSON
* python-dotenv

## API

This project uses the REST Countries API to retrieve country information.

## Security

The API key is stored in a `.env` file instead of being written directly in the Python code.

The `.env` file is excluded from Git using `.gitignore`.

## Example

```text
Enter country name: Pakistan

Country: Pakistan
Region: Asia
Continent: Asia
Population: ...
Capital: Islamabad
Currency: Pakistani rupee
Languages:
Urdu
English
```

## What I Learned

* Sending GET requests with Python
* Working with API headers
* Using environment variables for API keys
* Reading JSON responses
* Working with nested JSON data
* Working with lists and loops
* Handling API and connection errors
