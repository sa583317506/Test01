# a=0
# cust={}
# custh={}
# custl={}

# while a<3:
#     name=input("请输入名字：")
#     result=int(input("请输入"+name+"成绩："))
#     cust[a]=(name)
#     if result < 60:
#         custl[cust[a]]=result
#     else:
#         custh[cust[a]]=result
#     a=a+1

# print("不及格的：",custl)
# print("及格的：",custh)



for i in range(1,10):
    for j in range(1,i+1):  #[1,i+1)
        print(j,"*",i,"=",i*j,end=" ")
    print()
    


    #通过print打印，模拟一个红绿灯的功能，注意红灯30次，绿灯35次，黄灯3次

