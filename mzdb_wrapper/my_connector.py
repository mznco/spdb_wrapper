import MySQLdb
import logging

class mydb(object):
	def __init__(self, user, password, host, database):
		try:
			self.mydb_cnx = MySQLdb.connect(user=user, passwd=password, host=host, db=database)
			self.mydb_cursor = self.mydb_cnx.cursor()

		except Exception as e:
			logging.error("mydb: __init__: exception: %s" % e)

	def close(self):
		self.mydb_cnx.close()

	def exec_sql(self, sql):
		try:
			logging.debug("mydb: exec_sql: SQL statement: \n%s" % sql)
			self.mydb_cursor.execute(sql)
			return self.mydb_cursor.fetchall()
		except Exception as e:
			logging.debug("mydb: exec_sql: exception: %s" % e)
			return None