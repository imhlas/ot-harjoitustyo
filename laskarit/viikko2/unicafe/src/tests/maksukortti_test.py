import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 30.00 euroa")

    def test_ota_rahaa_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(150)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.50 euroa")

    def test_saldo_ei_mene_negatiiviseksi(self):
        kortti = Maksukortti(300)
        kortti.ota_rahaa(450)

        self.assertEqual(str(kortti), "Kortilla on rahaa 3.00 euroa")

    def test_ota_rahaa_palauttaa_false(self):
        kortti = Maksukortti(300)

        self.assertEqual(kortti.ota_rahaa(450), False)

    def test_ota_rahaa_palauttaa_true(self):
        kortti = Maksukortti(300)

        self.assertEqual(kortti.ota_rahaa(200), True)

