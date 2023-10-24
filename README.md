# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"


## Виконав: Ярема Тарасович Гунько (Група ІР-24)

### Лабораторна робота №1 (Варіант 2 Рівень 3)

Напишіть функцію, яка приймає невпорядкований масив цілих чисел і повертає діапазон індексів (початковий і кінцевий) найменшого підмасиву, який потрібно відсортувати для досягнення повного впорядкування всього масиву.
​
Наприклад, для вхідного масиву
1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
​
Результат:
(3, 9)
​
Підмасив, який потрібно відсортувати для впорядкування всього масиву, починається з індексу 3 (значення 7) і закінчується на індексі 9 (значення 7).
У випадку, якщо вхідний масив відсортований, слд повернути кортеж (-1, -1)
​
​
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити сценарії коли: вхідний масив посортований, вхідний масив необхідно сортувати весь, масив містить лише 1 елемент. 
​
Напишіть функцію, яка приймає невпорядкований масив цілих чисел і повертає діапазон індексів (початковий і кінцевий) найменшого підмасиву, який потрібно відсортувати для досягнення повного впорядкування всього масиву.
​
Наприклад, для вхідного масиву
1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
​
Результат:
(3, 9)
​
Підмасив, який потрібно відсортувати для впорядкування всього масиву, починається з індексу 3 (значення 7) і закінчується на індексі 9 (значення 7).
У випадку, якщо вхідний масив відсортований, слд повернути кортеж (-1, -1)
​
​
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити сценарії коли: вхідний масив посортований, вхідний масив необхідно сортувати весь, масив містить лише 1 елемент. 
​

***

### Лабораторна робота №2 (Варіант 2 Рівень 3)

Пiсля швидкого випуску нової версiї своєї операцiйної системи, компанiя NanoSoft
почала отримувати вiд користувачiв численнi повiдомлення про помилки. Щоб
слiдкувати за прогресом виправлення помилок, команда розробникiв вирiшила поставити
велику квадратну дошку, i прикрiпити до неї по листку для кожної помилки. Проте,
щоб дошка вмiстилася в кiмнатi, потрiбно, щоб вона була не надто великою.
Всi N листкiв мають прямокутну форму i однаковий розмiр W × H. Їх не можна
повертати, а також накладати один на iнший.
Знайдiть мiнiмальний розмiр квадратної дошки, яка здатна вмiстити всi листки.
Приклад мiнiмальної дошки, яка може вмiстити 10 листкiв 2 × 3 (див картинку)

Вхiднi данi
три числа N, W, H — кiлькiсть листкiв, ширина та висота листка вiдповiдно.
• 1 ≤ N ≤ 1012
• 1 ≤ W ≤ 109
• 1 ≤ H ≤ 109
Вихiднi данi
одне число — мiнiмальна довжина сторони квадратної дошки.

Приклад 1
N, W, H = 10, 2, 3
Результат:
9

Приклад 2
N, W, H = 2, 1000000000, 999999999
Результат:
1999999998

Приклад 3
N, W, H = 4, 1, 1
Результат:
2

***
### Лабораторна робота №3 (Варіант 2 Рівень 3)

Для заданого бінарного дерева перевірте, чи воно є збалансованим деревом. Бінарне дерево вважається збалансованим, якщо різниця у висоті його лівого та правого піддерев не перевищує 1 для будь-якого піддерева.

Розглянемо таке бінарне дерево:

    1
   / \
  2   3
 / \     
4   5   
Це дерево є збалансованим, оскільки різниця висоти лівого піддерева та правого піддерева не перевищує 1.

Реалізована вами функція is_tree_balanced(node: BinaryTree) -> bool отримує на вхід корінь бінарного дерева та повертає True, якщо бінарне дерево є збалансованим, та False, якщо воно не збалансоване.

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)


***


