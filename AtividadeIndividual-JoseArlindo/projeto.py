import json

def palavra_existe_em_json(caminho_arquivo, palavra):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
        palavra = palavra.lower()

       
        def busca_palavra(dados):
            if isinstance(dados, dict):
                
                for chave, valor in dados.items():
                    if palavra in str(chave).lower() or palavra in str(valor).lower():
                        return True
                    if busca_palavra(valor):
                        return True
            elif isinstance(dados, list):
               
                for item in dados:
                    if busca_palavra(item):
                        return True
            elif isinstance(dados, str):
              
                return palavra in dados.lower()
            return False
        
        return busca_palavra(dados)
    
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return False
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return False


caminho_arquivo = 'exemplo.json'
palavra = 'Recife'
existe = palavra_existe_em_json(caminho_arquivo, palavra)
print(f"A palavra '{palavra}' {'existe' if existe else 'não existe'} no arquivo JSON.")
