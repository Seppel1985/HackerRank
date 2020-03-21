if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
    #print (students)
    students_sorted = sorted(students, key = lambda x: (x[1],x[0]))
    #print (students_sorted)
    first_number = students_sorted[0][1]
    number_best = 0;
    for student in students_sorted:
        if (student[1] == first_number):
            number_best = number_best+1

    students_sorted_removed_first = students_sorted[number_best:]
    #print(students_sorted_removed_first)

    first_number = students_sorted_removed_first[0][1]
    #print(first_number)
    for student in students_sorted_removed_first:
        if (student[1] == first_number):
            print(student[0])