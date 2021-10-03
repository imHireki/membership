"""
Core's useful functions
"""
import json


def get_secret(key):
    """ Get secrets from a local jsonfile """
    with open('secret.json') as jsonfile:
        data = json.load(jsonfile)
        response = data.get(key)
        return response
