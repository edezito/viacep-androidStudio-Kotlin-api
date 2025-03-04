import mysql.connector
from mysql.connector import errorcode

def conectar(database=None):
    print("Conectando ao banco de dados...")
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Tim@o2812',
            database=database if database else 'gestao_escolar',
            port=3306
        )
        print("Conexão bem-sucedida!")
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar: {err}")
        return None

# Conexão inicial
conn = conectar()
if conn:
    cursor = conn.cursor()
    cursor.execute("DROP DATABASE IF EXISTS `gestao_escolar`;")
    cursor.execute("CREATE DATABASE `gestao_escolar`;")
    cursor.close()
    conn.close()

# Nova conexão ao banco recém-criado
conn = conectar(database="gestao_escolar")
cursor = conn.cursor()


TABLES = {}

TABLES['Turmas'] = ('''
    CREATE TABLE `turmas` (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `nome` VARCHAR(50) NOT NULL,
        `turno` VARCHAR(10) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')

TABLES['Alunos'] = ('''
    CREATE TABLE `alunos` (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `nome` VARCHAR(50) NOT NULL,
        `data_nascimento` DATE NOT NULL,
        `nota_primeiro_semestre` DOUBLE NOT NULL,
        `nota_segundo_semestre` DOUBLE NOT NULL,
        `turma_id` INT NOT NULL,
        FOREIGN KEY (`turma_id`) REFERENCES `turmas`(`id`) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')

TABLES['AlunosOutput'] = ('''
    CREATE TABLE `alunos_output` (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `aluno_id` INT NOT NULL,
        `nome` VARCHAR(50) NOT NULL,
        `data_nascimento` DATE NOT NULL,
        `nota_primeiro_semestre` DOUBLE NOT NULL,
        `nota_segundo_semestre` DOUBLE NOT NULL,
        `media_final` DOUBLE NOT NULL,
        FOREIGN KEY (`aluno_id`) REFERENCES `alunos`(`id`) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')

TABLES['Professores'] = ('''
    CREATE TABLE `professores` (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `nome` VARCHAR(50) NOT NULL,
        `data_nascimento` DATE NOT NULL,
        `disciplina` VARCHAR(50) NOT NULL,
        `salario` DOUBLE NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')

TABLES['ProfessoresOutput'] = ('''
    CREATE TABLE `professores_output` (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `professor_id` INT NOT NULL,
        `nome` VARCHAR(50) NOT NULL,
        `idade` INT(3) NOT NULL,
        `data_nascimento` DATE NOT NULL,
        `disciplina` VARCHAR(50) NOT NULL,
        `salario` DOUBLE NOT NULL,
        FOREIGN KEY (`professor_id`) REFERENCES `professores`(`id`) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')

# Criando tabelas no banco de dados
for tabela_nome, tabela_sql in TABLES.items():
    try:
        print(f'Criando tabela {tabela_nome}:', end=' ')
        cursor.execute(tabela_sql)
        print('OK')
    except mysql.connector.Error as err:
        print(f'Erro ao criar {tabela_nome}: {err.msg}')

# Commit e fechamento
conn.commit()
cursor.close()
conn.close()