# Write your MySQL query statement below
select Product.product_id, Product.product_name
from Product
join Sales on Sales.product_id = Product.product_id
group by product_id
having min(sale_date) >= '2019-01-01' and max(sale_date) <= '2019-03-31';