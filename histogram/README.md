# Histogramas


## Los 10 más votados

Para delimitar que peliculas deberian ser tomadas en cuenta primero se aplico un filtro donde solamente se buscarian las peliculas más votadas y representarlas en una grafica de barras como se muestra:

### Valores
* Forrest Gump (1994)    					 341
* Pulp Fiction (1994)    					 324
* Shawshank Redemption, The (1994)    		 311
* Silence of the Lambs, The (1991)    		 304
* Star Wars: Episode IV - A New Hope (1977)  291
* Jurassic Park (1993)    					 274
* Matrix, The (1999)    					 259
* Toy Story (1995)    						 247
* Schindler's List (1993)    				 244
* Terminator 2: Judgment Day (1991)    		 237


![alt text](https://github.com/drefk99/pythonClass/blob/master/histogram/best_10.png)

## Histogramas unidos.

Una forma de visualizarlo es con un histograma que contenga todas las peliculas y se pueda ver mejor su comportamiento enfrentandolas de forma más directa evaluando los votos totales por cada una de las calificaciones disponibles (0 al 5), en la siguiente imagen se puede observar esto:

![alt text](https://github.com/drefk99/pythonClass/blob/master/histogram/united_graphs.png)

### Histogramas separados

Si se busca una visión donde la granularidad sea mayor, se pueden separar cada una de las peliculas y ver su comportamiento frente a las calificaciones disponibles como se observa:

![alt text](https://github.com/drefk99/pythonClass/blob/master/histogram/separate_hist.png)

###Notas:
El codigo que genero las graficas se encuentra en hist.py en este mismo directorio.	
