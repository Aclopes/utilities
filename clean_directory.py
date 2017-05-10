#########################################################
#   Clear files older than informed number of the days  #
#   Informe yhe path of the folder                      #
#   And the number of the days it will keep the files   #
#   If this last is not informed the program will delete#
#       files older than 60 days                        #
#########################################################

import os
import glob
import sys
import datetime
import re
from time import sleep

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print "You need to inform Folder and number of days parameter\r"
        print "if you dont inform the number of days to delete it'll assume Older than 60 days \r"
        exit(1)
   
    
    retDays = 60
    
    if len(sys.argv) > 2:
        
        if re.search('^[0-9]+$', sys.argv[2]):
            retDays = sys.argv[2]
    
    folder = sys.argv[1]
    os.chdir(folder)
    today = datetime.date.today()
    
    #wait to user confirm or cancel
    print "It will delete all files in folder " + folder
    print "Older than " + retDays + " Days"
    
    for i in range(0,5):
        sleep(1)
        sys.stdout.write('.')
        sys.stdout.flush()
    
    print "\n"
    
    retDays = int(retDays)

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

        if diference > retDays:
            print 'Excluir'
            os.remove(name_file)

        print "\r"
