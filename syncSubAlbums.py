import os
import shutil
import MySQLdb


def moveimg():
    os.system("cd /opt/unsort && find . -type f | sed -e 's/.//' | sed -e  's/.//;'"
          "> /tmp/filetmp.txt")


    f = open('/tmp/filetmp.txt')

    for line in f.read().splitlines():
        a = line.split('-')
        src = "/opt/unsort/"
	image = line
        dst = "/opt/albums/%s/%s/%s/" % (a[0], a[1],a[2])
	if not os.path.exists(dst):
           os.makedirs(dst)
	   mysqlconn(a[0],a[1],a[2])
        else:
            shutil.move(os.path.join(src, image), os.path.join(dst, image))
    sync()

def sync():
    os.system("cd /opt/albums/ && find . -type d -maxdepth 2 | sed -e 's/.//' | "
          "grep [^'/PC'1-90] > /tmp/path.txt")


    f = open('/tmp/path.txt')
    for line in f.read().splitlines():
        print (line)
	print ("/opt/albums%s") % line
        comm = "cd /opt/lycheesync && python3 -m lycheesync.sync /opt/albums%s /var/www/html/screencast ressources/conf.json" % line
        print (comm)
        os.system(comm)


def mysqlconn(parent,name,new):
    db = MySQLdb.connect(host='localhost', user='root', passwd='|J1xcGC~jEF*', db='screencastprestige')
    
    cursor = db.cursor()

    cursor.execute('select id from lychee_albums where title="%s";' % parent)    
    result = cursor.fetchall()
    print result
    for record in result:
        par = record[0]

    cursor.execute('select id from lychee_albums where title="%s" AND parent=%s;' % (name,par))

    result = cursor.fetchall()
    print result
    for record in result:
        ids = record[0]

    cursor.execute('insert into lychee_albums (title,sysstamp,parent) VALUE ("%s",14012018,%s);' % (new, ids))

moveimg()
