from unittest import TestCase
from com.kuma.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	def test_soma(self):
		self.assertEqual(self.operacoes.somao([8,2]), 10,"Shold be 10")