import requests

def cep(cep):    
    try:
        response=requests.get(url=f"https://viacep.com.br/ws/{cep}/json/",params={})
        return response.json()        
    except:
        print("exception ocurred")

current_cep=input("Digite um cep válido, com 8 digitos: ")
current_address=cep(current_cep)
print(f"{current_address['logradouro']}, {current_address['bairro']}, {current_address['localidade']}, {current_address['uf']}")