from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/prompt', methods=['POST'])
def prompt():
    messages = request.json['messages']

    # nombreEssoye = 0
    # import random
    # nombreMystere = random.randint(1, 100)
    # while True:
    #     print('Devine le nombre')
    #     nombreEssoye = nombreEssoye + 1
    #     nombreEssaye = input()
    #     if nombreEssaye.isdigit():
    #         nombreEssaye = int(nombreEssaye)
    #         if nombreEssaye == nombreMystere:
    #             print("Bravo, tu as trouvé le nombre")
    #             print("le nombre d'essai est de ", end = "")
    #             print(nombreEssoye)
    #             break
    #         elif nombreEssaye < nombreMystere:
    #             print("Trop petit.")
    #         else:
    #             print("Trop grand.")
    #     else:
    #         print(nombreEssaye + " n'est pas un nombre")

    # return messages

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
