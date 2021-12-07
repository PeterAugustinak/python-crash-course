class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_serverd=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_serverd

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, increment):
        self.number_served += increment

    def describe_restaurant(self):
        print(f"This {self.restaurant_name} is a {self.cuisine_type} place")

    @staticmethod
    def open_restaurant():
        print("The restaurant is opened!")
