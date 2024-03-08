# Workshop 02 - Data Quality em Projetos de Dados

Bem-vindo à documentação do Workshop 02, focado na implementação de **data quality** em projetos de dados. 
## Objetivo
Desenvolver uma ETL com testes de qualidade de dados. Visa-se impedir que erros subam para as etapas finais do pipeline (o famoso "gold" no padrão medalhão).

## Fluxo do projeto
Abaixo, segue o fluxo de trabalho que iremos implementar.

```mermaid
graph TD;
    A[Configura Variáveis] --> B[Ler o Banco SQL];
    B --> V[Validação do Schema de Entrada];
    V -->|Falha| X[Alerta de Erro];
    V -->|Sucesso| C[Transformar os KPIs];
    C --> Y[Validação do Schema de Saída];
    Y -->|Falha| Z[Alerta de Erro];
    Y -->|Sucesso| D[Salvar no DuckDB];
```


## Contrato de dados

::: app.schema.ProdutoSchema