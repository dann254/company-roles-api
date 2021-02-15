[![Build Status](https://travis-ci.com/dann254/company-roles-api.svg?branch=master)](https://travis-ci.com/dann254/company-roles-api)


# COMPANY ROLES - [API]

authenticate users based on role

### Relevant Links
- [staging](https://company-roles-api.herokuapp.com/)


## How to set up
- Make sure you have **python3** installed.
- You should have **postgreSQL** or other [database management engines](https://github.com/jacobian/dj-database-url#supported-databases) installed in your development environment.
- Install **virtualenv** and **virtualenvwrapper** or use suitable alternatives to create a virtual environment.
 - using virtualenvwrapper
```
$ mkvirtualenv company-roles
$ workon company-roles
```
- Clone this repository:
```bash
git clone git@github.com:dann254/company-roles-api.git
```
- switch to the project folder:
```bash
cd company-roles-api
```
- install requirements:
```bash
pip install -r requirements.txt
```
- Create a **postgreSQL** database:
```bash
createdb company-roles
```
 *- follow appropriate tutorials for other DB managers*


- Create a **.env** file in the project the directory (**database-api/company-roles/**) with the following format.
```bash
  export DB_URL="postgres://USER:PASSWORD@HOST:PORT/company-roles-db"
  export CURRENT_ENV="development"
  export SECRET_KEY="your-secret-key"
```
 - instructions for setting up `DB_URL` on other recomended DB managers are found [Here](https://github.com/jacobian/dj-database-url#url-schema).


- Run migrations from the project root directory to update the database
```bash
python manage.py migrate
```

- To start the app, run:
```bash
python manage.py runserver
```
- All set up, you can now use the url  **http://127.0.0.1:8000/** to access the app from your development server. 🤗

- The API docs and relevant endpoints will be availabe in GIU by accessing the URL on a browser.

- #### running tests
  After setting up your development environment
  - run tests using the following command:
  ```bash
  ./manage.py test
  ```

- #### Django SuperUser
  After setting up your development environment
  - add a super user using the following command:
  ```bash
  python manage.py createsuperuser --email email@example.com
  ```
