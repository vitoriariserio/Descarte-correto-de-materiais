import sqlite3

def get_dados_residuos():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS residuos(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        residuos TEXT NOT NULL UNIQUE,
        descarte TEXT NOT NULL
    )
    """)

    # cursor.execute("""INSERT INTO residuos(residuos, descarte)
    #            VALUES('papel', 'Lixeira AZUL (papel). Mantenha seco e sem gordura.'),
    #                ('sacola plastica', 'Lixeira VERMELHA (plástico) ou pontos de coleta em supermercados.'),
    #                ('pilha', 'NUNCA jogue no lixo comum. Leve a postos de coleta em supermercados ou lojas.'),
    #                ('celular','NUNCA jogue no lixo comum. Leve a assistências técnicas ou pontos de coleta de eletrônicos.'),
    #                ('pneu','NUNCA jogue em terrenos ou lixo comum. Leve a borracharias ou pontos de coleta municipais.')""")

    conexao.commit()
    cursor.execute("SELECT residuos, descarte FROM residuos")
    resultado = cursor.fetchall()

    dados_residuos = {residuo.lower(): descarte for residuo, descarte in resultado}

    conexao.close()
    return dados_residuos