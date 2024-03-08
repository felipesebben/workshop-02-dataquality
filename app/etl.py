import os
from pathlib import Path

import duckdb
import pandas as pd
import pandera as pa
from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.schema import ProdutoSchema, ProdutoSchemaKPI


def rodar_configuracao():
    """
    Carrega as configuraçãoes a partir de variáveis de ambiente.
    """
    dotenv_path = Path.cwd() / ".env."
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "db_host": os.getenv("POSTGRES_HOST"),
        "db_user": os.getenv("POSTGRES_USER"),
        "db_pass": os.getenv("POSTGRES_PASSWORD"),
        "db_name": os.getenv("POSTGRES_DB"),
        "db_port": os.getenv("POSTGRES_PORT"),
    }

    return settings


@pa.check_output(ProdutoSchema, lazy=True)
def extrair_do_sql(query: str) -> pd.DataFrame:
    """
    Extrai os dados do banco de dados. Retorna um DataFrame.

    Args:
        `query`: A query SQL a ser executada.

    Returns:
        Um `DataFrame` do Pandas contendo os dados extraídos.
    """

    # Criar a string de conexão com base nas configurações fornecidas.
    settings = rodar_configuracao()

    # Criar a string de conexão com base nas configurações fornecidas.
    conn_str = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"
    # Criar engine de conexão.
    engine = create_engine(conn_str)

    with engine.connect() as conn, conn.begin():  # usar o with para fechar a conexão após o uso.
        df_crm = pd.read_sql(query, conn)

    return df_crm


@pa.check_input(ProdutoSchema, lazy=True)
@pa.check_output(ProdutoSchemaKPI, lazy=True)
def transformar(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma os dados do DataFrame ao aplicar cálculos e normalizações.

    Args:
        df: DataFrame do Pandas com os dados originais da camada bronze.

    Returns:
        DataFrame do pandas com as transformações aplicadas.
    """
    # Calcular valor_total_estoque
    df["valor_total_estoque"] = df["quantidade"] * df["preco"]

    # Normalizar categoria para maiúsculas
    df["categoria_normalizada"] = df["categoria"].str.upper()

    # Determinar disponibilidade (True se quantidade > 0)
    df["disponibilidade"] = df["quantidade"] > 0

    return df


@pa.check_input(ProdutoSchemaKPI, lazy=True)
def carregar_para_duckdb(df: pd.DataFrame, table_name: str, db_file="my_duckdb.db"):
    """
    Carrega o DataFrame no DuckDB, criando ou substituindo a tabela especificada como argumento para o parâmetro.

    Args:
        df: DataFrame do Pandas para ser carregado no DuckDB.
        table_name: Nome da tabela no DuckDB onde os dados serão inseridos.
        db_file: Caminho para o arquivo DuckDB. Caso não exista, será criado.

    """
    # Conectar ao DuckDB. Caso o arquivo não exista, será criado.
    con = duckdb.connect(database=db_file, read_only=False)

    # Registrar o DataFrame como uma tabela temporária.
    con.register("df_temp", df)

    # Utilizar SQL para inserir os dados da tabela temporária em uma tabela permanente.
    # Caso a tabela já existir, substitui-la.
    con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df_temp;")

    # Fechar a conexão.
    con.close()


if __name__ == "__main__":
    query = "SELECT * FROM produtos_bronze_email;"
    df_crm = extrair_do_sql(query=query)
    df_crm_kpi = transformar(df_crm)

    schema_crm = pa.infer_schema(df_crm)

    with open("inferred_schema_crm.json", "w", encoding="utf-8") as file:
        file.write(schema_crm.to_json())

    carregar_para_duckdb(df=df_crm_kpi, table_name="tabela_kpi")
