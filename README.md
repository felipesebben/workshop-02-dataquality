# Workshop 02 | Data Quality em Projetos de Dados
## Introdução ##
Bem-vindo ao meu repositório para o [workshop 02](https://github.com/lvgalvao/workshop_02_aovivo) do excelente [Luciano Galvão](https://www.linkedin.com/in/lucianovasconcelosf/)! Abaixo, é possível acessar a documentação, bem como as instruções de como rodar o projeto, seguidas de um breve descritivo do que foi feito.


## Visite minha documentação! ##
Selecione a imagem abaixo ou vá direto para o [link da documentação](https://felipesebben.github.io/workshop-02-dataquality/).
[![image](/assets/project_workflow.png)](https://felipesebben.github.io/workshop-02-dataquality/)

## Instruções ##
1. Clone o repositório:

```bash
git clone https://github.com/felipesebben/workshop-02-dataquality
cd workshop-02-data-quality
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

3. Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:

```bash
poetry env use 3.11.5
poetry shell
```

4. Instale as dependencias do projeto:

```bash
poetry install
```

5. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
poetry run task test
```

6. Execute o comando para ver a documentação do projeto:

```bash
poetry run task doc
```

7. Execute o comando de execucão da pipeline para realizar a ETL:

```bash
poetry run python app/etl.py
```

## Sobre o projeto ##
Em mais uma das excelentes workshops de [Luciano Galvão](https://github.com/lvgalvao/), abordamos, com mais detalhamento, meios de controle de qualidade e de validação de dados em projetos. 

Nesse caso, executamos um processo de validação do banco de dados. O fluxo é tal como se segue:
- Criamos um banco de dados no Render e populamos com alguns dados. 
- Em seguida, configuramos as variáveis do banco usando variáveis de ambiente (jamais passando credenciais no código!).
- Lemos o banco. Em paralelo, utilizamos o [Pandera](https://github.com/unionai-oss/pandera) para gerar uma validação do Schema de Entrada do banco.
    - O pandera faz uma série de inferências a partir da amostra de dados definidas pela query que fazemos do banco (pode ser o banco todo ou apenas uma amostragem definida pelo programa).

## Contato ##
Para dúvidas, feedback ou qualquer contato:
- Email: felipesebben@yahoo.com.br / sebbencomdoisb@gmail.com
- [LinkedIn](https://www.linkedin.com/in/felipe-sebben)