"""Simple example of an ETL process using Python."""
import csv

import requests


def extract(url):
    """Extract data from the given URL."""
    response = requests.get(url, timeout=10)
    data = response.json()
    return data


def transform(data):
    """Transform data by filtering out specific fields, formatting, and
    changing username and email to lowercase."""
    transformed_data = []
    for item in data:
        transformed_item = {
            "id": item["id"],
            "name": item["name"],
            "username": item["username"].lower(),
            "email": item["email"].lower(),
            "city": item["address"]["city"]
        }
        transformed_data.append(transformed_item)
    return transformed_data


def load(file_path, data):
    """Load data into a local CSV file."""
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(
            file, fieldnames=["id", "name", "username", "email", "city"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def run_etl():
    """Orchestrate the ETL process."""
    url = "https://jsonplaceholder.typicode.com/users"
    file_path = "transformed_users.csv"
    data = extract(url)
    transformed_data = transform(data)
    load(file_path, transformed_data)
    print("ETL process completed successfully. Data saved to:", file_path)


if __name__ == "__main__":
    run_etl()
