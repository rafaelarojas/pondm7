# Modelo

O objetivo central dos modelos desenvolvidos neste projeto é analisar o comportamento de dois dos maiores criptoativos do mercado, o Bitcoin (BTC) e a Solana (SOL), e realizar previsões futuras que possam indicar os melhores momentos para comprar e vender essas criptomoedas em determinado período de tempo. 

Essas previsões têm como foco ajudar investidores e traders a tomarem decisões mais informadas, aproveitando melhor as oscilações de preço no mercado de criptoativos, que é conhecido por sua alta volatilidade e dinamismo.

## Exploração dos Dados

O primeiro passo fundamental foi realizar uma análise detalhada do comportamento histórico de cada uma dessas criptomoedas. Para isso, os dados relacionados ao Bitcoin e à Solana foram coletados e analisados, com o intuito de compreender melhor suas tendências e padrões de preços ao longo do tempo. Essa exploração inicial dos dados foi conduzida através de um notebook, que pode ser acessado [aqui](https://github.com/rafaelarojas/pondm7/blob/main/src/model/exploracao_dados.ipynb).

Durante essa fase, foi possível identificar que os dados estavam organizados em uma linha do tempo, indicando que o comportamento das criptomoedas segue padrões temporais. Essa característica, aliada ao fato de que o mercado de criptoativos tende a seguir ciclos de alta e baixa, tornou evidente que o uso de modelos de séries temporais seria a abordagem mais adequada para as previsões. Modelos desse tipo permitem captar melhor a evolução dos preços ao longo do tempo e prever movimentos futuros com base em dados históricos.
    
Além disso, foram exploradas outras características importantes dos dados, como volume de negociação, valor de abertura, fechamento, máximas e mínimas diárias, entre outros indicadores que podem influenciar o comportamento futuro das criptomoedas. A correlação entre essas variáveis foi analisada para entender melhor como elas interagem e como podem contribuir para as previsões.

A partir dessa exploração inicial, o próximo passo foi avaliar o comportamento dos dados utilizando três modelos distintos de séries temporais: LSTM (Long Short-Term Memory), ARIMA (AutoRegressive Integrated Moving Average) e GRU (Gated Recurrent Unit). Cada um desses modelos foi escolhido por suas características específicas de processamento de dados temporais e capacidade de captura de padrões em séries históricas.

Neste contexto, o modelo ARIMA não possuiu um comportamento adequado, deixou as predições com um valor constante, o que não é adequado visto a volatividade que o mercado de criptomoedas da fato é. Sendo assim, para este projeto, foram utilizados os seguintes modelos:

- Modelo GRU para prever Bitcoin
- Modelo LSTM para prever Bitcoin
- Modelo GRU para prever Solana
- Modelo LSTM para prever Solana