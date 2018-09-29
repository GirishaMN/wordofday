# wordofday
python script to randomly get a word for day from mysql db

mysql data

mysql> select * from words;
+--------+---------------------------------+
| name   | description                     |
+--------+---------------------------------+
| test1  | this is test1 data for testing  |
| test2  | this is test2 data for testing  |
| test3  | this is test3 data for testing  |
| test4  | this is test4 data for testing  |
| test5  | this is test5 data for testing  |
| test6  | this is test6 data for testing  |
| test7  | this is test7 data for testing  |
| test8  | this is test8 data for testing  |
| test9  | this is test9 data for testing  |
| test10 | this is test10 data for testing |
+--------+---------------------------------+
10 rows in set (0.00 sec)

The Script datkes the system day and computes a hash function based on the total number of rows in the table.
Later this hashed value is used to specify that row to be retrived from the table using the limit option of mysql.

output:
python pymysql.py 
(u'test9', u'this is test9 data for testing')


