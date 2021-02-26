import fdb

con = fdb.connect(host="127.0.0.1", database="D:/Evolutiva/Databases/Vertice/VERTICE.FDB", user="SYSADM",
                      password="evolutiva010808", port=3050)

def getSql(sql):
    cur = con.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    return lista
    #print(f"{lista}")
    cur.close()
    con.close()

