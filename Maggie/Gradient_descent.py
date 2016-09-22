import numpy as np
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
import csv
from operator import itemgetter

def sigmoid_function(x, a):    #x is every sample
    y = 1.0 / (1 + np.exp(-np.dot(x, a)))  
    return y

def cost_function(X,Y,a):
    nrow, ncol = X.shape  
    error = 0.0    
    for i in range(0, nrow):
        error -= Y[i] * np.log(sigmoid_function(X[i],a)) + (1 - Y[i])* np.log(1 - sigmoid_function(X[i], a))
    return (error / nrow)

def plot_error(trainErr, testErr):
    
    fig, ax = plt.subplots()
    ax.grid()
    ax.plot([x for x in range(iteration)], trainErr, label="Training error")
    ax.plot([x for x in range(iteration)], testErr,  label="Test error")
    ax.set_ylabel('Cross-entropy error')
    ax.set_xlabel('Iteration')
    ax.set_title('Training and test error')
    ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()

def prediction(x, y, a):
    prediction=[]
    row, col = x.shape
     
    threshold=0.5


    for i in range(0, row):
        
        if (sigmoid_function(x[i],a) >= threshold):
            tempy = 1
        else:
            tempy = 0
        prediction.append(tempy)
    return prediction
    
def evaluation(x, y, a):
    row, col = x.shape
     
    threshold=0.5
    countACC = 0

    for i in range(0, row):
        
        if (sigmoid_function(x[i],a) >= threshold):
            tempy = 1
        else:
            tempy = 0
        
        if (y[i]-tempy)==0:
            countACC = countACC+1
            
    row=float(row)            
    return countACC / row

def plotEvaluation(trainACC, testACC):
    fig, ax = plt.subplots()
    ax.grid()
    ax.plot([x for x in range(iteration)], trainACC, label="Training accuracy")
    ax.plot([x for x in range(iteration)], testACC,  label="Test accuracy")
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Accurency')
    ax.set_title('Training and test accurency')
    ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()
    
#Main funtion
with open('classification_features.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
# Data pro-processing
your_list.pop(0)
getter1 = itemgetter(1,2,3,4,5,6,7,8)    
xData=map(list, map(getter1, your_list))
getter2 = itemgetter(9) 
yData=map(list, map(getter2, your_list))

xData=np.array(xData)
yData=np.array(yData)
xData = [map(int, i) for i in xData]
yData = [map(int, i) for i in yData]
xData=np.array(xData)
yData=np.array(yData)


#Main function
iteration = 100#5000
alpha = 5*10e-6 #alpha for each d[0.00002 1e-8 3e-13]
threshold = 0.5
init_a = 2
nrow, ncol = xData.shape
                              # Add bias term
one = np.ones((nrow,1))
xData = np.append(xData, one, axis=1)
train_x, test_x, train_y, test_y = train_test_split(xData, yData, test_size=0.2)
        
    
        
        # Initialize weight vectors a with random small numbers
trow, tcol = train_x.shape
a = np.random.uniform(-init_a, init_a, size=tcol)

        #a = np.zeros(shape = (trow, 1))
tempa = a
              
a_vector=np.zeros(shape = (iteration, 1))
trainErr = np.zeros(shape = (iteration, 1))
testErr = np.zeros(shape = (iteration, 1))
trainACC = np.zeros(shape = (iteration, 1))
testACC = np.zeros(shape = (iteration, 1))
test_predict=[]
train_predict=[]
# Iteration
for iter in range(0,iteration):
    #print ("Iteration:%d" % iter)
    # Update a_i
    for i in range(0, trow):                                
        delta=0
        #stochastic update
        delta += (train_y[i] - sigmoid_function(train_x[i],a)) * train_x[i]
        #alpha=0.000001
               # Update every a
        tempa = tempa + alpha * delta            
        # Finish one iteration update of a
    a = tempa    
    test_predict=prediction(test_x,test_y,a)
    train_predict=prediction(train_x,train_y,a)
    train_err =cost_function(train_x,train_y, a)
    test_err = cost_function(test_x, test_y, a)
    trainIndex = evaluation(train_x, train_y, a)
    testIndex = evaluation(test_x, test_y, a)
        
    a_vector[iter]=np.dot(a,a)            
    trainErr[iter] = train_err
    testErr[iter] = test_err
    trainACC[iter] = trainIndex
    testACC[iter] = testIndex
    # Plot evaluation indexes 
    #print ("Training error:", train_err)
    #print ("Test error:",  test_err)
    #print ("Training accuracy:" ,trainIndex)#, trainIndex[1], trainIndex[2]))
    #print ("Test accuracy:" ,  testIndex)#, testIndex[1], testIndex[2])) 
print  ("classification resultes for Naive Bayes method is :%f" % trainIndex)
print  ("classification resultes for Naive Bayes method is :%f" % testIndex )

plot_error(trainErr, testErr)
plotEvaluation(trainACC, testACC)
#plotEvaluation(trainACC, testACC)

#Naive Bayes     
from sklearn.naive_bayes import GaussianNB

X = train_x
Y = train_y
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
gnb = GaussianNB()
y_pred = gnb.fit(train_x, train_y).predict(test_x)
row, col =test_x.shape
countACC = 0

for i in range(0, row):
    if (y_pred[i]-test_y[i])==0:
            countACC = countACC+1
row=float(row) 
Naive_B_result=(countACC / row)         
print  ("classification resultes for Naive Bayes method is :%f" % Naive_B_result)



