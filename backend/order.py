import os
import mysql.connector

to_addr =""
subject=""
from_addr=""
password=""
dd_public_dashboard_url =""

def read_db_values():

	config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'dashboard_info'
    }

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	cursor.execute("SELECT to_addr,subject,from_addr,password,dd_public_dashboard_url FROM `emailer_info` LIMIT 1");
	records = cursor.fetchall()

	for row in records: 
		to_addr = row[0]
		subject = row[1]
		from_addr = row[2]
		password = row[3]
		dd_public_dashboard_url = row[4]

	user_value = {
		"to_addr" : to_addr,
		"subject" : subject,
		"from_addr" : from_addr,
		"password" : password,
		"dd_public_dashboard_url" : dd_public_dashboard_url
	}
	cursor.close()
	connection.close()

	return user_value

def execute_shell_cmd(user_value):
	try:
		gen_image = 'echo "hello alex" > test.txt'
		os.system(gen_image)
	except Exception as e:
		raise e
	# gen_image = "sudo /usr/bin/xvfb-run -a /usr/bin/wkhtmltoimage --javascript-delay 20000 '{}' /test.png".format(user_value['dd_public_dashboard_url'])


def execute_commands():
	user_value = read_db_values()
	execute_shell_cmd(user_value)

	return 'Finished'
