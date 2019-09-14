from unittest import TestCase
from com.kuma.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	def test_divisao(self):
		self.assertEqual(self.operacoes.divisao(8,2), 4, "Should be 4")
		
	