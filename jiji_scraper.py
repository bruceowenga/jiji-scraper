import requests
import json

s = requests.Session()

# Get user input for the query
query = input("Enter your query: ")
query = query.replace(" ", "+")  # Replace spaces with "+"

page = 1
output_file = f"{query}_listings.json"

# Create a list to store all products
all_products = []

while True:
    url = f"https://jiji.co.ke/api_web/v1/listing?query={query}&page={page}"
    resp = s.get(url)

    if resp.status_code == 200:
        resp_json = resp.json()
        products = resp_json['adverts_list']['adverts']

        if not products:
            # No more pages available, break the loop
            break

        # Append products from the current page to the all_products list
        all_products.extend(products)

        # Increment the page number for the next request
        page += 1

    else:
        print(f"Failed to fetch page {page}. Status code: {resp.status_code}")
        break  # Terminate the loop if there's an error

# Write all_products to the output file in JSON format
with open(output_file, 'w') as file:
    json.dump(all_products, file, indent=4)
