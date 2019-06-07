import random
from Jugador import Jugador
class JugadorCpu(Jugador):
	def __init__(self):
		Jugador.__init__(self)
		self.combinacionesGanadoras = [1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]

	def elegirMovimiento(self,listaPosicionesVacias,listaPosOcupadas,simboloRival):
		def VerificarPorGanar(simboloPropio):
			for grupocombinaciones in self.combinacionesGanadoras:
				contadorVerdaderos = 0
				posicionVacia = 0
				verificarOcupadoRival = 0
				for posicion in grupocombinaciones:
					if listaPosOcupadas[posicion] == simboloPropio:
						contadorVerdaderos +=1
					elif listaPosOcupadas[posicion] == '-':
						posicionVacia = posicion		
					else:
						verificarOcupadoRival = 1
				if contadorVerdaderos == 2 and verificarOcupadoRival == 0 :
					return posicionVacia
			return False

		if not(VerificarPorGanar(self.simbolo)):
			if not VerificarPorGanar(simboloRival):
				eleccion = random.choice(listaPosicionesVacias)
			else:
				eleccion = VerificarPorGanar(simboloRival)
		else:
			eleccion = VerificarPorGanar(self.simbolo)
		return eleccion