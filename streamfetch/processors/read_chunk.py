from .base import RecordProcessor
import fsspec
import chardet
from io import BytesIO
from pyspark.sql import SparkSession

class ChunkReader(RecordProcessor):
    def __init__(self, uri: str) -> None:
        super().__init__()
        self.uri = uri
        self.metadata: dict = None
        self.chunk: bytes = None
        self.sample_size = None

    def head(self, **kwargs):
        if self.metadata:
            return self.metadata
        encoding = "utf-8"
        with fsspec.open(self.uri, mode="rb", encoding=None) as f:
            self.chunk: bytes = f.read(self.sample_size)
            spark = SparkSession.builder.appName("SampleReader").getOrCreate()
            content = spark.sparkContext.binaryFiles(f.read())
            encoding_pred = chardet.detect(self.chunk)
            self.metadata = f.details
        if encoding_pred["confidence"] > 0.8:
            encoding = encoding_pred["encoding"]
        self.metadata["encoding"] = encoding
        return self.metadata