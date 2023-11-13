select s.ticker_symbol, h."date" , max(volume)
from historicaldata h inner join stocks s 
on s.stock_id = h.stock_id
group by s.ticker_symbol, h."date" 
having  "date" between '2023-08-07' and '2023-08-11'

