student_grade_low = 0
student_grade_high = 0

for x in range(40):
    y = input('Enter your name:')
    print('Hello, ' + y)
    z = int(input('Enter your grade:'))
    if z < 55:
        student_grade_low += 1

    elif z > 95:
        student_grade_high += 1
print('students w/ high grade: ' + str(student_grade_high))
print('students w/ low grade: ' + str(student_grade_low))