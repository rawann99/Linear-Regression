import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
path ='diabetic_kidney_disease (1).xlsx.csv'
data=pd.read_csv(path)
data=(data-data.min())/(data.max()-data.min())
data.insert(0,'ones',1)
cols=data.shape[1]
X=data.iloc [ : ,0:cols-3 ] # hya5od el 0 w el cols-3
y=data.iloc[ : ,cols-1:cols]#hay5od el cols -1 bs 3shan el cals bara el range
X=np.matrix(X.values)
y=np.matrix(y.values)
theta=np.matrix(np.array([0,0]))
def compute_cost (theta,X,y):
    z=np.power((X*theta.T)-y,2)
    return np.sum(z) / (2*len(X))

alpha = .01
iteration = 1000
def GradientDecent ( X,y,theta, alpha, iteration):
    theta_as=np.matrix(np.zeros(theta.shape)) #3mlt matrix zy
    # el theta blzbt 3shan ast5dmha bdl el theta
    number=int(theta.ravel().shape[1])
    cost=np.zeros(iteration)
    i=0
    j=0
    while i != iteration :
        error_rate=((X*theta.T)-y)
        j = 0
        while j != number:
            term=np.multiply(error_rate,X[:,j]) # 3shan a3wad el darb fl x in theta 1
            theta_as[0,j]=theta_as[0,j]- (( alpha /len(X)) * np.sum(term))
            j+=1

        theta=theta_as
        cost[i]=compute_cost(theta,X,y)
        i+=1
    return theta ,cost
zb=theta[0,0]+theta[0,1]*X #intial value od theta 0 and theta 1 for drawing line before gradient decent
fig,ax=plt.subplots(figsize=(5,5))
ax.plot(X,zb,'r',label="prediction Before")
ax.scatter(data['FBG (mg/dL)'],data['UACR (mg/g creatinine)'],label="trainig Data")
ax.legend(loc=2)
ax.set_xlabel('FBG')
ax.set_ylabel('UACR')
ax.set_title('Line Before Optimization ')
plt.show()

G,cost = GradientDecent(X,y,theta,alpha,iteration)
print( 'cost\n',cost[:])
H_x=G[0,0]+(G[0,1]*X) #compute the h(x)
fig,ax=plt.subplots(figsize=(5,5))
ax.plot(X,H_x,'b',label='Prediction')
ax.scatter(data['FBG (mg/dL)'],data['UACR (mg/g creatinine)'],label="trainig Data")
ax.legend(loc=2)
ax.set_xlabel('FBG')
ax.set_ylabel('UACR')
ax.set_title('Line After Optimization')
plt.show()


