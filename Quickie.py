# lambda <args> : <return Value> if <condition > ( <return value > if <condition> else <return value>)
converter = lambda x : x*2 if x < 10 else (x*3 if x < 20 else x)

# map(fun, iter)
result = map(lambda x, y: x + y, numbers1, numbers2)
test = list(map(list, l))
l = list(map(int,input().split()))


