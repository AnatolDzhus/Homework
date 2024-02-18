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
        if not len(Category.categories):
            Category.categories.append(new_name)
        elif new_name in Category.categories:
            raise ValueError(f"{cls.new_name} already exists")
        elif Category.categories[index]:
            Category.categories.insert(index,new_name)

Category.add("cat1")
print(Category.categories)
Category.get(0)
Category.delete(0)
print(Category.categories)
Category.update(0,"cat1")
print(Category.categories)