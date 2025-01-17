import os
from menu import *
from cpf_validade import *
import sqlite3

class Bank_login:
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


    @classmethod
    def login_user(self , cpf):
        self.cpf = cpf
        cursor.execute("SELECT * FROM usuarios WHERE cpf = ?", (cpf,))
        user = cursor.fetchone()