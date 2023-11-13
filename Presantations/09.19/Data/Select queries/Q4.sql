select s.ticker_symbol, max(h.closing_price - h.opening_price)
from stocks s inner join historicaldata h 
on h.stock_id = s.stock_id 
group by s.ticker_symbol 
order by max(h.closing_price - h.opening_price) desc
limit 1
