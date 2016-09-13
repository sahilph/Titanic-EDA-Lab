
# coding: utf-8

# ## Titanic EDA Lab - Week 3
# 
# This file contains Exploratory data analysis of the Titanic Data
# 
# Analysed By: Sahil Phule

# In[14]:

import pandas as panda

## changed as pylab is deprecated
get_ipython().magic(u'matplotlib inline')


# In[15]:

df=panda.read_csv("train.csv")


# In[16]:

df


# In[17]:

df.Survived.value_counts()


# In[18]:

df.Survived.value_counts().plot(kind='bar',title="Survival Rate")


# ## Passenger Class

# In[19]:

df.Pclass.value_counts()


# In[20]:

df.Pclass.value_counts().plot(kind='bar', title='Type of Passenger Class')


# ## Passenger Sex Ratio

# In[21]:

df.Sex.value_counts()


# In[22]:

df.Sex.value_counts().plot(kind='bar', title="Passenger Sex Ratio")


# ## Passenger survival By Gender

# In[78]:

fig , axs = plt.subplots(1,2)

df[df.Sex=='male'].Survived.value_counts().plot(kind = 'bar', ax=axs[0], title="Males Survival rate")
df[df.Sex=='female'].Survived.value_counts().plot(kind = 'bar', ax=axs[1], title="Females Survival rate")


# ## Passenger survival by class

# In[79]:

fig , axs = plt.subplots(ncols=3, figsize=(10,4)) ## changed a little as graphs were overlapping.

df[df.Pclass==1].Survived.value_counts().plot(kind = 'bar', ax=axs[0], title="1st Class Survival rate")
df[df.Pclass==2].Survived.value_counts().plot(kind = 'bar', ax=axs[1], title="2nd Class Survival Rate")
df[df.Pclass==3].Survived.value_counts().plot(kind = 'bar', ax=axs[2], title="3rd Class Survival rate")


# ## Passenger Age

# In[45]:

df[df.Age.isnull()]


# ### Age Averages

# In[47]:

df.Age.describe()


# ### Replacing The NaNs by average passenger age

# In[25]:

avg_Age = df.Age.mean()
## Not really a proper way. But I couldn't think of any other way. I guess it is bettr than discarding the NaN values


# In[26]:

avg_Age


# In[27]:

df.Age=df.Age.fillna(value=avg_Age)


# In[28]:

df[df.Age.isnull()]


# In[29]:

df.Age.hist(bins=8,range=(0,80))


# ## Passenger Having Siblings or Spouses

# In[30]:

df.SibSp.value_counts()


# In[31]:

df.SibSp.value_counts().plot(kind="bar")


# ## Passengers having Parents or Children

# In[32]:

df.Parch.value_counts()


# In[54]:

df.Parch.value_counts().plot(kind="bar")


# ## Passenger Travelling Alone
# 
# The '0' value in above two graphs only specify that the passeneres did not have any Spouse or Sibling, Or did not have any Children/ Parents. They do not Tell who were travelling alone. 
# 
# I have sliced the df accordingly to show the passengers travelling alone

# In[75]:

#Calculation of Passenger travelling Alone 
df[(df.SibSp == 0)  & (df.Parch == 0)].PassengerId.count()


# ## Passenger travelling Alone Survival Rate

# In[70]:

df[(df.SibSp == 0)  & (df.Parch == 0)].Survived.value_counts().plot(kind='bar', title="Passenger Travelling Alone Survival rate")


# ## Amount of Fares paid

# In[34]:

df[df.Fare.isnull()]


# In[35]:

df.Fare.describe()


# In[36]:

df.Fare.hist(bins=10)


# ## Embarkment Sites

# In[37]:

df.Embarked.value_counts()


# In[76]:

df.Embarked.value_counts().plot(kind='bar',title="Ebarkment sites")


# ## Notable Conclusions
# 
# I have given various descriptions wherever I have plotted Graphs. But following are some Notable Conclusions
# 
# * Survival rate of women and children is high.
# * As women and children were saved first. The survival Rate of Men is low.
# * The survival rate of 3rd Class passengers is low.
# * 537 Passengers were Travelling Alone.
# 
# Note: I have not calculated the children's survival rate as I found out that after entering average values for the NaN in the age field, quite a lot of people with name suffix 'Master' and 'Miss' were given age of the 29.7 (The average) but they had siblings and parents travelling with them. 
# Thus the calculation of survival rate of children wouldn't have been accurate.
# 
# The Conclusion which I made about the children was derived from the internet as Titinaic Sinkage is quite a famous incident. 

# ## Not so useful data
# 
# The Cabin data of most of the passengers were not available, so nothing could be derived from it.
# 
# The ticket data of passengers appeared quiet Random with no  major significance
