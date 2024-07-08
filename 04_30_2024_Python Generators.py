import sys

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = map(lambda i: i**2, x)

while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print('Done')
        break






import sys

class Iter:
    def __init__(self, n):
        self,n = n

    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        return self.current
    

for i in x:
    print(i)

    




import sys

def gen(n):
    for i in range(n):
        yeild n

for i in gen(5):
    print(i)




#Simple Ways to make a Generator 
x = (i for i in range(10))

for j in x:
    print(j)
    


