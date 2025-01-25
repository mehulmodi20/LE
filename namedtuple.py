from collections import namedtuple
nstudents = int(input())
Student = namedtuple('Student', ' '.join(input().split()))
totalScore = 0
# for student in range(nstudents):
#     s = Student(*input().split())
#     totalScore += int(s.MARKS)
# print(totalScore/nstudents)
print(sum([int(Student(input().split()).MARKS) for _ in range(nstudents)])/nstudents)

