import os
from menu import *
from cpf_validade import *
import sqlite3

class Bank:
    def __init__(self, cpf , password , name):
        self.cpf = cpf
        self.password = password
        self.name = name
    @classmethod
    def create_user(self , cpf , password , name):
        self.cpf = cpf
        self.password = password
        self.name = name

    
        cursor.execute("INSERT INTO usuarios (cpf, pass, nome) VALUES(?,?,?)", (cpf , password , name))
        conn.commit()


    