from abc import ABC, abstractmethod


class BaseFileTypeValidator(ABC):
    @abstractmethod
    def validate(self, content: bytes, **kwargs) -> bool:
        """Validate the file type based on content.

        Args:
            content (bytes): The content to validate.
            **kwargs: Additional arguments specific to file type validation.

        Returns:
            bool: True if validation is successful, False otherwise.
        """
        pass
