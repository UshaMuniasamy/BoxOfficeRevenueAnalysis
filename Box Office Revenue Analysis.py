#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 

#visualization
import matplotlib.pyplot as plt
import seaborn as sns 

get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('dark_background')


# In[2]:


#Data loading and Exploartion
get_ipython().run_line_magic('time', "train = pd.read_csv('G:/python/box office revenue/train.csv')")


# In[3]:


train.head()


# In[20]:


train = train.drop(['belongs_to_collection'],axis = 1)


# In[17]:


#statistics of the data
print("Shape of data is") 
train.shape


# In[10]:


#Datframe information
train.info()


# In[21]:


train.info()


# In[22]:


train = train.drop(['production_companies','production_countries','crew'],axis = 1)


# In[23]:


train.info()


# In[24]:


train.describe()


# In[25]:


#Lets create new coulmn for release date, weekday, mnth, and year
train['release_date'] = pd.to_datetime(train['release_date'],infer_datetime_format =True)


# In[28]:


train['release_day'] = train['release_date'].apply(lambda t : t.day)
train['release_weekday'] = train['release_date'].apply(lambda t : t.weekday)
train['release_month'] = train['release_date'].apply(lambda t : t.month)
train['release_year'] = train['release_date'].apply(lambda t : t.year
if t.year < 2018
else t.year - 100)


# In[30]:


#data analysis and visualization
train[train['revenue'] == train ['revenue'].max()]


# In[31]:


#1.which movies made the heighest revenue
train[['id','title','budget','revenue']].sort_values(['revenue'],ascending  = False).head(10).style.background_gradient(subset= 'revenue',cmap = 'BuGn')


# In[33]:


#2.which moves has the heighst budget?
train[train['budget'] == train['budget'].max()]


# In[37]:


train[['id','title','budget','revenue']].sort_values(['budget'],ascending  = False).head(10).style.background_gradient(subset= ['budget','revenue'],cmap = 'PuBu')


# In[38]:


#3which movies is longest movie?
train[train['runtime']== train['runtime'].max()]


# In[43]:


plt.hist(train['runtime'].fillna(0)/60, bins = 40);
plt.title('Distribution of length of film in hours', fontsize = 16, color = "white");
plt.xlabel('Duration of Movie in hours')
plt.ylabel('Number of Movies')


# In[44]:


train[['id','title','runtime','budget','revenue']].sort_values(['runtime'],ascending  = False).head(10).style.background_gradient(subset= ['runtime','budget','revenue'],cmap = 'YlGn')


# In[52]:


plt.figure(figsize = (20,12))
edgecolor = (0,0,0),
sns.countplot(train['release_year'].sort_values(),palette = "Dark2", edgecolor = (0,0,0))
plt.title("Movie Relaest Count by Year", fontsize = 20)
plt.xlabel ('Relaeast year')
plt.ylabel('Number of Movies Release')
plt.xticks(fontsize = 12, rotation =90)
plt.show()


# In[53]:


train['release_year'].value_counts().head()


# In[54]:


#movies  with highest and lowest population
#most Popular movies:
train[train ['popularity'] == train['popularity'].max()][['original_title','popularity','release_date','revenue']]


# In[55]:


#least popular movie:
train[train['popularity'] == train['popularity'].min()][['original_title','popularity','release_date','revenue']]


# In[58]:


#create popularity distribution plot
plt.figure(figsize = (20,12))
edgecolor = (0,0,0)
sns.distplot(train['popularity'],kde = False)
plt.title("Movie popularity count", fontsize = 20)
plt.xlabel ('popularity')
plt.ylabel('count')
plt.xticks(fontsize = 12, rotation =90)
plt.show()


# In[64]:


#Which month most movies are release from 1921 to2017
plt.figure(figsize = (20,12))
edgecolor = (0,0,0)
sns.countplot(train['release_month'].sort_values(),palette = "Dark2", edgecolor = (0,0,0))
plt.title("Movie release Count by Month", fontsize = 20)
plt.xlabel ('Release Month')
plt.ylabel('Number of Movies Release')
plt.xticks(fontsize = 12)
plt.show()


# In[66]:


train['release_month'].value_counts()


# In[67]:


#which date of month most movie are relaesed?
plt.figure(figsize = (20,12))
edgecolor = (0,0,0),
sns.countplot(train['release_day'].sort_values(),palette = "Dark2", edgecolor = (0,0,0))
plt.title("Movie release Count by day of Month", fontsize = 20)
plt.xlabel ('Release day')
plt.ylabel('Number of Movies Release')
plt.xticks(fontsize = 12)
plt.show()


# In[68]:


train['release_day'].value_counts().head()


# In[87]:


#which day of week most mob=vies are realased?
plt.figure(figsize = (20,12))

sns.countplot(train['release_weekday'].sort_values(),palette = "Dark2") 
loc = np.array(range(len(train['release_weekday'].unique())))
day_labels = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
plt.xlabel ('Release day of week')
plt.ylabel('Number of Movies Release')
plt.xticks(loc, day_labels, fontsize = 12)
plt.show()


# In[ ]:


train['release_weekday'].value_counts()


# In[88]:


plt.figure(figsize=(20,12))
sns.countplot(train['release_weekday'].sort_values(), palette='Dark2')
loc = np.array(range(len(train['release_weekday'].unique())))
day_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.xlabel('Release Day of Week')
plt.ylabel('Number of Movies Release')
plt.xticks(loc, day_labels, fontsize=12)
plt.show()


# In[ ]:




