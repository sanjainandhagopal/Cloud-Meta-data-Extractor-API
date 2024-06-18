import click
from streamfetch.detector import detect_file_type
from streamfetch.processors import FILE_PROCESSOR_MAP
import os

os.environ['AZURE_STORAGE_CONNECTION_STRING'] = '<CONNECTION_STRING>'

@click.command()
@click.argument("uri")
@click.option("--nrows", default=5, help="Number of records to fetch")
def main(uri, nrows):
    """StreamFetch CLI tool: Streams and processes files from URLs."""
    click.echo(f"Processing URL: {uri}")
    # Example functionality, replace with actual logic
    file_type = detect_file_type(uri)
    file_processor_cls = FILE_PROCESSOR_MAP[file_type]
    file_processor_client = file_processor_cls(uri)
    click.echo(file_processor_client.head())
    click.echo(file_processor_client.get_records(count=nrows))


if __name__ == "__main__":
    main()
