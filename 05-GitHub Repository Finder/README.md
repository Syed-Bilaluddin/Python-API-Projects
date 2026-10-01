# GitHub Repository Finder

A Python command-line application that retrieves the public repositories of a GitHub user using the GitHub API.

## Features

* Search for a GitHub user by username
* Retrieve the user's repositories
* Display repository names
* Display repository descriptions
* Display repository URLs
* Handle users with no repositories
* Handles API and connection errors

## Technologies Used

* Python
* Requests
* REST API
* JSON
* Lists and loops

## API

This project uses the GitHub REST API to retrieve a user's public repositories.

## Example

```text
Enter Your GitHub Username: octocat

=== GITHUB REPOSITORIES ===

Name: Hello-World
Description: My first repository on GitHub!
Repository URL: https://github.com/octocat/Hello-World
```

## What I Learned

* Working with API endpoints
* Handling JSON lists
* Looping through API results
* Extracting information from multiple JSON objects
* Accessing nested JSON data
* Handling empty results
* Working with API errors
