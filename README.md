# Project name
LibraryManagement

# Project description

*Importance of the project*

LibraryManagement enhances library management by providing a scalable, structured API for book records, ensuring efficient data retrieval and updates. Rate limiting prevents abuse, promoting fair usage and system stability. By following RESTful best practices, the API improves interoperability, making integration with front-end applications seamless. It deepens knowledge of Django REST Framework, API security, and error handling, while reinforcing industry standards like proper versioning, status codes, and request validation. The deployment on PythonAnywhere ensures accessibility, offering a practical foundation for real-world API development.

*What the project does*

The LibraryManagement project develops a RESTful API for managing a library system using Django REST Framework. It includes CRUD operations for books, allowing users to retrieve, add, update, and delete book records. Rate limiting is implemented to prevent abuse, restricting anonymous users to a set number of requests per hour. The API follows RESTful best practices with versioning ('/api/v1/books'), proper status codes, and structured responses. Pagination is applied to large book collections, and headers inform clients about their rate limits. The API is deployed on PythonAnywhere, with thorough documentation and testing via Postman [here](https://web.postman.co/workspace/7f74afd9-ffd7-491f-8597-e00bc0c70881/documentation/41687429-f11da102-d0d2-45fb-871c-d29ff79ac0ac) .

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
   
1. Download Python 3.11 to run the program [here](https://www.python.org/downloads/).
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
        + click on raw data, 
        + select JSON as ghe media type
        + in content box only send the dictionary items you want to update e.g. content {"availability": false} then click PATCH
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

1. Go to your Github repo settings -> Secrets and Variables -> Click on "New repository secret."
1. Copy the production secret key that can be generated with the get_random_secret_key mentioned earlier.

1. Create an [PythonAnyWhere](https://www.pythonanywhere.com/pricing/) account.
1. Choose the Beginner account.
1. Open a Bash console from your PythonAnyWhere Dashboard.
1. Clone the Github repository: `git clone https://github.com/KC-software-en/LibraryManagement.git`
1. Create a virtual environment: `mkvirtualenv --python=/usr/bin/python3.10 LibraryVenv`
    + Note: PythonAnyWhere only has python versions up to 3.10 so use this even though the project used 3.11
    + Note the path to the virtual environment e.g. /home/KCswe/.virtualenvs/LibraryVenv
1. `pip install django`
1. Import all the libraries: `python -m pip install -r requirements.txt`
    + if $ pip install -r requirements.txt gives ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt',
    + `find ~ -name "requirements.txt"`
    + `cd /path/to/your/directory/containing/requirements`
    + try installation again: `python -m pip install -r requirements.txt`

1. Get these 3 pieces of information:
    1. The path to your Django project's top folder (the folder that contains "manage.py"), e.g. /home/KCswe/LibraryManagement
        + Print your current working directory: `pwd`
        + Run:`ls -l`. If manage.py in the output, you're already in the top-level project folder.
    1. The name of your project (that's the name of the folder that contains your settings.py), e.g. LibraryManagement
    1. The name of your virtualenv, e.g. LibraryVenv

1. Go to the web tab to create a web application. 
1. Click on Create a New app.
1. Copy your PythonAnyWhere domain name from the pop-up
1. Select Manual Config.
1. Select Python version 3.10 as it is the highest available (project used 3.11).
1. Configure a WSGI file that imports your app, as a Python variable. You need to know two things:
    1. The path to the Python file containing your web app's WSGI file. e.g. /home/KCswe/LibraryManagement/LibraryManagement
    1. The name of the application. e.g. application = get_wsgi_application()
    1. Follow the WSGI configuration file link under the Code section of the web tab.
    1. Follow instructions to edit the WSGI file, save and reload at the top of the page.
1. Go to console tab
1. Click on bash , 
1. Activate virtual environment: `workon LibraryVenv`    
1. Run migrations in project directory: `python manage.py migrate`

1. Open your app with the link available on your dashboard.

**How to perform CRUD operations**
1. At https://kcswe.pythonanywhere.com/api/v1/books/:
    + GET → list (gets all books)
    + POST → create (creates a new book)

1. At https://kcswe.pythonanywhere.com/api/v1/books/<id>/:
    + GET → retrieve (gets a single book)
    + PUT → update (full update on a book)
        + click on html form
    + PATCH → partial update
        + click on raw data, 
        + select JSON as ghe media type
        + in content box only send the dictionary items you want to update e.g. content {"availability": false} then click PATCH
    + DELETE → destroy the book item    

**Testing API on Postman**    

1. Create a Postman account
1. Download the Postman desktop application
    + or get the Visual Studio Code extension
1. Sign in
1. Follow the instructions on [Postman](https://documenter.getpostman.com/view/41687429/2sAYX3q3FW) published documentation.
1. Paste the endpoint https://kcswe.pythonanywhere.com/api/v1/books/ in Postman to get you started.

# Credits
*Highlights and links to the authors of your project if the project has been created by more than one person*

@KC-software-en https://github.com/KC-software-en

# Add a URL to your GitHub repository
https://github.com/KC-software-en/LibraryManagement

# Add a url to the LibraryManagement website

Postman [documentation](https://documenter.getpostman.com/view/41687429/2sAYX3q3FW)

LibraryManagement was deployed with PythonAnyWhere and is available [here](https://kcswe.pythonanywhere.com/api/v1/books).

# Resources

**Django REST Framework**


**Deploy to PythonAnyWhere**

**Postman**

