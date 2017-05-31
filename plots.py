# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:06:45 2017

@author: lucas
"""
#import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from ggplot import *


# df = pd.read_csv('.\hist.csv', sep=';', decimal=',')

# df['Data'] = pd.to_datetime(df['Data'], dayfirst = True)
# dfNE = df[df['Sistema'] == 'Nordeste']

# #dfNE = dfNE.set_index('Data')

# #dfNE[dfNE['Data'] >= datetime.date(2016,1,1)].plot(x='Data', y = 'GWh')

# dfNE_2015 = dfNE[dfNE['Data'] >= datetime.date(2015,1,1)]
# dfNE_2015 = dfNE_2015[dfNE_2015['Data'] < datetime.date(2016,1,1)]

# dfNE_2016 = dfNE[dfNE['Data'] >= datetime.date(2016,1,1)]
# dfNE_2016 = dfNE_2016[dfNE_2016['Data'] < datetime.date(2017,1,1)]

# dfNE_2017 = dfNE[dfNE['Data'] >= datetime.date(2017,1,1)]
# dfNE_2017 = dfNE_2017[dfNE_2017['Data'] < datetime.date(2018,1,1)]

# plt.plot(dfNE_2015['Data'], dfNE_2015['GWh'], 
         # dfNE_2016['Data'], dfNE_2016['GWh'], 
         # dfNE_2017['Data'], dfNE_2017['GWh'])

#s = df['Data'].map(lambda x: x.year+2)

#==========================================================

dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%Y')
df = pd.read_csv('./hist.csv', sep=';',decimal=',', parse_dates=['Data'], date_parser=dateparse)

dfNE = df[df.Sistema == 'Nordeste']
dfNE = dfNE.reset_index(drop=True)
# dfNE[dfNE.Data < '2015-07-31' ]
# dfNE['d_m'] = dfNE.Data.map(lambda x: str(x.day) + '_' + str(x.month))

dfNE_2015 = dfNE[dfNE.Data <'2016']
dfNE_2015 = dfNE_2015.set_index('Data')

dfNE_2016 = dfNE[dfNE.Data < '2017']
dfNE_2016 = dfNE_2016[dfNE_2016.Data >= '2016']
dfNE_2016 = dfNE_2016.set_index('Data')

dfNE_2017 = dfNE[dfNE.Data >= '2017']
dfNE_2017 = dfNE_2017.set_index('Data')


dfNE_2015['a'] = dfNE_2015.index.map(lambda x: (x-datetime.datetime(2015,1,1)).days)
dfNE_2016['a'] = dfNE_2016.index.map(lambda x: (x-datetime.datetime(2016,1,1)).days)
dfNE_2017['a'] = dfNE_2017.index.map(lambda x: (x-datetime.datetime(2017,1,1)).days)


plt.plot(dfNE_2017.a, dfNE_2017.GWh, dfNE_2016.a, dfNE_2016.GWh, dfNE_2015.a, dfNE_2015.GWh)
plt.show()













