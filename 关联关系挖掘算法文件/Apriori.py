# -*- coding: cp936 -*-
import sys
if 'D:\\�����ѧ�Ƴ���רҵӢ��ʻ��Ľ���' not in sys.path:
    sys.path.append('D:\\�����ѧ�Ƴ���רҵӢ��ʻ��Ľ���')
import create
def creatC1(dataset):#�������е�ÿһ����¼��Ϊ����Ϊ1�ĺ�ѡƵ����
    c1=[]
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])#��ӵ���һ���б�
    c1.sort()
    return map(frozenset,c1)#��frozenset �����Ա�֮�������ֵ�ļ�ֵ

def scanD(D,Ck,miniSupport):
    ssCnt={}#һ���ֵ�
    for tid in D:#�������ݼ��е�ÿ�����׼�¼
        for can in Ck:#����ÿһ����ѡ��
            if can.issubset(tid):#������Ӽ�
                if not ssCnt.has_key(can):
                    ssCnt[can]=1
                else:
                    ssCnt[can]+=1#���Ӽ�¼��ֵ
    numItems=float(len(D))
    retList=[]
    supportData={}
    for key in ssCnt:
        support=ssCnt[key]/numItems
        if support>=miniSupport:
            retList.insert(0,key)#���б���ײ�������Ԫ��
        supportData[key]=support
    #������print(retList,supportData)
    return retList,supportData

def aprioriGen(Lk,k):#������ѡ��Ck
    retList=[]
    lenLk=len(Lk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1=list(Lk[i])[:k-2];L2=list(Lk[j])[:k-2]#ǰK-2������ͬʱ�������Ϻϲ�
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
def loadDataSet():#����һ��ʵ�����ݼ�
    return[[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
apriori(loadDataSet(),0.5)
