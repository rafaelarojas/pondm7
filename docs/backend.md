# Backend

Este backend foi desenvolvido utilizando o **FastAPI** para fornecer previsões de preços de criptomoedas usando modelos de deep learning (GRU e LSTM). O backend também oferece um sistema de **retreinamento** dos modelos, presente no arquivo `train_models.py`, além de contar com um banco de dados **PostgreSQL** para armazenar os logs do sistema.

## Rotas Disponíveis

O backend possui as seguintes rotas principais para previsão de preços de criptomoedas:

### 1. `GET /btc/gru`
Previsões de preços do Bitcoin (BTC) utilizando um modelo **GRU**.

- **Modelo utilizado**: `model_gru_btc.h5`
- **Fonte de dados**: `btc_data.csv`
- **Saída**:
  - Datas futuras
  - Previsões de preços
  - Melhor hora para venda
  - Melhor hora para compra

### 2. `GET /btc/lstm`
Previsões de preços do Bitcoin (BTC) utilizando um modelo **LSTM**.

- **Modelo utilizado**: `model_lstm_btc.h5`
- **Fonte de dados**: `btc_data.csv`
- **Saída**:
  - Datas futuras
  - Previsões de preços
  - Melhor hora para venda
  - Melhor hora para compra

### 3. `GET /sol/gru`
Previsões de preços do Solana (SOL) utilizando um modelo **GRU**.

- **Modelo utilizado**: `model_gru_sol.h5`
- **Fonte de dados**: `sol_data.csv`
- **Saída**:
  - Datas futuras
  - Previsões de preços
  - Melhor hora para venda
  - Melhor hora para compra

### 4. `GET /sol/lstm`
Previsões de preços do Solana (SOL) utilizando um modelo **LSTM**.

- **Modelo utilizado**: `model_lstm_sol.h5`
- **Fonte de dados**: `sol_data.csv`
- **Saída**:
  - Datas futuras
  - Previsões de preços
  - Melhor hora para venda
  - Melhor hora para compra

## Retreinamento dos Modelos

O sistema possui um mecanismo de **retreinamento** dos modelos de previsão, disponível no arquivo `train_models.py`. Esse processo permite que os modelos sejam atualizados conforme novos dados de mercado estejam disponíveis, garantindo maior acurácia nas previsões futuras.

## Banco de Dados

O backend também está integrado com um banco de dados **PostgreSQL**. Este banco de dados armazena **logs** do sistema, que incluem informações sobre as operações realizadas e dados importantes para monitoramento e auditoria do sistema. A conexão com o banco de dados é feita por meio da sessão `SessionLocal` e os logs são armazenados na tabela `Log`.

## Tecnologias Utilizadas

- **FastAPI**: Framework utilizado para construção das rotas da API.
- **TensorFlow/Keras**: Utilizado para carregar os modelos de deep learning (GRU e LSTM).
- **Scikit-learn**: Para pré-processamento de dados utilizando o `MinMaxScaler`.
- **YFinance**: Para coleta de dados de criptomoedas em tempo real.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar logs.

## Como Executar apenas o Backend

1. Instale as dependências do projeto.
2. Certifique-se de configurar o banco de dados PostgreSQL e o arquivo `train_models.py` para realizar o retrain dos modelos quando necessário.
3. Inicie a API com:

```bash
uvicorn main:app --reload
```