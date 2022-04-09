import cProfile
def loop(count):
    result = []
    for i in range(count):
        result.append(i)

cProfile.run('loop(10000)')


# def hello(wr):
#     print('hello',wr)


# a='good'
# b='morning'
# c=a+b
# import pdb;pdb.set_trace()
# print(a)
# print(c)
# hello('world')




