# Cultural Dictionary DB test
# Using sqlite3

import sqlite3 as s

cx = s.connect("dict.db")
cu = cx.cursor()
#sql = "create table dict (word varchar(50) not null, desc varchar(900) not null)"
#cu.execute(sql)
insert_sql = "insert into dict values (?,?)"
select_sql = "select desc from dict where word = ?"
a = ['einstein','Albert Einstein was born to a middle-class German Jewish family. His parents were concerned that he scarcely talked until the age of three, but he was not stupid as a quiet child. He would build tall houses of cards and hated playing soldier. At the age of twelve he was fascinated by a geometry book.']
#cx.execute(insert_sql, a)
#cx.commit()

#cu.execute("select desc from dict where word = 'einstein'")
cu.execute(select_sql,["einstein"])
s = cu.fetchone()
print s


