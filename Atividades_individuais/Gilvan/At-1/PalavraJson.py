import json
import os

def search_in_json(data, word):
    #Verifica se a palavra existe em qualquer valor de um JSON.

    # data: O JSON (ou um dicionário Python) onde procurar.
    # word: A palavra a ser procurada.
    # return: True se a palavra for encontrada, False caso contrário.
    
    if isinstance(data, dict):
        for key, value in data.items():
            if search_in_json(value, word):
                return True
    elif isinstance(data, list):
        for item in data:
            if search_in_json(item, word):
                return True
    elif isinstance(data, str):
        if word in data:
            return True
    return False

def find_word_in_json_file(file_path, word):
    #Verifica se a palavra existe em um arquivo JSON.
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    # Lê o conteúdo do arquivo JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Verifica se a palavra existe no JSON
    return search_in_json(data, word)

# Caminho para o arquivo JSON:
json_file_path = 'C:\\Users\\gilva\\Documents\\DataScience\\At-1\\JSON\\palavras.json' #A única forma de funcionar, foi usar o caminho absoluto, com barras inertidas duplas.
# Palavra a ser procurada:
word_to_search = 'Maria'

try:
    #True se a palavra for encontrada, e False caso contrário

    exists = find_word_in_json_file(json_file_path, word_to_search)
    print(f"A palavra '{word_to_search}' existe no arquivo JSON: {exists}")
except FileNotFoundError as e:
    print(e)
