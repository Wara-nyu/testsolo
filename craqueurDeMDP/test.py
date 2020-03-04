import unittest
from craqueur import *

class MotDePasse(unittest.TestCase):
    def test_renvoie_Salut(self):
        self.assertEqual("Salut!",craq("salut"))
    def test_renvoie_Motdepasse(self):
        self.assertEqual("Motdepasse!",craq("motdepasse"))
    def test_renvoie_motdepasse(self):
        self.assertEqual("motdepasse!",craq("Motdepasse"))
    def test_renvoie_nombre(self):
        self.assertEqual("1234567!",craq("1234567"))

unittest.main()
