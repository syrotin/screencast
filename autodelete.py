import os
import MySQLdb

##need set numbers day
def mysqlconn(days=10):
    db = MySQLdb.connect(host='localhost', user='root', passwd='*', db='screen')


    cursor = db.cursor()

    cursor.execute('select title from lychee_albums where id IN (select album from lychee_photos where takestamp  '
                   '< UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL %s day)));' % days)
    result = cursor.fetchall()

    for record in result:
        commands = "find /opt/albums/ -name %s -exec rm -rf {} \;" % record
        os.system(commands)

    cursor.execute('delete from lychee_albums where id IN (select album from lychee_photos where takestamp'
                   '< UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL %s day)));' % days)

    cursor.execute('DELETE FROM lychee_photos where takestamp < UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL %s day)));' % days)
