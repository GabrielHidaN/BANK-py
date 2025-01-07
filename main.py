import os
from menu import *
from cpf_validade import Validador_de_cpf
from app import Bank
import sqlite3 


conn = sqlite3.connect('dataBase/data_base.db')
cursor = conn.cursor()

'''
SISTEMA BANCARIO
DEVE CONTER BANCO DE DADOS CRUD
CODIGO O MAIS LIMPO POSSIVEL 
POO


FUNCIONALIDADES:

ACESSAR USUARIO
ACESSAR CONTA PRINCIPAL
ACESSAR CONTAS
SAQUE
DEPOSITO
EXTRATO
CRIAR CONTA
FECHAR CONTA
CALCULAR LIMITE DE EMPRESTIMO

'''
while True:

    input_menu = input(f'{menu_login}  =>\t')

    if input_menu == '0':
        break

    elif input_menu == '1':
        os.system('clear')
        cpf_input = input('Digite seu CPF:\n=>\t')
        cpf = Validador_de_cpf()       
        validate_cpf = cpf.validar_cpf(cpf_input)

        if validate_cpf == True:

            cursor.execute("SELECT * FROM usuarios WHERE cpf = ?", (cpf_input,))
            user = cursor.fetchone()


            if user:
                print(f"@@@ O CPF indicado já está registrado na nossa Lista de Clientes! @@@")

            else:
                password_input = str(input('Digite sua senha:\n=>\t'))
                name_input = str(input('Digite seu nome:\n=>\t'))
                Bank.create_user( cpf= cpf_input , password=password_input , name=name_input )




