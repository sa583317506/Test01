

# a=(1,2,3,4,"你好","你好","你好","大家好",True)
# # b=(a,"嘻嘻","哈哈")


# print(a[-2])
# print(a[3:])

# a=[1,2,3,4,"你好","大家好",True]
# #a.append(123)
# print(a[-2])
# print(a)
# print(a.index("大家好"))
# a.insert(a.index(3),3.5)
# print(a)
# b=a.pop(0)
# c=a.pop(0)
# print(a)
# print(b+c)
# a.extend(["张三","李四"])
# print(a)

# a={"name":"张三","age":25,"sex":"男"}
# print(a)

# a.update(name="lisa")
# print(a)

# a.pop("name")
# print(a)


a=input("请输入姓名：")
b=input("请输入性别：")
c=int(input("请输入年龄："))

d={"name":a,"sex":b,"age":c}
print(d)

print(d[1])


