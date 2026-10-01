# Python API Projects

A collection of Python projects built while learning and practicing REST APIs, HTTP requests, JSON, query parameters, and API error handling.

## Projects

### 01 — Currency Converter

A command-line currency converter that uses an exchange-rate API to convert an amount from one currency to another.

**Concepts practiced:**

* API requests
* HTTP GET requests
* Query/path parameters
* JSON responses
* Status codes
* User input
* Exception handling

---

### 02 — Random Quote Generator

A command-line application that retrieves a random quote from an online API.

**Concepts practiced:**

* GET requests
* JSON data
* Lists and dictionaries
* API response handling
* Exception handling

---

### 03 — Country Information

A command-line application that retrieves information about a country using an API.

**Displays:**

* Country name
* Capital
* Population
* Currency
* Languages
* Region

**Concepts practiced:**

* API requests
* JSON
* Nested JSON data
* User input
* Status codes
* Exception handling

---

### 04 — GitHub Profile Finder

A command-line application that retrieves information about a GitHub user.

**Displays:**

* Username
* Followers
* Following
* Public repositories
* Profile URL

**Concepts practiced:**

* API requests
* Path parameters
* JSON
* User input
* Status codes
* Exception handling

---

### 05 — GitHub Repository Finder

A command-line application that retrieves the public repositories of a GitHub user.

**Displays:**

* Repository name
* Description
* Repository URL

**Concepts practiced:**

* GET requests
* Path parameters
* JSON lists
* Dictionaries
* Loops
* Nested JSON
* Exception handling

---

### 06 — GitHub Repository Search

A command-line application that searches GitHub repositories using a search term.

**Displays:**

* Repository name
* Owner
* Description
* Stargazers count
* Repository URL

The application displays the first five matching repositories.

**Concepts practiced:**

* Query parameters
* API search endpoints
* JSON lists
* Nested JSON
* Loops
* Empty-result handling
* Exception handling

---

### 07 — Weather Forecast

A command-line weather application that retrieves weather information for a specified location using a weather API.

**Displays:**

* City
* Temperature
* Humidity
* Wind
* Weather condition

**Concepts practiced:**

* API requests
* Query parameters
* JSON
* API keys
* Status codes
* Error handling
* User input

---

## API Concepts Practiced

Throughout these projects, I practiced:

* REST APIs
* HTTP requests
* GET requests
* Request parameters
* Path parameters
* Query parameters
* JSON
* JSON lists and dictionaries
* Nested JSON
* HTTP status codes
* API error handling
* Connection errors
* Timeout handling
* User input
* Loops and data extraction

## Technologies

* Python
* `requests`
* REST APIs
* JSON

## Purpose

These projects were built as part of my Python learning journey to develop practical experience working with APIs and external services.

They represent my progression from basic API requests to working with parameters, nested JSON, lists, loops, and API search functionality.

## Project Status

* [x] Currency Converter
* [x] Random Quote Generator
* [x] Country Information
* [x] GitHub Profile Finder
* [x] GitHub Repository Finder
* [x] GitHub Repository Search
* [x] Weather Forecast

## Setup & Run

### Requirements

* Python 3.x
* `requests` library
* Internet connection

### Install Dependencies

Install the required Python package:

```bash
pip install requests
```

### Run a Project

Navigate to the project's folder and run the Python file.

Example:

```bash
py currencyconverterapi.py
```

Each project has its own `README.md` with information about its purpose, features, and concepts practiced.

### API Keys

Some APIs may require an API key.

API keys should **not** be uploaded to GitHub. Store them securely and use environment variables or a `.env` file when required.
