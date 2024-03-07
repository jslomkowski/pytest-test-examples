# pytest-test-examples# pytest-test-examples

This repository contains examples of tests written using pytest for a simple ETL (Extract, Transform, Load) process. The ETL process extracts user data from a remote source, transforms the data by changing usernames and emails to lowercase and filtering out specific fields, and then loads the data into a local CSV file.

## Files

- `etl.py`: The ETL process implementation.
- `etl_data_quality_test.py`: Data quality tests for the extracted and transformed data.
- `etl_unit_test.py`: Unit tests for the individual parts of the ETL process.
- `etl_integration_test.py`: An integration test for the entire ETL process.

## Running Tests

Ensure you have the required packages installed by running:

```bash
pip install -r requirements.txt
```

After installing pytest, you can run the tests with the following command:

```bash
pytest
```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.
