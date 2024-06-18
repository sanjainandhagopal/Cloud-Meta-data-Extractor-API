from typing import Dict, Union
from .read_row_column import StructuredReader
from .parquet import ParquetProcessor
from .base import RecordProcessor
from .read_chunk import ChunkReader
from .read_meta import MetaReader
from .extension_provider import JustifyExtension

#python cli.py abfs://abluva/entity_list.csv --nrows 6

FILE_PROCESSOR_MAP: Dict[str, Union[RecordProcessor]] = {
    **{ext: StructuredReader for ext in JustifyExtension.strategy_1_extentions()},
    **{ext: ChunkReader for ext in JustifyExtension.strategy_2_extentions()},
    **{ext: MetaReader for ext in JustifyExtension.strategy_3_extentions()},
}


def is_supported(file_extension: str) -> bool:
    if file_extension.lower() in FILE_PROCESSOR_MAP:
        return True
