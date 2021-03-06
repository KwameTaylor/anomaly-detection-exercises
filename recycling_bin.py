'''
**I'll check for (and remove) outliers in IPs' network and host seperately.**
'''

df.network.value_counts().tail(100)

df = df.groupby('network').filter(lambda x : len(x)>3)
df.network.value_counts()

df.shape

df.host.value_counts().tail(800)

df = df.groupby('host').filter(lambda x : len(x)>2)
df.host.value_counts()

df.shape

'''
I might choose to explore hosts with only one-time access at a later point, in which case I would re-add these dropped observations.

I decided to take this code out because it removed too many anomalies that could be interesting. I found that all of the ones I kept originally were from San Antonio during the Darden dates, so obviously I dropped meaningful information.

Saving this code here for documentation purposes, and in case I want to use it again later.
'''