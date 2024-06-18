from .base import RecordProcessor
import fsspec
import pandas as pd
import pyarrow as pa
import chardet
from io import StringIO, BytesIO


class StructuredReader(RecordProcessor):
    def __init__(self, uri: str) -> None:
        super().__init__()
        self.uri = uri
        self.metadata: dict = None
        self.chunk: bytes = None

    def get_records(self, count: int, **kwargs) -> dict:
        metadata = self.head()
        encoding = metadata["encoding"]
        # sep None to make pandas sniff it
        df_iter = self.csvReader(count, encoding)
        df = next(df_iter)
        table = pa.Table.from_pandas(df)
        return table

    def head(self, **kwargs):
        if self.metadata:
            return self.metadata
        encoding = "utf-8"
        with fsspec.open(self.uri, mode="rb", encoding=None) as f:
            # Read 10KB chunk, could draw less rows in case of large no of colums
            self.chunk: bytes = f.read(1024)
            encoding_pred = chardet.detect(self.chunk)
            self.metadata = f.details
        if encoding_pred["confidence"] > 0.8:
            encoding = encoding_pred["encoding"]
        self.metadata["encoding"] = encoding
        return self.metadata
    
    def csvReader(self, count, encoding=None, separator=','):
        df = pd.read_csv(
            BytesIO(self.chunk),
            sep=separator,
            encoding=encoding,
            chunksize=count,
            engine="python",
            on_bad_lines="skip",
        )
        return df