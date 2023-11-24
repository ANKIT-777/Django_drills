# Ipl project

Welcome to the Base project! This is a Django web application that provides solution of IPL project using DJango 

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your machine:

- Python (3.6 or higher)
- Pipenv (optional but recommended for managing virtual environments)

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/ANKIT-777/Django_drills.git
    cd base
    ```

2. Create a virtual environment (if not using Pipenv, you can use `virtualenv` or `venv`):

    ```bash
    pipenv install  # if using Pipenv
    ```

    ```bash
    python -m venv venv  # if using virtualenv or venv
    source venv/bin/activate  # on Linux/Mac
    .\venv\Scripts\activate  # on Windows
    ```

3. Install dependencies:

    ```bash
    pipenv install  # if using Pipenv
    ```

    ```bash
    pip install -r requirements.txt  # if not using Pipenv
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

The app should now be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

Explain how to use the application and any additional setup needed.

### Routes for Calculating Results

#### 1. Number of Matches Played per Year

- **URL:** `/number_of_matches_per_year/`
- **Description:** Returns the number of matches played per year for all the years in IPL.

#### 2. Number of Matches Won per Team per Year

- **URL:** `/number_of_matches_won_per_team_per_year/`
- **Description:** Returns the number of matches won per team per year in IPL.

#### 3. Extra Runs Conceded per Team in 2016

- **URL:** `/extra_runs_conceded_per_team_in_2016/`
- **Description:** Returns the extra runs conceded per team in the year 2016.

#### 4. Top 10 Economical Bowlers in 2015

- **URL:** `/top_10_economical_bowlers_in_2015/`
- **Description:** Returns information about the top 10 economical bowlers in the year 2015.

## Contributing

If you'd like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LIC
