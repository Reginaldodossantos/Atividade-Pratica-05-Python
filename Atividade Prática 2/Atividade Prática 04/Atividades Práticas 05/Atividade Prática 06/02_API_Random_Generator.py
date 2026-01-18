import requests

try:
    response = requests.get("https://randomuser.me/api/?nat=br", timeout=5) 
    
    # Tempo de 5 segundos pela resposta do servidor.”

    if response.status_code == 200:
        dados = response.json()["results"][0]

        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados["email"]
        pais = dados["location"]["country"]
        idade = dados["dob"]["age"]
        cidade = dados["location"]["city"]
        usuario = dados["login"]["username"]

        """
             Estou acrescentando mais código na estrutura.
        """   
        print(f"Idade: {idade} anos")
        print(f"Cidade: {cidade}")
        print(f"Usuário: {usuario}")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao acessar a API. Código:", response.status_code)

except requests.exceptions.RequestException:
    print("Erro de conexão. Verifique sua internet.")
