# KNN
Метод K ближайших соседей
# KNN Метод K ближайших соседей
Задача: есть информация по станциям метро сколько человек на какой станции пьёт чай или кофе. Необходимо по заданному K и названию станции определить что на этой станции больше всего пьют (чай, кофе или портвейн), то есть к какому классу относится данная станция метро "Чай" или "Кофе". 
# Решение
Код состоит из двух частей: подготовки данных и алгоритмов KNN с кодом выполнения программы. Основная программа - ноутбук Jupiter - knn_metro.ipynb который загружает дополнительные данные и выполняет код из других файлов (.py). Чтобы все успешно работало необходимо в переменной FILES_DIR указать путь к каталогу где находятся файлы проекта. В процессе выполнения будут сгенерированы дополнительные файлы с данными по метро: metro_by_line.py и full_dist_matrix. В Jupiter может глючить ввод данных с клавиатуры в программе если поменять данные в каких-то ячейках. Реализовано два алгоритма KNN - простое суммирование с взвешенным голосованием в случае равных голосов и полностью взвешенное суммирование с учётом расстояний от указанной станции метро.

Кирилл Прохоров<br>
Глеб Догверд<br>
Игнат Догверд<br>
Альберт Латыпов<br>
Павел Осипов
