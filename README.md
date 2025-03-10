# Salary Predictor App

## Overview
The **Salary Predictor App** is a Python-based application that allows users to estimate the average monthly salary for a given job skill using data from **HeadHunter API**. The app fetches job vacancy data, processes salary information, and provides statistical insights into salary ranges.

## Features
- Fetches job vacancy data from the [HeadHunter API](https://api.hh.ru/vacancies).
- Analyzes salaries in **RUR (Russian Rubles)**.
- Computes key salary statistics:
  - Total number of vacancies found.
  - Number of vacancies with salary data.
  - Minimum and maximum salary.
  - Average salary.
- Allows users to input a skill and retrieve salary insights.

## Installation

### Prerequisites
Ensure you have Python installed (Python 3.x recommended). If not, download and install it from [Python.org](https://www.python.org/downloads/).

### Setup
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/salary-predictor.git
   cd salary-predictor
   ```
2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script to analyze salaries based on the chosen job skill:

```sh
python salary_predictor.py
```

The script will prompt you to enter a skill (e.g., "Python Developer") and then fetch salary data from the HeadHunter API.

## Code Structure

### `get_salary(skills, page)`
- **Parameters**:
  - `skills` (str): The job skill to search for.
  - `page` (int): The page number of results.
- **Returns**:
  - `count_vacancies` (int): Number of vacancies found on that page.
  - `salary_list` (list): List of salary values.
- **Description**: This function retrieves job vacancy data from the HeadHunter API, extracts salary information, and filters only relevant data.

### `get_statistic()`
- **Returns**:
  - A list containing:
    - Total vacancies found.
    - Vacancies with salary data.
    - Minimum salary.
    - Maximum salary.
    - Average salary.
- **Description**: Calls `get_salary()` across multiple pages, aggregates data, and computes salary statistics.

## Example Output
```
write which job are you finding: Data Scientist
[500, 320, 80000, 250000, 145000]
```
**Explanation:**
- `500`: Total vacancies found.
- `320`: Vacancies with salary data.
- `80000`: Minimum salary.
- `250000`: Maximum salary.
- `145000`: Average salary.

## API Reference
- **Base URL:** `https://api.hh.ru/vacancies`
- **Parameters:**
  - `text`: Search query (job skill)
  - `per_page`: Number of vacancies per request (default: 100)
  - `page`: Page number

## Contributing
Contributions are welcome! If you have improvements or bug fixes, feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by [Your Name](https://github.com/yourusername).

