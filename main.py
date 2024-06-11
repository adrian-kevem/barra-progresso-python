from tqdm import tqdm
import requests
import os

with open("ceps.txt", "r") as arquivo:
    ceps_list = arquivo.readlines()

ceps = []
for cep in ceps_list:
    ceps.append(cep.strip())

enderecos = []
endereco = {}

for cep in tqdm(ceps):
    link = f"https://cep.awesomeapi.com.br/json/{cep}"
    requisicao = requests.get(link)
    resposta = requisicao.json()
    endereco = {
        "CEP": cep,
        "Rua": resposta["address_name"],
        "Bairro": resposta["district"],
        "Cidade": resposta["city"],
        "Estado": resposta["state"]
    }
    enderecos.append(endereco)

os.system("cls" if os.name == 'nt' else "clear")

for item in enderecos:
    print(f"CEP: {item["CEP"]}")
    print(f"Rua: {item["Rua"]}")
    print(f"Bairro: {item["Bairro"]}")
    print(f"Cidade: {item["Cidade"]}")
    print(f"Estado: {item["Estado"]}")
    print("\n===================================================\n")
