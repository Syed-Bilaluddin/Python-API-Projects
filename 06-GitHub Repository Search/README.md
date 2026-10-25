# GitHub Repository Search

A Python command-line application that searches GitHub repositories using the GitHub REST API, filters results by minimum stars and programming language, groups repositories by their owners, and saves the results to text files.

## Overview

Finding relevant GitHub repositories and identifying developers with multiple projects can be time-consuming. This tool automates the process by fetching repository data, applying filters, sorting results by popularity, grouping repositories by owner, and generating readable reports.

## Features

- Search repositories by keyword
- Filter repositories by minimum star count
- Filter by programming language, or search across all languages
- Fetch up to three pages of results, with up to 30 repositories per page
- Handle API errors, timeouts, connection errors, and rate-limit responses
- Sort filtered repositories by star count in descending order
- Group repositories by their owners
- Generate two text reports automatically
- Identify developers who own multiple matching repositories

## Technologies Used

- **Language:** Python
- **Library:** Requests
- **API:** GitHub REST API
- **Data format:** JSON
- **Output format:** TXT
- **Version control:** Git and GitHub

## How It Works

1. The user enters a repository search keyword.
2. The program requests a minimum star count and an optional programming language.
3. It sends requests to the GitHub repository search endpoint.
4. It retrieves up to three pages of repository results.
5. It filters repositories according to the selected criteria.
6. It sorts the matching repositories by star count.
7. It groups the repositories by developer account.
8. It writes the results into two text files.

## Output Files

The program creates or overwrites the following files in the current working directory each time it reaches the file-writing stage.

### 1. `developers_results.txt`

Contains the developers who own repositories matching the search filters.

For each developer, the report includes:
- Developer username
- GitHub profile URL
- Repository name
- Repository description
- Star count
- Repository URL

Example format:

```text
Owner: octocat
Profile URL: https://github.com/octocat
Repository: example-project
Description: An example project
Stars: 150
Repository URL: https://github.com/octocat/example-project
```

### 2. `developers_with_multiple_repositories.txt`

Contains developers who own more than one repository among the filtered search results.

For each matching developer, the report includes:
- Developer username
- GitHub profile URL
- Number of matching repositories
- Repository names, star counts, and URLs

If no developer has multiple matching repositories, the file records that no such owners were found.

**Important:** These reports are generated from the repositories returned by this search, not from every repository each developer owns on GitHub.

## Requirements

- Python 3.9 or later
- An active internet connection
- The `requests` library

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Syed-Bilaluddin/Python-API-Projects.git
```

### 2. Open the project folder

```bash
cd Python-API-Projects
```

Navigate to the GitHub Repository Search script's directory if it is stored in a subfolder.

### 3. Install the dependency

```bash
python -m pip install requests
```

## How to Run

Execute the Python script from your terminal:

```bash
python main.py
```

Replace `main.py` with your script's actual filename if it differs.

The application will prompt you for:

1. **Search keyword:** The repository topic or term to search for.
2. **Minimum stars:** The minimum number of stars a repository must have.
3. **Programming language:** For example, Python or JavaScript. Press Enter to include all languages.

After processing the results, the program displays the number of repositories before and after filtering, saves the reports, and prints the number of unique developers and developers with multiple matching repositories.

## Error Handling

The application includes handling for:
- Internet connection errors
- Request timeouts
- Other request-related exceptions
- GitHub API rate-limit responses
- Unsuccessful HTTP status codes
- Invalid minimum-star input

## What I Learned

- Integrating Python with a REST API
- Sending HTTP requests with query parameters
- Processing JSON API responses
- Implementing pagination
- Filtering and sorting data
- Using dictionaries to group related records
- Writing structured reports to text files
- Handling exceptions and invalid user input

## Future Improvements

- Add unit tests
- Support configurable result limits
- Improve API rate-limit handling
- Add command-line arguments
- Export reports to JSON or CSV
- Improve logging and error reporting

## Author

**Syed Bilaluddin**

- GitHub: [Syed-Bilaluddin](https://github.com/Syed-Bilaluddin)
- Portfolio: [Python & API Development Portfolio](https://docs.google.com/document/d/1tzRQ-D8gOsWUlyhF5B9fQOXDiaufyJsAnuznmXVl9DA/edit?usp=sharing)

---

*Built to practice Python programming, REST API integration, data filtering, and automation.*
