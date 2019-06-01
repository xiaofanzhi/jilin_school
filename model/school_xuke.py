
import pymysql

#连接数据库
try:
    db = pymysql.connect(host="111.116.20.92",user="ccut",
        passwd="ccut",
        db="ccut1",
        charset='utf8')
except:
    print("could not connect to mysql server")

school = []
def search_school():
    cursor = db.cursor()
    select = "SELECT id,name FROM university" #获取表中xxxxx记录数
    cursor.execute(select) #执行sql语句
    line = cursor.fetchone()
    while line!=None:
        school.append((line[0],line[1]))
        line = cursor.fetchone()
    return school



school_list = []
def search_school_id():
    cursor = db.cursor()
    select = "SELECT id FROM university" #获取表中xxxxx记录数
    cursor.execute(select) #执行sql语句
    line = cursor.fetchone()
    while line!=None:
        school_list.append(str(line[0]))
        line = cursor.fetchone()
    return school_list




xueshuo = []
def search_xueke():
    cursor = db.cursor()
    select = "SELECT code,name FROM xueshuo"  # 获取表中xxxxx记录数
    cursor.execute(select)  # 执行sql语句
    line = cursor.fetchone()
    while line != None:
        xueshuo.append((line[0], line[1]))
        line = cursor.fetchone()
    return xueshuo

school_xuke = {}
def search_school_xuke():
    cursor = db.cursor()
    select = 'select university_id , xueke_code from xueshuo_mid '
    cursor.execute(select)  # 执行sql语句
    line = cursor.fetchone()
    while line!=None:
        school_xuke.setdefault(line[0],[]).append(line[1])
        line = cursor.fetchone()
    return school_xuke


school1 = []
def search_school1():
    cursor = db.cursor()
    select = "SELECT name FROM university" #获取表中xxxxx记录数
    cursor.execute(select) #执行sql语句
    line = cursor.fetchone()
    while line!=None:
        school1.append(line[0])
        line = cursor.fetchone()
    return school1
print(search_school1())