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
);

-- Create Exchanges table
CREATE TABLE Exchanges (
    exchange_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    founded_date DATE,
    number_of_listed_companies INTEGER
);

INSERT INTO Companies (name, sector, headquarters, founded_date, website) VALUES 
('Apple', 'Technology', 'Cupertino, CA', '1976-04-01', 'https://www.apple.com'),
('Microsoft', 'Technology', 'Redmond, WA', '1975-04-04', 'https://www.microsoft.com'),
('Amazon', 'E-commerce', 'Seattle, WA', '1994-07-05', 'https://www.amazon.com'),
('Google (Alphabet)', 'Technology', 'Mountain View, CA', '1998-09-04', 'https://www.google.com'),
('Facebook (Meta Platforms)', 'Social Media', 'Menlo Park, CA', '2004-02-04', 'https://www.facebook.com'),
('Tesla', 'Automobile', 'Palo Alto, CA', '2003-07-01', 'https://www.tesla.com'),
('Netflix', 'Entertainment', 'Los Gatos, CA', '1997-08-29', 'https://www.netflix.com'),
('Walmart', 'Retail', 'Bentonville, AR', '1962-07-02', 'https://www.walmart.com'),
('The Walt Disney Company', 'Entertainment', 'Burbank, CA', '1923-10-16', 'https://www.disney.com'),
('Berkshire Hathaway', 'Conglomerate', 'Omaha, NE', '1839-00-00', 'https://www.berkshirehathaway.com'),
('JPMorgan Chase & Co.', 'Finance', 'New York, NY', '2000-12-31', 'https://www.jpmorganchase.com'),
('Visa Inc.', 'Financial Services', 'San Francisco, CA', '1958-09-18', 'https://www.visa.com'),
('Johnson & Johnson', 'Pharmaceuticals', 'New Brunswick, NJ', '1886-01-01', 'https://www.jnj.com'),
('Procter & Gamble', 'Consumer Goods', 'Cincinnati, OH', '1837-10-31', 'https://www.pg.com'),
('Coca-Cola', 'Beverages', 'Atlanta, GA', '1886-05-08', 'https://www.coca-colacompany.com'),
('McDonalds', 'Restaurants', 'Oak Brook, IL', '1955-04-15', 'https://www.mcdonalds.com'),
('Nike, Inc.', 'Apparel', 'Beaverton, OR', '1964-01-25', 'https://www.nike.com'),
('PepsiCo', 'Beverages', 'Purchase, NY', '1965-06-08', 'https://www.pepsico.com'),
('Exxon Mobil', 'Oil and Gas', 'Irving, TX', '1999-11-30', 'https://www.exxonmobil.com'),
('Chevron Corporation', 'Oil and Gas', 'San Ramon, CA', '1879-09-10', 'https://www.chevron.com'),
('Adobe Systems', 'Software', 'San Jose, CA', '1982-12-02', 'https://www.adobe.com'),
('Intel Corporation', 'Semiconductors', 'Santa Clara, CA', '1968-07-18', 'https://www.intel.com'),
('Cisco Systems', 'Technology', 'San Jose, CA', '1984-12-10', 'https://www.cisco.com'),
('IBM', 'Technology', 'Armonk, NY', '1911-06-16', 'https://www.ibm.com'),
('Unilever', 'Consumer Goods', 'London, UK & Rotterdam, Netherlands', '1929-09-02', 'https://www.unilever.com');

INSERT INTO Stocks (company_id, ticker_symbol, exchange, current_price) VALUES 
(1, 'AAPL', 1, 145.00),          -- NASDAQ
(2, 'MSFT', 1, 305.00),          -- NASDAQ
(3, 'AMZN', 1, 3450.00),         -- NASDAQ
(4, 'GOOGL', 1, 2800.00),        -- NASDAQ
(5, 'FB', 1, 360.00),            -- NASDAQ
(6, 'TSLA', 1, 750.00),          -- NASDAQ
(7, 'NFLX', 1, 560.00),          -- NASDAQ
(8, 'WMT', 2, 140.00),           -- NYSE
(9, 'DIS', 2, 180.00),           -- NYSE
(10, 'BRK-A', 2, 420000.00),     -- NYSE
(11, 'JPM', 2, 155.00),          -- NYSE
(12, 'V', 2, 230.00),            -- NYSE
(13, 'JNJ', 2, 165.00),          -- NYSE
(14, 'PG', 2, 140.00),           -- NYSE
(15, 'KO', 2, 55.00),            -- NYSE
(16, 'MCD', 2, 240.00),          -- NYSE
(17, 'NKE', 2, 160.00),          -- NYSE
(18, 'PEP', 1, 150.00),          -- NASDAQ
(19, 'XOM', 2, 60.00),           -- NYSE
(20, 'CVX', 2, 105.00),          -- NYSE
(21, 'ADBE', 1, 520.00),         -- NASDAQ
(22, 'INTC', 1, 55.00),          -- NASDAQ
(23, 'CSCO', 1, 55.00),          -- NASDAQ
(24, 'IBM', 2, 140.00),          -- NYSE
(25, 'UL', 2, 60.00);            -- NYSE

INSERT INTO Exchanges (name, location, founded_date, number_of_listed_companies) VALUES 
('NASDAQ', 'New York, NY', '1971-02-04', 3300),
('NYSE', 'New York, NY', '1792-05-17', 2400);

