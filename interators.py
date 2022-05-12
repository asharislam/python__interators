#Iterators
#Iterable: strings, list, tuple, set, sictionary

"""nums = [2, 3, 4, 7, 8]
my_iterator = iter(nums)
print(next(my_iterator))
print(next(my_iterator))
my_iterator = iter(nums)
print(next(my_iterator))
print(next(my_iterator))
my_iterator = iter(nums)
print(next(my_iterator))
print(next(my_iterator))"""

###################
"""nums = [2, 3, 4, 7, 8]
for num in nums:
    print(num)"""

#########################
#making ierator ##########
#__iter__, __next__, duble unerscore / dunder methods

"""class powerTwo:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        result = self.num ** 2
        self.num += 1
        return result

my_num = powerTwo()
num_iterator = iter(my_num)
print(next(num_iterator))
print(next(num_iterator))
print(next(num_iterator))"""

##### for condition in iterators #####
########  not solve ########
class powerTwo:
    def __iter__(self):
        self.num = 1
        return self

    deff __next__(self):
    if self.num <= 3:
        result = self.num ** 2
        self.num += 1
    else:
        raise StopIteration
    return result

my_num = powerTwo()
num_iterator = iter(my_num)
