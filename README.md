# Recipe Sharing Application

## Overview

This is a full-stack Django application designed for sharing recipes. Users can manage (edit, remove, modify) and share recipes, search and filter recipes using keywords, and keep track of their favorite recipes on a personalized dashboard.

## Features

- **User Accounts and Authentication**: Users can register for an account and log in to access personalized features.
- **Recipe Management**: Users can add, edit, delete, and share their recipes.
- **Search and Filter**: Recipes can be searched using keywords, and filters (e.g., category) can be applied for more specific results.
- **Personalized Dashboard**: Users can view their favorite recipes and manage their personal recipe collections.
- 
## Getting Started

### Prerequisites

- Python 3.10+ (lower versions of Python 3 likely work, but I used 3.10)
- Other dependencies in `requirements.txt`

### Installation

1. Clone the repository:
   ```
   git clone git@github.com:beka-zhvania/recipe-sharing.git
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Migrate the database:
   ```
   python manage.py migrate
   ```
4. Run the development server:
   ```
   python manage.py runserver
   ```

### Usage

After starting the server, by default the application will be available at `http://localhost:8000/`. You can start by registering a new account and then adding your recipes.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

