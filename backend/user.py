class User:
    """User class keeps track of the user's body metrics (weight, bmi,
    etc.)."""

    def __init__(self, first: str, last: str, height: int, weight: int, age: int, gender: str) -> None:
        """Initializes user object's with basic information."""
        self.first = first
        self.last = last
        self.height = height # height in inches (in.)
        self.weight = weight # weight in pounds (lbs)
        self.age = age
        self.gender = gender
        self.bmi = None
        self.body_fat_percentage = None

    def calculate_bmi(self):
        """Calculates the user's BMI (Body Mass Index)."""

        self.bmi = (self.weight * 703) / (self.height ** 2)

    def calculate_body_fat_percentage(self):
        """Calculates the user's body fat percentage. This calculation,
        though, is not as accurate as real body fat percentage tests. It is

        only an estimate."""
        calc = (1.20 * self.bmi) + (0.23 * self.age)
        if self.gender == "Male":
            self.body_fat_percentage = calc - 16.2
        elif self.gender == "Female":
            self.body_fat_percentage = calc - 5.4