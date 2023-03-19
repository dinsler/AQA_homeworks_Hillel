from writer import Writer


class TxtWriter(Writer):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def write(self, new_data: str, mode: str):
        with open(self.file_path, mode) as file:
            text = file.write(new_data)
        return text
