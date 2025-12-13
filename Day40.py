def simple_gen(x):
    for i in range(x):
        yield i
        
g = simple_gen(5)

for i in g:
    print(i)