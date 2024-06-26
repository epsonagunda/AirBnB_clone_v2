#!/usr/bin/python3
"""defines a class User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
