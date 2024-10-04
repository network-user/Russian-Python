import importlib.abc
import importlib.util
from translate import RussianTransformer


replacements = RussianTransformer.replacements
time_replacements= {  # Пример добавления своих команд
    'время': "time",
    'спать': "sleep",
}
replacements.update(time_replacements)


class RussianLoader(importlib.abc.SourceLoader):
    """
    Пользовательский загрузчик для чтения и преобразования файлов с русским
    кодом.
    """

    def get_data(self, path):
        """
        Считывает файл и преобразует его содержимое с русского на английский.
        """
        try:
            with open(path, 'r', encoding='utf-8') as file:
                code = file.read()
            # Transform the code
            code = RussianTransformer.transform(code)
            return code.encode('utf-8')
        except FileNotFoundError:
            raise Exception(f"File not found: {path}")
        except Exception as e:
            raise Exception(f"Error reading file {path}: {e}")

    def get_filename(self, fullname):
        """
        Возвращает имя файла.
        """
        return fullname


def import_and_run(file_path):
    """
    Импортирует и запускает Python-файл с русскими ключевыми словами.
    """
    spec = importlib.util.spec_from_file_location("code.py", file_path,
                                                  loader=RussianLoader())
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        raise Exception(f"Error executing the module: {e}")


# Запуск файла, расширение у файла может быть любым, хоть .txt
import_and_run('code.py')