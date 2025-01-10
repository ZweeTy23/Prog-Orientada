class Personaje:
    #Atributos de la clase
    # nombre="Default"
    # fuerza=0
    # inteligencia=0
    # vida=0
    # defensa=0
    #Indicar que no se haga nada en este momento
    #pass

    #Constructor
    def __init__(self,nombre,fuerza,inteligencia,vida,defensa):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.vida=vida
        self.defensa=defensa
    
    def imprimir_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Vida: {self.vida}")
        print(f"Defensa: {self.defensa}")

    def subir_nivel(self,fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia=self.inteligencia+inteligencia
        self.defensa=self.defensa+defensa

    def esta_vivo(self):
        return self.vida>0
    
    def morir(self):
        self.vida=0
        print(f"El personaje {self.nombre} ha muerto")

    def dmg(self, enemy):
        return self.fuerza - enemy.defensa
    
    def atacar(self, enemy):
        dmg = self.dmg(enemy) 
        enemy.vida = enemy.vida - dmg
        print(f"El personaje {self.nombre} ha atacado a {enemy.nombre} y le ha hecho {dmg} de daño")
        print(f"La vida de {enemy.nombre} es {enemy.vida}")
    

#Variable del constructo vscio de la clase
mi_personaje = Personaje("Dante", 100,3,70,100)
mi_personaje.imprimir_atributos()
mi_enemy = Personaje("Lucifer", 70,30,70,100)
print(mi_personaje.dmg(mi_enemy))

print(mi_personaje.esta_vivo())
mi_personaje.atacar(mi_enemy)
print(mi_personaje.esta_vivo())
mi_enemy.imprimir_atributos()

# print('---------------------------------')
# mi_personaje.subir_nivel(10,1,5) 
# mi_personaje.imprimir_atributos()
# mi_personaje.nombre="Diabeto"
# mi_personaje.fuerza=30
# mi_personaje.inteligencia=10
# mi_personaje.vida=40
# mi_personaje.defensa=15
    

# print('el nombre del personaje es: ',mi_personaje.nombre)
# print('la fuerza del personaje es: ',mi_personaje.fuerza)
# print('la inteligencia del personaje es: ',mi_personaje.inteligencia)
# print('la vida del personaje es: ',mi_personaje.vida)
# print('la defensa del personaje es: ',mi_personaje.defensa)

