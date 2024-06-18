from .base import BaseFileTypeValidator
import csv
import chardet


class CSVValidator(BaseFileTypeValidator):
    def validate(self, content: bytes, **kwargs) -> bool:
        """Validate if the content is a CSV like."""
        pass
