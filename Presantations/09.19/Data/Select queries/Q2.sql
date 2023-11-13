select stocks.ticker_symbol, historicaldata."date"  , historicaldata.volume
from historicaldata inner join stocks 
on historicaldata.stock_id = stocks.stock_id
where  ticker_symbol = 'MSFT'
and "date" between '2023-08-07' and '2023-08-11' 