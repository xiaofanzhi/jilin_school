from setting import db

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


chaye = []
def search_chanye():
    cursor = db.cursor()
    select = "SELECT id,name FROM industry"  # 获取表中xxxxx记录数
    cursor.execute(select)  # 执行sql语句
    line = cursor.fetchone()
    while line!=None:
        chaye.append((line[0]+40,line[1]))
        line = cursor.fetchone()
    return chaye


school_chanye = {}
def search_school_chanye():
    cursor = db.cursor()
    select = "select distinct university.id school_id,industry.id industry_id from university,industry,xueshuo_mid,xs_cy where university.id=xueshuo_mid.university_id and xueshuo_mid.xueke_code=xs_cy.xueshuo_code and xs_cy.industry_id=industry.id"
    cursor.execute(select)  # 执行sql语句
    line = cursor.fetchone()
    while line!=None:
        school_chanye.setdefault(line[0],[]).append(line[1]+40)
        line = cursor.fetchone()
    return school_chanye

print(search_school_chanye())