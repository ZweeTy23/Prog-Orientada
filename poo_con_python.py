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

class Guerrero(Personaje):
    #Sobreescribir constructor
    def __init__(self,nombre,fuerza,inteligencia,vida,defensa, espada):
        super().__init__(nombre,fuerza,inteligencia,vida,defensa)
        self.espada= espada

    #Sobreescribir método imprimir_atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("Espada:", self.espada)

    def elegir_arma(self):
        opcion = int(input("Elige un arma:\n(1)Lanza de obsidiana, dano 10 \n(2)Lanza de Chaya, dano 5\nEligue aqui>>>>"))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 5
        else:
            print("Opción no válida")
            self.elegir_arma()

    #sobreescribir calculo de dano
    def dmg(self, enemy):
        return self.fuerza * self.espada - enemy.defensa



class Mago(Personaje):
    #Sobreescribir constructor
    def __init__(self,nombre,fuerza,inteligencia,vida,defensa, biblia):
        super().__init__(nombre,fuerza,inteligencia,vida,defensa)
        self.biblia= biblia

    #Sobreescribir método imprimir_atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("Biblia:", self.biblia)

    def elegir_arma(self):
        opcion = int(input("Elige un arma:\n(1)Biblia antigua, dano 10 \n(2)Biblia de Maradona, dano 100\nEligue aqui>>>>"))
        if opcion == 1:
            self.biblia = 10
        elif opcion == 2:
            self.biblia = 5
        else:
            print("Opción no válida")
            self.elegir_arma()

    #sobreescribir calculo de dano
    def dmg(self, enemy):
        return self.inteligencia * self.biblia - enemy.defensa
    
tlatoani = Guerrero("Apocalipto",20,15,10,100,5)
# tlatoani.elegir_arma()

michaelJackson = Personaje("Michael Jackson" ,20,15,10,100)    
Magician = Mago("Merlin",20,15,10,100,5)
# Magician.elegir_arma()
# Magician.imprimir_atributos()
tlatoani.imprimir_atributos()
Magician.imprimir_atributos()
michaelJackson.imprimir_atributos()

#ataques masivos
michaelJackson.atacar(tlatoani)


tlatoani.atacar(Magician)
Magician.atacar(michaelJackson)

#Variable del constructo vscio de la clase
# mi_personaje = Personaje("Dante", 100,3,70,100)
# mi_personaje.imprimir_atributos()
# mi_enemy = Personaje("Lucifer", 70,30,70,100)
# print(mi_personaje.dmg(mi_enemy))

# print(mi_personaje.esta_vivo())
# mi_personaje.atacar(mi_enemy)
# print(mi_personaje.esta_vivo())
# mi_enemy.imprimir_atributos()

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

