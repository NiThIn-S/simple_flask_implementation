#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests

r = requests.post('http://127.0.0.1:5000/test', json={"key": "value"})
print("Request with payload.\n",r.json())

r = requests.post('http://127.0.0.1:5000/test', json=None)
print("\nRequest without payload.\n",r.json())


# In[ ]:




