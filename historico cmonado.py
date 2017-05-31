dfNE
dfNE.head
dfNE.head(0)
dfNE.head(1)
dfNE.head(2)
dfNE.Data < '2015-05-06'
dfNE.Data < '2015-06'
dfNE[dfNE.Data < '2015-31-07' ]
dfNE.Data < '2015-31-07'
dfNE.Data < '2015-07-31'
dfNE[dfNE.Data < '2015-07-31' ]
dfNE['dm'] = dfNE.Data.map(lambda x: str(x.day()) + '_' + str(x.month()))
dfNE.head()
dfNE.Data
dfNE.head()
dfNE.Data[0]
dfNE.Data[0].year
dfNE['dm'] = dfNE.Data.map(lambda x: str(x.day) + '_' + str(x.month))
dfNE.head()
dfNE.Data[0].month
dfNE.Data[1].month
df = pd.read_csv('./hist.csv', sep=';',decimal=',', parse_dates=['Data'])
df.head()
df.Data
for i in df.iterrows:
    print (i)
for i, v in df.iterrows:
    print(r[date])
df.head()
df.Data[0]
df.Data[0].month
dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%Y')
df = pd.read_csv('./hist.csv', sep=';',decimal=',', parse_dates=['Data'], date_parser=dateparse)
df.head()
df.Data[0].month
df.Data[1].month
%history
dfNE = df[df.Sistema == 'Nordeste']
dfNE.head()
gg = ggplot(dfNE, aes(x='Data', y='GWh')) + geom_dot() + geom_line()
gg = ggplot(dfNE, aes(x='Data', y='GWh')) + geom_point() + geom_line()
gg
dfNE.Data.dtype
dfNE.Data.dtype()
dfNE.Data.dtype
dfNE.Data
gg = ggplot(dfNE, aes(x='Data', y='GWh')) + geom_point() + geom_line()
dfNEd = dfNE.set_index(['Data'])
dfNEd.head()
dfNEd.index
dfNEd.index.name
gg = ggplot(dfNEd, aes(x='Data', y='GWh')) + geom_point() + geom_line()
gg = ggplot(dfNEd, aes('Data', y='GWh')) + geom_point() + geom_line()
dfNEd
gg = ggplot(dfNEd, aes(y='GWh')) + geom_point() + geom_line()
gg
gg = ggplot(dfNEd, aes(y='GWh', x = dfNEd.index.name)) + geom_point() + geom_line()
dfNEd.index.name = 'Data'
gg = ggplot(dfNEd, aes(y='GWh', x = dfNEd.index.name)) + geom_point() + geom_line()
gg = ggplot(dfNEd, aes(y='GWh', x = dfNEd.index)) + geom_point() + geom_line()
dfNE.hist()
dfNE['GWh'].hist()
plt.show
import matplotlib.pyplot as plt
plt.show
plt.show()
dfNE['GWh'].hist?
dfNE['GWh'].hist(_?
dfNE['GWh'].hist()?
pd.hist()
pd.hist?
plt.hist>
plt.hist?
dfNE['GWh'].hist(bins=5)
plt.show
plt.show()
dfNE['GWh'].hist(bins=1)
plt.show()
dfNE['GWh'].hist(bins=1)
plt.show()
dfNE['GWh'].hist(bins=20)
plt.show()
dfNE['GWh'].hist(bins=50)
plt.show()
dfNE['GWh'].hist(bins=50, normed=True)
plt.show()
dfNE['GWh'].hist(bins=2, normed=True)
plt.show()
dfNE['GWh'].hist(bins=20, normed=True)
plt.show()
from scipy.stats import norm
dfN = pd.DataFrame({'A': np.random.normal(size=100)})
import numpy as np
from scipy.stats import norm
dfN = pd.DataFrame({'A': np.random.normal(size=100)})
dfN.hist()
plt.show()
from scipy.stats import norm
dfN = pd.DataFrame({'A': np.random.normal(size=1000)})
dfN.hist(bin=100)
dfN.hist(bins=100)
plt.show()
dfN.A.plot(kind='hist', normed=True)
plt.show()
dfN = pd.DataFrame({'A': np.random.normal(size=1000)})
dfN.A.plot(kind='hist', normed=True)
plt.show()
range = np.arange(-4, 4, 0.001)
plt.plot(range, norm.pdf(range,0,1))
plt.show()
dfNE['GWh'].plot(kinf='hist', normed=True)
dfNE['GWh'].plot(kind='hist', normed=True)
range = np.arange(-4, 4, 0.001)
plt.plot(range, norm.pdf(range,0,1))
plt.show()
range = np.arange(-0, 120, 0.001)
plt.plot(range, norm.pdf(range,0,1))
dfNE['GWh'].plot(kind='hist', normed=True)
plt.show()
range = np.arange(0, 1, 0.001)
plt.plot(range, norm.pdf(range,0,120))
plt.show()
range = np.arange(0, 120, 0.001)
plt.plot(range, norm.pdf(range,0,1))
plt.show()
range = np.arange(-5, 5, 0.001)
plt.plot(range, norm.pdf(range,0,1))
plt.show()
range = np.arange(0, 5, 0.001)
plt.plot(range, norm.pdf(range,0,1))
plt.show()
range = np.arange(0, 5, 0.001)
plt.plot(range, norm.pdf(range,0,1))
dfNE.GWh.mean()
dfNE.GWh.std()
import matplotlib.mlab as mlab
mu = dfNE.GWh.mean()
sigma = dfNE.GWh.std()
dfNE.GWh.var()
x = np.linspace(0,150,500)
plt.plot(x, mlab.normpdf(x, mu, sigma))
plt.show()
plt.plot(x, mlab.normpdf(x, mu, sigma))
plt.show()
plt.plot(x, mlab.normpdf(x, mu, sigma))
dfNE['GWh'].plot(kind='hist', normed=True)
plt.show()
dfNE['GWh'].plot(kind='hist', normed=True, bins=50)
plt.plot(x, mlab.normpdf(x, mu, sigma))
plt.show()
plt.show()
dfNE['GWh'].plot(kind='hist', normed=True, bins=50)
plt.plot(x, mlab.normpdf(x, mu, sigma))
plt.show()
%hist
%save
%save plotnoite
%save plotnoite.txt
%save 'plotnoite.txt'
%save '.\plotnoite.txt'
%save .\plotnoite.txt
%save .\plotnoite
%hist1