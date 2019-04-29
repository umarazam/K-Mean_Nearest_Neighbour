from math import sqrt
from random import choice

def mean(l):
    sum=0
    mean=0
    for a in l:
        sum +=a[0]
        sum +=a[1]
    count = len(l) *2 
    
    mean = sum/count
    return mean

# k--> Clusters
def k_mean(l1, k):
    sample = choice(l1) 
    cluster1 =[]
    cluster2 = []
    data = l1
    tempCentroid=0
    centroid1 = sample[0]
    centroid2 = sample[1]
    while centroid1 !=  tempCentroid:
        data = []
        if cluster1 != []:
            centroid1 = mean(cluster1) # now, Centroid is from the mean.
            tempCentroid=centroid1
            data += (cluster1)
            cluster1  = []
        if cluster2 != []:  
            centroid2 = mean(cluster2)
            data +=(cluster2)
            cluster2 = []
        if data == []:
            data = l1
        for a in (data):
            d = sqrt((a[0]-centroid1) **2 + (a[1]-centroid2)**2)
            t1 = (a[0], a[1], a[2])
            if d < centroid1:
                cluster1.append(t1)
            else:
                cluster2.append(t1)
    return cluster1, cluster2          

def K_MeanNearestDistance(cluster, value):
    d=0
    temp =-1
    for a in cluster:  
        d = sqrt((a[0]-value[0]) **2 + (a[1]-value[1])**2)
        if temp < d:
            temp = d
    return temp

def clusterIdentification(d1,d2):
    if d1 < d2:
        return 0
    else:
        return 1

def assignLabel(cluster1, cluster2, cluster_No):
    if cluster_No == 0:
        return cluster1[0][2]
    else:
	    return cluster2[0][2]

# 0 --> Bad
# 1 --> Good
def main():
    l1 = [(7,7,0),(7,4,0),(3,4,1), (1,4,1)]
    cluster1, cluster2 = k_mean(l1,2)
    print('Cluster1: \n ',cluster1)
    print('--------')
    print('CLuster2: \n ', cluster2)                            
    a = int(input(('Enter Acid Durabilty: ')))
    b = int(input(('Enter Acid Strength: ')))
    check_Value = (a,b)
    d1 = K_MeanNearestDistance(cluster1, check_Value)
    d2 = K_MeanNearestDistance(cluster2, check_Value)
    cluster_No = clusterIdentification(d1,d2)
    label = assignLabel(cluster1, cluster2, cluster_No)
    print(f'Label for:{check_Value} --> {label}')
if __name__ == '__main__':
    main();
