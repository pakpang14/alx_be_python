class Calculator:
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a,b):
        """Static method to add two numbers."""
        return a + b
    @classmethod
    def multiply(cls,a,b):
        """Class method to multiply two numbers"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b