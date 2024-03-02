def calculator():
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    
    print("请选择运算符：")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    
    operator = input("请输入运算符的编号：")
    
    if operator == "1":
        result = num1 + num2
        print("结果：", result)
    elif operator == "2":
        result = num1 - num2
        print("结果：", result)
    elif operator == "3":
        result = num1 * num2
        print("结果：", result)
    elif operator == "4":
        if num2 != 0:
            result = num1 / num2
            print("结果：", result)
        else:
            print("除数不能为零")
    else:
        print("无效的运算符编号")

calculator()


