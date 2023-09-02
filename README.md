![fCSgPE4](https://github.com/PioBuczek/Language_Learning_App/assets/137912290/1959d677-a125-4252-8a52-45d39c2c20ae)


### A few words about project:

The "Language Learning App" project is a web application that enables users to learn new words and phrases in various languages. The app allows users to create word lists, categorize them by groups, and take quizzes to test their language skills. This project is built using the Django framework and utilizes a database to store words and groups. The app also provides a user-friendly interface for adding new words and categories. It is a valuable tool for individuals who are learning a new language or looking to expand their vocabulary in a foreign language. The application will continue to be developed.


### How start this application ?

Before we start, you need to create a database(This project is used PostgreSQL version 15). You need to know, that this project was tested in Postgres, but if you want to use a different database you need to configure settings accordingly.

Firstly, you need to clone my repo to my GitHub, and you need to use commande: 
<div class="termy">

```console
git clone https://github.com/PioBuczek/Language_Learning_App.git
```
</div> 

Then you need to go into a higher file, you need the command:
<div class="termy">

```console
cd .\Language_Learning_App\
```
</div> 

Second, you need to change this settings. In the tree, click on "settings" and find DATABASE, and change this data:

<div class="termy">

```console
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "{{NAME}}",
        "USER": "{{USER}}",
        "PASSWORD": "{{PASSWORD}}",
        "HOST": "{{HOST}}",
        "PORT": "{{PORT}}",
    },
}

```
</div> 

Next, you need to create of virtual environments (venv). In the terminal, write the command that will create your venv and install library which are necessery:
<div class="termy">

```console
python -m venv YourVenv
./YourVenv/Scripts/activate.ps1
pip install -r requirements.txt  
```
</div> 

If after this command you will get error, you need to open Windows PowerShell and you need to write command: 

<div class="termy">

```console
Set-ExecutionPolicy RemoteSigned 
```
</div> 


### Run it
You need to generate migration files for the models defined in application. The migration files contain the changes to the database schema to be applied.


<div class="termy">

```console
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
</div>


The development server will start,at
<div class="termy">

```console
http://localhost:8000/
```
</div>
  in browser.
