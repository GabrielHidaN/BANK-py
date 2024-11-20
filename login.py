import sys
import sqlite3

conn = sqlite3.connect('dataBase/data_base.db')


class Validador_de_cpf:
    def __init__(self , cpf):
        self.cpf = cpf

    def verificar_modelo_enviado(self):
        self.cpf = cpf
        
        if cpf.isdigit():

            if len(self.cpf) != 11:
                #print('@@@ CPF Inválido. Um CPF Válido Deve conter 11 Caracter!')
                return False
            return True
        #print('@@@ Você Deve enviar Um digito!')
        return False


    def verificar_numeros(self ):
        self.cpf = str(cpf)
        if self.verificar_modelo_enviado() == True:
            cpf_valido = set(cpf)
            if len(cpf_valido) == 1:
                #print('@@@ CPF Inválido, Você tentou me sacanear hahaha @@@')
                return False
            return True
        return False
    
    def validar_cpf(self):
        if self.verificar_numeros():
        # Cálculo do primeiro dígito verificador
            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            primeiro_digito = (soma * 10) % 11
            primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

            if primeiro_digito != int(cpf[9]):
                #print('@@@ CPF Inválido /1 digit @@@')
                return False

        # Cálculo do segundo dígito verificador
            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            segundo_digito = (soma * 10) % 11
            segundo_digito = 0 if segundo_digito == 10 else segundo_digito

            if segundo_digito == int(cpf[10]):
                #print(f'O CPF :  {cpf} é Válido.')
                return True
            else:
                #print('@@@ CPF Inválido /2 digit @@@')
                return False
        


class Login:


    def __init__(self , cpf , password , data_base):
        self.data_base = data_base
        self.cpf = cpf
        self.password = password

    def approve_login(self):
        if self.cpf in self.data_base:
            print('Está aqui')
        else:
            print ('nao esta')