import sqlite3



conn = sqlite3.connect('dataBase/data_base.db')
cursor = conn.cursor()


class Validador_de_cpf:

    @classmethod
    def verificar_modelo_enviado(self , cpf):
        self.cpf = cpf
        
        if cpf.isdigit():

            if len(self.cpf) != 11:
                print('@@@ CPF Inválido. Um CPF Válido Deve conter 11 Caracter!')
                return False
            return True
        print('@@@ Você Deve enviar Um digito!')
        return False

    @classmethod
    def verificar_numeros(self , cpf ):
        self.cpf = str(cpf)
        if self.verificar_modelo_enviado(cpf) == True:
            cpf_valido = set(cpf)
            if len(cpf_valido) == 1:
                print('@@@ CPF Inválido, Você tentou me sacanear hahaha @@@')
                return False
            return True
        return False
    @classmethod
    def validar_cpf(self , cpf):
        if self.verificar_numeros(cpf):
        # Cálculo do primeiro dígito verificador
            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            primeiro_digito = (soma * 10) % 11
            primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

            if primeiro_digito != int(cpf[9]):
                print('@@@ CPF Inválido /1 digit @@@')
                return False

        # Cálculo do segundo dígito verificador
            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            segundo_digito = (soma * 10) % 11
            segundo_digito = 0 if segundo_digito == 10 else segundo_digito

            if segundo_digito == int(cpf[10]):

                return True
            else:
                print('@@@ CPF Inválido /2 digit @@@')
                return False




def create_user(cpf , password , name):
    
    cursor.execute("INSERT INTO usuarios (cpf, pass, nome) VALUES(?,?,?)", (cpf , password , name))
    conn.commit()


