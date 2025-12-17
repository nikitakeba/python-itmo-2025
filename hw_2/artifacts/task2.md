0. Скачал картинку superman.png - с логотипом superman

Создал аккаунт и токен на test pypi

1. Собрал

```
python3.11 -m build
```

2) Выложил на TestPyPI

```

python3.11 -m twine upload --repository testpypi dist/*
```

https://test.pypi.org/project/latex-gen-nikitakeba/1.0.0/

Установил библиотеку

```
pip install -i https://test.pypi.org/simple/ latex-gen-nikitakeba
```

4) Сгенерировал .tex и PDF

```
python3.11 task_2.py
```

Результат: [document.pdf](document.pdf)

5) Docker

На python:3.11-alpine собралось

```
docker build -t latex-gen .
docker run -v $(pwd)/artifacts:/app/artifacts latex-gen
```

Результат генерировался в artifacts/document.pdf
