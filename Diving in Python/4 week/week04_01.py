import os.path
import tempfile


class File:

    def __init__(self, path_to_file):
        self._path_to_file = path_to_file
        self._itero = None  # Ссылка на файл-объект для итерации по строкам
        if not os.path.exists(self._path_to_file):
            open(self._path_to_file, 'w').close()

    def read(self):
        try:
            with open(self._path_to_file, 'r') as fin:
                return fin.read()
        except:
            return str()

    def write(self, string):
        try:
            with open(self._path_to_file, 'w') as fout:
                return fout.write(string)
        except IOError as err:
            print(f'Error! {err.filename} {err.errno} {err.strerror}')

    def __str__(self):
        return self._path_to_file

    def __add__(self, other):
        new_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        try:
            with open(new_file.name, 'a') as fadd:
                with open(self._path_to_file, 'r') as ftmp:
                    data = ftmp.read()

                fadd.write(data)

                with open(other._path_to_file, 'r') as ftmp:
                    data = ftmp.read()

                fadd.write(data)

            return File(new_file.name)
        except IOError as err:
            print(f'Error! {err.filename} {err.errno} {err.strerror}')
            return None

    def __iter__(self):
        try:
            self._itero = open(self._path_to_file, 'r')
        except IOError as err:
            print(f'Ошибка! {err.filename} {err.errno} {err.strerror}')
        return self

    def __next__(self):
        if self._itero is None:
            raise StopIteration
        result = self._itero.readline()
        if not result:
            self._itero.close()
            raise StopIteration
        return result
