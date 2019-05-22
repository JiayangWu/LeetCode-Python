# Write your MySQL query statement below
select Name as Customers
from Customers
where not Customers.Id in (select CustomerId
                           from Orders)