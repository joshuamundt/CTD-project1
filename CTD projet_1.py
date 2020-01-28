#!/usr/bin/env python
# coding: utf-8

# In[269]:


import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np


# #1.1.1 Cabled Axial Seamount Axial Base Shallow Profiler Mooring - Shallow Profiler 
# 
# 2019-07-06 02:00:50.000  -  2019-07-07 02:00:50.000
# 
# ASS=Axial summer shallow     z=depth [m]; z=h=P/(rho*g)

# In[307]:


ASS=pd.read_csv("Axial_summer_shallow.csv")
A1=ASS.seawater_pressure
AA1=ASS.time
B1=ASS.seawater_temperature
C1=ASS.practical_salinity
z1=(A1*10000)/(1000*9.81)


# In[308]:


ssp1=1449.2+(4.6*B1)-(0.055*B1**2)+(0.00029*B1**3)+(1.34-0.01*B1)*(C1-35)+(0.016*z1)
ssp1mean=np.mean(ssp1)
x=ssp1mean
y=max(ssp1)
print(x)
print(y)


# In[310]:


plt.plot(z1,ssp1)
plt.ylabel('ssp [m/s]')
plt.xlabel('depth [m]')
plt.title('Summer Shallow')
plt.axhline(y=ssp1mean, color='r', linestyle='-')
plt.gca().legend(('ssp [m/s]','ssp average [m/s]'))
plt.show()


# In[311]:


plt.plot(AA1,z1)
plt.ylabel('depth [m]')
plt.xlabel('time [s]')
plt.title('Summer Shallow')


# In[312]:


plt.plot(AA1,ssp1)
plt.ylabel('ssp [m/s]')
plt.xlabel('time [s]')
plt.title('Summer Shallow')


# =========================================================================================================

# #1.1.2 Cabled Axial Seamount Axial Base Shallow Profiler Mooring - 200m Platform
# 
# 2019-01-06 03:00:49.000  -  2019-01-07 03:00:49.000
# 
# AWS= Axial winter shallow

# In[275]:


AWS=pd.read_csv("Axial_winter_shallow.csv")
A2=AWS.seawater_pressure
AA2=AWS.time
B2=AWS.seawater_temperature
C2=AWS.practical_salinity
z2=(A2*10000)/(1000*9.81)


# In[276]:


ssp2=1449.2+(4.6*B2)-(0.055*B2**2)+(0.00029*B2**3)+(1.34-0.01*B2)*(C2-35)+(0.016*z2)
ssp2mean=np.mean(ssp2)
x2=ssp2mean
y2=max(ssp2)
print(x2)
print(y2)


# In[277]:


plt.plot(z2,ssp2)
plt.ylabel('ssp [m/s]')
plt.xlabel('depth [m]')
plt.title('Winter Shallow')
plt.axhline(y=ssp2mean, color='r', linestyle='-')
plt.gca().legend(('ssp [m/s]','average ssp [m/s]'))
plt.show()


# In[278]:


plt.plot(AA2,z2)
plt.ylabel('depth [m]')
plt.xlabel('time [s]')
plt.title('Winter Shallow')


# In[279]:


plt.plot(AA2,ssp2)
plt.ylabel('ssp [m/s]')
plt.xlabel('time [s]')
plt.title('Winter Shallow')


# =====================================================================================================

# #1.2.1 Cabled Axial Seamount Axial Base Deep Profiler Mooring - Wire-Following Profiler 
# 
# 2019-07-06 19:32:36.000  -  2019-07-07 19:32:36.000
# 
# ASD=Axial summer deep

# In[280]:


ASD=pd.read_csv("Axial_summer_deep.csv")
A3=ASD.pressure
AA3=ASD.time
B3=ASD.temp
C3=ASD.practical_salinity
z3=A3


# In[281]:


ssp3=1449.2+(4.6*B3)-(0.055*B3**2)+(0.00029*B3**3)+(1.34-0.01*B3)*(C3-35)+(0.016*z3)
ssp3mean=np.mean(ssp3)
x3=ssp3mean
y3=max(ssp3)
print(x3)
print(y3)


# In[285]:



plt.plot(z3,ssp3)
plt.ylabel('ssp [m/s]')
plt.xlabel('time [s]')
plt.title('Summer Deep')
plt.axhline(y=ssp3mean, color='r', linestyle='-')
plt.gca().legend(('ssp [m/s]','ssp average [m/s]'))
plt.show()


# In[287]:


plt.plot(AA3,z3)
plt.ylabel('depth [m]')
plt.xlabel('time [s]')
plt.title('Summer Deep')


# In[ ]:





# ========================================================================================

