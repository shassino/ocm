from flask import jsonify
from settings import config, cursor


def lista():
    return jsonify("ciuppa")


def root():
    return jsonify("root")