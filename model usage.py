#!/usr/bin/env python
# coding: utf-8

# In[1]:


from joblib import dump,load
import numpy as np
import pickle

model = load('Dragon.joblib')


# In[3]:


features = np.array([[-0.43942006,  3.12628155, -1.12165014, -0.27288841, -1.42262747,
       -0.23268537, -1.31238772,  2.61111401, -1.0016859 , -0.5778192 ,
       -0.97491834,  0.41164221, -0.86091034]])
final_predictions= model.predict(features)
print(final_predictions)




