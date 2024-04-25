"""Unit tests for the ETL process."""
import os

from etl import extract, load, transform

# Define test data directly in the test module
TEST_DATA = [{
    "id": 1,
    "name": "Test User",
    "username": "User1",
    "email": "TEST@EMAIL.COM",
    "address": {"city": "Testville"}
}]


def test_extract():
    """Test that extract function runs without errors for a valid URL."""
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        data = extract(url)
        assert isinstance(data, list), "Extract should return a list"
    except Exception as e:
        assert False, f"Extract function raised an error: {e}"


def test_transform():
    """Test that transform function processes data correctly."""
    transformed_data = transform(TEST_DATA)
    assert isinstance(transformed_data, list), "Transform should return a list"
    assert transformed_data[0]['username'].islower(
    ), "Username should be converted to lowercase"
    assert transformed_data[0]['email'].islower(
    ), "Email should be converted to lowercase"


def test_load():
    """Test that load function runs without errors given valid data and path."""
    test_data = transform(TEST_DATA)
    file_path = "test_output.csv"
    try:
        load(file_path, test_data)
        assert os.path.exists(file_path), "Load function should create a file"
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
