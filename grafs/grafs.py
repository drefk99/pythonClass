import matplotlib as plt
plt.bar(range(len(count_sort['genres'][0:5])),count_sort['count'][0:5])
plt.xticks(range(len(count_sort['genres'][0:5])),count_sort['genres'][0:5])
count_sort=count.sort('count', ascending=False)
count=rated_movies.groupby('genres')["genres"].mean(axis=0).reset_index(name="count")
count=rated_movies.groupby('genres')["genres"].count().reset_index(name="count")
plt.plot(count["count"])

rated_movies["rating"]=pd.to_numeric(rated_movies["rating"])

medias=rated_movies.groupby('genres')["rating"].mean().reset_index(name="mean")
medias_sort=medias.sort('mean', ascending=False)

plt.bar(range(len(medias_sort['genres'][0:5])),medias_sort['mean'][0:5])
plt.xticks(range(len(medias_sort['genres'][0:5])),medias_sort['genres'][0:5])

count_GR=rated_movies.groupby(['genres','rating'])["genres"].count().reset_index(name="count")



rat_GR=count_GR.sort('count',ascending=False).groupby('rating')['count'].mean().reset_index(name="mean")

count_GR.groupby(['genres'])['rating'].mean().reset_index(name='rating')

cout_20s=count_sort[0:20]


top_20s=count_sort[0:20]
top_20_rat=pd.merge(top_20s, medias, on='genres')
rat_20sort=top_20_rat.sort('mean', ascending=False)
plt.bar(range(len(rat_20sort[0:5])),rat_20sort['mean'][0:5])
plt.xticks(range(len(rat_20sort[0:5])), rat_20sort['genres'][0:5])
plt.bar(range(len(rat_20sort[15:20])),rat_20sort['mean'][15:20])
plt.xticks(range(len(rat_20sort[15:20])), rat_20sort['genres'][15:20])

