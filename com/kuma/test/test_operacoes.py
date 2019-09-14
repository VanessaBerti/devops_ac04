from unittest import TestCase
from com.kuma.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()

	def test_eh_primo_5():
		self.assertEqual(self.operacao.eh_primo(5), "Should be True")

		