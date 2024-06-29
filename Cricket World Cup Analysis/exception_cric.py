class MissingColumnError(Exception):
    def _init_(self, column):
        super()._init_(f"Missing expected column: {column}")
        self.column = column

class DataCleaningError(Exception):
    def _init_(self, message):
        super()._init_(f"Error cleaning data: {message}")
        self.message = message

class FileLoadError(Exception):
    def _init_(self, year, file_path, message):
        super()._init_(f"Error loading data for year {year}: {file_path} - {message}")
        self.year = year
        self.file_path = file_path
        self.message = message