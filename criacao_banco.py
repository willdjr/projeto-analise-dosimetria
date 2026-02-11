import sqlite3
import random
from datetime import datetime, timedelta

# Criar conexão
conexao = sqlite3.connect("hospital.db")
cursor = conexao.cursor()

# Criar tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS pacientes (
    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    sexo TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS exames (
    id_exame INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_exame TEXT,
    regiao_corpo TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS equipamentos (
    id_equipamento INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT,
    ano_fabricacao INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS registros_exames (
    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
    id_paciente INTEGER,
    id_exame INTEGER,
    id_equipamento INTEGER,
    data_exame TEXT,
    dose_mSv REAL,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
    FOREIGN KEY (id_exame) REFERENCES exames(id_exame),
    FOREIGN KEY (id_equipamento) REFERENCES equipamentos(id_equipamento)
)
""")

# 🔹 Limpar dados anteriores (evita duplicação ao rodar novamente)
cursor.execute("DELETE FROM registros_exames")
cursor.execute("DELETE FROM pacientes")
cursor.execute("DELETE FROM exames")
cursor.execute("DELETE FROM equipamentos")

# Inserir dados fixos
cursor.executemany("""
INSERT INTO pacientes (nome, idade, sexo)
VALUES (?, ?, ?)
""", [
    ("Ana Silva", 34, "F"),
    ("Carlos Souza", 52, "M"),
    ("Mariana Lima", 28, "F"),
    ("João Pereira", 45, "M")
])

cursor.executemany("""
INSERT INTO exames (tipo_exame, regiao_corpo)
VALUES (?, ?)
""", [
    ("Raio-X", "Tórax"),
    ("Tomografia", "Crânio"),
    ("Mamografia", "Mama"),
    ("Raio-X", "Abdômen")
])

cursor.executemany("""
INSERT INTO equipamentos (modelo, ano_fabricacao)
VALUES (?, ?)
""", [
    ("Siemens AX-200", 2018),
    ("GE Revolution CT", 2020),
    ("Philips MammoPlus", 2019)
])

# -------- GERAÇÃO AUTOMÁTICA --------
registros = []

for _ in range(300):

    id_paciente = random.randint(1, 4)
    id_exame = random.randint(1, 4)
    id_equipamento = random.randint(1, 3)

    data_inicial = datetime(2025, 1, 1)
    dias_aleatorios = random.randint(0, 364)
    data_exame = data_inicial + timedelta(days=dias_aleatorios)

    if id_exame in [1, 4]:
        dose = round(random.uniform(0.1, 0.3), 2)
    elif id_exame == 2:
        dose = round(random.uniform(2.0, 7.0), 2)
    else:
        dose = round(random.uniform(0.3, 0.7), 2)

    registros.append((
        id_paciente,
        id_exame,
        id_equipamento,
        data_exame.strftime("%Y-%m-%d"),
        dose
    ))

cursor.executemany("""
INSERT INTO registros_exames
(id_paciente, id_exame, id_equipamento, data_exame, dose_mSv)
VALUES (?, ?, ?, ?, ?)
""", registros)

conexao.commit()
conexao.close()

print("Banco criado e populado com sucesso.")
