"""K-nn Algorithm"""

import pandas as pd
import numpy as np
import csv as csv
from scipy.spatial import distance
test = pd.read_csv("Test_Set.csv")
train = pd.read_csv("Train_Set.csv")


def knn(k,train,test):
    
    
    
    dist = []
    ans = 0
    
    for i in range (891):
        dist.append(distance.euclidean(test,train.ix[i,2:]))
        
    index = sorted(range(len(dist)),key=lambda x:dist[x])
    
    for i in range(0,k):
        if train.ix[index[i],1]==1:
            
            ans += 1
    if ans > k/2:
        predict = 1 
    else:
        predict = 0

    return predict
    
result=[]
for i in range(0,418):
    result.append(knn(5, train, test.ix[i,1:]))
    print(len(result))

id=[]
for i in range (0,418):
    id.append(892+i)



raw_data = {'PassengerId': id,
            'Survived': result}
df = pd.DataFrame(raw_data, columns = ['PassengerId','Survived'])

df.to_csv('predict.csv')