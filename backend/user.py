class User:
    """User class keeps track of the User's basic information."""

    def __init__(self, first: str, last: str, height: int, weight: int,
                 age: int, gender: str, activity_level: str, goal: str) -> None:
        """Initializes user object's with basic information."""
        self.first = first
        self.last = last
        self.height = height # height in inches (in.)
        self.weight = weight # weight in pounds (lbs)
        self.age = age
        self.gender = gender
        self.activity_level = activity_level
        self.goal = goal