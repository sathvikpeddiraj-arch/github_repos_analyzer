
# GitHub Repository Analyzer

A simple Python project that uses the GitHub REST API to analyze a user's public repositories.

The program retrieves repository information, sorts repositories by star count, filters repositories with more than 10 stars, and exports the results to a CSV file.

## Features

- Fetch public repositories using a GitHub username
- Display repository names, stars, and primary languages
- Sort repositories by stars in descending order
- Filter repositories with more than 10 stars
- Export filtered results to a CSV report
- Handle unsuccessful API responses

## Technologies Used

- Python
- Requests
- GitHub REST API
- CSV module

## Requirements

- Python 3.8 or later
- Internet connection

## Installation

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project folder:

   ```bash
   cd github-repository-analyzer
   ```

3. Install the required package:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:

```bash
python app.py
```

Enter a GitHub username when prompted.

The program displays repositories with more than 10 stars, sorted from highest to lowest, and saves the results to `repositories.csv`.

## Example

```text
Enter GitHub username: octocat

Repository-A | Stars: 120 | Language: Python
Repository-B | Stars: 45 | Language: JavaScript

CSV report saved successfully!
```

*Example output is illustrative.*

## Project Structure

```text
github-repository-analyzer/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Learning Outcomes

This project demonstrates practical use of:

- HTTP GET requests
- REST API responses and JSON
- Python lists and dictionaries
- Sorting and filtering
- CSV file handling
- Basic API error handling

## Future Improvements

- Support automatic pagination
- Allow users to choose the minimum star count
- Export additional repository information
- Improve network error handling

## License

This project is open source and available under the MIT License.
