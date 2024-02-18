# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError
class Category:
    categories = []

    @classmethod
    def add(cls, category_name):
        cls.category_name=category_name
        if category_name not in cls.categories:
            cls.categories.append(category_name)
            return print(Category.categories.index(category_name))
        else:
            raise ValueError(f"{cls.categories} already exists")
    @classmethod
    def get(cls,index):
        cls.index=index
        if Category.categories[index]:
            return print(Category.categories[index])
        else:
            raise IndexError(f"{cls.index} out of range")
    @classmethod
    def delete(cls,index):
        cls.index=index
        if Category.categories[index]:
            cls.categories.pop(index)
    @classmethod
    def update(cls,index,new_name):
        cls.index=index
        cls.new_name=new_name
        if not len(Category.categories) and not index:
            Category.categories.append(new_name)
        elif new_name in Category.categories:
            raise ValueError(f"{cls.new_name} already exists")
        elif Category.categories[index]:
            Category.categories.insert(index,new_name)

# Category.add("cat1")
# print(Category.categories)
# Category.get(0)
# Category.delete(0)
# print(Category.categories)
Category.update(0,"cat1")
print(Category.categories)