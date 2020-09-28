
dir='data/病史特点-'#你可以需改成你的目录
n=2205#病例总数
dic={}
index=0
line=open('flist.txt',encoding='utf-8').readlines()#目前总结的症状，您可以增加您需要的症状,如果有修改请同时上传
flist=[]
for i in range(len(line)):
    word=line[i]
    word=word[0:len(word)-1]
    wordn=len(word)
    if (wordn>7) | wordn<2:
        continue
    hash=word[wordn-2:wordn]
    if hash not in dic:
        dic[hash]=[]
    dic[hash].append([i,wordn,word])
flist=[]

for i in range(1,2):
    fea=[]
    line = open(dir+str(i), encoding='utf-8').readline()#访问每个文件

    for j in range(5,len(line)-2):
        hash= line[j-1]+line[j]
        if hash in dic:
           # print(hash)
            a=dic[hash]
            for k in a:
               # print(line[(j-k[1]+1):(j+1)],k[2])
                if line[(j-k[1]+1):(j+1)]==k[2]:
                    #print(k[2],j)
                    fea.append(k[0])
    flist.append(fea)
#print(flist)
import numpy
numpy.save('a.npy',numpy.array(flist))#保存提取症状
#请将a.npy 发送至邮箱cuiyj17@mails.tsinghua.edu.cn,我们会反馈问诊二维码。