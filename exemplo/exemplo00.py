from pydantic import BaseModel, PositiveFloat, PositiveInt

dados = {
    "id_produto": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "nome": ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E", "Produto F", "Produto G", "Produto H", "Produto I", "Produto J"],
    "quantidade": [100, 150, 200, 560, 12, 130, 240, 500, 100, 200],
    "preco": [10.0, 15.0, 20.0, 56.0, 1.2, 13.0, 24.0, 50.0, 10.0, 20.0],
    "categoria": ["eletronicos", "mobilia", "informatica", "decoracao", "eletronicos", 
                  "mobilia", "informatica", "decoracao", "eletronicos", "mobilia"]
}

class SchemaDados(BaseModel):
    """
    Classe para validar os dados.
    """
    id_produto: int
    nome: str
    quantidade: PositiveInt
    preco: PositiveFloat
    categoria: str


venda = {
    "id_produto": 1,
    "nome": "Produto A",
    "quantidade": -10,
    "preco": 10.0,
    "categoria": "eletronicos"
}


# Instanciando a classe SchemaDados
schema = SchemaDados(**venda)
print(schema)
