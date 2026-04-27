import psycopg2
from configparser import ConfigParser
import os

def get_config(filename='database.ini', section='postgresql'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    
    parser = ConfigParser()
    parser.read(file_path)
    
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        print(f"Ошибка: Секция '{section}' не найдена в {file_path}")
    return db

def connect():
    params = get_config()
    conn = psycopg2.connect(**params)
    return conn