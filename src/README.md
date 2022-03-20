## Metodos Numericos UNSAM 2022
### Método de trisección
En un lenguaje de programación a elección, implementar la siguiente variante del método de bisección para hallar alguna raíz real de una función (especificada en el código del programa y que tenga al menos una).

El método a usar debe ser análogo a bisección, pero en lugar de dividir en dos intervalos en cada paso, se dividirá en tres intervalos para las iteraciones pares, y en dos intervalos para las impares. En cada iteración se evaluará la función en cada uno de los puntos que limitan estos dos o tres intervalos uno de otro, y con un criterio adecuado a determinar por Uds. se decidirá cuál de los dos o tres intervalos definidos tomar para el próximo paso. (Nota: no importa cuál de las raíces existentes dentro del intervalo consigan aproximar, solo hay que aproximar alguna.)

El programa deberá recibir como entrada dos valores reales a y b que definen el intervalo inicial y un real epsilon positivo para acotar el error. El programa al comienzo deberá verificar si los valores a y b ingresados cumplen con la condición inicial que asegura la existencia de una raíz dentro de ese intervalo inicial. De no ser así, informará el error, lo mismo ante cualquier otra eventualidad que lo impida (decidan Uds. cuál o cuáles).

En cuanto a la condición de parada, ustedes deberán elegir dos entre las las explicadas en clase, que sean razonables. El algoritmo tendrá entonces como condición de parada la primera que se cumpla entre esas dos condiciones elegidas, usando el valor epsilon dado (o, si fuera necesario, otro parámetro a ingresar como entrada).

El programa deberá imprimir una tabla donde en cada fila aparezca el número de iteración, los puntos que definen los intervalos actuales, el valor de la raíz aproximada actual y la función aplicada a esos puntos considerados. Y, finalmente, la raíz aproximada con error menor que epsilon o según la condición de parada propuesta.

La salida del programa podrá ser la estándar, o bien un archivo, a elección de Uds.

Entrega: integrantes, descripción de la solución y decisiones tomadas (lenguaje y versión, funciones, criterios), código fuente, ejemplos de corrida capturados.

