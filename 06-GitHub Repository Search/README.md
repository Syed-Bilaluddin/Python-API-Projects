# GitHub Repository Search

A Python command-line application that searches GitHub repositories using the GitHub Search API.

## Features

* Search GitHub repositories using a keyword
* Display the first 5 matching repositories
* Display repository name
* Display repository owner
* Display repository description
* Display star count
* Display repository URL
* Handle searches with no results
* Handles API and connection errors

## Technologies Used

* Python
* Requests
* REST API
* JSON
* Query parameters
* Lists and loops

## API

This project uses the GitHub Search API to search for public repositories.

## Example

```text
Enter repository to search: python calculator

Name: ipcalc
Owner: tehmaze
Description: Python IP Calculator
Stargazers Count: 190
HTML URL: https://github.com/tehmaze/ipcalc

Name: Calculator
Owner: programiz
Description: Source Code for Calculator App
Stargazers Count: 117
HTML URL: https://github.com/programiz/Calculator
```

## What I Learned

* Using query parameters with APIs
* Working with API search endpoints
* Handling JSON dictionaries containing lists
* Accessing nested JSON data
* Looping through search results
* Limiting results using list slicing
* Handling empty search results
* Handling API and connection errors
