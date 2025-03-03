"""
if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  fact:int=1
  factorial_de_num =(lambda x,y: ((i*y) for i in range(x)))(num,fact)
  print("El factorial de " + str(num) + " es " + str(factorial_de_num))

  def fibo_recursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fibo_recursivo(n-1)+fibo_recursivo(n-2)  

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serie_fibo = fibo_recursivo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serie_fibo))
"""#a recursiva
"""
def pot_recursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return pot_recursivo(n-1)+pot_recursivo(n-2)  

if __name__ == "__main__":
  x = int(input("Ingrese numero a: "))
  op =pot_recursivo(x)
  print("La operacion de" + str(x) + " es " + str(op))

  #if __name__ == "__main__":
#  x = int(input("Ingrese numero a: "))
#  op = (lambda x,: (x/(((x)**(1/3))-1)))(x)
#  print("La suma de " + str(x) + " y "  + " es " + str(op))
"""
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
 # si tiempo mayor a 40% y menor a 80%
  # sumar 1 punto
 # si tiempo menor a 40%
  # sumar 0 puntos
 
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

