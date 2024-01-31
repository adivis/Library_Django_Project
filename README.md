# Libraray Project

## To Run The Project Locally

### Download or Clone

1. Download the code from repo or clone `git clone https://github.com/adivis/Library_Django_Project`.
2. run `pip install virtualenv`(make sure python is installed).
3. go to the directory in the command prompt.
4. run `virtualenv venv`
5. run `venv\Scripts\activate`
6. run `cd src` to go to src folder.
7. run `pip install -r requirements.txt` to install the dependencies.

8. **Run migrations** - Run `python manage.py makemigrations` and `python manage.py migrate`

9. **Run the server** - `python manage.py runserver`.

## Description

- Once the server is started, a admin is already create with email as `admin@gmail.com` and password as `1234`. User can access base_url/admin/ using these creds.
- To add books and save them user will need to login otherwise many unregistered user can also add books with yours.
- The project contains authentication and authorization, so to keep track it is better to login.
