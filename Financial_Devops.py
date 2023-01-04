import pandas as pd
import os
import csv

# Write your code here
customer_dir = '/root/customers'
file_name = 'data.csv'
file_path = os.path.join(customer_dir, file_name)
data = pd.read_csv(file_path)
customer_count = len(data['NAME'])

print(f'Total customers:')
print(customer_count)

customers_count_city = data.groupby(['CITY'])['ID'].count().reset_index()
print('Customers by city:')
# for i in range(len(customers_count_city.CITY)):
#     print(f'{customers_count_city.CITY.iloc[i]}: {customers_count_city.ID.iloc[i]}')

for k,v in customers_count_city.iterrows():
    print(f'{v.CITY}: {v.ID}')

customers_count_country = data.groupby(['COUNTRY'])['ID'].count().reset_index()
print('Customers by country:')
for i in range(len(customers_count_country.COUNTRY)):
    print(f'{customers_count_country.COUNTRY.iloc[i]}: {customers_count_country.ID.iloc[i]}')

print("Country with the largest number of customers' contracts:")
contracts_count_country = data.groupby(['COUNTRY'])['CONTRCNT'].sum().reset_index()
target_index = contracts_count_country['CONTRCNT'].idxmax
largest_contracts = int(max(contracts_count_country.CONTRCNT))
largest_contract_countries = contracts_count_country.COUNTRY[
    contracts_count_country.CONTRCNT == max(contracts_count_country.CONTRCNT)]
largest_country = max(largest_contract_countries, key=len)

largest_contract_country = contracts_count_country[
    (contracts_count_country.CONTRCNT == int(max(contracts_count_country.CONTRCNT))) &
    (contracts_count_country.COUNTRY == largest_country)]

print(f'{largest_contract_country.COUNTRY.iloc[0]} ({largest_contract_country.CONTRCNT.iloc[0]} contracts)')
print('Unique cities with at least one customer:')
unique_cities_with_min_one_cust = len(customers_count_city[customers_count_city.ID >= 1].CITY.unique())
print(unique_cities_with_min_one_cust)

