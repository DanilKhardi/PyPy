

class FileReader:
    def __init__(self, path_to_file):
        self.path = path_to_file


    def read(self):
        try:
            with open(self.path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''