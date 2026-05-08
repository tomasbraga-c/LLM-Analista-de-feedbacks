
import json
import re

from contato_llm import recebe_linhas_retorna_jason


lista_de_resenhas = []

with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

lista_r_json = []


for resenha in lista_de_resenhas:
    resenha_json = recebe_linhas_retorna_jason(resenha)
    resenha_json = resenha_json.replace("\n", " ")
    resenha_json = resenha_json.replace("\t", " ")
    resenha_json = resenha_json.replace("\r", " ")
    resenha_json = re.sub(r'\\"(?=\s*[,\}])', '"', resenha_json)
    resenha_dict = json.loads(resenha_json)
    if isinstance(resenha_dict, list):
        lista_r_json.extend(resenha_dict)
    else:
        lista_r_json.append(resenha_dict)


def contador_julgamento(lista_de_dicionario):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0
    lista_de_dicionario_str = []
    for dicionario in lista_de_dicionario:
        if dicionario['Avaliação'] == 'Positivo':  
            contador_positivas += 1
        elif dicionario['Avaliação'] == 'Negativo': 
            contador_negativas += 1
        else:
            contador_neutras += 1
        lista_de_dicionario_str.append(str(dicionario))
    textos_unidos = " [----] ".join(lista_de_dicionario_str)  
    return contador_positivas, contador_negativas, contador_neutras, textos_unidos


pos, neg, neut, textos = contador_julgamento(lista_r_json)

print(f"Postivas: {pos}")
print(f"Negativas: {neg}")
print(f"Neutras: {neut}")