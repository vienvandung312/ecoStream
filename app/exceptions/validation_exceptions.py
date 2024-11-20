class MissingParameterException(Exception):
    def __init__(self, key: str):
        self.key = key
        self.message = f'{key} is required'