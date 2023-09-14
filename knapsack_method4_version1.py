#Knapsack Problem

import random
import numpy as np
import pandas as pd

# Initailize knapsack ploblem---------------------------------------------------------------
capacity = 50 # 50, 70
items = 500 # objects 500, 1000, 10000,
k_weight = [items] # value and a weight between 1 and 10.
k_value = [items]
ks = [items]

#Initailize values------------------------------------------------------------------------
#random.randint(start, stop) https://www.w3schools.com/python/ref_random_randint.asp
k_weight = np.random.randint(low=1,high=11,size=items) #value and a weight between 1 and 10
k_value = np.random.randint(low=1,high=11,size=items)
ks = 0 #Knapsack start value is 0 (no item in knapsack)

# Set columns for use in DataFrame
k = {'w': k_weight, 'v':k_value, 'knapsack':ks}

# Create dataFrame
df = pd.DataFrame(k)

# Sort data by Method-----------------------------------------------------------
#df_sort = df.sort_values(by='w', ascending=True) #increasing weight method1
df_sort = df.sort_values(by='v', ascending=False) #Decreasing value method4

# Make new dataFrame and add new index for sorted data
df_sort_reset = df_sort.reset_index()

# Initailize for Adding item im the knapsack------------------------------------
current_w = 0
current_v = 0
tol_w =0
tol_v = 0
i = 0
size = len(df_sort_reset)

#Start construction method 4 by sort value decreasing-----------------------------

while (i < size):
      # Start item to the knapsack------------------------------------------------
      if tol_w <= capacity: # Total wieght must <= capacity
            # Check if current item + new item <= capacity
            if(tol_w + df_sort_reset.iloc[i]['w']<=capacity):
                  tol_w = tol_w + df_sort_reset.iloc[i]['w'] # Update total weight ,value
                  tol_v = tol_v + df_sort_reset.iloc[i]['v']
                  df_sort_reset.loc[[i],'knapsack']=1 # Mark item in knapsack

      i = i + 1
#End while loop------------------------------------------------------------------

# Show inforamation--------------------------------------------------------------
print(f'Total value Phase1: {tol_v}')
print(f'total weight Phase1: {tol_w}')# Show total weight

# End initailize knapsack-------------------------------------------------------



# Start Phase2-------------------------------------------------------------------

df_phase2 = df_sort_reset.copy() # Copy dataframe from phase1
old_val = tol_v  #result total value from phase1
old_weight  = tol_w
#Initailize varibles
new_val =0
j = 0
iteration = 2*items # number of iteration for improvement
in_randaom = 0 # choose item is in the knapsack
not_random = 0 # choose item is not in the knapsack

#----------------------------------------------------------------------------
#Start Local Search: Greedy Improvement method- Version-1


while(j < iteration):
      df_temp = df_phase2.copy() # create temp. dataframe
      #Split Dataframe to in and out of knapsack
      in_knapsack = df_temp.loc[df_sort_reset['knapsack']==1] # in Knapsack
      not_knapsack= df_temp.loc[df_sort_reset['knapsack']==0]# not in knapsack

      # Selct random item from in and out of knapsack to exchange item
      in_randaom  = np.random.randint(low=in_knapsack.index.min(), high=in_knapsack.index.max())
      not_random= np.random.randint(low=not_knapsack.index.min(), high=not_knapsack.index.max())

      #Exchange item
      df_temp.loc[[in_randaom],'knapsack']=0 # Mark item that is out of knapsack
      df_temp.loc[[not_random], 'knapsack'] = 1# Mark item that add in the knapsack
      # Choose item that in the knapsack
      # Split dataframe that has knapsack item
      df_temp2_k = df_temp.loc[df_temp['knapsack']==1]
      df_temp2_k.reset_index(inplace = True) # reset index for dataframe

      # Initailize variables for While-loop to calulate new weight and value
      k = 0
      temp_w  =0
      temp_v = 0
      diff = 0
      while(k < len(df_temp2_k)): # Loop until all item in dataframe
                  # Calculate new weight and value
            temp_w = temp_w +df_temp2_k.iloc[k]['w']
            temp_v = temp_v + df_temp2_k.iloc[k]['v']
            #print(f'temp_v {temp_v}')
            #print(f'temp_w {temp_w}')
            k = k +1
      #print(df_temp2_k)
      # Calculate differance between Old and New value--------------------------
      diff = temp_v - old_val

            # Check if new value is better result
      if temp_w <= capacity and diff >= 0:
            #print("Better")
            old_val = temp_v # Update old value with new value
            old_weight = temp_w
            #print(f'old_val in if: {old_val}')
                  # Update dataframe for phase2 with new better value
            df_phase2 = df_temp
      #print(f'old_val før j: {old_val}')
      j = j +1
print(f'Final value Phase2: {old_val}')
print(f'Final weight Phase2: {old_weight}')

# End Local Search: Greedy Improvement method- Version-1
