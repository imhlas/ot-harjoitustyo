import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_rahamaara_ja_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_maksu_riittava(self):
        vastaus = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(vastaus, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_maksu_ei_riita(self):
        vastaus = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(vastaus, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_maksu_riittava(self):
        vastaus = self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(vastaus, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_maksu_ei_riita(self):
        vastaus = self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(vastaus, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_maksu_riittava(self):
        kortti = Maksukortti(500)

        vastaus = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(vastaus, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla_maksu_ei_riita(self):
        kortti = Maksukortti(100)

        vastaus = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(vastaus, False)

    def test_syo_maukkaasti_kortilla_maksu_riittava(self):
        kortti = Maksukortti(500)

        vastaus = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(vastaus, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_syo_maukkaasti_kortilla_maksu_ei_riita(self):
        kortti = Maksukortti(100)

        vastaus = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(vastaus, False)

    def test_kortin_lataus_kasvattaa_kassaa(self):
        kortti = Maksukortti(200)

        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortille_yritetaan_ladata_neg_summaa(self):
        kortti = Maksukortti(200)

        self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
