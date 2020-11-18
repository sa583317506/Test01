# """
# 通过print打印模拟红绿灯:红灯30s，绿灯35s，黄灯3s
# """
# for red in range(1,31):
#     print("现在是红灯",red)
#     if red == 30:
#         for yellow1 in range(1,4):
#             print("现在是黄灯",yellow1)
#             if yellow1 == 3:
#                 for green in range(1,36):
#                     print("现在是绿灯",green)
#                     if green == 35:    
#                         for yellow2 in range(1,4):
#                             print("现在是黄灯",yellow2)
#                             if yellow2 == 3:
#                                 break

"""
实现注册功能：用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头
"""
account={}


acc=input("请输入账号：")
while len(acc) < 5 or len(acc) > 8 or acc[0].islower()==False:
    acc=input("账号不合法,请重新输入：")
account.update(username=acc)

password1=input("请设置密码：")
while len(password1)<6 or len(password1)>12:
    password1=input("密码过长或过短，请重新输入：")

password2=input("请再确认一次密码：")
while password2!=password1:
    password2=input("密码不相同：")
account.update(password=password2)
print(account)