import json

class Student:
    # Initializing the student with name, ID, and an empty list for grades
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  # A list to hold grades for each student

    #add a grade to the student's grades list
    def add_grade(self, grade):
        if 0 <= grade <= 100:  # Ensure grade is within valid range
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")

    #calculate the average grade of the student
    def calculate_average(self):
        if self.grades:  # Check if there are grades to calculate
            return sum(self.grades) / len(self.grades)
        else:
            return 0  # Return 0 if there are no grades

    #determine if the student has passed
    def has_passed(self):
        average = self.calculate_average()
        return average >= 60  #Return True if average is 60 or higher

    #save student details to a JSON file
    def save_to_json(self, filename):
        student_data = {
            'name': self.name,
            'student_id': self.student_id,
            'grades': self.grades,
            'average': self.calculate_average(),
            'passed': self.has_passed()
        }
        try:
            with open(filename, 'w') as file:
                json.dump(student_data, file, indent=4)
            print(f"Student data saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving to JSON: {e}")

#Example
#Create a new student object
student = Student("Ishan", "CT/2020/007")

#Add grades to the student
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)

#Display average and pass status
print(f"Average Grade: {student.calculate_average()}")
print(f"Passed: {student.has_passed()}")

#Save student details to a JSON file
student.save_to_json("student_data.json")
