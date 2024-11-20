import os
from menu import *
from signed import *
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
    os.system('clear')
    input_login = input(f'{menu_login}  =>\t')

    if input_login == '0':
        break

    elif input_login == '1':
        os.system('clear')
        cpf_input = input('digite um cpf:')
        cpf = Validador_de_cpf()       
        validate_cpf = cpf.validar_cpf(cpf_input)

        if validate_cpf == True:
            password_input = str(input('digite sua senha:'))
            name_input = str(input('digite seu nome:'))
            create_user(cpf= cpf_input , password=password_input , name=name_input)

#TODO resolver problema de chave primaria está no db