# This is Phase3 code .Calculating ‘ErrorRate’ from Clusters data we got from Phase2

from  main_phase2 import *
import pandas as pd


# For mu_2, calculating Error rate B
def error_B(CA):
    total_pred_with_4_with_actual_2=0
    total_pred_with_2=0
    for i in range(699):
      if(CA.iloc[i,2]==4 and CA.iloc[i,1]==2):     #Predicted vs  Actual
        total_pred_with_4_with_actual_2=total_pred_with_4_with_actual_2+1
      if(CA.iloc[i,2]==2):                         # If total predicated=2  
        total_pred_with_2=total_pred_with_2+1
     
    error_B=total_pred_with_4_with_actual_2/total_pred_with_2
    return(error_B)
 
    
 # For mu_4 ,calculating Error rate M   

def error_M(CA):
    total_pred_with_2_with_actual_4=0
    total_pred_with_4=0
    for i in range(699):
      if(CA.iloc[i,2]==2 and CA.iloc[i,1]==4):     #Predicted vs  Actual
        total_pred_with_2_with_actual_4=total_pred_with_2_with_actual_4+1
      if(CA.iloc[i,2]==4):                         # If total predicated=2  
        total_pred_with_4=total_pred_with_4+1
    error_M=total_pred_with_2_with_actual_4/total_pred_with_4
    return(error_M)
 
     
 # Main function calling both the error functions and printing the results
if __name__ == "__main__":
     error_B=error_B(CA)
     print("Error B:",error_B)
     error_M=error_M(CA)
     print("Error M",error_M)
     TotalError=error_B+error_M
     print("Total Error:",TotalError)
