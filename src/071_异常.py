def input_password():
    pwd=input("请输入密码(>8位)：")
    if len(pwd) >=8:
        return pwd
    print("主动抛出异常")
    ex=Exception("密码长度不足8位")
    raise ex        #主动抛出异常

try:
    print(input_password())
except Exception as result:
    print(result)