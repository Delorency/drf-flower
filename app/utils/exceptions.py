class MyError(Exception):
    def __init__(self, key:str, message:str, status_code:int):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return {key:[self.message]}