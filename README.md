# Proyecto
## Integrates: Daniel Poveda Ruiz y Diego Esteban Reyes Nova

### Indice: 

-Introducción al ahorcado 

-Temática (The Last of Us)

-Requisitos Mínimos

-Parámetros definidos por el usuario

-Complementarios

-Diagrama de flujo

-Pseudocódigo

-Código real

-Integración de las dos temáticas

## Introducción al ahorcado:

El ahorcado es un juego clásico en el que una personas trata de adivinar una palabra en específico por medio de escribir letras sobre una determinada cantidad de líneas dependiendo de la palabra a descubrir, la cual ha de ser elegida por una segunda persona que según el jugador vaya avanzando se encargará de indicar al jugador si es que acieta o no a la tarea de adivinar la palabra esto por medio de dibujar una persona ahorcada en un arból mediante una representación de palitos, todo esto hecho sobre una hoja; sin embargo si el jugador no llega a descubrir por completo la palabra enigma antes de que se complete el dibujo del ahorcado, se dará por perdido el juego.

## Temática (The Last of Us):

### Historia y origen: 

Juego hecho por Naughty Dog para playstation 3 y porteado a PS 4, 5 y pc por medio de remaster’s y remakes del original. Se ha adaptado a la pantalla pequeña por medio de la serie homónima, por HBO, y ya tiene una secuela y un DLC. Es una obra de culto entre varios gamers tanto casuales como personas que viven del medio. Se sitúa en estados unidos, en un contexto Postapocalíptico por una pandemia por parte del hongo Cordyceps, que infecta a los humanos transformándolos en una clase de zombies ciegos que perciben, por medio del sonido, a potenciales presas o vectores de infección.

Seguimos la vida de Joel, que intentará cuidar de la niña Ellie, la única persona inmune de la infección del Cordyceps en el mundo, mientras vive un dilema moral entre sacrificarla para tener una potencial cura, o proteger su vida.

## Requisitos Mínimos:

Código original.

Uso de herramientas vistas en el curso.

Interacción y manejo a través de la consola.

Base de datos de al menos 1000 palabras.

Dibujo de hangman en interfaz gráfica.


## Parámetros definidos por el usuario:

Ingreso de las letras.

Nivel de dificultad: Asociado a la cantidad de intentos para dibujar el ahorcado, cantidad de caracteres de la palabra.

Diagrama de flujo: 

![image](https://github.com/user-attachments/assets/9ed98229-5b87-42c4-8a0d-e76b567db629)

## Pseudocódigo:

#Librerías a usar

#random



#listas_de palabras_fáciles=Listado

#listas_de palabras_medias=Listado

#listas_de_palabras_dificiles=Listado

#valor_de_dificultad=texto

#valor de ingresar a partida=texto

#valor_de_puntaje=número

#valor_de_tiempo=número

#valor_tiempo_punto=número



#def función_de_cinematica_inicial:


  #iniciar cinemática 
  


  
#def función_de_cinemática_interaccion:

 
 #si_intento_es_igual_a_5
 
  #imprimir_primera_imagen
  
 #si_intento_es_igual_a_4
 
  #imprimir_segunda_imagen
  
 #si_intento_es_igual_a_3
 
  #imprimir_tercera_imagen
  
 #si_intento_es_igual_a_2
 
  #imprimir_cuarta_imagen
  
 #si_intento_es_igual_a_1
 
  #imprimir_ultima_imagen
  
 #si_intento_es_igual_a_0
 
  #ejecutar_funcion_cinemática_final()

  
#def función_de_cinemática_final:

 #si_puntaje_es_igual_a_cero
 
  #imprimir_cinemática_final_malo
  

 #si_puntaje_es_mayor_a_cero
 
  #imprimir_cinemática_final_bueno


#def función_de_selección_de_dificultad:

#si tal dificultad(facil, media, dificil), ejecutar siguiente lista y cinemática:

 #iniciar cinemática, asignar lista, asignar tiempo, asignar valor de puntaje
 


#def función_tiempo_punto:

 #ejecutar un contador que empiece con tiempo x
 
 #restar a tiempo x 1 segundo
 
 #si tiempo mayor a 80%
 
  #sumar 2
  
 #si tiempo mayor a 40% y menor a 80%
 
  #sumar 1 punto
  
 #si tiempo menor a 40%
 
  #Sumar 0 puntos
  

 
#def función_comparación_palabra:

 #bucle de intentos hasta 0
 
 #si palabra coincide con palabra de la lista
 
  #ejecutar función cinemática final bueno
  
  #sumar a puntos totales puntos de tiempo
  
 #sino:
 
  #restar intento 1 punto
  

#def iniciar juego:

 #si valor de empezar partida es afirmativa
 
  #continue
  
 #sino:
 
  #cerrar_juego_y_despedirse
  

#def función_juego:

 #ejecutar función tiempo
 
 #tomar palabra de lista e imprimir guiones segun cantidad de letras
 
 #mientras tiempo sea mayor a 0:
 
  #palabra_ingresada_por_usuario=()
  
  #ejecutar función comparacion palabra
  
 #si tiempo igual a 0:
 
  #ejecutar cinemática final malo
  

#función principal:

#ingresar valor de empezar partida=input()

#ingresar valor de de dificultad=input()

#ingresar valor de empezar partida=input()

#ejecutar_funcion1: función_de_iniciar_juego()

#ejecutar_funcion2:función_de_selección_de_dificultad()

#ejecutar_funcion3: función_de_cinematica_inicial()

#ejecutar_funcion4:función_juego()

## Integración de las dos temáticas:

Según la dificultad se presentarán distintas temáticas de palabras, según el lore. Fácil: Nombres de personajes, Medio: Lugares de los capítulos, Difícil: Temáticas y elementos del lore.



