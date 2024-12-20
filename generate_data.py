# link repostiório redash https://github.com/getredash/redash/wiki/Local-development-setup

import mysql.connector
import random
from datetime import datetime, timedelta

# Conectando ao banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",      # Endereço do servidor MySQL
    user="root",    # Seu usuário do MySQL
    password="root",  # Sua senha do MySQL
    database="test-database"   # Nome do banco de dados
)

cursor = conn.cursor()

create_temperatura_table = """
CREATE TABLE IF NOT EXISTS Temperatura (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    temperatura FLOAT NOT NULL,
    horario DATETIME NOT NULL
)
"""

create_ph_table = """
CREATE TABLE IF NOT EXISTS PH (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    horario DATETIME NOT NULL,
    ph FLOAT NOT NULL
)
"""

create_user_table = """
CREATE TABLE IF NOT EXISTS User (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
)
"""

# Função para gerar dados e inserir na tabela
def gerar_temperaturas():
    
    cursor.execute(create_temperatura_table)
    cursor.execute(create_ph_table)
    cursor.execute(create_user_table)
    
    cursor.execute(
        "INSERT INTO User (email, password) VALUES (%s, %s)", 
        ("admin@gmail.com", "$2a$12$rQDWkleOIAvo/SUL5ImEMe22xFkGhsKMus8.gRdS2ZGtx1gDdIU/6")
    )
    for _ in range(100):
        temperatura = round(random.uniform(0, 50), 2)  # Temperatura entre 0 e 50, com 2 casas decimais
        horas_anteriores = random.randint(0, 100)      # Intervalo de horas aleatório (0 a 100 horas atrás)
        ph = random.randint(0,14);
        horario = datetime.now() - timedelta(hours=horas_anteriores)
        
        # Comando para inserir na tabela
        cursor.execute(
            "INSERT INTO Temperatura (temperatura, horario) VALUES (%s, %s)", 
            (temperatura, horario)
        )
        
        cursor.execute(
            "INSERT INTO PH (ph, horario) VALUES (%s, %s)", 
            (ph, horario)
        )
        


    # Commit das alterações no banco
    conn.commit()

# Chama a função para gerar e inserir os dados
gerar_temperaturas()


# Fechar a conexão
cursor.close()
conn.close()

print("100 registros inseridos com sucesso!")
