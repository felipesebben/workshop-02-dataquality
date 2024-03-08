import pytest
import pandas as pd

from unittest.mock import patch, MagicMock
from sqlalchemy.engine import create_engine

from app.etl import rodar_configuracao, extrair_do_sql


@pytest.fixture
def setup_env_vars(monkeypatch):
    """
    Definir variáveis de ambiente para testes.
    """
    monkeypatch.setenv("POSTGRES_HOST", "localhost")
    monkeypatch.setenv("POSTGRES_USER", "testuser")
    monkeypatch.setenv("POSTGRES_PASSWORD", "testpass")
    monkeypatch.setenv("POSTGRES_DB", "testdb")
    monkeypatch.setenv("POSTGRES_PORT", "5432")


def test_rodar_configuracao_functional(setup_env_vars):
    """
    Testa a função `configuracao` do módulo `etl`.
    """
    expected = {
        "db_host": "localhost",
        "db_user": "testuser",
        "db_pass": "testpass",
        "db_name": "testdb",
        "db_port": "5432",
    }

    config = rodar_configuracao()
    assert (
        config == expected
    )  # Espera-se que rodar_configuracao carregue corretamente as variáveis.

# @pytest.fixture
# def mock_engine():
#     """
#     Fixture que cria um mock de um engine SQLAlchemy.
#     """
#     with patch("sqlalchemy.create_engine") as mock_engine:
#         yield mock_engine

# @pytest.fixture
# def mock_conn(mock_engine):
#     """
#     Fixture que cria mock da conexão como o banco de dados.
#     """
#     mock_conn = MagicMock()
#     mock_engine.return_value.connect.return_value.__enter__.return_value = mock_conn
#     return mock_conn

# def test_extrair_do_sql(mock_conn):
#     """
#     Testa a extração do sql simulando cenário com ferramentas mock.
#     """
#     # Definir a query SQL a ser testada.
#     query = "SELECT * FROM my_table"

#     # Simular os resultados em um conjunto para a query.
#     mock_result_set = pd.DataFrame({
#         "column1": [1, 2, 3],
#         "column2": ["a", "b", "c"]
#     })

#     with patch("pandas.read_sql", return_value=mock_result_set) as mock_read_sql:
#         result_df = extrair_do_sql(query)

#         # Certificar-se que 'pd.read_sql' foi usado com os argumentos corretos.
#         mock_read_sql.assert_called_once()
#         args, kwargs = mock_read_sql.call_args
#         assert args[0] == query
#         assert kwargs["con"] == mock_conn

#         # Validar o DataFrame de retorno
#         pd.testing.assert_frame_equal(result_df, mock_result_set)
