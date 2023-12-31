# Jiji Web Scraper

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

The Jiji Web Scraper is a Python script that allows you to extract product listings from the Jiji.co.ke website. It provides a convenient way to collect product data for analysis, research, or any other purpose.

## Features

- Search for products on Jiji.co.ke based on a user-defined query.
- Replace spaces in the query with "+" signs automatically.
- Retrieve product listings from multiple pages of search results.
- Save the scraped data in a JSON file for further processing.

## Prerequisites

Before using the scraper, ensure you have the following:

- Python 3.7 or higher installed.
- The requests library (you can install it using `pip install requests`).

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/jiji-web-scraper.git
   cd jiji-web-scraper
   ```

2. Run the scraper"

   ```
   python scraper.py

   ```

3. You will be prompted to enter your query. Input your desired search query, and spaces will be automatically replaced with "+" signs.

4. The scraper will start fetching data from the Jiji.co.ke API. It will retrieve product listings from multiple pages of search results.

5. The scraped product data will be saved to a JSON file named after your query, e.g., optiplex+i7_listings.json.

## Customization

You can customize the scraper by modifying the scraper.py script to extract specific fields or perform additional data processing.

## Disclaimer

This scraper is intended for educational and research purposes only. Be sure to use it responsibly and in compliance with Jiji.co.ke's terms of service and all applicable laws and regulations.

## License

This project is licensed under the MIT License.

Please remember to replace `"https://github.com/yourusername/jiji-web-scraper.git"` with the actual URL of your GitHub repository if you plan to host the scraper there. You can also tailor the README to your specific needs or preferences.
