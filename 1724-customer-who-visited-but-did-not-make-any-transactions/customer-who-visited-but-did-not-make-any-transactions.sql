select count(v.customer_id) as count_no_trans , v.customer_id from Visits v 
left join Transactions t
on v.visit_id = t.visit_id 
where t.visit_id is NULL 
group by v.customer_id 
; 
