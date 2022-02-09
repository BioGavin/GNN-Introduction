import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx

edges = pd.DataFrame()
edges['sources'] = [0,1,2,3,4,4,6,7,7,9,1,4,4,4,6,7,5,8,9,8]
edges['targets'] = [1,4,4,4,6,7,5,8,9,8,0,1,2,3,4,4,6,7,7,9]
edges['weights'] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

G = nx.from_pandas_edgelist(edges, source='sources',target='targets')

# 可视化
fig, ax = plt.subplots()
nx.draw(G, ax=ax, with_labels=True)
plt.show()

# degree: 每个节点所连接的边数
print(nx.degree(G))
# 连通分量: 无向图的一个极大连通子图
print(list(nx.connected_components(G)))
# 图直径: 两两节点最短路径的最大值
print(nx.diameter(G))
# 度中心性: 节点N的度/(节点总数n-1), 数值越大, 表示节点的度在图中越大, 位置越重要
print('度中心性',nx.degree_centrality(G))
# 特征向量中心性
print('特征向量中心性',nx.eigenvector_centrality(G))
# betweenness
print('betweenness',nx.betweenness_centrality((G)))
# closeness
print('closeness',nx.closeness_centrality(G))
# pagerank
print('pagerank',nx.pagerank(G))
# HITS
print('HITS',nx.hits(G,tol=0.00001))