from flask import jsonify
import settings

from cryptography.fernet import Fernet

db = settings.db
cursor = settings.cursor
config = settings.config
#load CRYPTO PWD from settings and init fernet
key = config['CRYPTO_PWD'].encode("utf-8")
cipher_suite = Fernet(key)

def encryptPWD(password):
    encoded_cipher = cipher_suite.encrypt(password.encode("utf-8"))
    return encoded_cipher.decode("utf-8")

def loginUser(username, password):
    return jsonify("root")

def logoutUser(sid):
    return jsonify("root")

def createUser(sid, body):
    pwd = encryptPWD(body['password'])
    query = "INSERT INTO users (username, password, email) VALUES('{0}', '{1}', '{2}')".format(body['username'], db.escape_string(pwd), body['email'])
    cursor.execute(query)
    return jsonify('OK'), 200

def getUserByName(sid, username):
    return jsonify("root")

def deleteUser(sid, username):
    return jsonify("root")

def updateUser(sid, username, body):
    return jsonify("root")

