import requests


def consultar_cep(cep: str) -> None:

    
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print("Erro: falha na requisição à API ViaCEP.")
        return

    dados = response.json()

    if dados.get("erro"):
        print("Erro: CEP não encontrado.")
        return

    logradouro = dados.get("logradouro", "Não informado")
    bairro = dados.get("bairro", "Não informado")
    cidade = dados.get("localidade", "Não informado")
    estado = dados.get("uf", "Não informado")

    print("\nInformações do CEP")
    print("------------------")
    print(f"Logradouro: {logradouro}")
    print(f"Bairro: {bairro}")
    print(f"Cidade: {cidade}")
    print(f"Estado: {estado}")


def main():
    cep = input("Digite o CEP (apenas números): ").strip()
    consultar_cep(cep)


if __name__ == "__main__":
    main()
