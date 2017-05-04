# pythonClass


## Graficas

Para esta practica se generaron tres graficas donde se explica el comportamiento con respecto a las criticas del publico sobre cada genero disponible en la base de datos.

Para tener una mejor visión de lo que pasa con nuestors datos veremos cada una de las componentes principales.

### Rating
En la siguiente grafica obtenemos el promedio de cada uno de los ratings para ver en donde se concentrala mayoria de las observaciones.

* count_GR=rated_movies.groupby(['genres','rating'])["genres"].count().reset_index(name="count")
* rat_GR=count_GR.sort('count',ascending=False).groupby('rating')['count'].mean().reset_index(name="mean")
![alt text](https://github.com/drefk99/pythonClass/blob/master/figure_1-5.png)

### Genres
Hay algunos casos donde la cantidad de observaciones solo llegan a 1 y esto le quita claridad a nuestro analizis, por ello se filtraron unicamente los 20 mas comentados de todas la peliculas.

* count_sort=count.sort('count', ascending=False) *
* top_20s=count_sort[0:20] *
![alt text](https://github.com/drefk99/pythonClass/blob/master/figure_1-4.png)

### Rating and count in genres

Ahora que se tienen claro estos puntos podemos hacer la union entre los dato seleccionados anteriormente para obtener los generos con las mejores calificaciones.

* top_20_rat=pd.merge(top_20s, medias, on='genres') *
* rat_20sort=top_20_rat.sort('mean', ascending=False) * 
* plt.bar(range(len(rat_20sort[0:5])),rat_20sort['mean'][0:5]) *
* plt.xticks(range(len(rat_20sort[0:5])), rat_20sort['genres'][0:5]) *

#### Mejores
![alt text](https://github.com/drefk99/pythonClass/blob/master/figure_1-6.png)

#### Peores 
![alt text](https://github.com/drefk99/pythonClass/blob/master/figure_1-7.png)
