import re

def main():
    # читаем файл с настройками
    with open('settings.py', 'r') as f:
        settings = f.read()

    # извлекаем нужные переменные
    title = re.search(r'title\s*=\s*"(.+?)"', settings).group(1)
    name = re.search(r'name\s*=\s*"(.+?)"', settings).group(1)
    lastname = re.search(r'lastname\s*=\s*"(.+?)"', settings).group(1)
    age = re.search(r'age\s*=\s*"(.+?)"', settings).group(1)
    profession = re.search(r'profession\s*=\s*"(.+?)"', settings).group(1)

    # читаем заготовку
    with open('myCV.template', 'r') as f:
        template = f.read()

    # заменяем все вхождения переменных в заготовке на соответствующие значения
    template = template.format(title=title, name=name, lastname=lastname, age=age, profession=profession)

    # записываем результат в новый файл
    with open('result.html', 'w') as f:
        f.write(template)

if __name__=='__main__':
    main()