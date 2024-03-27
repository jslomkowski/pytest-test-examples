"""Test the quality of the extracted, transformed, and loaded data.
"""
import csv
import os

import pytest

from etl import extract, load, transform


@pytest.fixture(scope="module")
def transformed_data_fixture():
    """Fixture for setting up and tearing down transformed data."""
    url = "https://jsonplaceholder.typicode.com/users"
    data = extract(url)
    transformed_data = transform(data)
    yield transformed_data


@pytest.fixture(scope="module")
def csv_file_fixture(transformed_data_fixture):
    """Fixture for setting up and tearing down the CSV file."""
    file_path = "test_transformed_users.csv"
    load(file_path, transformed_data_fixture)
    yield file_path
    os.remove(file_path)


def test_extracted_data_quality():
    """Test the quality of the extracted data."""
    url = "https://jsonplaceholder.typicode.com/users"
    data = extract(url)
    for item in data:
        assert isinstance(item, dict), "Data item is not a dictionary"
        assert "id" in item, "Missing 'id' in data item"
        assert "name" in item, "Missing 'name' in data item"
        assert "username" in item, "Missing 'username' in data item"
        assert "email" in item, "Missing 'email' in data item"
        assert "address" in item and "city" in item["address"], "Missing 'city' in data item"
        assert item["email"].count("@") == 1, "Invalid email format"


def test_transformed_data_quality(transformed_data_fixture):
    """Test the quality of the transformed data."""
    transformed_data = transformed_data_fixture
    for item in transformed_data:
        assert isinstance(
            item, dict), "Transformed data item is not a dictionary"
        assert "id" in item, "Missing 'id' in transformed data item"
        assert "name" in item, "Missing 'name' in transformed data item"
        assert "username" in item, "Missing 'username' in transformed data item"
        assert "email" in item, "Missing 'email' in transformed data item"
        assert "city" in item, "Missing 'city' in transformed data item"
        assert item["email"].count(
            "@") == 1, "Invalid email format in transformed data"


def test_csv_file_quality(csv_file_fixture):
    """Test the quality of the CSV file."""
    file_path = csv_file_fixture
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            assert "id" in row, "Missing 'id' in CSV row"
            assert "name" in row, "Missing 'name' in CSV row"
            assert "username" in row, "Missing 'username' in CSV row"
            assert "email" in row, "Missing 'email' in CSV row"
            assert "city" in row, "Missing 'city' in CSV row"
            assert row["email"].count("@") == 1, "Invalid email format in CSV"