INSERT INTO HistoricalData (stock_id, date, opening_price, closing_price, volume) VALUES
(1, '2023-08-01', 196.240005, 195.610001, 35175100),
(1, '2023-08-02', 195.039993, 192.580002, 50389300),
(1, '2023-08-03', 191.570007, 191.169998, 61235200),
(1, '2023-08-04', 185.520004, 181.990005, 115799700),
(1, '2023-08-07', 182.130005, 178.850006, 97576100),
(1, '2023-08-08', 179.690002, 179.800003, 67823000),
(1, '2023-08-09', 180.869995, 178.190002, 60378500),
(1, '2023-08-10', 179.479996, 177.970001, 54686900),
(1, '2023-08-11', 177.320007, 177.789993, 51988100),
(1, '2023-08-14', 177.970001, 179.460007, 43675600),
(1, '2023-08-15', 178.880005, 177.449997, 43622600),
(1, '2023-08-16', 177.130005, 176.570007, 46964900),
(1, '2023-08-17', 177.139999, 174.0, 66062900),
(1, '2023-08-18', 172.300003, 174.490005, 61114200),
(1, '2023-08-21', 175.070007, 175.839996, 46311900),
(1, '2023-08-22', 177.059998, 177.229996, 42084200),
(1, '2023-08-23', 178.520004, 181.119995, 52722800),
(1, '2023-08-24', 180.669998, 176.380005, 54945800),
(1, '2023-08-25', 177.380005, 178.610001, 51449600),
(1, '2023-08-28', 180.089996, 180.190002, 43820700),
(1, '2023-08-29', 179.699997, 184.119995, 53003900),
(1, '2023-08-30', 184.940002, 187.649994, 60813900),
(1, '2023-08-31', 187.839996, 187.869995, 60794500);

INSERT INTO HistoricalData (stock_id, date, opening_price, closing_price, volume) VALUES
(2, '2023-08-01', 335.190002, 336.339996, 18311900),
(2, '2023-08-02', 333.630005, 327.5, 27761300),
(2, '2023-08-03', 326.0, 326.660004, 18253700),
(2, '2023-08-04', 331.880005, 327.779999, 23727700),
(2, '2023-08-07', 328.369995, 330.109985, 17741500),
(2, '2023-08-08', 326.959991, 326.049988, 22327600),
(2, '2023-08-09', 326.470001, 322.230011, 22373300),
(2, '2023-08-10', 326.019989, 322.929993, 20113700),
(2, '2023-08-11', 320.26001, 321.01001, 24342600),
(2, '2023-08-14', 321.390015, 324.040009, 18836100),
(2, '2023-08-15', 323.0, 321.859985, 16966300),
(2, '2023-08-16', 320.799988, 320.399994, 20698900),
(2, '2023-08-17', 320.540009, 316.880005, 21257200),
(2, '2023-08-18', 314.48999, 316.480011, 24744800),
(2, '2023-08-21', 317.929993, 321.880005, 24040000),
(2, '2023-08-22', 325.5, 322.459991, 16102000),
(2, '2023-08-23', 323.820007, 327.0, 21166400),
(2, '2023-08-24', 332.850006, 319.970001, 23281400),
(2, '2023-08-25', 321.470001, 322.980011, 21684100),
(2, '2023-08-28', 325.660004, 323.700012, 14808500),
(2, '2023-08-29', 321.880005, 328.410004, 19284600),
(2, '2023-08-30', 328.670013, 328.790009, 15222100),
(2, '2023-08-31', 329.200012, 327.76001, 26411000);

INSERT INTO HistoricalData (stock_id, date, opening_price, closing_price, volume) VALUES
(3, '2023-08-01', 133.550003, 131.690002, 42098500),
(3, '2023-08-02', 130.149994, 128.210007, 51027600),
(3, '2023-08-03', 127.480003, 128.910004, 88585200),
(3, '2023-08-04', 141.059998, 139.570007, 152938700),
(3, '2023-08-07', 140.990005, 142.220001, 71213100),
(3, '2023-08-08', 140.619995, 139.940002, 51710500),
(3, '2023-08-09', 139.970001, 137.850006, 50017300),
(3, '2023-08-10', 139.070007, 138.559998, 58928400),
(3, '2023-08-11', 137.399994, 138.410004, 42832100),
(3, '2023-08-14', 138.300003, 140.570007, 47148700),
(3, '2023-08-15', 140.050003, 137.669998, 42781500),
(3, '2023-08-16', 137.190002, 135.070007, 41675900),
(3, '2023-08-17', 135.460007, 133.979996, 48354100),
(3, '2023-08-18', 131.619995, 133.220001, 48469400),
(3, '2023-08-21', 133.740005, 134.679993, 41442500),
(3, '2023-08-22', 135.080002, 134.25, 32935100),
(3, '2023-08-23', 134.5, 135.520004, 42801000),
(3, '2023-08-24', 136.399994, 131.839996, 43646300),
(3, '2023-08-25', 132.470001, 133.259995, 44147500),
(3, '2023-08-28', 133.779999, 133.139999, 34108400),
(3, '2023-08-29', 133.380005, 134.910004, 38646100),
(3, '2023-08-30', 134.929993, 135.070007, 36137000),
(3, '2023-08-31', 135.059998, 138.009995, 58781300);
