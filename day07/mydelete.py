import pymysql

conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', charset='utf8', port=3305)

curs = conn.cursor()

e_id = "3"
sql = f"""
        delete from emp
        where e_id={e_id}
       """

cnt = curs.execute(sql)
print(curs.rowcount, "record delete")

conn.commit()

curs.close()
conn.close()