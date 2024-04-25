# pytest-test-examples

This repository contains examples of tests written using pytest for a simple ETL (Extract, Transform, Load) process. The ETL process extracts user dummy data from a remote source, transforms the data by changing usernames and emails to lowercase and filtering out specific fields, and then loads the data into a local CSV file. Based on that process 4 types of tests are available: unit, integration, end-to-end and data quality. Those are ment to be minimalistic so no fixtures or mockups were applied

## Files

- `etl.py`: The ETL process implementation.
- `etl_data_quality_test.py`: Data quality tests for the extracted and transformed data.
- `etl_unit_test.py`: Unit tests for the individual parts of the ETL process.
- `etl_integration_test.py`: An integration test for function pairs.
- `etl_end_to_end_test.py`: An full end-to-end test for whole pipeline.

## Running Tests

Ensure you have the required packages installed by running:

```bash
pip install -r requirements.txt
```

Go to `etl.py` and execute it.
after that you can run the tests with the following command:

```bash
pytest
```

## Test explanation

### Unit Tests

- Definition: Tests that focus on individual components of the code or model in isolation to ensure each part functions correctly by itself.

- Example in Machine Learning: Testing a function that preprocesses data, such as scaling or encoding, to verify it outputs data in the expected format without integrating with model training.

- Example in Data Engineering: Testing a function that extracts data from a source system, ensuring it correctly handles various data types and formats as expected.

### Integration Tests
- Definition: Tests that evaluate the cooperation between multiple components to ensure they work together as expected.

- Example in Machine Learning: Verifying that the data preprocessing pipeline correctly feeds into the model training process, and that the trained model can receive and predict new data accurately.

- Example in Data Engineering: Ensuring that data flows seamlessly through a pipeline from extraction, through transformation stages, and loads accurately into a target database.

### End-to-End Tests
- Definition: Comprehensive tests that simulate a real-world scenario from start to finish to ensure the system behaves as intended when all components are integrated.

- Example in Machine Learning: Running a complete pipeline from data ingestion, preprocessing, model training, and prediction to verify the entire workflow produces the correct outputs.

- Example in Data Engineering: Executing a data pipeline that starts with data extraction, moves through data cleansing, transformation, and ends with loading into a data warehouse, validating the end-to-end data integrity and latency.

### Data Quality Tests
- Definition: Tests that check the accuracy and quality of the data used in machine learning models and data pipelines to ensure it meets the defined standards and requirements.

- Example in Machine Learning: Verifying that training datasets contain no missing values, outliers, or incorrect labels that could adversely affect model training.

- Example in Data Engineering: Ensuring that data loaded into a data warehouse matches expected formats, meets all field constraints, and does not introduce duplicates.

### Regression Tests
- Definition: Tests that ensure new code changes do not disrupt or degrade existing functionalities in the data pipelines or machine learning models.

- Example in Machine Learning: After updates to a model's codebase, verifying that its performance on a standard test set has not decreased compared to previous runs.

- Example in Data Engineering: Checking that changes to a data transformation step do not cause increases in data processing time or errors in subsequent data loads.