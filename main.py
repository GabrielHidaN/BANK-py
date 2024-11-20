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
    input_login = input(f'{menu_login}  =>\t')

    if input_login == '0':
        break

    elif input_login == '1':
        os.system('clear')
        cpf = input('digite um cpf:')
        cpf_1 = Validador_de_cpf()       
        cpf_1.validar_cpf(cpf)