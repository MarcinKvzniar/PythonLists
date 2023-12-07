from datetime import date
from statistics import mean, stdev


class HealthProfile:
    range_of_healthy_bmi = (18.5, 24.9)

    def __init__(self, name, dob, height, weight):
        self.name = name
        self.dob = dob  # year of birth
        self.height = height  # in cm
        self.weight = weight  # in kg

    def get_age(self):
        """
        This function calculates the age in years based on the year
        of birth

        Returns:
            age (int): age of the patient in years

        Raises:
            ValueError: If dob is not an integer or calculated age
                        is invalid (smaller than 0 or greater than 120)

        Example how to do such a function was taken from here:
        https://www.codingem.com/how-to-calculate-age-in-python/
        """
        if not isinstance(self.dob, int):
            raise ValueError("Invalid data provided, integer expected.")

        today = date.today()
        age = today.year - self.dob

        if age < 0 or age > 120:
            raise ValueError("Provided age of this patient is impossible.")
        else:
            return age

    def get_target_hr(self):
        """
        This function calculates the target heart rate for
        moderate-intensity for a particular patient. Handling of
        exceptions for this function has been already done in function
        get_age as this function is dependent on that one.

        Returns:
            target_hr (tuple): Tuple that contains a minimal and
            maximal target heart rate
        """
        max_hr = 220 - self.get_age()
        target_hr_min = round(max_hr * 0.64, 2)
        target_hr_max = round(max_hr * 0.76, 2)

        return target_hr_min, target_hr_max

    def get_bmi(self):
        """
        This function calculates the BMI for a particular patient from
        the formula for calculating BMI (kg/m^2):
        https://www.diabetes.ca/resources/tools---resources/body-mass
        -index-(bmi)-calculator

        Returns:
            bmi (float): Value of the BMI of a patient

        Raises:
            ValueError:
                        - If provided height or weight is not an integer
                        - If weight is smaller than 2kg or greater than 300kg
                        - If height is smaller than 50cm or greater than 270cm
        """
        if not isinstance(self.weight, int):
            raise ValueError("Invalid weight provided, integer expected")

        if not isinstance(self.height, int):
            raise ValueError("Invalid height provided, integer expected")

        if self.weight > 300 or self.weight < 2:
            raise ValueError("Weight of this patient is impossible.")

        elif self.height > 270 or self.height < 50:
            raise ValueError("Height of this patient is impossible.")

        else:
            bmi = self.weight / ((self.height / 100) ** 2)
            return round(bmi, 2)

    @staticmethod
    def calculate_age_stats(patients_list):
        """
        This function calculates mean and standard deviation of ages
        from a list of patients

        Arguments:
            patients_list (list): List of patients

        Returns:
            mean_age (float): mean age of list of patients calculated
            by a function mean from statistics module

            std_dev_age (float): standard deviation of age of a list of
            patients calculated by a function stdev imported from
            statistics module

        Raises:
            ValueError: If patients_list is not a list
        """
        if not isinstance(patients_list, list):
            raise ValueError("patients_list must be a list")

        ages = []
        for patient in patients_list:
            age = patient.get_age()
            ages.append(age)

        mean_age = mean(ages)
        std_dev_age = stdev(ages)
        return mean_age, std_dev_age

    @staticmethod
    def find_people_at_risk(patients_list):
        """
        This function identifies patients with their BMI out of
        healthy range

        Arguments:
            patients_list (list): List of patients

        Returns:
            str: If all patients have their BMI in the healthy range
            bmi_out_of_range (list): List of patients that have
            their BMI outside a valid range

        Raises:
            ValueError: If patients_list is not a list

        """
        if not isinstance(patients_list, list):
            raise ValueError("Invalid patients list provided,"
                             " expected list type")

        bmi_out_of_range = []

        for patient in patients_list:
            bmi = patient.get_bmi()
            if (bmi < HealthProfile.range_of_healthy_bmi[0]
                    or bmi > HealthProfile.range_of_healthy_bmi[1]):
                bmi_out_of_range.append(patient)

        if not bmi_out_of_range:
            return "All patients have their BMI in the healthy range"
        else:
            return bmi_out_of_range


if __name__ == '__main__':

    patient1 = HealthProfile("John Smith", 2003,
                             189, 81)
    patient2 = HealthProfile("Michael Jackson", 1958,
                             176, 70)
    patient3 = HealthProfile("Ricky Martin", 1971,
                             174, 72)
    patient4 = HealthProfile("Lionel Messi", 1987,
                             170, 72)
    patient5 = HealthProfile("Adam Malysz", 1977,
                             170, 55)
    patients_list = [patient1, patient2, patient3,
                     patient4, patient5]

    invalid_patients_list = []

    for patient in patients_list:
        try:
            if not isinstance(patient.name, str):
                raise ValueError("Name has to be a string.")

            print(f"Patient {patient.name} is"
                  f" {patient.get_age()} years old")
            print(f"His target heart rate is"
                  f" {patient.get_target_hr()}")
            print(f"His height is {patient.height} cm")
            print(f"His weight is {patient.weight} kg")
            print(f"His BMI is {patient.get_bmi()} \n")

        except ValueError as e:
            invalid_patients_list.append(patient)
            print(f"Error: {e} This patient has been removed from the"
                  f" list. \n")

    for patient in invalid_patients_list:
        patients_list.remove(patient)

    mean_age, std_dev_age = HealthProfile.calculate_age_stats(patients_list)
    print(f"Mean age: {mean_age:.2f}")
    print(f"Standard deviation of age: {std_dev_age:.2f}")

    patients_at_risk = HealthProfile.find_people_at_risk(patients_list)
    print("\nPatients with out of range BMI: ")
    for patient in patients_at_risk:
        print(f"{patient.name}: {patient.get_bmi():.2f} BMI")

