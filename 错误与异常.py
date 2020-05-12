try:
    num1=int(input('请输入一个被除数'))
    num2=int(input('请输入一个除数'))
    print(num1/num2)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('请输入数值型整数')
except:
    print('这是一个通用型异常')
else:
    print('这个程序没有异常')
finally:
    print('有没有异常都输出')