# Estructuras de datos lineales
**Problema 9.3** Escribir un programa que, hacienda uso de una Pila, procese cada uno de los caracteres de una expresión que viene dada en una línea. La finalidad es verificar el equilibrio de paréntesis, llaves y corchetes. Por ejemplo, la siguiente expresión tiene un número de paréntesis equilibrado:  
((a+b)*5)-7

A esta otra expresión le falta un corchete: 2*[(a+b)/2.5 + x - 7*y

**Diccionario de palabras desconocidas**:

**¿Qué es una pila?** 

Una pila (_stack_) es una colección ordenada de elementos a los cuales sólo se puede acceder por un único lugar o extremo de la pila. Los elementos se añaden o se quitan (borran) de la pila sólo por su parte superior (cima). 
Es una estructura de datos que almacena y recupera sus elementos atendiendo a un orden estricto. Las pilas se conocen también como estructuras LIFO (_Last-in, first-out_, último en entrar primero en salir).  Este es el caso de una pila de platos, una pila de libros, etc.

**Uso de las pilas**:

Las pilas se utilizan en compiladores, sistemas operativos y programas de aplicaciones. Una aplicación interesante es la evaluación de expresiones aritméticas, también la organización de la memoria.


**Las pilas y los lenguajes de programación** :

Los compiladores comprueban los programas buscando errores sintácticos. A menudo, la falta de un símbolo (como por ejemplo la falta de un finalizador de comentario * / o } ) causa que el compilador desparrame cientos de líneas de mensajes de error sin identificar el error real. 
Una herramienta útil en esta situación es un programa que comprueba si todo está equilibrado: es decir, si para todo { existe un } correspondiente, todo [ tiene un ], etc. La secuencia [ {  } ] es correcta, pero [ ( ] )  no lo es, por lo que contar simplemente el número de apariciones de cada símbolo no es suficiente. (suponga por ahora que estamos procesando una secuencia de tokens y no se preocupe de problemas tales como que la constante carácter ‘ { ‘ no necesita emparejarse con ‘ } ‘,)
Una pila es útil para comprobar si hay símbolos desequilibrados, porque sabemos que cuando se encuentra un símbolo de determinación como ), debe emparejarse con el símbolo no cerrado (  más recientemente visto. 


**Fuente:** 

Joyanes-Aguilar, L., & Zahonero-Martinez, I. (2008). Estructuras de datos en Java. Madrid, España: McGraw-Hill.