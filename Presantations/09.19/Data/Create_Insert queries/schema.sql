-- Create Companies table
CREATE TABLE Companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    sector VARCHAR(100),
    headquarters VARCHAR(255),
    founded_date DATE,
    website VARCHAR(255)
);

-- Create Stocks table
CREATE TABLE Stocks (
    stock_id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES Companies(company_id),
    ticker_symbol VARCHAR(10) NOT NULL,
    exchange VARCHAR(50),
    current_price DECIMAL(10, 2)
);


-- Stock History Master table
CREATE TABLE HistoricalData (
    data_id SERIAL NOT NULL,
    stock_id INTEGER NOT NULL,
    date DATE NOT NULL,
    opening_price DECIMAL(10, 2),
    closing_price DECIMAL(10, 2),
    volume BIGINT,
    PRIMARY KEY (stock_id, date)
) PARTITION BY LIST (stock_id);


-- Partition for AAPL (Assuming stock_id for AAPL is 1)
CREATE TABLE HistoricalData_AAPL PARTITION OF HistoricalData FOR VALUES IN (1);

-- Partition for MSFT (Assuming stock_id for MSFT is 2)
CREATE TABLE HistoricalData_MSFT PARTITION OF HistoricalData FOR VALUES IN (2);

-- Partition for AMZN (Assuming stock_id for AMZN is 3)
CREATE TABLE HistoricalData_AMZN PARTITION OF HistoricalData FOR VALUES IN (3);


-- Create Exchanges table
CREATE TABLE Exchanges (
    exchange_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    founded_date DATE,
    number_of_listed_companies INTEGER
);

