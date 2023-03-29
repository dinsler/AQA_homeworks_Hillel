"""
Get code from the lesson.
Add writer to a proxy pattern.
When you call write to file status of file should change and read should call from TxTReader.
"""

from txt_reader import TxtReader
from txt_writer import TxtWriter


class TxtProxyWriterReader:
    def __init__(self, file_path: str):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result

    def write_file(self, new_data: str, mode: str = 'w'):
        if mode not in ['w', 'a']:
            raise ValueError('Mode should be "w" for write or "a" for append')
        if not new_data:
            raise ValueError('New data shouldn\'t be a blank line')
        if new_data == self.__result and mode == 'w':
            print('Data already exist')
            return
        new_data = f'\n{new_data.strip()}' if mode == 'a' else new_data.strip()
        self.__txt_writer.write(new_data, mode)
        self.__is_actual = False


if __name__ == '__main__':
    proxy_tool = TxtProxyWriterReader('my_file.txt')
    print(proxy_tool.read_file())
    # print()
    proxy_tool.write_file('Some data', 'a')
    # proxy_tool.write_file('Some data', 'z')
    # proxy_tool.write_file('')
    print(proxy_tool.read_file())
    # print()
    proxy_tool.write_file('Some new data', 'w')
    print(proxy_tool.read_file())
    proxy_tool.write_file('Some new data', 'w')
