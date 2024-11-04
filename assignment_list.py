# 1. Print the list containing names of Partria, Faith, Phiona and Anita
studentList = ['Sandra','Partricia', 'Phiona', 'Anita']
print(f"\nThe Students' List: {studentList}\t")

#Excluding first and last names
print(f"\nStudents' List excluding first and last names:{studentList[1:3]}\t")

# 2. Add Masha to the 4th position
studentList.insert(4,'Masha')
print(f"\nAdding Masha to th Students' List: {studentList}\t")

# 3. Update the name Phiona to Aladina
studentList[2]='Aladina'
print(f"\nUpdating the name Phiona to Aladina: {studentList}\t")

# 4. Display the length of the students' list
print(f"\nThe Number of Students in the List: {len(studentList)}\t")

# 5. Print all students' names/ list using a for loop
print(f"\nPrinting List using a for loop\t")
studentList = ['Partricia', 'Aladina', 'Anita', 'Masha']
for students in studentList:
    print(students)


# 6. Calculate the total marks for students' marks variable and the answer is 304
studentMarks =[80,56,78,90]

totalMarks = sum(studentMarks)
print(f"\nTotal Marks: {totalMarks}\t")


#Alternatively;
def calculate_total_marks(marks):
    total = sum(marks)
    return total
studentMarks = [80,56,78,90]  
totalMarks = calculate_total_marks(studentMarks)

print("Total marks:", totalMarks)  
