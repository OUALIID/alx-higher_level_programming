#!/usr/bin/python3
from sys import exc_info as err


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception:
        print("Exception: {}".format(err()[1]), file=stderror)
        return None