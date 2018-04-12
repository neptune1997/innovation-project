# -*- coding: cp936 -*-
import sys
if 'D:\\计算机学科常用专业英语词汇库的建设' not in sys.path:
    sys.path.append('D:\\计算机学科常用专业英语词汇库的建设')
import create
def creatC1(dataset):#将数据中的每一个记录记为长度为1的候选频繁集
    c1=[]
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])#添加的是一个列表
    c1.sort()
    return map(frozenset,c1)#用frozenset 类型以便之后用作字典的键值

def scanD(D,Ck,miniSupport):
    ssCnt={}#一个字典
    for tid in D:#对于数据集中的每条交易记录
        for can in Ck:#对于每一个候选集
            if can.issubset(tid):#如果是子集
                if not ssCnt.has_key(can):
                    ssCnt[can]=1
                else:
                    ssCnt[can]+=1#增加记录的值
    numItems=float(len(D))
    retList=[]
    supportData={}
    for key in ssCnt:
        support=ssCnt[key]/numItems
        if support>=miniSupport:
            retList.insert(0,key)#在列表的首部插入新元素
        supportData[key]=support
    #测试用print(retList,supportData)
    return retList,supportData

def aprioriGen(Lk,k):#创建候选集Ck
    retList=[]
    lenLk=len(Lk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1=list(Lk[i])[:k-2];L2=list(Lk[j])[:k-2]#前K-2个项相同时两个集合合并
            L1.sort();L2.sort()
            if L1==L2:
                retList.append(Lk[i]|Lk[j])
    return retList

def apriori(dataSet,miniSupport=0.5):
    C1=creatC1(dataSet)
    D= map(set,dataSet)
    L1, supportData=scanD(D,C1,miniSupport)
    L=[L1]
    k=2
    while(len(L[k-2])>0):
        Ck=aprioriGen(L[k-2],k)
        Lk,supK=scanD(D,Ck,miniSupport)
        supportData.update(supK)
        L.append(Lk)
        k=k+1
    print(L,supportData)
    return L,supportData
def loadDataSet():#创建一个实验数据集
    return[[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
apriori(loadDataSet(),0.5)
