class Polynomial:

    def __init__(self, coefficients):

        if not isinstance(coefficients, list):
            raise ValueError("Invalid input."
                             " Coefficients have to be a list.")
        for i in coefficients:
            if not isinstance(i, (int, float)):
                raise ValueError("Invalid input."
                                 " Coefficients have to be numbers.")

        self.coefficients = coefficients

    def degree(self):
        """
        This function calculates a degree of a polynomial

        Returns:
            deg (int): A degree of a provided polynomial

        """
        deg = len(self.coefficients) - 1
        return deg

    def __str__(self):
        """
        This function creates a string representation of a polynomial

        Returns:
            pol_str (str): A string representation of a polynomial
        """
        pol_str = ""
        power = self.degree()
        for coefficient in self.coefficients:
            if power == 1:
                if coefficient == 1:
                    pol_str += "x + "
                elif coefficient == -1:
                    pol_str += "-x + "
                else:
                    pol_str += str(coefficient) + "x + "
            elif power == 0:
                pol_str += str(coefficient)
            else:
                if coefficient == 1:
                    pol_str += "x^" + str(power) + " + "
                elif coefficient == -1:
                    pol_str += "-x^" + str(power) + " + "
                else:
                    pol_str += str(coefficient) + "x^" + str(power) + " + "

            power -= 1

        return pol_str

    def __call__(self, x):
        """
        This function calculates a result of a polynomial if we
                substitute x with provided number

        Returns:
            result (int): A result of a polynomial if we
                substitute x with provided number
        """
        result = 0
        power = self.degree()
        for coefficient in self.coefficients:
            result += coefficient * pow(x, power)
            power -= 1

        return result

    def __add__(self, other):
        """
        This function implements an addition operator
        for polynomial objects

        Arguments:
            other (Polynomial): other polynomial that we want to add to
                the first one

        Returns:
            Polynomial(added_coefficients) (Polynomial): A new polynomial
                with resulting coefficients

        Raises:
            ValueError: If other is not a polynomial
        """
        if not isinstance(other, Polynomial):
            raise ValueError("This is not a polynomial."
                             " Only polynomial can be added to a polynomial.")

        added_coefficients = []
        length = max(len(self.coefficients), len(other.coefficients))

        if len(self.coefficients) < length:
            self.coefficients = ([0] * (length - len(self.coefficients))
                                 + self.coefficients)

        if len(other.coefficients) < length:
            other.coefficients = ([0] * (length - len(other.coefficients))
                                  + other.coefficients)

        for i in range(length):
            added_coefficients.append(self.coefficients[i]
                                      + other.coefficients[i])

        return Polynomial(added_coefficients)

    def __sub__(self, other):
        """
        This function implements a subtraction operator for polynomial objects

        Arguments:
            other (Polynomial): other polynomial that we want to subtract from
                the first one

        Returns:
            Polynomial(subtracted_coefficients) (Polynomial): A new polynomial
                with resulting coefficients

        Raises:
            ValueError: If other is not a polynomial
        """
        if not isinstance(other, Polynomial):
            raise ValueError("This is not a polynomial."
                             " Only polynomial can be added to a polynomial.")

        subtracted_coefficients = []
        length = max(len(self.coefficients), len(other.coefficients))

        if len(self.coefficients) < length:
            self.coefficients = ([0] * (length - len(self.coefficients))
                                 + self.coefficients)

        if len(other.coefficients) < length:
            other.coefficients = ([0] * (length - len(other.coefficients))
                                  + other.coefficients)

        for i in range(length):
            subtracted_coefficients.append(self.coefficients[i]
                                           - other.coefficients[i])

        return Polynomial(subtracted_coefficients)

    def __mul__(self, other):
        """
        This function implements a multiplication operator for polynomial objects

        Arguments:
            other (Polynomial): other polynomial that we want to multiply by
                the first one

        Returns:
            Polynomial(multiplied_coefficients) (Polynomial): A new polynomial
                with resulting coefficients

        Raises:
            ValueError: If other is not a polynomial
        """
        if not isinstance(other, Polynomial):
            raise ValueError("This is not a polynomial."
                             " Only polynomial can be added to a polynomial.")

        length = len(self.coefficients) + len(other.coefficients) - 1
        multiplied_coefficients = [0] * length

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                multiplied_coefficients[i + j] += (self.coefficients[i]
                                                   * other.coefficients[j])

        zero_list = []

        for i in multiplied_coefficients:
            if i == 0:
                zero_list.append(i)
            else:
                break

        for i in zero_list:
            multiplied_coefficients.remove(i)

        return Polynomial(multiplied_coefficients)

    def __iadd__(self, other):
        """
        This function implements a += operator for polynomial objects

        Arguments:
            other (Polynomial): other polynomial that will be added
                to the first polynomial

        Returns:
            self: First polynomial increased by the other

        Raises:
            ValueError: If other is not a polynomial
        """
        if not isinstance(other, Polynomial):
            raise ValueError("This is not a polynomial."
                             " Only a polynomial can be added to a polynomial.")

        length = max(len(self.coefficients), len(other.coefficients))

        if len(self.coefficients) < length:
            self.coefficients = ([0] * (length - len(self.coefficients))
                                 + self.coefficients)

        if len(other.coefficients) < length:
            other.coefficients = ([0] * (length - len(other.coefficients))
                                  + other.coefficients)

        for i in range(length):
            self.coefficients[i] += other.coefficients[i]

        return self

    def __isub__(self, other):
        """
        This function implements a -= operator for polynomial objects

        Arguments:
            other (Polynomial): polynomial that will be subtracted to
                the first polynomial

        Returns:
            self: First polynomial decreased by the other

        Raises:
            ValueError: If other is not a polynomial
        """
        if not isinstance(other, Polynomial):
            raise ValueError("This is not a polynomial."
                             " Only a polynomial can be added to a polynomial.")

        length = max(len(self.coefficients), len(other.coefficients))

        if len(self.coefficients) < length:
            self.coefficients = ([0] * (length - len(self.coefficients))
                                 + self.coefficients)

        if len(other.coefficients) < length:
            other.coefficients = ([0] * (length - len(other.coefficients))
                                  + other.coefficients)

        for i in range(length):
            self.coefficients[i] = self.coefficients[i] - other.coefficients[i]

        return self

    def __imul__(self, other):
        """
        This function implements a += operator for polynomial objects

        Arguments:
            other (Polynomial): other polynomial that will be added
                to the first polynomial

        Returns:
            self: First polynomial increased by the other

        Raises:
            ValueError: If other is not a polynomial
        """

        if not isinstance(other, Polynomial):
            raise ValueError("This is not a polynomial."
                             " Only polynomial can be added to a polynomial.")

        length = len(self.coefficients) + len(other.coefficients) - 1
        result = [0] * length

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result[i + j] += self.coefficients[i] * other.coefficients[j]

        self.coefficients = result

        zero_list = []

        for i in self.coefficients:
            if i == 0:
                zero_list.append(i)
            else:
                break

        for i in zero_list:
            self.coefficients.remove(i)

        return self


