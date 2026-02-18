import os


def get_secret(name, default=None):
    # Making decouple first as os.environ can fail on local sometimes.
    try:
        from decouple import config

        return config(name, default)
    except (ImportError, ModuleNotFoundError) as err:
        return os.environ.get(name, default)
