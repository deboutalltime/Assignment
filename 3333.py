from collections import deque

students = deque(range(1,3334))
count = 1

while len(students) > 1:
    student = students.popleft()

    if count == 1:
        students.append(student)

    count = count % 3 + 1

print(students[0])
