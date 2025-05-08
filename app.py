import random
from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env.local", override=True)  # Charge les variables d’environnement

app = Flask(__name__)

# Configuration à partir du fichier .env.local
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

# exemple de code pour récuperer des données depuis le BDD
# cur = mysql.connection.cursor()
# cur.execute("SELECT mysteryNumber, pseudo, trials, date FROM bestScore ORDER BY trials ASC LIMIT 5")
# scores = cur.fetchall()
# cur.close()

# exemple de code pour enregistrer des données en BDD
# cur = mysql.connection.cursor()
# cur.execute("INSERT INTO bestScore (mysteryNumber) VALUES (%s)", (trial,))
# mysql.connection.commit()
# cur.close()

nombreMystere = None  # Variable en mémoire
trialNumber = 0

@app.route("/")
def home():
    global nombreMystere
    global trialNumber
    nombreMystere = random.randint(1, 100)
    trialNumber = 0

    return render_template('index.html')

@app.route('/prompt', methods=['POST'])
def prompt():
    global nombreMystere
    global trialNumber

    trial = request.json['prompt']
    pseudo = request.json['pseudo']
    if pseudo == '':
        pseudo = 'sans pseudo'
    if trial.isdigit():
        trial = int(trial)
        trialNumber = trialNumber + 1
        nombreEssaye = trial
        if nombreEssaye == nombreMystere:
            message = "Bravo, tu as trouvé le nombre mystère !"
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO bestScore (mysteryNumber, pseudo, trials, date) VALUES (%s, %s, %s, NOW())", (nombreMystere, pseudo, trialNumber))
            mysql.connection.commit()
            cur.close()
        elif nombreEssaye < nombreMystere:
            message = str(nombreEssaye) + " est trop petit."
        else:
            message = str(nombreEssaye) + " est trop grand."
    else:
        message = str(nombreEssaye) + " n'est pas un nombre."

    return jsonify({'message': message})

@app.route("/bestscore")
def bestScore():

    cur = mysql.connection.cursor()
    cur.execute("SELECT mysteryNumber, pseudo, trials, date FROM bestScore ORDER BY trials ASC")
    bestScores = cur.fetchall()
    cur.close()

    return render_template('bestscore.html', bestScores=bestScores)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
