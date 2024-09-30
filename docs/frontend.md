# Frontend

Este projeto é uma aplicação de visualização de previsões de preços de criptomoedas, desenvolvida em **Streamlit**. Ele exibe as previsões geradas por modelos GRU e LSTM para **Bitcoin (BTC)** e **Solana (SOL)**, e utiliza gráficos interativos criados com **Plotly**.

## Funcionalidades Principais

### 1. Previsão de Preços
A aplicação oferece duas abas principais, uma para o **BTC-USD** e outra para o **SOL-USD**, cada uma exibindo as seguintes informações:
- Preço previsto para a criptomoeda.
- Melhor hora para comprar e vender, com base nas previsões dos modelos.
- Tabela comparativa das previsões dos modelos GRU e LSTM.

### 2. Gráficos Interativos
Os dados de previsão são visualizados através de gráficos interativos utilizando **Plotly**. Esses gráficos permitem ao usuário ver a evolução dos preços futuros previstos ao longo do tempo, com opções de diferentes cores para as previsões GRU e LSTM:
- **BTC-USD (GRU)**: Exibido em azul.
- **BTC-USD (LSTM)**: Exibido em laranja.
- **SOL-USD (GRU)**: Exibido em verde.
- **SOL-USD (LSTM)**: Exibido em vermelho.

## Estrutura do Código

### 1. Título e Estilos
O título da página é definido como **CryptoPredictor**, e um estilo básico de cor de fundo é aplicado para uma melhor experiência visual:

```python
st.title("CryptoPredictor")
st.markdown("<style>body {background-color: #1e1e1e;}</style>", unsafe_allow_html=True)
```

### 2. Função de Busca de Previsões
A função fetch_predictions(url) é responsável por fazer requisições HTTP ao backend para buscar os dados de previsão. Se houver um erro na solicitação, uma mensagem de erro é exibida:

```python
def fetch_predictions(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching data")
        return None
```

## Como Executar apenas o Frontend
Instale as dependências necessárias com o comando:
```bash
pip install -r requirements.txt
```

Certifique-se de que o backend esteja rodando corretamente em http://backend:8000.

Execute a aplicação Streamlit com o comando:

```
bash
streamlit run app.py
```

Acesse a aplicação no navegador em http://localhost:8501.