# Lista de valores
areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]

# Imprimir el segundo elemento.
print("Primer elemento : "+str(areas[1]))
# Imprimir el ultimo elemento.
print("Ultimo elemento : "+str(areas[-1]))
# Imprimir el area de la terraza.
print("El area de la "+str(areas[4])+" es "+str(areas[5]))
# Imprimir del primer al tercer elemento.
print("Del primer al tercer elemento : "+ str(areas[0:2]))
# Imprimir del tercer elemento hasta el ultimo.
print("Del tercer al ultimo elemento : "+str(areas[2:]))
# Imprimir el total del area de las dos habitaciones.
print("Suma de las areas de las dos habitaciones: "+str(areas[9]+areas[11]))
# Modificar el area del lavabo y impimir la nueva lista.
areas[7] = 7
print("Lista con el area del lavabo modificado: \n"+str(areas))
# Agregar el area "pati interior" i 2.78 en las ultimas posiciones. Imprime la nueva lista area.
areas.extend(["pati interior", 2.78])
print("Lista con dos valores nuevos añadidos al final: \n"+str(areas))

