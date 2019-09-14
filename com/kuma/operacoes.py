class Operacoes():
	def eh_primo(num):
		for i in range(2, num // 2):
			if num % i == 0:
				return False
		return True