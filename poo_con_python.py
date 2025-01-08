class Personaje:
    #Atributos de la clase
    nombre="Default"
    fuerza=0
    inteligencia=0
    vida=0
    defensa=0
    #Indicar que no se haga nada en este momento
    pass
#Variable del constructo vscio de la clase
mi_personaje = Personaje()
mi_personaje.nombre="Diabeto"
print('el nombre del personaje es: ',mi_personaje.nombre)
print('la fuerza del personaje es: ',mi_personaje.fuerza)
print('la inteligencia del personaje es: ',mi_personaje.inteligencia)
print('la vida del personaje es: ',mi_personaje.vida)
print('la defensa del personaje es: ',mi_personaje.defensa)
