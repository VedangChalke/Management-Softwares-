# THIS PROGRAM IS TO CREATE A FUNCTION TO COMPARE FILE IN PC TO THE FILE IN CREATE IN PYTHON LIBRARY
# IF THE FILE FORMAT IS NOT SAME, CAPITALISE IN FILE FIRST LETTER IN PC
# For eg ( PC file ----> content.txt  and python library file ----> content.xlsx  ,then change PC file will be ---> Content.txt)
# IF FILE ARE SIMILAR CONVERT NAME OF FILES IN THE LINEAR LOOP OF ASCENDING NUMBERS LIKE (1,2,3,...)
# eg (1.txt, 2.txt,...) in PC folder



import os

def soldier(path,file,format):
    os.chdir(path)
    i = 1
    files =os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")


    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file , f"{i}{format}")
            i +=1


soldier(r'C:\Users\Vedang\Dropbox\PC\Desktop\Python_Projects\FileManagementProject\pyfiles',r'C:\Users\Vedang\Dropbox\PC\Desktop\Python_Projects\FileManagementProject\abc.txt' ,'.txt')