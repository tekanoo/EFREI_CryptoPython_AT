from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:cle>/<string:valeur>')
def encryptage(cle, valeur):
    try:
        # Convertir la clé fournie par l'utilisateur en bytes
        cle_bytes = cle.encode()
        # Créer une instance Fernet avec la clé de l'utilisateur
        f = Fernet(cle_bytes)
        
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        token = f.encrypt(valeur_bytes)  # Encrypt la valeur
        return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
    except Exception as e:
        return f"Erreur d'encryptage : {str(e)} (vérifiez que la clé est valide)"

@app.route('/decrypt/<string:cle>/<string:valeur>')
def decryptage(cle, valeur):
    try:
        # Convertir la clé fournie par l'utilisateur en bytes
        cle_bytes = cle.encode()
        # Créer une instance Fernet avec la clé de l'utilisateur
        f = Fernet(cle_bytes)
        
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        decrypted_value = f.decrypt(valeur_bytes)  # Décrypt la valeur
        return f"Valeur décryptée : {decrypted_value.decode()}"  # Retourne la valeur en str
    except’atException as e:
        return f"Erreur de décryptage : {str(e)} (vérifiez que la clé est correcte)"

if __name__ == "__main__":
    app.run(debug=True)
