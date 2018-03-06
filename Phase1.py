#This is phase1 .It includes Impute missing values  and Graph plotting 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#Calculate Mean,Median,Std Deviation and Variance

def calculatemetrics(data):
    #Calculations 
    meanval=data.mean()         #Calculate Mean value for Column  
    median=data.median()        #Calculate Median value for Column
    stddev=data.std()           #Calcluate std deviation
    v=data.var()                #Caclculate Variance
    
    print("Mean Value:",round(meanval,3))
    print("Median Value:",round(median,3))
    print("Standard deviation:",round(stddev,3))
    print("Variance:",round(v,3))
    return meanval,median,stddev,v



#Function to Plot the histogram

def plothistogram():

 url="https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
 d=pd.read_csv(url,header=None)

 #This code repalces ? in columns with na value first and then mean of all remaining values from column A7 
 colno=6
 d[colno].replace('?',np.nan,inplace=True)
 d[colno]=d[colno].astype(float)
 Meanval=round(d[colno].mean(skipna=True),3)
 d=d.fillna(Meanval)
 
 
#This code plots all the histograms for A2-A10 columns

 columnname=['Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses']
 for i in range(0,9):    
    data = d.iloc[:,i+1]        # Take data from 2nd column onwards
    print("Attribute :",columnname[i])
    meanval,median,stddev,v=calculatemetrics(data) # Callfunction to cacluate mean ,median,std deviation and variation
    plt.title(columnname[i])     #Title of column to add in the graph
    plt.xlabel(columnname[i])    #X-label on the graph   
    plt.ylabel('Frequency')      #Y Label for frequency. 
   
  

    p, r, _ = plt.hist(data,bins=38)     #Calcuate max possible valuep of column to plot 
    plt.axis([1, 10, 1,p.max()+100])     #Specify X & Y axis  co-ordinates
    plt.hist(data, alpha =0.8,bins=30,color='b',label='Frequency') #Plot histogram 

    #Plotting different metrics
    
    plt.axvline(meanval, color='c', linestyle='dashed', linewidth=2,label='Mean') #Mean line
    plt.axvline(median, color='r', linestyle='dashed', linewidth=2,label='Median')  #Median line
    plt.axvline(stddev, color='y', linestyle='dashed', linewidth=2,label='Std deviation')  #Standard deviation line
    plt.axvline(v, color='m', linestyle='dashed', linewidth=2,label='Variance')       #Variance line
    plt.legend()
    plt.grid(True)     
    plt.show()     


# Main function     

if __name__ == "__main__":
   plothistogram()
      


