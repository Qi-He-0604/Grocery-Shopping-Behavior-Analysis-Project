# Grocery-Shopping-Behavior-Analysis-Project
Constructed a database based on data files and analyzed customer's shopping behavior.
There are 4 data files containing the following information:
## Households Data File:  
o hh_id: long integer (PK)
o hh_race: integer
 1: White Caucasian
 2: African American
 3: Asian
 4: Other
o is_latinx: Integer indicating whether
 1 Yes
 2 No
o hh_income: Integer indicating the income bracket.
 3: Under $5k yearly income
 4: $5k ‐ $7.9k
 6: $8k ‐ $9.9k
 8: $10k ‐ $11.9k
 10:  $12k – $14.9k
 11:  $15k – $19.9k
 13:  $20k – $24.9k
 15:  $25k – $29.9k
 16:  $30k – $34.9k
 17:  $35k – $39.9k
 18:  $40k – $44.9k
 19:  $45k – $49.9k
 21:  $50k – $59.9k
 23:  $60k – $69.9k
 26:  $70k – $99.9k
 27: $100.0k or more
o hh_size: integer indicating the number of members composing the household.
 1: Single member
 2: Two members
 3: Three members
 …
 9: Nine or more members
o hh_zip_code: 5 digits zipcode coded as integer
o hh_state: 2 character abbreviation of the state
o hh_residence_type:
 1: One family house
 2: One family house – condo
 3: Two family house
 4: Two family house ‐ condo
 5: Three family house
 6: Three family house –condo
 7: Trailer
 8: Not reported.
## Products Data File:
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
## Purchases Data File:
o TC_id (FK)
o quantity_at_TC_prod_id
o total_price_paid_at_TC_prod_id:
o coupon_value_at_TC_prod_id
o deal_flag_at_TC_prod_id
o prod_id (FK)

In this project, I tried to answer the following questions:
a. How many:
 Store shopping trips are recorded in your database?  
 Households appear in your database?
 Stores of different retailers appear in our data base?
 Different products are recorded?
i. Products per category and products per module
ii. Plot the distribution of products and modules per department
 Transactions?
i. Total transactions and transactions realized under some kind of promotion.
b. Aggregate the data at the household‐monthly level to answer the following questions:
 How many households do not shop at least once on a 3 month periods.
i. Is it reasonable?  
ii. Why do you think this is occurring?
 Loyalism: Among the households who shop at least once a month, which % of them
concentrate at least 80% of their grocery expenditure (on average) on single retailer? And
among 2 retailers?  
i. Are their demographics remarkably different? Are these people richer? Poorer?
ii. What is the retailer that has more loyalists?
iii. Where do they live? Plot the distribution by state.
 Plot with the distribution:
i. Average number of items purchased on a given month.
ii. Average number of shopping trips per month.
iii. Average number of days between 2 consecutive shopping trips.
c. Answer and reason the following questions: (Make informative visualizations)
 Is the number of shopping trips per month correlated with the average number of items
purchased?
 Is the average price paid per item correlated with the number of items purchased?
 Private Labeled products are the products with the same brand as the supermarket. In
the data set they appear labeled as ‘CTL BR’
i. What are the product categories that have proven to be more “Private labelled”
ii. Is the expenditure share in Private Labeled products constant across months?
iii. Cluster households in three income groups, Low, Medium and High. Report the
average monthly expenditure on grocery. Study the % of private label share in
their monthly expenditures. Use visuals to represent the intuition you are
suggesting.
