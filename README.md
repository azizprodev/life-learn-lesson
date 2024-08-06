# LifeLearnLesson
LifeLearnLesson is a web application built with Python, Django, HTML, CSS, and Bootstrap.
This platform allows users to register, log in, and share life lessons or quotes from notable figures
The application features user-specific data management and public display of lessons.

## Features
- **User Registration and Login:** Users can create an account and log in to manage their data.
- **Add Life Lessons:** Logged-in users can add new life lessons or quotes, including the name, quote text, and an image of the person who said the quote.
- **Manage Lessons:** Users can view, edit, or delete their added lessons.
- **Public Display:** The home page displays all life lessons and quotes, visible to all visitors, whether logged in or not.
- **Private Data Management:** Only logged-in users can add, edit, or delete their lessons.
- 
## Installation
- To get started with the LifeLearnLesson project, follow these steps:

## Prerequisites
- Python (>= 3.8)
- pip (Python package installer)
- Django (>= 4.0)

## Clone the Repository
- git clone https://github.com/azizprodev/lifelearnlesson.git
- cd lifelearnlesson

## Set Up a Virtual Environment
- python -m venv .venv
- source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

## Install Dependencies
- pip install -r requirements.txt

## Configure the Database
- python manage.py migrate

## Run the Development Server
- python manage.py runserver

## Usage
- **Register:** Click on the registration link to create an account.
- **Log In:** Use your credentials to log in.
- **Add Lesson:** After logging in, navigate to the "Add Lesson" page to submit new quotes or life lessons.
- **Manage Lessons:** Access the "Manage Lessons" page to view, edit, or delete your entries.
- **Home Page:** The home page displays all submitted lessons and quotes for everyone to see.

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.
Make sure to follow the coding standards and include tests for new features.
