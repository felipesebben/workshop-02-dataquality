import pandera as pa
from pandera.typing import DataFrame, Series

email_regex = r"[^@]+@[^@]+\.[^@]+"


class ProdutoSchema(pa.SchemaModel):
    """
    Define o esquema para a validação de dados de produtos utilizando o Pandera.

    Este esquema inclui campos básicos para produtos.

    Attributes:
        id_produto (Series[int]): Identificador do produto.
        nome (Series[str]): Nome do produto.
        quantidade (Series[int]): Quantidade disponível do produto, deve estar entre 10 e 800.
        preco (Series[float]): Preço do produto, deve estar entre 1.0 e 310.0.
        categoria (Series[str]): Categoria do produto.
        email (Series[str]): E-mail associado ao produto, deve seguir o formato padrão de e-mails.

    """

    id_produto: Series[int]
    nome: Series[str]
    quantidade: Series[int] = pa.Field(
        ge=10,  # greater_than_or_equal_to min_value=10.0
        le=800,  # less_than_or_equal_to max_value=800.0
        nullable=False,
    )
    preco: Series[float] = pa.Field(
        ge=10.0,  # greater_than_or_equal_to min_value=10.0
        le=310.0,  # less_than_or_equal_to max_value=310.0
        nullable=False,
    )
    categoria: Series[str]
    email: Series[str] = pa.Field(regex=email_regex)

    class Config:
        coerce = True
        strict = True  # if you want to ensure no extra columns are present


class ProdutoSchemaKPI(pa.SchemaModel):
    """
    Define o esquema para a validação de dados dos KPI criados utilizando o Pandera.

    Este esquema os campos resultantes de agregações.

    Attributes:
        valor_total_estoque (Series[float]): Valor total disponível em estoque. Resulta do cálculo `preco` x `quantidade`.
        categoria_normalizada (Series[str]): Categoria normalizada sem letras maiúsculas.
        disponibilidade (Series[bool]): Identificador booleano que retorna `True` se a quantidade do produto for maior que zero.

    """

    valor_total_estoque: Series[float] = pa.Field(
        ge=0
    )  # O valor total em estoque deve ser >=0
    categoria_normalizada: Series[
        str
    ]  # Assume-se que a categoria será uma sting, sem necessidade de quaisquer outras validaç~eos.
    disponibilidade: Series[bool]
