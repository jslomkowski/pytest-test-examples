"""Component integration tests for the ETL process."""

import os

from etl import extract, load, transform


def test_extract_and_transform_integration():
    """Test the integration between extract and transform functions."""
    data = extract("https://jsonplaceholder.typicode.com/users")
    transformed_data = transform(data)
    assert isinstance(transformed_data,
                      list), "Transformed data should be a list"
    assert len(transformed_data) > 0, "Transformed data should not be empty"
    assert transformed_data[0]['username'].islower(
    ), "Username should be lowercase in transformed data"


def test_transform_and_load_integration(tmp_path):
    """Test the integration between transform and load functions."""
    file_path = tmp_path / "test_output.csv"
    test_data = [
        {"id": 1, "name": "Test User", "username": "User1",
            "email": "TEST@EMAIL.COM", "address": {"city": "Testville"}}
    ]
    transformed_data = transform(test_data)
    load(file_path, transformed_data)
    assert os.path.exists(
        file_path), "CSV file should be created by load function"
    with open(file_path, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        assert len(
            lines) >= 2, "CSV file should contain headers and at least one row of data"
