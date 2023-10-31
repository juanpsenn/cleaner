from core.models import Catalog


class FileAdapter:
    """Interface for extracting information from different file formats."""

    def extract_data(self, file_path: str) -> Catalog:
        """
        Extracts data from the specified file and returns the extracted data.

        Parameters:
            file_path (str): The path to the file from which data needs to be extracted.

        Returns:
            Any: The extracted data from the file.
        """
        raise NotImplementedError()
