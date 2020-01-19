from django.test import TestCase

from olympic.models import NOC, Athlete


class NOCModelTestCase(TestCase):
    def setUp(self):
        print("Running NOC Tests")
        NOC.objects.create(noc="BRA", country_name="Brazil", notes=None)
        NOC.objects.create(noc="USA", country_name="United States", notes="Test Note")

    def test_NOC_get_and_field_tests(self):
        br = NOC.objects.get(noc="BRA")
        us = NOC.objects.get(noc="USA")
        self.assertEqual(br.country_name, 'Brazil')  # Expected
        self.assertNotEqual(br.country_name, 'Brasil')  # Not expected
        self.assertEqual(us.country_name, 'United States')  # Expected
        self.assertIsNone(br.notes)
        self.assertIsNotNone(us.notes)


class AthleteModelTestCase(TestCase):
    def setUp(self):
        print("Running Athlete Tests")
        Athlete.objects.create(
            athlete_id=23567,
            name="Fulano de Tal",
            sex="M",
            age="22",
            height="182",
            weight="152",
            team="BRA",
            noc=NOC.objects.create(noc="TST", country_name="Teste", notes=""),
            games="2016 Rio",
            year="2016",
            season="Summer",
            city="Rio",
            sport="Basketball",
            event="Men Basketball",
            medal="Gold"
        )
        Athlete.objects.create(
            athlete_id=23567,
            name="Ciclana de Tal",
            sex="F",
            age="20",
            height="162",
            weight="122",
            team="BRA",
            noc=NOC.objects.create(noc="TSA", country_name="Teste 2", notes=""),
            games="2016 Rio",
            year="2016",
            season="Rio",
            city="Rio",
            sport="Basketball",
            event="Men Basketball",
            medal="Silver"
        )

    def test_NOC_get_and_field_tests(self):
        fulano = Athlete.objects.get(name="Fulano de Tal")
        ciclana = Athlete.objects.get(name="Ciclana de Tal")
        self.assertEqual(fulano.sport, 'Basketball')  # Expected
        self.assertNotEqual(fulano.sex, 'F')  # Not expected
        self.assertEqual(ciclana.sex, 'F')  # Expected
        self.assertIsNotNone(ciclana.medal)
