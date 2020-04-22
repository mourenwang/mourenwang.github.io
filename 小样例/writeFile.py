import time

filename = input("请输入文件名称：");
time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
while True:
    string = input("请输入输入内容：")
    if string=='0':
        print("已写入文件！")
        break
    with open("%s.txt"%(filename),"a+") as f :
        f.write(time+"      "+string+"\n")
        f.close()
 