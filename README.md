# Project name
LibraryManagement

# Project description

*Importance of the project*

LibraryManagement enhances library management by providing a scalable, structured API for book records, ensuring efficient data retrieval and updates. Rate limiting prevents abuse, promoting fair usage and system stability. By following RESTful best practices, the API improves interoperability, making integration with front-end applications seamless. It deepens knowledge of Django REST Framework, API security, and error handling, while reinforcing industry standards like proper versioning, status codes, and request validation. The deployment on PythonAnywhere ensures accessibility, offering a practical foundation for real-world API development.

*What the project does*

The LibraryManagement project develops a RESTful API for managing a library system using Django REST Framework. It includes CRUD operations for books, allowing users to retrieve, add, update, and delete book records. Rate limiting is implemented to prevent abuse, restricting anonymous users to a set number of requests per hour. The API follows RESTful best practices with versioning ('/api/v1/books'), proper status codes, and structured responses. Pagination is applied to large book collections, and headers inform clients about their rate limits. The API is deployed on PythonAnywhere, with thorough documentation and testing via Postman.

# Installation section
*Tell other users how to install your project locally*

Outline the steps necessary to build and run your application with venv:

1. Open the Command Prompt
1. Create a Virtual Environment:
    + in Command Prompt (powershell)
    + create a folder for new project: `mkdir Library`
    + `cd Library`
    + create virtual env: `virtualenv LibraryVenv --python=python3.11`
    + you will see Scripts in LibraryVenv
    + change to Command Prompt (admin) 
    
1. Activate the Virtual Environment:
    + On Windows (Command Prompt):
        + cd to path to Scripts "C:\Users\path\to\LibraryVenv\Scripts"
        + `activate.bat`
   
1. Download Python 3.11 to run the program @ https://www.python.org/downloads/
1. Run the Python Installer
1. Check the Box for "Add Python to PATH"
In cmd:
1. Verify pip installation: `pip --version`

*Note: Django Secret Key is in the .env*

You will need to set up your custom Secret Key before running the website.

1. Clone this repository
1. In the Command Prompt:
    + Generate a secret key in Python Shell. Run `python` to open the Python Shell. 
    + `from django.core.management.utils import get_random_secret_key`
    + `print(get_random_secret_key())`    
1. Create a `.env` file in the project's root directory with the following content:
    + SECRET_KEY=mysecretkeygoeshere    

1. Install Packages:
    + pip install [package_name]
    
    OR
    + python -m pip install -r requirements.txt

# Usage section
*Instruct others on how to use your project after they’ve installed it*

**Run LibraryManagement on your local server**

In the Command Prompt:
+ Change directory to project root directory

1. Run the command to start the local server: `python manage.py runserver`
1. Go to the [homepage](http://127.0.0.1:8000/api/v1/books).

**How to perform CRUD operations**
1. At api/v1/books/:
    + GET → list (gets all books)
    + POST → create (creates a new book)

1. At api/v1/books/<id>/:
    + GET → retrieve (gets a single book)
    + PUT → update (full update on a book)
        + click on html form
    + PATCH → partial update
        + click on raw data, in content box only send the dictionary items you want to update e.g. content {"availability": false} then click PATCH
    + DELETE → destroy the book item

1. In CMD, stop the server: `CTRL + C`
1. Deactivate the Virtual Environment:
    + `deactivate`

*Include screenshots of your project in action*

![Homepage](screenshots/.png)
![](screenshots/.png)
![](screenshots/.png)
![](screenshots/.png)

**Deploy LibraryManagement to PythonAnyWhere**

1. Create an [PythonAnyWhere](https://www.pythonanywhere.com/pricing/) account.
1. Choose the Beginner account.
1. Open a Bash console from your PythonAnyWhere Dashboard.
1. Clone the Github repository: `git clone https://github.com/KC-software-en/LibraryManagement.git`
1. Create a folder for new project: `mkdir Library`
1. `cd Library`
1. Create virtual environment: `virtualenv LibraryVenv --python=python3.11`
1. Import all the libraries: `python -m pip install -r requirements.txt`
1. Go to your Github repo settings -> Secrets and Variables -> Click on "New repository secret."
1. Copy the production secret key that can be generated with the get_random_secret_key mentioned earlier.

1. Go to the web tab to create a web application. 
1. Click on Create a New app.
1. Select Manual Config.
1. Select Python version.
1. Copy your PythonAnyWhere app name from ...

1. Open your app with the link available on your dashboard.

# Credits
*Highlights and links to the authors of your project if the project has been created by more than one person*

@KC-software-en https://github.com/KC-software-en

# Add a URL to your GitHub repository
https://github.com/KC-software-en/LibraryManagement

# Add a url to the LibraryManagement website

LibraryManagement was deployed with PythonAnyWhere and is available [here]().

# Resources

**Django REST Framework**


**Deploy to PythonAnyWhere**

**Postman**

