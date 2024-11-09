class User:
    """User class keeps track of the user's body metrics (weight, bmi,
    etc.)."""

    def __init__(self, name, height, weight, age, gender):
        """Initializes user object's with basic information."""
        self.name = name
        self.height = height # height in inches (in.)
        self.weight = weight # weight in pounds (lbs)
        self.age = age
        self.gender = gender
        self.bmi = None
        self.body_fat_percentage = None

    def calculate_bmi(self):
        try:
            self.bmi = (self.weight * 703) / (self.height ** 2)
        except ZeroDivisionError:
            print("Invalid height.")

    def calculate_body_fat_percentage(self):
        if self.bmi:
            body_fat_percentage = (1.20 * self.bmi) + (0.23 * self.age) - 16.2
        else:
            print("BMI must be calculated.")








