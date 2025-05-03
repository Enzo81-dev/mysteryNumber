## ✅ Prérequis

- Python 3.8+
- `pip` ou `venv` installé

## 🔧 Installation

1. Clone le dépôt :
   ```bash
   git clone https://github.com/ton-utilisateur/flaskgpt.git
   cd flaskgpt

2. Créer une Base de données (BDD)
    installer MySql
    se connecter
    mysql>SHOW DATABASES;
    mysql>CREATE DATABASE mysteryNumber;
    mysql>USE mysteryNumber;
    mysql>CREATE TABLE mysteryNumber (
        id INT AUTO_INCREMENT PRIMARY KEY,
        mysteryNumber INT
    );
    mysql>SHOW TABLES;
    mysql>DESCRIBE mysteryNumber;
    mysql>CREATE TABLE bestScore (
        id INT AUTO_INCREMENT PRIMARY KEY,
        trials INT,
        pseudo VARCHAR(100),
        date DATE
    );
    mysql>SHOW TABLES;
    mysql>DESCRIBE bestScore;

    ajouter des données fixtives :
    mysql>INSERT INTO mysteryNumber (mysteryNumber) VALUES (81);
    mysql>INSERT INTO bestScore (trials, pseudo, date) VALUES (100, 'Xav', NOW());

    voir les données ajoutées :
    mysql>SELECT * FROM mysteryNumber;
    mysql>SELECT * FROM bestScore;

3. 📦 Installer les bibliothèques nécessaires
    pip install flask
    pip install flask-mysqldb      sur ubuntu lancer avant pip install flask-mysqldb : sudo apt-get install libmysqlclient-dev
    pip install python-dotenv


## 🔧 Installation

1. Installer les dépendances :
    ```bash
    npm cache clean --force
    npm install

2. Compiler :
     ```bash
     npm run watch

##  ▶️ Lancer le serveur flask

    Windows => se placer dans app.py => ▶ Run Python file
    Ubuntu => 
        ```bash
        source venv/bin/activate
        python app.py


Sites
    Coder et héberger un site web de A à Z avec Python et Flask
    https://www.google.com/search?q=youtube+site+web+de+a+%C3%A0+z+avec+python&sca_esv=d8c2b4a8fa54c828&ei=fuUVaMmHGdikkdUPkoiy8A4&ved=0ahUKEwjJvrDogYeNAxVYUqQEHRKEDO4Q4dUDCBA&uact=5&oq=youtube+site+web+de+a+%C3%A0+z+avec+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiJnlvdXR1YmUgc2l0ZSB3ZWIgZGUgYSDDoCB6IGF2ZWMgcHl0aG9uMgUQABjvBTIFEAAY7wUyCBAAGIAEGKIEMgUQABjvBUj0IFDDGViUH3ACeACQAQCYAUugAfsBqgEBNLgBA8gBAPgBAZgCBqACjQLCAggQABiwAxjvBcICCxAAGIAEGLADGKIEwgIKECEYoAEYwwQYCpgDAIgGAZAGA5IHATagB-gNsgcBNLgHiAI&sclient=gws-wiz-serp#fpstate=ive&vld=cid:018d09e8,vid:AYmcV3b7lWQ,st:0
    https://github.com/DocstringFr/FlaskGPT

    Créer une app web moderne de A à Z avec Python
    https://www.youtube.com/watch?v=ns7cmSaiA9E

    
