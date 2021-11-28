import os
import shutil

path="D:\PBL"

os.chdir(path)
filelist=os.listdir(path)
print("\nfile list:",filelist)
exlist=[]

for file in filelist:
    ex=file.split(".")[-1]
    exlist.append(ex)

print("\n ex:",exlist)
exlist=set(exlist)
print(exlist)

des="D:\destination"

for ex in exlist:
    os.mkdir(des + "/" + ex)
    for file in filelist:
        if ex == file.split(".")[-1]:
            shutil.move(file,des + "/" + ex)