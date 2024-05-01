import pandas as pd

hub1 = pd.read_csv('Hub-1.csv')
hub_all = pd.read_csv('Hub_all.csv')
hub1['hub'] = 'hub1'
print(hub1.shape)

print(hub_all.shape)

hub = pd.concat([hub_all, hub1])
print(hub.shape)

hub.to_csv('hub_all.csv', index=False)
