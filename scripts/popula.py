from copy import deepcopy
from uuid import uuid4

import logging
import requests


# Define como faremos o log das ações
logging.basicConfig()
logger = logging.getLogger("intranet_trece.popula")
logger.setLevel(logging.INFO)


# Constantes utilizadas no script
BASE_URL="http://localhost:8080/Plone/++api++"
USUARIO="admin"
SENHA="admin"

CONTEUDOS_BASE = {
    "/documentos": {
        "id": "documentos",
        "@type": "Document",
        "title": "Documentos da Organização",
        "blocks": {
            "a10e3d32-d2b5-4442-923b-e1e5e720948c": {
                "@type": "title"
            },
            "52eb0f0d-6131-4696-a794-510bd086ebac": {
                "@type": "listing"
            },
        },
        "blocks_layout": {
            "items": [
                "a10e3d32-d2b5-4442-923b-e1e5e720948c",
                "52eb0f0d-6131-4696-a794-510bd086ebac"
            ]
        },
        "language": "pt-br",
        "subjects": [
            "Documentos",
            "Arquivos"
        ]
    },
}


def gerar_norma(idx: int=1):
    uid = str(uuid4())
    return {
        "id": f"norma-{idx:02d}",
        "@type": "Document",
        "title": f"Norma {idx:02d}",
        "blocks": {
            uid: {
                "@type": "title"
            },
        },
        "blocks_layout": {
            "items": [
                uid
            ]
        },
        "language": "pt-br",
        "subjects": [
            "Documentos"
        ]
    }



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

# Criar documentos
conteudos = deepcopy(CONTEUDOS_BASE)
for idx in range(1, 30):
    path = "/documentos"
    value = gerar_norma(idx=idx)
    key = f"{path}/{value['id']}"
    conteudos[key] = value

for path, data in conteudos.items():
    url = f"{BASE_URL}{path}"
    response = session.get(url)
    if response.status_code == 200:
        logger.info(f"Conteúdo existente: '{path}'")
        continue
    id_conteudo = data["id"]
    # Obtem o caminho para o "pai" desse novo documento
    # /documentos/norma-001 -> /documentos
    # /documentos ->
    parent = path[:len(path) - len(id_conteudo) - 1]
    parent_url = f"{BASE_URL}{parent}"
    response = session.post(parent_url, json=data)
    if response.status_code > 300:
        logger.error(f"Erro ao criar '{path}': {response.status_code}")
    else:
        logger.info(f"Conteúdo criado: '{path}'")
