select s.ticker_symbol, max(volume)
from historicaldata h inner join stocks s 
on s.stock_id = h.stock_id
group by s.ticker_symbol 
limit 1
