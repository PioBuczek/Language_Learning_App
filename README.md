![fCSgPE4](https://github.com/PioBuczek/Language_Learning_App/assets/137912290/1959d677-a125-4252-8a52-45d39c2c20ae)


### A few words about project:

The "Language Learning App" project is a web application that enables users to learn new words and phrases in various languages. The app allows users to create word lists, categorize them by groups, and take quizzes to test their language skills. This project is built using the Django framework and utilizes a database to store words and groups. The app also provides a user-friendly interface for adding new words and categories. It is a valuable tool for individuals who are learning a new language or looking to expand their vocabulary in a foreign language. The application will continue to be developed.


### How start this application ?

Before we start, you need to create a database(This project is used PostgreSQL version 15). You need to know, that this project was tested in Postgres. 

Firstly, you need to clone my repo to my GitHub, and you need to use commande: 
<div class="termy">

```console
git clone https://github.com/PioBuczek/Language_Learning_App.git
```
</div> 

Then you need to go into a higher file, you need the command:
<div class="termy">

```console
cd PasswordValidator
```

You need to create Environment Variables. You can set up environment variables in your system by following these steps:

1. Open "Control Panel" and search for "System Properties."
2. Click on "Environment Variables."
3. In the "System Variables" section, click "New" to add a new variable.
4. Add the variable name (e.g., pv_dbname) and its corresponding value (e.g., my_database_name).
5. Repeat the above step for all the environment variables listed above.

If you don't want set up environment variables, you can create a .env file in the root directory of the project and add the environment variables there in the following format:

<div class="termy">

```console
pv_dbname=my_database_name
pv_host=my_host
pv_user=my_username
pv_password=my_password
pv_port=my_port

```
</div> 


Next, you need to create of virtual environments (venv). In the terminal, write the command that will create your venv and install library which are necessery:


```console
python -m venv YourVenv
./YourVenv/Scripts/activate.ps1
pip install -r requirements.txt  
python main.py
```
