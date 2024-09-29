# Математические формулы
Библиотека предоставляет функции для расчета параметров круга, прямоугольника, квадрата и треугольника
## Функции

### Площадь
Позволяет расчитать площадь фигуры, исходя из нужных параметров
- Круг: S = πR²
```python
import circle

circle_area = circle.area(3)
print(circle_area)
```
```bash
28.274333882308138
```
- Прямоугольник: S = ab
```python
import rectangle

rectangle_area = rectangle.area(2, 8)
print(rectangle_area)
```
```bash
16
```
- Квадрат: S = a²
```python
import square

square_area = square.area(3)
print(square_area)
```
```bash
9
```
- Треугольник: S = ah / 2
```python
import triangle

triangle_area = triangle.area(5, 7)
print(triangle_area)
```
```bash
17.5
```

### Периметр
Позволяет расчитать периметр фигуры, исходя из нужных параметров
- Круг: P = 2πR
```python
import circle

circle_perimeter = circle.perimeter(6)
print(circle_perimeter)
```
```bash
37.69911184307752
```
- Прямоугольник: P = 2a + 2b
```python
import rectangle

rectangle_perimeter = rectangle.perimeter(5, 10)
print(rectangle_perimeter)
```
```bash
30
```
- Квадрат: P = 4a
```python
import square

square_perimeter = square.perimeter(8)
print(square_perimeter)
```
```bash
32
```
- Треугольник P = a + b + c
```python
import triangle

triangle_perimeter = triangle.perimeter(4, 5, 7)
print(triangle_perimeter)
```
```bash
16
```

# История коммитов

## 6ad324d6850030dabbb345b5edf4cea9e654b284
(HEAD -> new_features_466524, origin/new_features_466524)<br>
Автор: Chef<br>
Время:   Thu Sep 5 09:50:45 2024 +0300<br>
Была исправлена ошибка в rectangle.py, добавлен triangle.py

## 8e9d6ea0c5c855d2d8e578006ae85db30b910210
Автор: Chef<br>
Время:   Thu Sep 5 09:46:08 2024 +0300<br>
Был добавлен новый файл с формулами прямоугольника

## d078c8d9ee6155f3cb0e577d28d337b791de28e2
(origin/main, origin/HEAD, main)<br>
Автор: smartiqa <info@smartiqa.ru><br>
Время:   Thu Mar 4 14:55:29 2021 +0300<br>
L-03: Docs added

## 8ba9aeb3cea847b63a91ac378a2a6db758682460
Автор: smartiqa <info@smartiqa.ru><br>
Время:   Thu Mar 4 14:54:08 2021 +0300<br>
L-03: Circle and square added
