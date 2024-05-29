from configparser import ConfigParser
import os


def read_config(filename='database.ini', section='postgresql'):
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(path, filename)
    parser = ConfigParser()
    parser.read(file_path)
    db_params = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_params[param[0]] = param[1]
    else:
        raise Exception(f'Раздел {section} не найден в файле {filename}.')
    return db_params