if __name__ == '__main__':

    try:
        pol1 = Polynomial([7, 0, 172, -18, 0])
        pol2 = Polynomial([0, 1, -2, 2])

        degree = Polynomial.degree(pol1)
        print(f"The degree of this polynomial is: {degree} \n")

        pol_str = str(pol1)
        print(f"The text representation of this polynomial is:"
              f" {pol_str} \n")

        pol_result = Polynomial.__call__(pol1, 2)
        print(f"The value of this polynomial for the provided x is:"
              f" {pol_result} \n")

        pol_add = pol1 + pol2
        print(f"The result of addition of these polynomials is:"
              f" {pol_add.coefficients} \n")

        pol_sub = pol1 - pol2
        print(f"The result of subtraction of these polynomials is:"
              f" {pol_sub.coefficients} \n")

        pol_mul = pol1 * pol2
        print(f"The result of multiplication of these polynomials is:"
              f" {pol_mul.coefficients} \n")

        pol1 += pol2
        print(f"The result of in-place addition of these polynomials is:"
              f" {pol1.coefficients} \n")

        pol1 -= pol2
        print(f"The result of in-place subtraction of these polynomials is:"
              f" {pol1.coefficients} \n")

        pol1 *= pol2
        print(f"The result of in-place multiplication of these polynomials is:"
              f" {pol1.coefficients} \n")

    except ValueError as e:
        print(f"Error: {e}")
