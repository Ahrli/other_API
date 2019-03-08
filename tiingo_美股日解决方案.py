
# coding: utf-8

# In[1]:


import tiingo


# In[2]:


get_ipython().system('pip show tiingo')


# In[3]:


from tiingo import TiingoClient
config = {}

# To reuse the same HTTP Session across API calls (and have better performance), include a session key.
config['session'] = True

# If you don't have your API key as an environment variable,
# pass it in via a configuration dictionary.
config['api_key'] = "5ad45e5247e9f3ddc3a85005ea92c69d1bc4a552"

# Initialize
client = TiingoClient(config)


# In[4]:


client.get_dataframe('GOOGL',
                    #"000001.sh",
                    # tickers='000001',
                     #frequency='1Min',
                     #frequency='day',
                     startDate='2017-05-15',
                     endDate='2018-05-31')

