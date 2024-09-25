import requests
from pymongo import MongoClient

# Configurações da API Clash Royale
API_URL = 'https://api.clashroyale.com/v1'
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjZmYmE1ZDczLTM5ZTMtNGZlYi04NjUxLTRiMWY4ZjQwNmMyMiIsImlhdCI6MTcyNzI4OTA4NCwic3ViIjoiZGV2ZWxvcGVyL2Q4MjU4ZDQ2LWY4MTYtNjNkNi1kMzU4LTc5MmJiZmU0NDhkOCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODEuMTc0LjIwOC4xNzIiXSwidHlwZSI6ImNsaWVudCJ9XX0.UKI6SxaBzoUEmgyoiGdSh_YzhznOPlm6qMOAZ_q7NpkGvfT7JErDl0_KigLUOCHE1ERbsjzoT3Lk8hzfz4bLeA'
}

# Obter dados de um jogador específico
player_tag = 'PLAYER_TAG'
response = requests.get(f'{API_URL}/players/%232VGG29RJ2', headers=headers)

# Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['clash_royale']
players_collection = db['players']

# Salvar os dados do jogador no MongoDB
if response.status_code == 200:
    players_collection.insert_one(response.json())
    print("Dados do jogador inseridos com sucesso!")
else:
    print("Erro ao buscar os dados:", response.status_code)
