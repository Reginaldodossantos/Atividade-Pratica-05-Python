import sys, requests

BASE = "https://economia.awesomeapi.com.br/json/last/"

def par(m):
    m = m.strip().upper()
    return m if "-" in m else f"{m}-BRL"

raw = sys.argv[1:] or input("Moedas: (USD,EUR,BTC) ").replace(";", ",").split(",")
moedas = [par(x) for x in raw if x.strip()]
if not moedas:
    print("Erro: nenhuma moeda informada.")
    raise SystemExit(1)

url = BASE + ",".join(dict.fromkeys(moedas))

try:
    r = requests.get(url, timeout=10)
except requests.RequestException as e:
    print("Erro: requisição falhou.")
    raise SystemExit(1)

if not r.ok:
    print("Erro: requisição falhou.")
    raise SystemExit(1)

try:
    data = r.json()
except Exception:
    print("Erro: requisição falhou.")
    raise SystemExit(1)

for _, i in data.items():
    print(f"\n{i.get('name','?')} ({i.get('code','?')}/{i.get('codein','BRL')})")
    print(f"Atual: {float(i.get('bid','nan')):.2f} | Máx: {float(i.get('high','nan')):.2f} | Mín: {float(i.get('low','nan')):.2f}")
    print(f"Atualizado: {i.get('create_date','N/A')}")

