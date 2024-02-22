from pathlib import Path
from faker import Faker
import logging
import requests
from random import choice

fake = Faker("pt_BR")
# Define como faremos o log das ações
logging.basicConfig()
logger = logging.getLogger("intranet_trece.popula")
logger.setLevel(logging.INFO)


# Constantes utilizadas no script
PASTA_ATUAL = Path(__file__).parent.resolve()
PASTA_DADOS = PASTA_ATUAL / "data"
BASE_URL="http://localhost:8080/Plone/++api++"
USUARIO="admin"
SENHA="admin"

# Cabeçalhos HTTP
headers = {
    "Accept": "application/json"
}

session = requests.Session()
session.headers.update(headers)

# Autenticar o usuário admin utilizando um Token JWT
login_url = f"{BASE_URL}/@login"
response = session.post(login_url, json={"login": USUARIO, "password": SENHA})
data = response.json()
token = data["token"]
session.headers.update(
    {"Authorization": f"Bearer {token}"}
)




AREAS = {
    "/estrutura/secom": {
        "id": "secom",
        "@type": "Area",
        "title": "SECOM",
        "description": "Secretaria de Comunicação",
        "ramal": "0123",
        "tipo_email": "corporativo",
        "email": f"secom@tre-ce.jus.br",
    },
    "/estrutura/sti": {
        "id": "sti",
        "@type": "Area",
        "title": "STI",
        "description": "Secretaria de Tecnologia de Informação",
        "ramal": "0324",
        "tipo_email": "corporativo",
        "email": f"sti@tre-ce.jus.br",
    },
    "/estrutura/sti/seweb": {
        "id": "seweb",
        "@type": "Area",
        "title": "Web",
        "description": "Secretaria de Tecnologia de Informação - Web",
        "ramal": "0087",
        "tipo_email": "corporativo",
        "email": f"sti-seweb@tre-ce.jus.br",
    }
}

# Criar Áreas

for path in AREAS:
    data = AREAS[path]
    parent_path = "/".join(path.split("/")[:-1])[1:]
    response = session.get(f"{BASE_URL}/{path}")
    if response.status_code != 404:
        logger.info(f"Ignorando {BASE_URL}{path}: Conteúdo já existe")
        continue
    response = session.post(f"{BASE_URL}/{parent_path}", json=data)
    if response.status_code > 300:
        logger.error(f"Erro ao criar '{path}': {response.status_code}")
    else:
        logger.info(f"Conteúdo criado: '{path}'")


areas = [path for path in AREAS]
parent_url = f"{BASE_URL}/colaboradores"
for idx in range(1, 50):
    area = choice(areas)
    profile = fake.profile()
    username = profile["username"]
    data = {
        "id": f"{username}",
        "@type": "Pessoa",
        "title": profile["name"],
        "description": profile["job"],
        "cargo": profile["job"],
        "area": [
            {
                "@id": area,
            }
        ],
        "ramal": f"1{idx:03d}",
        "tipo_email": "corporativo",
        "email": f"{username}@tre-ce.jus.br",
    }
    path = data['id']
    response = session.get(f"{parent_url}/{path}")
    if response.status_code != 404:
        logger.info(f"Ignorando {parent_url}/{path}: Conteúdo já existe")
        continue
    response = session.post(parent_url, json=data)
    if response.status_code > 300:
        logger.error(f"Erro ao criar '{path}': {response.status_code}")
    else:
        logger.info(f"Conteúdo criado: '{path}'")
