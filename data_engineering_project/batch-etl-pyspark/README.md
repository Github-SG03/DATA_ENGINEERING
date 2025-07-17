# batch-etl-pyspark

## Overview
The `batch-etl-pyspark` project is designed to facilitate the extraction, transformation, and loading (ETL) of e-commerce sales data. This pipeline processes raw sales data to generate valuable insights and analytics that can drive business decisions.

## Project Structure
The project is organized into the following main directories and files:

- **src/**: Contains the source code for the ETL pipeline and analytics.
  - **etl/**: Includes scripts for extracting, transforming, and loading data.
    - `extract.py`: Functions for extracting data from various sources.
    - `transform.py`: Functions for cleaning and transforming the extracted data.
    - `load.py`: Functions for loading the transformed data into the desired format.
  - **analytics/**: Contains scripts for analyzing the processed data.
    - `sales_metrics.py`: Functions to calculate various sales metrics.
    - `customer_segmentation.py`: Functions for segmenting customers based on behavior.
  - **utils/**: Utility functions to support the ETL processes.
    - `spark_session.py`: Manages the Spark session configuration.
  - **config/**: Configuration settings for the project.
    - `settings.py`: Reads environment variables and constants.

- **data/**: Directory for storing data files.
  - **raw/**: Contains raw input data files (e.g., `customers.csv`, `products.csv`, `orders.csv`).
  - **processed/**: Holds processed data files after the ETL pipeline runs.
  - **analytics/**: Stores analytics outputs or reports.

- **tests/**: Contains unit tests for the ETL and analytics functions.
  - `test_extract.py`: Unit tests for the extraction functions.
  - `test_transform.py`: Unit tests for the transformation functions.
  - `test_load.py`: Unit tests for the loading functions.
  - `test_sales_metrics.py`: Unit tests for sales metrics calculations.

- **requirements.txt**: Lists the Python dependencies required for the project.

- **.gitignore**: Specifies files and directories to be ignored by Git.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd batch-etl-pyspark
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare the raw data files in the `data/raw` directory.

4. Run the ETL pipeline:
   - Execute the main ETL script (to be created) that orchestrates the extraction, transformation, and loading processes.

## Usage Examples
- To extract data from CSV files, call the functions defined in `extract.py`.
- Use `transform.py` to clean and derive KPIs from the extracted data.
- Load the processed data using the functions in `load.py`.
- Analyze the results with the functions in `sales_metrics.py` and `customer_segmentation.py`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.