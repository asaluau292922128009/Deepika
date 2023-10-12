class student:

  def __ init __(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa



def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

students = [student("Hari","B123",7.8),
            student("shakthi","B124",8.6),
            student("priya","B125",9.5),
            student("nithya","B126",9.6),

           ]
sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number,student.cgpa))