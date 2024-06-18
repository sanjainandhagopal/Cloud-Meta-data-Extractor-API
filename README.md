# StreamFetch

StreamFetch is a Python library designed to efficiently stream and process files from various object storage services, including Amazon S3, Azure Blob Storage, and Google Cloud Storage. It enables applications to read the metadata, sample records, and selectively fetch parts of files based on the content type, such as CSV, JSON, or AVRO, without the need to download entire files. This approach is particularly useful for dealing with large datasets, minimizing memory usage and network bandwidth.

## Getting Started

StreamFetch leverages `fsspec` to interact with files stored in various remote backends, determining the appropriate storage interface based on the URL's protocol. Here's how you can get started with StreamFetch for different cloud storage services:

### Amazon S3

StreamFetch supports Amazon S3 via `s3fs`. To access files stored in S3, you need to configure your credentials with env variables as described in the [s3fs documentation](https://s3fs.readthedocs.io/en/latest/#credentials).

To fetch metadata and a few records from a file stored in S3, use the following command:

```bash
streamfetch s3://<bucket-name>/<path>
```

### Azure Blob Storage and Azure Data Lake

StreamFetch uses `adlfs` for interfacing with Azure storage solutions. This includes support for Azure Data Lake (`adl://`) and Azure Blob Storage (`abfs://` or `az://`). For more details on URI structure and configuration options, refer to the [adlfs documentation](https://pypi.org/project/adlfs/).

To work with Azure storage, one method involves configuring the environment variable `AZURE_STORAGE_CONNECTION_STRING`. Here's an example command to read the metadata and a few records from a CSV file in Azure Blob Storage:

```bash
streamfetch abfs://<container-name>/<path> --nrows 6
```

## Development

### Setting Up Your Development Environment

1. **Clone the project repository:**
   ```bash
   git clone git@github.com:abluva-research/streamfetch.git
   cd streamfetch
   ```

2. **Install Poetry:**
   If you don't have Poetry installed, you can install it by following the instructions on the [Poetry documentation](https://python-poetry.org/docs/#installation).

3. **Install dependencies:**
   Run the following command in the project directory to install the project dependencies:
   ```bash
   poetry install
   ```

4. **Activate the virtual environment:**
   To work within the project's virtual environment, run:
   ```bash
   poetry shell
   ```

### Configuring Pre-commit Hooks

1. **Install `pre-commit` (if not already done):**
   ```bash
   poetry add --dev pre-commit
   ```

2. **Set up the pre-commit hooks:**
   Ensure you have a `.pre-commit-config.yaml` file at the root of your project. Then, run:
   ```bash
   pre-commit install
   ```
   This command sets up `pre-commit` to run automatically before each commit to ensure code quality and style consistency.

### Running Tests

Explain how to run the automated tests for this system. For example:
```bash
poetry run pytest
```

### Code Formatting and Linting

- **To automatically format your code with Black and isort**, run:
  ```bash
  poetry run black . && poetry run isort .
  ```

- **To lint your code with Flake8**, run:
  ```bash
  poetry run flake8
  ```

### Contributing

Please refer Git workflow [doc](!https://docs.google.com/document/d/1ha9_iSMC4iUbUJZJ4GW2QiWx5NUtJoE15Oz4qBqlVF8/edit#heading=h.slgcs6xdqoj5).