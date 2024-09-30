# CryptoPredictor

CryptoPredictor é uma plataforma que utiliza modelos de Machine Learning para prever o melhor dia e horário para comprar e vender criptomoedas, especificamente Bitcoin e Solana. O projeto utiliza dois tipos de modelos de redes neurais recorrentes: LSTM (Long Short-Term Memory) e GRU (Gated Recurrent Unit), abordando dois pontos de vista diferentes para análise dos dados de mercado. O objetivo do CryptoPredictor é auxiliar investidores de criptomoedas a tomar decisões informadas, fornecendo previsões sobre o momento ideal para realizar transações.

![alt text](gif.gif)

[![Button Click]][Link]

  [Button Click]: https://img.shields.io/badge/Demonstração-37a779?style=for-the-badge
  [Link]: https://drive.google.com/file/d/1Uxo7q5cIMKbGofoXXPzxOACv645wyNuj/view?usp=sharing


## Funcionalidades 

- **Previsão de Compra e Venda**: Utiliza os modelos treinados para fornecer as melhores datas e horários para compra e venda de Bitcoin e Solana.
- **Modelos LSTM e GRU**: A plataforma permite comparar previsões geradas pelos dois modelos para escolher a estratégia mais eficaz.
- **API de Previsão**: FastAPI é utilizada para disponibilizar as previsões para consumo via API.
- **Armazenamento em Banco de Dados**: Utiliza PostgreSQL para armazenar logs do sistema.
- **Interface de Visualização**: Uma plataforma frontend será implementada para visualização das previsões.

## Estrutura de Pastas

```
CryptoPredictor/
├── docs/
│   └── (documentação do projeto)
├── src/
│   ├── backend/
│   │   ├── db/
│   │   ├── logs/
│   │   ├── ml_models/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── main.py
│   │   └── utils/
│   └── frontend/
│   │   └── (código frontend da interface do usuário)
│   ├── database/
│   │   └── (modelo de banco de dados com SQLAlchemy)
│   └── notebooks/
│       └── (notebooks para treinamento dos modelos LSTM e GRU)
```

### Diretórios

- `docs/`: Contém a documentação detalhada do projeto, explicando as funcionalidades e como o sistema foi implementado.
- `src/backend/`: Contém a API FastAPI e o código relacionado ao backend, incluindo a integração com o banco de dados PostgreSQL.
- `src/frontend/`: Interface de usuário para visualização das previsões e histórico de dados.
- `src/database/`: Modelos do banco de dados, configurados com SQLAlchemy para gerenciar as previsões e dados de treinamento.
- `src/notebooks/`: Notebooks usados para treinamento e análise dos modelos de redes neurais LSTM e GRU.


## Execução do projeto

Antes de começar, certifique-se de que você tem o Docker e Docker Compose instalados no seu sistema.

1. Clone o repositório:

```bash
git clone https://github.com/rafaelarojas/pondm7.git
```

2. Navegue até o diretório raiz do projeto:
```bash
cd pondm7
```

3. Crie uma venv
```bash
python3 -m venv venv
```

4. Execute o Docker Compose:
```bash
docker-compose up --build
```
O comando irá baixar as dependências e levantar os containers necessários para o backend, banco de dados, e qualquer outra aplicação configurada no `docker-compose.yml`.

5. Acesse a aplicação:

```arduino
http://localhost:8501
```