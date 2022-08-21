import zipfile
import os
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Student number!!!')
        sys.exit()
    cwd = os.getcwd()
    file_name = "asg03_%s.zip" % sys.argv[1]
    zip_file = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)
    zip_file.write('solutions.py')
    zip_file.close()
