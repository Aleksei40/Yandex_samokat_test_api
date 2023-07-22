Select cr.login, COUNT(ord."inDelivery")
FROM "Couriers" AS cr
LEFT JOIN "Orders" AS ord ON cr.id=ord."courierId"
Where ord."inDelivery"=true
Group By cr.login;



SELECT track,
CASE
WHEN "finished"=true THEN 2
WHEN "cancelled"=true THEN -1
WHEN "inDelivery"=true THEN 1
ELSE 0
END
AS status
FROM "Orders";
