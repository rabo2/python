import pymysql

class DaoNaver:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
            db='python', charset='utf8', port=3305)
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    
    def select(self):
        sql = "select * from naver"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows
    
    def insert(self, title, link, description, bloggername, bloggerlink, postdate):
        sql = f"""
             insert into naver 
                (title, link, description, bloggername, bloggerlink, postdate) 
             values 
                ('{title}', '{link}', '{description}', '{bloggername}', '{bloggerlink}'
                , '{postdate}')"""
        
        self.curs.execute(sql)  
        self.conn.commit()
        
        return self.curs.rowcount
    
    def update(self, e_id, name, tel):
        sql = f"""
            update naver
               set name = '{name}', tel='{tel}'
             where e_id = {e_id} 
        """
        
        self.curs.execute(sql)
        self.conn.commit()
        
        return self.curs.rowcount
    
    def delete(self, e_id):
        sql = f"""
            delete from naver
             where e_id={e_id}
        """
        
        self.curs.execute(sql)
        self.conn.commit()
        
        return self.curs.rowcount
        
    
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    pass
    # rows = de.select()
    # print(rows)
    
    # count = de.insert(4, "4", "4")
    # print(count)
    
    # count = de.update(3, '4', '4')
    # print(count)
    
