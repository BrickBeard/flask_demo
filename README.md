# Flask Demo Project (OKC Python)

[![built-with-Flask](https://img.shields.io/badge/Built%20With-Flask%201.0.2-brightgreen.svg?style=flat-square)](http://flask.pocoo.org/) [![Database-Postgres](https://img.shields.io/badge/Database-Postgres-blue.svg?style=flat-square)](https://postgresapp.com/)  [![Python-Version](https://img.shields.io/badge/Python-3.7-orange.svg?style=flat-square)](https://www.python.org/downloads/) 

Demo project showing a few stages of development of a basic Flask application.  Each branch presents another step in the progression of the app:

> |Branches| |
> |---|---|
> |**01-basics** | Presents the most basic form of a Flask application|
> |**02-templates** | Static website with styling showcasing Flasks templating engine (Jinja2)|
> |**03-api** | Combination app (Website/API) tied to a single-table postgres DB|
> |**04-blueprints** | Optimized app using Flask's Blueprints feature (Ideal for scaling apps/APIs)|

Please feel free to fork/clone this repo and play with it!  

## Before You Start
This app was built to try and isolate specific stages in the development stream.  In doing so, I had to make a few adjustments that are not advised in your local environment.  They are:
- The `.gitignore` file contains some files you will definitely want to exclude from version control.  These were commented out to prevent them from being visable across all branches. 
- 2 separate databases were used for these demos.  
  -  `okc_python_demo` was used for the 3rd branch
  -  `test` was used for the final branch & master 
  -  *I did this because the first example used only a single table while the second expanded to two... using the same DB would have broken one of them*

---

## Instructions    -    *master* and *04-blueprints* branches
> For branches  `01-basics` and `02-templates` all you need is the virtualenv and ```
                                                                                  pip install flask
                                                                                  ```

First clone the repo and initialize a virtualenv:
```
git clone https://github.com/BrickBeard/flask_demo.git
cd flask_demo
virtualenv env
source env/bin/activate
(env) pip install -r requirements.txt
```
Next, make sure you have **[Postgres](https://postgresapp.com/)** installed and then:
-  create a database called ***test***
   -  ```
      createdb test
      ```
-  create a postgres user ***test*** with password ***test***
   -  ```
      createuser test --pwprompt
      Enter password for new role:
      Enter it again:
      ```
-  grant user privileges to that database
   -  ```
      psql
      postgres=#   GRANT CONNECT ON DATABASE test TO test; 
      ```

### Create Tables and Run App!

```
flask db migrate
flask db upgrade

flask run
```
> ### Before navigating to the API page:
> - Create a company first (users > companies > [![New Company](https://img.shields.io/badge/New_Company_+-blue.svg?style=round-square)]()) 
> - add a user (users > [![New User](https://img.shields.io/badge/New_User_+-blue.svg?style=round-square)]())
> 
> *...The API page runs a query to get the first user id from the database before rendering the html.*
  
  
<h2 align="center">**Don't Forget to uncomment the files in .gitignore!!!**</h2>


### Questions or Comments

Please leave feedback on here or reach out to me on the Techlahoma Slack **@brickbeard**
