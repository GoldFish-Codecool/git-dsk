select s.ticker_symbol, h."date", h.volume 
from historicaldata h inner join stocks s 
on s.stock_id = h.stock_id
order by volume desc 
limit 10 
