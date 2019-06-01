from setting import db


chanye = []
def search_chanye():
    cursor = db.cursor()
    select = "SELECT id,name FROM industry"  # 获取表中xxxxx记录数
    cursor.execute(select)  # 执行sql语句
    line = cursor.fetchone()
    while line!=None:
        chanye.append((line[0],line[1]))
        line = cursor.fetchone()
    return chanye


chanye_id = []
def search_chanye_id():
    cursor = db.cursor()
    select = "SELECT id FROM industry"  # 获取表中xxxxx记录数
    cursor.execute(select)  # 执行sql语句
    line = cursor.fetchone()
    while line!=None:
        chanye_id.append(line[0])
        line = cursor.fetchone()
    return chanye_id



xueshuo = []
def search_xueke():
    cursor = db.cursor()
    select = "SELECT code,name FROM benke"  # 获取表中xxxxx记录数
    cursor.execute(select)  # 执行sql语句
    line = cursor.fetchone()
    while line != None:
        xueshuo.append((line[0], line[1]))
        line = cursor.fetchone()
    return xueshuo


chanye_zhuanye={}
def search_chanye_zhuan():
    cursor = db.cursor()
    select = 'SELECT industry_id,zhuanye_code from bk_cy'
    cursor.execute(select)  # 执行sql语句
    line = cursor.fetchone()
    while line != None:
        chanye_zhuanye.setdefault(line[0],[]).append(line[1])
        line =cursor.fetchone()
    return chanye_zhuanye

