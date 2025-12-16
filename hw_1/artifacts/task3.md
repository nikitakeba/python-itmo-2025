1) Проверил на одном файле [file1.txt](../test_files/file1.txt)

```
~/python-itmo-2025/hw_1 ❯ wc test_files/file1.txt
       4       5       9 test_files/file1.txt
~/python-itmo-2025/hw_1 ❯ ./task_3.py test_files/file1.txt
       4       5       9 test_files/file1.txt
```

2) Проверил на нескольких файлах

```
~/python-itmo-2025/hw_1 ❯ wc test_files/file1.txt test_files/long_file.txt
       4       5       9 test_files/file1.txt
      15      15      36 test_files/long_file.txt
      19      20      45 total
~/python-itmo-2025/hw_1 ❯ ./task_3.py test_files/file1.txt test_files/long_file.txt
       4       5       9 test_files/file1.txt
      15      15      36 test_files/long_file.txt
      19      20      45 total
```

3) Проверил чтение из stdin

```
~/python-itmo-2025/hw_1 main ?2 ❯ echo -e "ok" | wc                                                                                                                                                                                         Py base
       1       1       3
~/python-itmo-2025/hw_1 main ?2 ❯ echo -e "ok" | ./task_3.py                                                                                                                                                                                Py base
       1       1       3
```

Две строки

```
~/python-itmo-2025/hw_1 ❯ echo -e "Hello World\nTest" | wc
       2       3      17
~/python-itmo-2025/hw_1 ❯ echo -e "Hello World\nTest" | ./task_3.py
       2       3      17
```

