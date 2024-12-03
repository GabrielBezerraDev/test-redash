# link repostiório redash https://github.com/getredash/redash/wiki/Local-development-setup

import mysql.connector
import random
from datetime import datetime, timedelta

# Conectando ao banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",      # Endereço do servidor MySQL
    user="root",    # Seu usuário do MySQL
    password="root",  # Sua senha do MySQL
    database="fishTrack"   # Nome do banco de dados
)

cursor = conn.cursor()

# Função para gerar dados e inserir na tabela
def gerar_temperaturas():
    for _ in range(100):
        temperatura = round(random.uniform(0, 50), 2)  # Temperatura entre 0 e 50, com 2 casas decimais
        horas_anteriores = random.randint(0, 100)      # Intervalo de horas aleatório (0 a 100 horas atrás)
        horario = datetime.now() - timedelta(hours=horas_anteriores)
        
        # Comando para inserir na tabela
        cursor.execute(
            "INSERT INTO Temperatura (temperatura, horario) VALUES (%s, %s)", 
            (temperatura, horario)
        )

    # Commit das alterações no banco
    conn.commit()

# Chama a função para gerar e inserir os dados
gerar_temperaturas()


# Fechar a conexão
cursor.close()
conn.close()

print("100 registros inseridos com sucesso!")
