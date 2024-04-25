"""End-to-end test for the ETL process."""
import csv
import os

from etl import extract, load, transform


def test_etl_end_to_end():
    """Test the entire ETL process from extraction to loading into a CSV
    file."""
    file_path = "transformed_users.csv"
    if os.path.exists(file_path):
        os.remove(file_path)
    try:
        url = "https://jsonplaceholder.typicode.com/users"
        data = extract(url)
        transformed_data = transform(data)
        load(file_path, transformed_data)
        assert os.path.exists(
            file_path), "ETL process did not create the output file."
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assert row['username'].islower(
                ), "Username is not in lowercase."
                assert row['email'].islower(), "Email is not in lowercase."
                assert 'id' in row and 'name' in row and 'city' in row, \
                    "Missing expected fields."
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
