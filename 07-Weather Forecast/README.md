# Weather Application

A Python command-line weather application that retrieves current weather information for a city using a weather API.

## Features

* Search weather by city name
* Display temperature
* Display humidity
* Display wind speed
* Display weather condition
* Handles invalid cities
* Handles API errors
* Handles connection and timeout errors

## Technologies Used

* Python
* Requests
* REST API
* JSON
* API parameters

## API

This project uses a weather API to retrieve current weather information.

The city entered by the user is sent to the API as a request parameter.

## Example

```text
Enter city: Karachi

===== WEATHER =====

City: Karachi
Temperature: 31°C
Humidity: 72%
Wind: 15 km/h
Condition: Clear
```

## Error Handling

The application handles:

* Invalid city names
* API failures
* Connection errors
* Timeout errors
* Missing or invalid API credentials

## Security

The API key is stored separately from the Python source code and should not be uploaded to GitHub.

The `.env` file is excluded using `.gitignore`.

## What I Learned

* Making API requests with Python
* Using query parameters
* Working with API keys
* Reading JSON responses
* Extracting data from API responses
* Handling HTTP status codes
* Handling API and connection errors
* Using environment variables for API credentials
