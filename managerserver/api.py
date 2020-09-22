from flask import jsonify


def lista():
    return jsonify("ciuppa")


def root():
    return jsonify("root")