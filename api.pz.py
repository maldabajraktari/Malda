import streamlit as st

from abc import ABC, abstractmethod
class Person(ABC):

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self._weight = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass
    def print_info(self):
        return f"{self.name}, Age: {self.age}, Weight: {self.weight} kg, Height: {self.height} m, BMI: {self.calculate_bmi():.2f}, Category: {self.get_bmi_category()}"

class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)
    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.3
    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"
class BMIApp:
    def __init__(self):
        self.people = []
    def add_person(self, person):
        self.people.append(person)
    def collect_user_data(self):
        st.title("BMI Calculator")
        name = st.text_input("Enter Name: ")
        age = st.number_input("Age: ", step=1)
        weight = st.number_input(
            "Weight in kg", min_value=0, max_value=120, value=25)
        height = st.number_input("Height in meters", min_value=0.0, value=1.75)

        if st.button("Add Person"):
            if age >= 18:
                person = Adult(name, age, weight, height)
            else:
                person = Child(name, age, weight, height)
            self.add_person(person)
            st.success(f"{name} has been added")

 def print_result(self):
        st.subheader("Results")
        for person in self.people:
            st.write(person.print_info())

    def run(self):
        self.collect_user_data()
        if self.people:
            self.print_result()
if __name__ == "__main__":
    app = BMIApp()
    app.run()

