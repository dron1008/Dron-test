
"""

    1.编写一个程序模拟注册和登录的过程

    * 创建一个user表 包含 用户名和密码字段
    * 应用程序当中模拟注册和登录功能

        注册则输入用户名密码,将用户名密码存入到数据库(用户名不能重复)

        登录则进行数据库比对,如果有该用户则打印登录成功,否则让重新输入

"""

import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu')

cur = db.cursor()


def register():
    name = input("请输入用户名: ")
    password = input("请输入密码: ")
    # 判断用户名是否重复
    sql = "select * from user where username='%s';"%name        # 拼接字符串记得加引号
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False

    try:
        sql = "insert into user (username,password) values(%s,%s)"
        cur.execute(sql,[name,password])
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        return False


def login():
    name = input("请输入用户名: ")
    password = input("请输入密码: ")
    sql = "select * from user where username ='%s' and password = %s;" %(name,password)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True



while True:
    print("""
             ===========================
               1.注册    2.登录    3.退出
             ===========================
          """
          )

    cmd = input('请输入命令: ')
    if cmd == "1":
        # 执行注册
        if register():
            print("注册成功")
        else:
            print("注册失败")

    elif cmd == "2":
        # 执行登录
        if login():
            print("登录成功")
        else:
            print("登录失败,用户名或密码错误")

    elif cmd == "3":
        break

    else:
        print("暂时没有这个功能")


cur.close()
db.close()
















