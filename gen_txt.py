import os

path="C:\\Users\\kk\\PycharmProjects\\"
lst=os.listdir(path)
file1=open("train.txt","a")
for i in lst:
    new_path = path + str(i)
    last=os.listdir(new_path)
    for j in last:
        file1.write(new_path+"     :    "+j+"\n")
file1.close()