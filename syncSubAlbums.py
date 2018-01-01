import os

os.system("cd /home/demerzel/albums/ && find . -type d -maxdepth 2 | sed -e 's/.//' | "
          "grep [^'/pc'1-90] > /home/demerzel/screencast/screencast/path.txt")
comm="ls -l"
f = open('path.txt')
for line in f.readlines():
    os.system("cd /home/demerzel/albums%s %s" % (line,comm) )
