from flask import jsonify
import settings

from cryptography.fernet import Fernet

db = settings.db
cursor = settings.cursor
config = settings.config
# load CRYPTO PWD from settings and init fernet
key = config['CRYPTO_PWD'].encode("utf-8")
cipher_suite = Fernet(key)


def encrypt_pwd(password):
    encoded_cipher = cipher_suite.encrypt(password.encode("utf-8"))
    return encoded_cipher.decode("utf-8")


def user_login(username, password):
    return jsonify("root")


def user_logout(sid):
    return jsonify("root")


def user_create(sid, body):
    pwd = encrypt_pwd(body['password'])
    query = "INSERT INTO users (username, password, email) VALUES('{0}', '{1}', '{2}')".format(body['username'], db.escape_string(pwd), body['email'])
    cursor.execute(query)
    return jsonify('OK'), 200


def user_get_by_name(sid, username):
    return jsonify("root")


def user_delete(sid, username):
    return jsonify("root")


def user_update(sid, username, body):
    return jsonify("root")

