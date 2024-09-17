CREATE TABLE IF NOT EXISTS historical_prices (
    id SERIAL PRIMARY KEY,
    asset VARCHAR(50) NOT NULL,        -- Nome ou símbolo do ativo, ex: BTC, SOL
    date TIMESTAMP NOT NULL,           -- Data e hora do preço
    open_price DECIMAL(15, 8),         -- Preço de abertura
    close_price DECIMAL(15, 8),        -- Preço de fechamento
    created_at TIMESTAMP DEFAULT NOW() -- Timestamp de criação
);

CREATE TABLE IF NOT EXISTS trade_recommendations (
    id SERIAL PRIMARY KEY,
    asset VARCHAR(50) NOT NULL,        -- Nome ou símbolo do ativo
    recommendation_type VARCHAR(10) CHECK (recommendation_type IN ('BUY', 'SELL')),  -- Tipo de recomendação (compra ou venda)
    price DECIMAL(15, 8) NOT NULL,     -- Preço sugerido
    timestamp TIMESTAMP NOT NULL,      -- Hora da recomendação
    created_at TIMESTAMP DEFAULT NOW() -- Timestamp de criação
);

CREATE INDEX idx_historical_prices_asset_date ON historical_prices (asset, date);
CREATE INDEX idx_trade_recommendations_asset ON trade_recommendations (asset);
