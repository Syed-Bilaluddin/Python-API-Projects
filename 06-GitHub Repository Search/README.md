# GitHub Repository Search

A Python application that uses the GitHub REST API to search for repositories by keyword and retrieve repository information.

## Overview

This project demonstrates how to integrate a REST API with Python, send HTTP requests, process JSON responses, and retrieve repository data across multiple pages of results.

## Features

- Search GitHub repositories using a keyword
- Retrieve repository information through the GitHub REST API
- Process API responses in JSON format
- Fetch results across multiple pages using pagination
- Handle unsuccessful HTTP responses
- Stop fetching when no additional results are available

## Technologies Used

- **Language:** Python
- **Library:** Requests
- **API:** GitHub REST API
- **Data Format:** JSON
- **Version Control:** Git and GitHub

## Project Structure

```text
GitHub-Repository-Search/
├── main.py
├── README.md
└── .gitignore
```

*Update the filenames above if your actual project uses a different structure.*

## Requirements

- Python 3.9 or later
- Internet connection
- Python `requests` library

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/Syed-Bilaluddin/Python-API-Projects.git
```

**2. Open the project directory**

```bash
cd Python-API-Projects
```

Navigate to the GitHub Repository Search project folder if it is inside a subdirectory.

**3. Install the dependency**

```bash
python -m pip install requests
```

## Usage

Run the Python script from your terminal:

```bash
python main.py
```

Enter a search keyword when prompted, if your script uses interactive input. The application will request repository data from GitHub and display the results.

## What I Learned

- Making HTTP requests using Python's `requests` library
- Working with REST APIs and JSON responses
- Implementing pagination to retrieve multiple pages of results
- Handling HTTP errors and empty API responses
- Organizing API-related Python code
- Using Git and GitHub for version control

## Future Improvements

- Add more detailed repository information
- Improve command-line input and output
- Add configurable result limits
- Add automated tests
- Improve logging and error reporting

## Author

**Syed Bilaluddin**

- GitHub: [Syed-Bilaluddin](https://github.com/Syed-Bilaluddin)
- Portfolio: [Python & API Development Portfolio](https://docs.google.com/document/d/1tzRQ-D8gOsWUlyhF5B9fQOXDiaufyJsAnuznmXVl9DA/edit?usp=sharing)

---

*Built as a practical project to develop Python programming and REST API integration skills.*