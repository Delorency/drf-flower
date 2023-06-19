from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status



class MyError(APIException):
    def __init__(self, key:str, message:str, status_code:int):
        self.key = key
        self.message = message
        self.detail = {self.key:[self.message]}