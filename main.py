import conn
from datetime import date

con = conn
sql = ("SELECT P.GPESSOA_ID, P.NM_PESSOA "
      "FROM ED_MATRICULA M "
      "INNER JOIN GPESSOA "
      "P ON P.GPESSOA_ID = M.GALUNO_ID "
      "WHERE M.GANO_ID = 2021"
      "AND M.FL_SITUACAO = 1")

a = con.getSql(sql)

hoje = date.today()

for i in a:
      con1 = conn
      sql1 = ("SELECT PF.DT_NASCTO, PF.FL_SEXO "
             "FROM GPESSOA_FISICA PF "
             "WHERE PF.GPESSOA_ID = " + str(i[0]))
      b = con1.getSql(sql1)
      for j in b:
            if j[1] == 'M':
                  oa = 'o'
            else:
                  oa = 'a'
            diff = hoje - j[0]
            days = diff.days
            years, days = days // 365, days % 365

            print(f'{str.upper(oa)} Alun{oa} {i[1]} e nasceu dia {j[0].day} de {j[0].month} de {j[0].year}')
            print('E tem {} anos'.format(years))




