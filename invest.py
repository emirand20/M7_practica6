# Imprimir el total dels diners acumulats després de 7 anys

def invest(dinero, year, incres):
    return (dinero * incres)*year

# A invest le pasas los valores de el dinero que tienes, los años a los que se le aplica y el precio que se le incrementa
print(invest(100, 7, 1.1))