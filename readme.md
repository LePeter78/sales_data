# Sales Data
This project simulates the sales of a company and processes its data for analysing.

## Handling data:
The *data_handler.ipynb* notebook reads the data from *raw_data.csv*. It filters dirty data, such as missing or unknown values, or invalid numbers. Dirty data is not corrected, only marked as **NA**.
The processed data gets stored in 3 *.json* files:
- all_sales.json: every processed record.
- faulty_data.json: only records with missing or incorrect data.
- verified_sales.json: records with no fault, ready for further processing.

## Queries:
Verified sales are used for queries in *queries.ipnyb*. Currently the following queries exist:
- Total Revenue: the sum of the values of all sold products.
- Sales by Category: a list of categories with their total values sold, in decreasing order.
- Top Customer: the customer with the most amount of money spent on products.
- Top Products: a list of products with the most amount sold.
- Most Valuable Day: the day the most amounty of money was made

## Used technologies:
Used technologies:
Visual Studio Code
Python:
- json
- csv
- jupyter notebook
- pandas

## Next Update:
Implementing more advanced file managment, using the **Pathlib** library