# #1.2.2 Cabled Axial Seamount Axial Base Deep Profiler Mooring - Wire-Following Profiler 
# 
# 2019-01-06 19:32:36.000  -  2019-01-07 19:32:36.000 
# 
# AWD= Axial winter deep

# In[302]:



AWD=pd.read_csv("Axial_winter_deep.csv")
A4=AWD.pressure
AA4=AWD.time
B4=AWD.temp
C4=AWD.practical_salinity
z4=A4


# In[303]:


ssp4=1449.2+(4.6*B4)-(0.055*B4**2)+(0.00029*B4**3)+(1.34-0.01*B4)*(C4-35)+(0.016*z4)
ssp4mean=np.mean(ssp4)
x4=ssp4mean
y4=max(ssp4)
print(x4)
print(y4)


# In[304]:


plt.plot(z4,ssp4)
plt.ylabel('ssp [m/s]')
plt.xlabel('depth [m]')
plt.title('Winter Deep')
plt.axhline(y=ssp4mean, color='r', linestyle='-')
plt.gca().legend(('ssp [m/s]','average ssp [m/s]'))
plt.show()


# In[305]:


plt.plot(AA4,z4)
plt.ylabel('depth [m]')
plt.xlabel('time [s]')
plt.title('Winter Deep')


# In[306]:


plt.plot(AA4,ssp4)
plt.ylabel('ssp [m/s]')
plt.xlabel('time [s]')
plt.title('Winter Deep)')


# =====================================================================================================

# #2.1.1 Cabled Continental Margin Oregon Slope Base Shallow Profiler Mooring - 200m Platform
# 
# 2019-07-06 02:00:49.000  -  2019-07-07 02:00:49.000
# 
# SSS=Slope summer shallow

# In[120]:


SSS=pd.read_csv("")


# In[ ]:





# In[ ]:





# In[ ]:





# ======================================================================================================

# #2.1.2 Cabled Continental Margin Oregon Slope Base Shallow Profiler Mooring - 200m Platform
# 
# 2019-01-06 03:00:48.000  -  2019-01-07 03:00:48.000
# 
# SWS=Slope winter shallow

# In[ ]:


SWS=pd.read_csv("")


# In[ ]:





# In[ ]:





# In[ ]:





# ==============================================================================================================

# #2.2.1 Cabled Continental Margin Oregon Slope Base Deep Profiler Mooring - Wire-Following Profiler 
# 
# 2019-07-06 17:42:10.000  -  2019-07-07 17:42:10.000
# 
# SSD=slope summer deep

# In[ ]:


SSD=pd.read_csv("")


# In[ ]:





# In[ ]:





# In[ ]:





# =========================================================================================================

# #2.2.2 Cabled Continental Margin Oregon Slope Base Deep Profiler Mooring - Wire-Following Profiler 
# 
# 2019-01-06 17:42:10.000  -  2019-01-07 17:42:10.000 
# 
# SWD= slope winter deep

# In[ ]:


SWD=pd.read_csv("")


# In[ ]:





# In[ ]:





# In[ ]:





# =========================================================================================================

# #3.1.1 Coastal Endurance Oregon Offshore Cabled Shallow Profiler Mooring - 200m Platform
# 
# 2019-07-06 03:00:48.000  -  2019-07-07 03:00:48.000
# 
# OSS= offshore summer shallow

# In[ ]:


OSS=pd.read_csv("")


# In[ ]:





# In[ ]:





# In[ ]:





# =========================================================================================================

# #3.1.2 Coastal Endurance Oregon Offshore Cabled Shallow Profiler Mooring - 200m Platform
# 
# 2019-01-06 03:00:48.000  -  2019-01-07 03:00:48.000
# 
# OWS= offshore winter shallow
# 

# In[ ]:


OWS=pd.read_csv("")


# In[ ]:





# In[ ]:





# In[ ]:





# ==========================================================================================================

# #3.2.1  Coastal Endurance Oregon Offshore Cabled Deep Profiler Mooring - Wire-Following Profiler
# 
# 
# 2019-07-06 22:07:54.000  -  2019-07-07 22:07:54.000 
# 
# OSD= offshore summer deep
# 

# In[ ]:


OSD=pd.read_csv("")


# In[ ]:





# In[ ]:





# In[ ]:





# ===========================================================================================================

# #3.2.2 Coastal Endurance Oregon Offshore Cabled Deep Profiler Mooring - Wire-Following Profiler
# 
# 2019-01-06 22:07:54.000  -  2019-01-07 22:07:54.000
# 
# OWD= offshore winter deep

# In[ ]:


OWD=pd.read_csv("")


# In[ ]:





# In[ ]:





# In[ ]:




