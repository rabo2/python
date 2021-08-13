import pymysql
import matplotlib.pyplot as plt       
import numpy as np
#삼전 lg sk    

def getAllSName():
    ret =[]

    con = pymysql.connect(host='localhost', user='root', password='python', port=3305, db='python', charset='utf8')
    cur = con.cursor()

    sql = "SELECT s_name FROM stock group by s_name"
    cur.execute(sql)
    
    rows = cur.fetchall()
    for row in rows:
        ret.append(row[0])
    con.close()
    return ret

def getPrices(s_name):
    ret =[]

    con = pymysql.connect(host='localhost', user='root', password='python', port=3305, db='python', charset='utf8')
    cur = con.cursor()

    sql = "SELECT price FROM stock where s_name='{}'".format(s_name)
    cur.execute(sql)
    
    rows = cur.fetchall()
    for row in rows:
        ret.append(row[0])
    con.close()
    return ret

fig = plt.figure(1)
graph = fig.add_subplot(111,projection = '3d')



x = np.zeros(10)
y = range(10)
zs =[]

allnames = getAllSName()

for n in allnames:
    zs.append(getPrices(n))

for idx,n in enumerate(allnames):
    graph.plot(x+idx,y,zs[idx])
     



graph.set_xlabel('x')
graph.set_ylabel('y')
graph.set_zlabel('zs')



plt.show()