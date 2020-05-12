# name='Tom'
# str="my name is %s,my age is %d"%(name,20)
# print(str)
# print("pi=%.2f"%3.1415926)
# name1='tom'
# name='jerry'
# print('two boy are {} and {}'.format(name1,name))
# print('tao boy are {0} and {1},{0} is tom,{1} is jerry'.format(name1,name))
dic={'name':'tom','age':'20'}
print('my name is {name} ,my age is {age}'.format(**dic))