class Calculator:
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a, b):
        """Using Static method to summing two numbers."""
        return a + b


    @classmethod
    def multiply(cls, a, b):
        """Multiplying two numbers using class method"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b