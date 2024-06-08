Build a Tournament Management System

Postman Endpoint API Documentation Link : https://documenter.getpostman.com/view/29389936/2sA3XJnRE9

Please run the server with command "python manage.py runserver"
please start celery with commanad "celery -A TMS worker --loglevel=INFO --pool=solo"

Description:

User Authentication:
● Implemented user registration, login, and logout functionalities using Django
REST built-in token authentication system.

API Endpoints:
● Team Management:
● Register a team (POST)
● Update team details (PUT/PATCH)
● Delete a team (DELETE)
● Tournament Management:
● Create a tournament (POST)
● Update tournament details (PUT/PATCH)
● Delete a tournament (DELETE)
● Generate fixtures of the teams through an API.

Asynchronous Tasks (Celery):
● Send a notification email to the contact email of the team, prior to every
match day.

Signals:
● Send an email notification to registered teams (use contact email) upon
tournament creation.


