
select subquery.ticker_symbol, h2."date", subquery.max from

(select s.stock_id, s.ticker_symbol, max(h.closing_price) 
from historicaldata h 
inner join stocks s 
on h.stock_id = s.stock_id 
group by s.stock_id, s.ticker_symbol 
order by s.ticker_symbol ) as subquery

inner join historicaldata h2 on subquery.stock_id = h2.stock_id 

where subquery.max = h2.closing_price 

