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
# cur.execute("SELECT pseudo, trials, date FROM bestScore ORDER BY trials ASC LIMIT 5")
# scores = cur.fetchall()
# cur.close()

# exemple de code pour enregistrer des données en BDD
# cur = mysql.connection.cursor()
# cur.execute("INSERT INTO mysteryNumber (mysteryNumber) VALUES (%s)", (trial,))
# mysql.connection.commit()
# cur.close()

best_score = None  # Variable en mémoire

@app.route("/")
def home():
    global best_score
    best_score = random.randint(1, 100)

    
    return render_template('index.html')

@app.route('/prompt', methods=['POST'])
def prompt():
    global best_score

    trials = request.json['prompt']
    if trials[-1].isdigit():
        trial = int(trials[-1])
            
    # Code réalisé par Enzo
    
    # nombreEssai = 0
    # import random
    # nombreMystere = random.randint(1, 100)
    # while True:
    #     print('Devine le nombre')
    #     nombreEssai = nombreEssai + 1
    #     nombreEssaye = input()
    #     if nombreEssaye.isdigit():
    #         nombreEssaye = int(nombreEssaye)
    #         if nombreEssaye == nombreMystere:
    #             print("Bravo, tu as trouvé le nombre")
    #             print("le nombre d'nombreEssai est de ", end = "")
    #             print(nombreEssai)
    #             break
    #         elif nombreEssaye < nombreMystere:
    #             print("Trop petit.")
    #         else:
    #             print("Trop grand.")
    #     else:
    #         print(nombreEssaye + " n'est pas un nombre")

    messages = 'essai'  # Exemple de messages
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
