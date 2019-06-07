import random
from Jugador import Jugador
from JugadorCpu import JugadorCpu
class Juego:
 	def __init__(self):
		self.posiciones = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}
		movimientos = 9
		self.combinacionesGanadoras = [1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]
		self.posicionesVacias = [1,2,3,4,5,6,7,8,9]
		self.jugadorPersona = Jugador()
		self.jugadorCpu = JugadorCpu()
		self.juegosEmpatados = 0
	def MenuPrincipal(self):
		volverAjugar = True
		self.elegirSimbolo()
		while volverAjugar:
			continuar = True
			self.iniciarJuego()
			while continuar:
				respuestaVolveraJugar = input("Desea volver a jugar 1:si 2:no")
				if respuestaVolveraJugar == 2:
					volverAjugar = False
					continuar = False
				elif respuestaVolveraJugar == 1:
					self.posiciones = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}
					self.posicionesVacias = [1,2,3,4,5,6,7,8,9]
					continuar = False
				else:
					print("Recuerda que tienes que elegir entre 1 y 2")



	def seleccionPosicion(self,posicion,simbolo):
		self.posiciones[posicion] = simbolo

	def printJuego(self):
		print(self.posiciones[1]+"|"+self.posiciones[2]+"|"+self.posiciones[3])
		print(self.posiciones[4]+"|"+self.posiciones[5]+"|"+self.posiciones[6])
		print(self.posiciones[7]+"|"+self.posiciones[8]+"|"+self.posiciones[9])
	
	def iniciarJuego(self):
		self.elegirTurno()
		if self.empezarTurnos():
			print("El juego fue un empate")
		self.imprimirResultados()

	def elegirSimbolo(self):
		continuar = True
		while continuar:
			simbolo = input("seleccione el simbolo que desea (selecione '1'-->O / 2-->X): ")
			if simbolo == 1:
				self.jugadorPersona.simbolo = 'O'
				self.jugadorCpu.simbolo = 'X'
				continuar = False
			elif simbolo == 2:
				self.jugadorPersona.simbolo = 'X'
				self.jugadorCpu.simbolo = 'O'
				continuar = False
			else:
				print("Recuerda que debes elegir entre 1 y 2")
		print("Elegiste: "+self.jugadorPersona.simbolo)

	def elegirTurno(self):
		seleccion = input("Se sortea el turno elegir 1 o 2:" )
		ramdomNum = (random.randint(1, 2))
		if seleccion == ramdomNum:
			print("felicitaciones salio "+str(ramdomNum)+", Juegas primero")
			self.jugadorPersona.turno = 1
			self.jugadorCpu.turno = 2
		else:
			print("Mala suerte salio "+str(ramdomNum)+", la maquina juega primero ")
			self.jugadorPersona.turno = 2
			self.jugadorCpu.turno = 1

	def seleccionJugador(self):
		continuar = True
		while continuar:
			print("--------------------")
			seleccion = int(input("Elige la posicion: "))
			print("--------------------")
			if seleccion in self.posicionesVacias:
				self.posiciones[seleccion]= self.jugadorPersona.simbolo
				self.posicionesVacias.remove(seleccion)
				continuar = False
			else:
				print("El numero ingresado esta ocupado o es incorrecto")

	def seleccionCPU(self):
		seleccioncpu = self.jugadorCpu.elegirMovimiento(self.posicionesVacias,self.posiciones,self.jugadorPersona.simbolo)
		self.posiciones[seleccioncpu] = self.jugadorCpu.simbolo
		self.posicionesVacias.remove(seleccioncpu)
		print("-------------------")
		print("La maquina elige: "+str(seleccioncpu))
		print("-------------------")

	
	def empezarTurnos(self):
		for i in range(5):
			if self.jugadorPersona.turno == 1:
				self.seleccionJugador()
				self.printJuego()
				if self.verificarGanador():
					return(False)
				if i == 4:
					self.juegosEmpatados +=1
					return(True)
				else:
					self.seleccionCPU()
					self.printJuego()
					if self.verificarGanador():
						return(False)
			else:
				self.seleccionCPU()
				self.printJuego()
				if self.verificarGanador():
					return(False)
				if i == 4:
					self.juegosEmpatados +=1
					return(True)
				else:
					self.seleccionJugador()
					self.printJuego()
					if self.verificarGanador():
						return(False)

	def verificarGanador(self):
		for CombGan in self.combinacionesGanadoras:
			if (self.posiciones[CombGan[0]] == self.posiciones[CombGan[1]] and self.posiciones[CombGan[1]] == self.posiciones[CombGan[2]] and not(self.posiciones[CombGan[2]]== '-')):
				print("Fin del juego, GANADOR = "+ self.posiciones[CombGan[1]])
				if self.posiciones[CombGan[1]] == self.jugadorPersona.simbolo:
					self.jugadorPersona.juegosGanados += 1
				else:
					self.jugadorCpu.juegosGanados += 1 
				return True

	def imprimirResultados(self):
		print("Resultados Parciales")
		print("Tus Victorias: "+str(self.jugadorPersona.juegosGanados))
		print("Tus Derrotas: "+str(self.jugadorCpu.juegosGanados))
		print("Empates: "+ str(self.juegosEmpatados))


juego = Juego()
juego.MenuPrincipal()
#posicionJugada = input("elige una posicion: ")
#juego.seleccionPosicion(posicionJugada,'o')
#juego.printJuego()