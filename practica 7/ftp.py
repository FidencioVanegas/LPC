from ftplib import FTP
import os

#ftp = FTP('ftp.heanet.ie')
ftp = FTP('ftp.us.debian.org')
ftp.login()
print("Directorio actual: "+ftp.pwd())
ftp.dir()
os.mkdir("TXT")
os.chdir("TXT")
ftp.cwd("debian/doc/dedication")
ar = ftp.nlst()
for i in ar:
	with open(i,'wb')as fp:
		ftp.retrbinary('RETR '+i,fp.write)
ftp.quit()
