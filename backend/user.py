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
        """Calculates the user's BMI (Body Mass Index)."""

        try:
            self.bmi = (self.weight * 703) / (self.height ** 2)
        except ZeroDivisionError:
            print("Invalid height.")

    def calculate_body_fat_percentage(self):
        """Calculates the user's body fat percentage. This calculation,
        though, is not as accurate as real body fat percentage tests. It is
        only an estimate."""

        if self.bmi:
            calc = (1.20 * self.bmi) + (0.23 * self.age)
            if self.gender == "Male":
                self.body_fat_percentage = calc - 16.2
            elif self.gender == "Female":
                self.body_fat_percentage = calc - 5.4

        else:
            print("BMI must be calculated.")








