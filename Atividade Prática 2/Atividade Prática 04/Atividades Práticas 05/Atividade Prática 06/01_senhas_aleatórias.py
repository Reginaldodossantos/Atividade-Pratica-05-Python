# Gerador de senha via randomuser.me

import json
from urllib.request import urlopen

# Link solicitado 
# https://randomuser.me/api/?password=upper,lower,1-16

tamanho = int(input("Tamanho da senha (1 a 16): "))

# padrão do link solicitado (upper,lower,1-16)
url_exemplo = f"https://randomuser.me/api/?password=upper,lower,1-{tamanho}"

# Opção 2: senha mais completa (letras + números + símbolos) com tamanho escolhido
url_segura = f"https://randomuser.me/api/?password=special,upper,lower,number,{tamanho}"

# Escolha qual URL usar:
url = url_segura  # troque para url_exemplo se quiser

dados = json.loads(urlopen(url).read().decode("utf-8"))
senha = dados["results"][0]["login"]["password"]

print("\nSenha gerada:", senha)
print("API usada:", url)

