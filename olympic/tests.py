from django.test import TestCase

from olympic.models import NOC


class NOCModelTestCase(TestCase):
    def setUp(self):
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
