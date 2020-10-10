# Grocery-Shopping-Behavior-Analysis-Project
Constructed a database based on data files and analyzed customer's shopping behavior.

There are 4 data files containing the following information:
### Households Data File:  
o hh_id: long integer (PK)/
o hh_race: integer/
o is_latinx: Integer indicating whether/
o hh_income: Integer indicating the income bracket.
o hh_size: integer indicating the number of members composing the household.
o hh_zip_code: 5 digits zipcode coded as integer
o hh_state: 2 character abbreviation of the state
o hh_residence_type

### Products Data File:
o brand_at_prod_id
o department_at_prod_id
o prod_id (PK)
o group_at_prod_id
o module_at_prod_id
o amount_at_prod_id
o units_at_prod_id
## Trips Data File:
o hh_id (FK)
o TC_date
o TC_retailer_code
o TC_retailer_code_store_code
o TC_retailer_code_store_zip3
o TC_total_spent:
o TC_id (PK)
### Purchases Data File:
o TC_id (FK)
o quantity_at_TC_prod_id
o total_price_paid_at_TC_prod_id:
o coupon_value_at_TC_prod_id
o deal_flag_at_TC_prod_id
o prod_id (FK)

## In this project, I tried to answer the following questions:
### a. How many:
1. Store shopping trips are recorded in your database?  
2. Households appear in your database?
3. Stores of different retailers appear in our data base?
4. Different products are recorded?
i. Products per category and products per module
ii. Plot the distribution of products and modules per department
5. Transactions?
i. Total transactions and transactions realized under some kind of promotion.
### b. Aggregate the data at the household‐monthly level to answer the following questions:
1. How many households do not shop at least once on a 3 month periods.
i. Is it reasonable?  
ii. Why do you think this is occurring?
2. Loyalism: Among the households who shop at least once a month, which % of them
concentrate at least 80% of their grocery expenditure (on average) on single retailer? And
among 2 retailers?  
i. Are their demographics remarkably different? Are these people richer? Poorer?
ii. What is the retailer that has more loyalists?
iii. Where do they live? Plot the distribution by state.
3. Plot with the distribution:
i. Average number of items purchased on a given month.
ii. Average number of shopping trips per month.
iii. Average number of days between 2 consecutive shopping trips.
### c. Answer and reason the following questions: (Make informative visualizations)
1. Is the number of shopping trips per month correlated with the average number of items
purchased?
2. Is the average price paid per item correlated with the number of items purchased?
3. Private Labeled products are the products with the same brand as the supermarket. In
the data set they appear labeled as ‘CTL BR’
i. What are the product categories that have proven to be more “Private labelled”
ii. Is the expenditure share in Private Labeled products constant across months?
iii. Cluster households in three income groups, Low, Medium and High. Report the
average monthly expenditure on grocery. Study the % of private label share in
their monthly expenditures. Use visuals to represent the intuition you are
suggesting.
