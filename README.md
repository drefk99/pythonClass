# pythonClass


## Graficas

Para esta practica se generaron tres graficas donde se explica el comportamiento con respecto a las criticas del publico sobre cada genero disponible en la base de datos.

Para tener una mejor visión de lo que pasa con nuestors datos veremos cada una de las componentes principales.

En la siguiente grafica obtenemos el promedio de cada uno de los ratings para ver en donde se concentrala mayoria de las observaciones.

** count_GR=rated_movies.groupby(['genres','rating'])["genres"].count().reset_index(name="count") ** 
** rat_GR=count_GR.sort('count',ascending=False).groupby('rating')['count'].mean().reset_index(name="mean") **
