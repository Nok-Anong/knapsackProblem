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

# Initailize for Adding item in the knapsack------------------------------------
current_w = 0
current_v = 0
tol_w =0
tol_v = 0
i = 0
size = len(df_sort_reset)

#Start construction method 4 by sort value decreasing-----------------------------

while (i < size):
      # Item for tuppleshooting
      #df_sort_reset.index[i]
      #df_sort_reset.iloc[i]['w']

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
#print(df_sort_reset.loc[df_sort_reset['knapsack']==1]) # Show choosed items
#print(f'df_sort_reset\n {df_sort_reset}') # Show all in dataframe
 #     f'{}')

# End initailize knapsack-----------------------------------------------------

