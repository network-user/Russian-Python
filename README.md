# Russian Python

## Описание проекта

**Russian Python** — это проект, который позволяет писать код на Python, используя русскоязычные названия функций и методов. Проект предоставляет возможность переводить ключевые слова и функции из русского языка на английский. Проект был создан исключительно в развлекательных целях, поэтому прошу отнестись с пониманием

## Как пользоваться

### Запуск

1. Создайте файл с любым расширением
2. Напишите необходимый код для работы скрипта
3. Запустите Python-скрипт с функцией `preprocessor`:
   ```bash
   python main.py
   ```

### Пример использования

```python
импорт время

x = 123

пока x <= 1000:
    x += 1
    время.спать(1)
    вывод(x)


вывод(x)
```

## Добавление новых команд

Чтобы добавить новые русскоязычные команды в проект, выполните следующие шаги:

1. Откройте файл `preprocessor.py` и импортируйте из `translate.py` RussianTransformer.
2. Определите словарь `replacements`.
3. Добавьте новые пары ключ-значение в формате `('русское слово', 'английское слово')`.:
Пример:

```python
from translate import RussianTransformer


replacements = RussianTransformer.replacements
time_replacements= {
    'время': "time",
    'спать': "sleep",
}
replacements.update(time_replacements)
