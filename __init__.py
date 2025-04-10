from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:cle>/<string:valeur>')
def encryptage(cle, valeur):
    try:
        # Vérifier si la clé est valide (doit être 32 bytes en base64)
        cle_bytes = cle.encode()
        if len(base64.urlsafe_b64decode(cle)) != 32:
            return "Erreur : La clé doit être une clé Fernet valide (32 bytes encodée en base64)", 400
        
        # Créer une instance Fernet avec la clé de l'utilisateur
        f = Fernet(cle_bytes)
        
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        token = f.encrypt(valeur_bytes)  # Encrypt la valeur
        return f"Valeur encryptée : {token.decode()}"
    except ValueError as e:
        return f"Erreur d'encryptage : Clé invalide ({str(e)})", 400
    except Exception as e:
        return f"Erreur d'encryptage : {str(e)}", 500

@app.route('/decrypt/<string:cle>/<string:valeur>')
def decryptage(cle, valeur):
    try:
        # Vérifier si la clé est valide (doit être 32 bytes en base64)
        cle_bytes = cle.encode()
        if len(base64.urlsafe_b64decode(cle)) != 32:
            return "Erreur : La clé doit être une clé Fernet valide (32 bytes encodée en base64)", 400
        
        # Créer une instance Fernet avec la clé de l'utilisateur
        f = Fernet(cle_bytes)
        
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        decrypted_value = f.decrypt(valeur_bytes)  # Décrypt la valeur
        return f"Valeur décryptée : {decrypted_value.decode()}"
    except ValueError as e:
        return f"Erreur de décryptage : Clé ou valeur invalide ({str(e)})", 400
    except Exception as e:
        return f"Erreur de décryptage : {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
