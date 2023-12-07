import unittest
from health_profile import HealthProfile


class TestHealthProfile(unittest.TestCase):

    def test_get_age_valid_input(self):
        patient1 = HealthProfile("John Smith", 2003, 189, 81)
        self.assertEqual(patient1.get_age(), 20)
        patient2 = HealthProfile("John Smith", 1903, 189, 81)
        self.assertEqual(patient2.get_age(), 120)
        patient3 = HealthProfile("John Smith", 2023, 189, 81)
        self.assertEqual(patient3.get_age(), 0)

    def test_get_age_invalid_input(self):
        invalid_patient1 = HealthProfile("John Smith", -4, 189, 81)
        invalid_patient2 = HealthProfile("John Smith", 'f', 189, 81)
        invalid_patient3 = HealthProfile("John Smith", 174, 189, 81)
        with self.assertRaises(ValueError):
            invalid_patient1.get_age()
            invalid_patient2.get_age()
            invalid_patient3.get_age()

    def test_get_target_hr_valid_input(self):
        patient1 = HealthProfile("John Smith", 2003, 189, 81)
        self.assertAlmostEqual(patient1.get_target_hr(), (128.0, 152.0))
        patient2 = HealthProfile("John Smith", 1903, 189, 81)
        self.assertAlmostEqual(patient2.get_target_hr(), (64.0, 76.0))
        patient3 = HealthProfile("John Smith", 2023, 189, 81)
        self.assertAlmostEqual(patient3.get_target_hr(), (140.8, 167.2))

    def test_get_target_hr_invalid_input(self):
        invalid_patient1 = HealthProfile("John Smith", -4, 189, 81)
        invalid_patient2 = HealthProfile("John Smith", 'f', 189, 81)
        invalid_patient3 = HealthProfile("John Smith", 174, 189, 81)
        with self.assertRaises(ValueError):
            invalid_patient1.get_target_hr()
            invalid_patient2.get_target_hr()
            invalid_patient3.get_target_hr()

    def test_get_bmi_valid_input(self):
        patient1 = HealthProfile("John Smith", 2003, 189, 81)
        self.assertEqual(patient1.get_bmi(), 22.68)
        patient2 = HealthProfile("John Smith", 2003, 210, 120)
        self.assertEqual(patient2.get_bmi(), 27.21)
        patient2 = HealthProfile("John Smith", 2003, 51, 3)
        self.assertEqual(patient2.get_bmi(), 11.53)

    def test_get_bmi_invalid_input(self):
        invalid_patient1 = HealthProfile("John Smith", 2003, 42, 370)
        invalid_patient2 = HealthProfile("John Smith", 2003, 0, 0)
        invalid_patient3 = HealthProfile("John Smith", 2003, 'f', 'c')
        with self.assertRaises(ValueError):
            invalid_patient1.get_bmi()
            invalid_patient2.get_bmi()
            invalid_patient3.get_bmi()

    def test_calculate_age_stats_valid_input(self):
        patients_list = [
            HealthProfile("John Smith", 2003, 189, 81),
            HealthProfile("Michael Jackson", 1958, 176, 70),
            HealthProfile("Ricky Martin", 1971, 174, 72),
            HealthProfile("Lionel Messi", 1987, 170, 72),
            HealthProfile("Adam Malysz", 1977, 170, 55)
        ]
        mean_age, std_dev_age = HealthProfile.calculate_age_stats(patients_list)
        self.assertAlmostEqual(mean_age, 43.80, places=2)
        self.assertAlmostEqual(std_dev_age, 16.95, places=2)

    def test_find_people_at_risk(self):
        patients_list = [
            HealthProfile("John Smith", 2003, 189, 81),
            HealthProfile("Michael Jackson", 1958, 176, 70),
            HealthProfile("Ricky Martin", 1971, 174, 72),
            HealthProfile("Lionel Messi", 1987, 170, 72),
            HealthProfile("Joe Big", 1977, 170, 150)
        ]
        patients_at_risk = HealthProfile.find_people_at_risk(patients_list)
        self.assertEqual(len(patients_at_risk), 2)
        self.assertEqual(patients_at_risk[0].get_bmi(), 24.91)
        self.assertEqual(patients_at_risk[1].get_bmi(), 51.9)


if __name__ == '__main__':
    unittest.main()
