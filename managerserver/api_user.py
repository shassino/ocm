from flask import jsonify
import settings

db = settings.db
cursor = settings.cursor

def loginUser(username, password):
    return jsonify("root")

def logoutUser(sid):
    return jsonify("root")

def createUser(sid, body):
    return jsonify("ciuppa")

def getUserByName(sid, username):
    return jsonify("root")

def deleteUser(sid, username):
    return jsonify("root")

def updateUser(sid, username, body):
    return jsonify("root")

