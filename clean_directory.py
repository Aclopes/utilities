# 1. Lista todos os arquivos da pasta
# 2. verifica a data dos arquivos
# 3. move todos que tem mais de 3 meses

import os
import glob
import sys
import datetime

if __name__ == '__main__':

    folder = sys.argv[1]
    os.chdir(folder)
    today = datetime.date.today()


    for name_file in glob.glob('*'):

        if os.path.isdir(name_file):
            continue

        print "------------------------------------------------------\r"
        print name_file + "\r"

        file_stat = os.lstat(name_file)
        file_date = datetime.date.fromtimestamp(file_stat.st_mtime)
        diference = today - file_date
        diference = diference.days

        print "Date:\t\t" + str(datetime.date.isoformat(file_date))
        print "Today is:\t" + today.isoformat()
        print "diff is:\t" + str(diference)

        if diference > 90 :
            print 'Excluir'
            os.remove(name_file)

        print "\r"
