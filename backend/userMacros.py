from backend.user import User

class UserMacros:
    """Class containing the amount of macronutrients the user must consume
    per day to reach their goal."""

    def __init__(self, user):
        self.user = user
        self.bmi = None  # body mass index
        self.body_fat_percentage = None
        self.bmr = None  # basal metabolic rate (number of calories body needs)
        self.tdee = None  # total daily energy expenditure
        self.daily_calories_min = None
        self.daily_calories_max = None
        self.daily_protein_min = None
        self.daily_protein_max = None
        self.daily_fat_min = None
        self.daily_fat_max = None
        self.daily_carbs_min = None
        self.daily_carbs_max = None

    def calculate_bmi(self):
        """Calculates the user's BMI (Body Mass Index)."""

        self.bmi = (self.user.weight * 703) / (self.user.height ** 2)

    def calculate_body_fat_percentage(self):
        """Calculates the user's body fat percentage. This calculation,
        though, is not as accurate as real body fat percentage tests. It is
        only an estimate."""
        calc = (1.20 * self.bmi) + (0.23 * self.age)
        if self.user.gender == "Male":
            self.body_fat_percentage = calc - 16.2
        elif self.user.gender == "Female":
            self.body_fat_percentage = calc - 5.4

    def calculate_bmr(self):
        """Calculates the user's BMR (Basal Metabolic Rate). The BMR is the
        number of calories your body needs to maintain its basic physiological
        functions at rest."""
        if self.user.gender == "Male":
            return (66 + (6.23 * self.user.weight) + (12.7 * self.user.height)
                    - (6.8 * self.user.age))
        elif self.user.gender == "Female":
            return (655 + (4.35 * self.user.weight) + (4.7 * self.user.height)
                    - (4.7 * self.user.age))

    def calculate_tdee(self):
        """Calculates the user's TDEE (Total Daily Energy Expenditure). Based
        on the User's activity level, this function will multiply the BMR by a
        specific rate."""
        if self.user.activity_level == "Sedentary":
            self.tdee = self.bmr * 1.2
        elif self.user.activity_level == "Lightly Active":
            self.tdee = self.bmr * 1.375
        elif self.user.activity_level == "Moderately Active":
            self.tdee = self.bmr * 1.55
        elif self.user.activity_level == "Very Active":
            self.tdee = self.bmr * 1.725
        elif self.user.activity_level == "Super Active":
            self.tdee = self.bmr * 1.9

    def calculate_daily_calories(self):
        """Calculates the amount of calories the User needs to consume per day
        in order to reach their goal. If a male goes below 1500 calories or a
        female goes below 1200 calories, it is unhealthy and requires medical
        supervision. Therefore, we will not risk the health of our users and
        establish a bare minimum calorie amount for both genders."""
        if self.user.goal == "Maintain Weight":
            self.daily_calories_min = self.tdee - 100
            self.daily_calories_max = self.tdee + 100
        elif self.user.goal == "Lose Weight":
            self.daily_calories_min = self.tdee - 750
            self.daily_calories_max = self.tdee - 500
        elif self.user.goal == "Gain Weight":
            self.daily_calories_min = self.tdee + 250
            self.daily_calories_max = self.tdee + 500

        if self.user.gender == "Male" and self.daily_calories_min < 1500:
            self.daily_calories_min = 1500
            self.daily_calories_max = 1750
        elif self.user.gender == "Female" and (self.daily_calories_min < 1200):
            self.daily_calories_min = 1200
            self.daily_calories_max = 1450

    def calculate_macronutrients(self):
        """Calculates the amount of protein, carbs, and fat the user needs to
        consume per day in order to reach their goal. These calculations are
        based off of the amount of calories a user must consume per day."""
        if self.user.goal == "Maintain Weight":
            self.daily_protein_min = (0.25 * self.daily_calories_min) / 4
            self.daily_protein_max = (0.25 * self.daily_calories_max) / 4
            self.daily_fat_min = (0.30 * self.daily_calories_min) / 9
            self.daily_fat_max = (0.30 * self.daily_calories_max) / 9
            self.daily_carbs_min = (0.45 * self.daily_calories_min) / 4
            self.daily_carbs_max = (0.45 * self.daily_calories_max) / 4
        elif self.user.goal == "Lose Weight":
            self.daily_protein_min = (0.35 * self.daily_calories_min) / 4
            self.daily_protein_max = (0.35 * self.daily_calories_max) / 4
            self.daily_fat_min = (0.30 * self.daily_calories_min) / 9
            self.daily_fat_max = (0.30 * self.daily_calories_max) / 9
            self.daily_carbs_min = (0.35 * self.daily_calories_min) / 4
            self.daily_carbs_max = (0.35 * self.daily_calories_max) / 4
        elif self.user.goal == "Gain Weight":
            self.daily_protein_min = (0.30 * self.daily_calories_min) / 4
            self.daily_protein_max = (0.30 * self.daily_calories_max) / 4
            self.daily_fat_min = (0.25 * self.daily_calories_min) / 9
            self.daily_fat_max = (0.25 * self.daily_calories_max) / 9
            self.daily_carbs_min = (0.45 * self.daily_calories_min) / 4
            self.daily_carbs_max = (0.45 * self.daily_calories_max) / 4