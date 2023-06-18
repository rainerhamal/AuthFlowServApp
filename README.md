# AuthFlowServApp
 This is a repository containing the code for the AuthFloweServApp, a Django project that implements authentication flow service - user login, roles and permissions.

 <h1>Technologies Used</h1>
 <ul>
  <li>Python 3.11</li>
  <li>pipenv (for managing virtual environments and dependencies</li>
  <li>Django web framework</li>
  <li>crispy-bootstrap5 (to enhance the appearacance of Djnago Forms)</li>
  <li>MySQL Workbench as local database</li>
 </ul>

 <h1>Installation</h1>
 <h3>1</h3>Clone the repository using the following command:
 
git clone https://github.com/rainerhamal/AuthFlowServApp.git

<h3>2</h3>Create a virtual environment and activate it:
pip install pipenv
cd AuthFlowServApp
pipenv install --python 3.11
pipenv shell

<h3>3</h3>Install the project dependencies:

pipenv install django crispy-bootstrap5

<h3>4</h3>Create a MySQL database using MySQL Workbench.
Ensure that MySQL Workbench is installed and running on your local machine.
Create a new MySQL database for the project.

<h3>5</h3>Update the database configuration in the AuthFlowServApp/settings.py file:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


<h3>6</h3>Apply the database migrations:

Open the AuthFlowServApp/settings.py file.
python manage.py migrate

<h3>7</h3>Run the development server:

python manage.py runserver 9000(or any available ports in your machine)

<h3>8</h3>Access the application at http://localhost:9000.

<h1>API Endpoints</h1>
<ul>
    <li>POST /api/signup - Sign up a user with a username, email, and password.</li>
    <li>POST /api/login - Log in a user with a username/email and password.</li>
    <li>POST /api/permissions - Create a new permission.</li>
    <li>GET /api/permissions - Get the available permissions.</li>
    <li>POST /api/roles - Create a new role.</li>
    <li>GET /api/roles - Get the available roles.</li>
    <li>POST /api/roles/:id/permissions - Assign a permission to a role.</li>
    <li>GET /api/roles/:id/permissions - Get the available permissions for a certain role.</li>
    <li>POST /api/users/:id/roles - Add a list of roles to a user.</li>
    <li>GET /api/users/:id/roles - Get the list of roles added to a user.</li>
    <li>GET /api/users/:id/permissions - Get the list of permissions assigned to a user.</li>
</ul>

<h1>Unit Tests</h1>
Unit tests have been written to ensure the functionality of the API services. You can run the tests using the following command:
-python manage.py test

<h1>Usage</h1>
<ul>
 <li>The AuthFlowServApp is an authentication flow service application built with Django.</li>
 <li>It provides registration, login, logout, roles and permission assigning, and password reset functionality.</li>
 <li>Users can create an account, log in with their credentials, and reset their password if necessary.</li>
 <li>The application utilizes the MySQL Workbench database for storing user information.</li>
</ul>

<h1>License</h1>
This project is licensed under the MIT License.

<h1>Acknowledgments</h1>
This project was created by rainerhamal.
