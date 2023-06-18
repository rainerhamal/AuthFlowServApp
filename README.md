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

<h3>2</h3>Navigate to the project directory:
cd AuthFlowServApp

<h3>3</h3>Create a virtual environment and activate it using pipenv:

pipenv install
pipenv shell

<h3>4</h3>Install the project dependencies:

pipenv install django crispy-bootstrap5

<h3>5</h3>Set up the local database:

Ensure that MySQL Workbench is installed and running on your local machine.
Create a new MySQL database for the project.

<h3>6</h3>Configure the database settings:

Open the AuthFlowServApp/settings.py file.
Update the DATABASES configuration with your local database settings (database name, username, password, host, and port).

<h3>7</h3>Apply database migrations:

python manage.py migrate

<h3>8</h3>Run the development server:

python manage.py runserver

<h3>9</h3>Access the application by visiting http://localhost:8000 in your web browser.

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
