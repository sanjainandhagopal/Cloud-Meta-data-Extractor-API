from typing import Union

from pathlib import Path
from streamfetch.processors import is_supported
import mimetypes
import logging

logger = logging.getLogger(__name__)


# Later should validate based on content/magic number
# https://en.wikipedia.org/wiki/List_of_file_signatures
def detect_file_type(uri: str, **kwargs) -> str:
    """Detect file type and details from the partial content."""
    uri_path = Path(uri)
    print(uri_path.suffix)
    if is_supported(uri_path.suffix):
        return uri_path.suffix
    raise ValueError("File type not supported.")
