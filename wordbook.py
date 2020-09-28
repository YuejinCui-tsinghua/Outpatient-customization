#line=open('dataset/症状.txt',encoding='utf-8').readlines()
line=open('flist.txt',encoding='utf-8').readlines()
#outline=open('flist.txt','w',encoding='utf-8')

dir='dataset/unlabel/病史特点-'
dic={}
index=0
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
for i in range(1,2205):
    fea=[]
    line = open(dir+str(i), encoding='utf-8').readline()

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
import numpy
numpy.save('a',numpy.array(flist))
#for i in dic:
#    for j in dic[i]:
#        if flist[j[0]]>5:
#            outline.write(j[2]+'\n')
#outline.close()