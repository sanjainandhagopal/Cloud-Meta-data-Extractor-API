from abc import abstractmethod, ABC


class RecordProcessor(ABC):
    def head(self, **kwargs):
        """Get metadata of the file"""
        pass

    def get_records(sefl, count: int, **kwargs):
        """Get records"""
        pass
