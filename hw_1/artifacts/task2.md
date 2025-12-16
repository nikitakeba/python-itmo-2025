1) Проверил на коротком файле [file1.txt](../test_files/file1.txt) (меньше 10 строк)

```
~/python-itmo-2025/hw_1 ❯ tail test_files/file1.txt
1
2
3
4
5
~/python-itmo-2025/hw_1 ❯ ./task_2.py test_files/file1.txt
1
2
3
4
5
```

2) Проверил на длинном файле [long_file.txt](../test_files/long_file.txt) (15 строк, выводятся последние 10)

```
~/python-itmo-2025/hw_1 ❯ tail test_files/long_file.txt
6
7
8
9
10
11
12
13
14
15
~/python-itmo-2025/hw_1 ❯ ./task_2.py test_files/long_file.txt
6
7
8
9
10
11
12
13
14
15
```

3) Проверил на нескольких файлах (выводится заголовок с именем файла)

```
~/python-itmo-2025/hw_1 ❯ tail test_files/file1.txt test_files/long_file.txt
==> test_files/file1.txt <==
1
2
3
4
5
==> test_files/long_file.txt <==
6
7
8
9
10
11
12
13
14
15
~/python-itmo-2025/hw_1 ❯ ./task_2.py test_files/file1.txt test_files/long_file.txt
==> test_files/file1.txt <==
1
2
3
4
5
==> test_files/long_file.txt <==
6
7
8
9
10
11
12
13
14
15
```

4) Проверил чтение из stdin (последние 17 строк)

```
~/python-itmo-2025/hw_1 main ?2 ❯ ./task_2.py                                                                                                                                                                                                               Py base
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
# тут нажал ctrl+D
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

