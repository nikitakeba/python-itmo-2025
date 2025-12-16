1) Проверил на файл [file1.txt](../test_files/file1.txt)

```
~/python-itmo-2025/hw_1 ❯ nl -b a test_files/file1.txt
     1  100
     2  101
     3  102
     4  103
     5  104
     6  105
~/python-itmo-2025/hw_1 ❯ ./task_1.py test_files/file1.txt
     1  100
     2  101
     3  102
     4  103
     5  104
     6  105
```

2) Попробовал проверить на файле с пустыми строчками [test_empty.txt](../test_files/test_empty.txt)

```
~/python-itmo-2025/hw_1 ❯ nl -b a test_files/test_empty.txt
     1  First
     2
     3  Third
~/python-itmo-2025/hw_1 ❯ ./task_1.py test_files/test_empty.txt
     1  First
     2
     3  Third
```

3) Проверил чтение из stdin

```
~/python-itmo-2025/hw_1 ❯ ./task_1.py
First

Third
     1  First
     2
     3  Third
```
