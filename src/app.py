import os

# SIMULAÇÃO DE VULNERABILIDADE: Senha exposta no código
DATABASE_PASSWORD = "SuperSenhaSecretaSmartShop2026!"

def calcular_total(produtos):
    if not produtos:
        return 0
    return sum(produtos)

def conectar_banco():
    print(f"Conectando com a senha: {DATABASE_PASSWORD}")
    return True
