import os
import shutil
import MySQLdb


def moveimg():
    os.system("cd /opt/unsort && find . -type f | sed -e 's/.//' | sed -e  's/.//;'"
          "> /home/demerzel/PycharmProjects/screencast/filetmp.txt")


    f = open('/home/demerzel/PycharmProjects/screencast/filetmp.txt')

    for line in f.read().splitlines():
        a = line.split('-')
        image = "/opt/unsort/%s" %line
        folder = "/opt/albums/%s/%s/%s/" % (a[0], a[1],a[2])
        if not os.path.exists(folder):
            mysqlconn(a[1],a[2])
            os.makedirs(folder)
        else:
            shutil.move(image, folder)
    sync()

def sync():
    os.system("cd /opt/albums/ && find . -type d -maxdepth 2 | sed -e 's/.//' | "
          "grep [^'/PC'1-90] > /home/demerzel/PycharmProjects/screencast/path.txt")


    f = open('/home/demerzel/PycharmProjects/screencast/path.txt')
    for line in f.read().splitlines():
        print (line)
        comm = "cd /home/demerzel/lycheesync && python3 -m lycheesync.sync /opt/albums%s /srv/www/htdocs/ ressources/conf.json" % line
        print (comm)
        os.system(comm)


def mysqlconn(name,new):
    db = MySQLdb.connect(host='localhost', user='root', passwd='rl451kme9m', db='screen')

    cursor = db.cursor()

    cursor.execute('select id from lychee_albums where title="%s";' % name)

    result = cursor.fetchall()
    print result
    for record in result:
        ids = record[0]

    cursor.execute('Select max(id) from lychee_albums;')

    result = cursor.fetchall()
    for record in result:
        max_id = record[0]

    cursor.execute('insert into lychee_albums (id,title,sysstamp,parent) VALUE (%s,"%s",14012018,%s);' % (max_id + 1, new, ids))
moveimg()