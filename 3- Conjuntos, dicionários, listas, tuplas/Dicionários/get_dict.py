princesas = {
    "aurora@outlook.com": {"nome": "Aurora", "apelido": "Bela Adormecida", "telefone": "1253-8762"},
}

princesas["chave"] #KeyError

princesas.get("chave")
princesas.get("chave", {})
princesas.get("aurora@outlook.com", {})