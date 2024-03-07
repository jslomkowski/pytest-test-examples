"""Test the quality of the extracted and transformed data."""
import csv
import re

from etl import extract, run_etl


def validate_email(email):
    """Basic email validation."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def test_extracted_data_quality():
    """Test the quality of the extracted data."""
    url = "https://jsonplaceholder.typicode.com/users"
    data = extract(url)

    assert isinstance(data, list), "Extracted data should be a list."
    assert len(data) > 0, "Extracted data should not be empty."

    for item in data:
        assert 'id' in item and isinstance(
            item['id'], int), "Each item must have an integer id."
        assert 'name' in item, "Each item must have a name."
        assert 'username' in item, "Each item must have a username."
        assert 'email' in item and validate_email(
            item['email']), "Each item must have a valid email."
        assert 'address' in item and 'city' in item['address'], \
            "Each item must have an address with a city."


def test_transformed_data_quality():
    """Test the quality of the transformed data."""
    run_etl()
    file_path = "transformed_users.csv"
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            assert 'id' in row and row['id'].isdigit(
            ), "Each row must have an integer id."
            assert 'name' in row, "Each row must have a name."
            assert 'username' in row, "Each row must have a username."
            assert 'email' in row and validate_email(
                row['email']), "Each row must have a valid email."
            assert 'city' in row, "Each row must have a city."
