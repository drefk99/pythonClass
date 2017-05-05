#To get the top 10
count=rated_movies.groupby('title')["title"].count().reset_index(name="count")
count_sort=count.sort('count', ascending=False)
top10=count_sort[0:10]

#To create the bar graph
plt.figure()
plt.bar(range(len(top10)), top10['count'])
plt.xticks(range(len(top10)), top10['title'], rotation=60, size=10)
plt.title("Top 10")
plt.ylabel("Votes")
#plt.xlabel("Movies")
plt.tight_layout()

#To get ratings from each movies (top 5)
gump=rated_movies.where(rated_movies["title"]=='Forrest Gump (1994)').dropna()
pulp=rated_movies.where(rated_movies["title"]=='Pulp Fiction (1994)').dropna()
shaw=rated_movies.where(rated_movies["title"]=='Shawshank Redemption, The (1994)').dropna()
lambs=rated_movies.where(rated_movies["title"]=='Silence of the Lambs, The (1991)').dropna()
start=rated_movies.where(rated_movies["title"]=='Star Wars: Episode IV - A New Hope (1977)').dropna()

gump['rating']=pd.to_numeric(gump['rating'])
pulp['rating']=pd.to_numeric(pulp['rating'])
shaw['rating']=pd.to_numeric(shaw['rating'])
lambs['rating']=pd.to_numeric(lambs['rating'])
start['rating']=pd.to_numeric(start['rating'])

#To get separate graph
plt.figure()
plt.subplot(231)
plt.title("Forrest Gump")
plt.ylabel("Value")
plt.xlabel("Grade")
plt.legend()
plt.hist(gump['rating'], bins=np.arange(0,5+2,1), histtype='stepfilled', normed=True, color='grey',alpha=0.8, label='Forrest Gump')


plt.subplot(232)
plt.title("Pulp Fiction")
plt.ylabel("Votes")
plt.xlabel("Grades")
plt.legend()
plt.hist(pulp['rating'], bins=np.arange(0,5+2,1), histtype='stepfilled', normed=True, color='yellow',alpha=1, label='Pulp Fiction')

plt.subplot(133)
plt.title("Shawshank Redemption")
plt.ylabel("Votes")
plt.xlabel("Grades")
plt.legend()
plt.hist(shaw['rating'], bins=np.arange(0,5+2,1), histtype='stepfilled', normed=True, color='orange',alpha=1, label='Shawshank Redemption')

plt.subplot(234)
plt.title("Silence of the Lambs")
plt.ylabel("Votes")
plt.xlabel("Grades")
plt.legend()
plt.hist(lambs['rating'], bins=np.arange(0,5+2,1), histtype='stepfilled', normed=True, color='red',alpha=1, label='Silence of the Lambs')
plt.subplot(235)
plt.title("Star Wars: Episode IV - A New Hope")
plt.ylabel("Votes")
plt.xlabel("Grades")
plt.legend()
plt.hist(start['rating'], bins=np.arange(0,5+2,1), histtype='stepfilled', normed=True, color='brown',alpha=1, label='Star Wars: Episode IV - A New Hope')
plt.tight_layout()

#To get united graph
plt.figure()
plt.hist([gump['rating'], pulp['rating'], shaw['rating'], lambs['rating'], start['rating']], bins=np.arange(0,5+2,1), color=['grey','yellow','orange', 'red', 'brown'], label=['Forrest Gump', 'Pulp fiction', 'Shawshank Redemption', 'Silence of the Lambs', 'Star Wars: Episode IV - A New Hope'])
plt.title("Top 5")
plt.ylabel("Votes")
plt.xlabel("Grades")
plt.legend()
plt.show()