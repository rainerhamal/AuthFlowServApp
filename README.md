# AuthFlowServApp
 This is a repository containing the code for the AuthFloweServApp, a Django project that implements authentication flow service - user login, roles and permissions.

 <h1>Technologies Used</h1>
 <ul>
  <li>Python 3.11</li>
  <li>pipenv (for managing virtual environments and dependencies</li>
  <li>Django web framework</li>
  <li>crispy-bootstrap5 (to enhance the appearacance of Django Forms)</li>
  <li>MySQL Workbench as local database</li>
 </ul>

 <h1>Installation:</h1>
 <h3>1</h3>Clone the repository using the following command:

 ```
git clone https://github.com/rainerhamal/AuthFlowServApp.git
```


<h3>2</h3>
<ol>
 <li>Download the latest version of Python https://www.python.org/downloads/</li>
 <li>Open your cmd terminal</li>
 <li>
  run this code in your terminal

  ```
  pip install pipenv
  ```
 </li>
 
 <li>
  Create a folder location for your Django project, in this case authflowservapp.

  ```
mkdir authflowservapp
```

  Change directory to your project folder
  
  ```
  cd AuthFlowServApp
  ```

 </li>
 <li>
  run the following 

  ```
  pipenv install django
  ```
 </li>
 
 <li>
  Open the folder in your VSCode or whatever IDE you have. To create your Django project, run the following

  ```
  django-admin startproject authflowservapp .
```

make sure there's a dot at the end of the command so it doesn't create redundant folders for the project.
 </li>
 <li>
  Create a virtual environment and activate it:

```
pipenv shell
```

</li>
<li>
 Create your first app

 ```
python manage.py startapp main
```
</li>

<li>
 run the app

 ```
python manage.py runserver 9000(or you can leave this blank or nominate a different port)
```

</li>
</ol>


<h3>3</h3>Install the project dependencies:

pipenv install django crispy-bootstrap5

<h3>4</h3>Create a MySQL database using MySQL Workbench.
Ensure that MySQL Workbench is installed and running on your local machine.
Create a new MySQL database for the project.

<h3>5</h3>Update the database configuration in the AuthFlowServApp/settings.py file:

```django
<div>
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
</div>
```
<h3>6</h3>Apply the database migrations:

Open the AuthFlowServApp/settings.py file.
python manage.py migrate

<h3>7</h3>Run the development server:

python manage.py runserver 9000(or any available ports in your machine)

<h3>8</h3>Access the application at http://localhost:9000.

<h1>Project Structure:</h1>

```django

authflowservapp/
├── main/
│   ├── templates/
│   │   └── main/
│   │       ├── base.html
│   │       ├── home.html
│   │       └── nav.html
│   └── registration/
│       ├── login.html
│       ├── sign_up.html
│       └── user_update.html
├── manage.py
└── README.md
```
<ul>
 <li>The main project directory is named authflowservapp.</li>
 <li>The main application within the project is named main.</li>
 <li>The project includes two folders within the main application: templates and registration.</li>
 <li>
  The templates folder contains the following files in a subfolder named main:
 <ul>
  <li>base.html</li>
  <li>home.html</li>
  <li>nav.html</li>
 </ul>
 </li>
 <li>
  The registration folder contains the following files:
  <ul>
  <li>login.html</li>
  <li>sign_up.html</li>
  <li>user_update.html</li>
 </ul>
 </li>
 
 <li>The manage.py file is the entry point for managing the Django project.</li>
 <li>The README.md file contains information about the project.</li>
</ul>

<h1>Configuration</h1>
<h3>I</h3>
<p>In the authflowservapp/urls.py file, you need to configure the URL patterns for your application. Add the following code to the urlpatterns list:</p>

```django
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),
]
```

<p>The code above includes URL patterns for the admin site, your main application, and Django's built-in authentication URLs.</p>

<h3>II</h3>
<p>In the main/urls.py file, add the following code to the urlpatterns list:</p>

```django
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'), #get request to retrieve and display user information 
    path('sign_up', views.sign_up, name='sign_up'), #get and post request for insert/sign up operation
    path('<int:id>/', views.user_update, name='user_update'), #get and post request for update operation
]
```

<h1>Test Instructions</h1>
<p>To test the /api/signup and /api/login endpoints in the Django project, follow these instructions:</p>
<ol>
 <li>Make sure you have set up the project environment and dependencies as mentioned in the project's README file.</li>
 <li>Open the Django project in your preferred code editor.</li>
 <li>Navigate to the file containing the tests, which is usually located at my_project/main_project/tests.py.</li>
 <li>Copy the following test code into the 'main/tests.py' file:</li>
</ol>

```django
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class SignupAPITests(TestCase):

    def test_signup_with_valid_data(self):
        client = APIClient()
        data = {
            "username": "test_user",
            "email": "test_user@example.com",
            "password": "password123",
        }
        response = client.post("/api/signup", data=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data["username"] == "test_user")

    def test_signup_with_invalid_data(self):
        client = APIClient()
        data = {
            "username": "",
            "email": "test_user@example.com",
            "password": "password123",
        }
        response = client.post("/api/signup", data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["username"], ["This field is required."])


class LoginAPITests(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="test_user", email="test_user@example.com", password="password123"
        )

    def test_login_with_valid_credentials(self):
        client = APIClient()
        data = {
            "username": "test_user",
            "password": "password123",
        }
        response = client.post("/api/login", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["token"])

    def test_login_with_invalid_credentials(self):
        client = APIClient()
        data = {
            "username": "test_user",
            "password": "wrong_password",
```

<ol>
 <li>Make sure you have your Django project environment set up and dependencies installed.</li>
 <li>Open a terminal or command prompt and navigate to the root directory of your Django project.</li>
 <li>
  Open a terminal or command prompt and navigate to the root directory of your Django project.

 ```django
python manage.py test main_project.tests
```
This command runs the tests located in the main.tests module.
 </li>
 
 <li>
  The test runner will execute the test cases and display the test results in the terminal or command prompt. You will see information about the test suite, the number of tests run, and any failures or errors encountered during the tests.
If all the tests pass successfully, you will see an output similar to the following:

```
----------------------------------------------------------------------
Ran x tests in x.xxxs

OK
```

If any test fails or raises an error, you will see detailed information about the failure or error, including the specific line of code where the failure occurred.

Review the test results to ensure that all the tests are passing as expected.
</li>

<li>By running the tests, you can verify the behavior and correctness of the /api/signup and /api/login endpoints in your Django project.</li>
</ol>

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
