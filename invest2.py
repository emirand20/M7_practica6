#Creamos una funcion la cual le pasaremos saving es el dinero que hemos ahorrado en un mes
#increase el dinero que incrementamos cada año ahorrado
#years el control de años
def invest2(savings, increase, years):
    result = (savings * increase) * years
    return round(result)

print('El dinero ahorrado es ' + str(invest2(100, 1.1, 7)))
