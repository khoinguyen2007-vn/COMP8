class Student:
    def __init__(self,name):
        self.name = name
        self.scores = []
    def add_score(self,subject,score):
        self.scores.append(score)
    def avg(self):
        if not self.scores:
            return 0.00
        return sum(self.scores) / len(self.scores)
    def rank(self):
        average = self.avg()
        if average >= 8.00:
            return "Excellent"
        if average >= 6.50:
            return "Good"
        if average >= 5.00:
            return "Average"
        return "Poor"
name = input()
n = int(input())
student = Student(name)
for i in range(n):
    line = input().split()
    score = float(line[-1])
    subject = " ".join(line[:-1])
    student.add_score(subject,score)
print(f'{name} {student.avg():.2f} {student.rank()}')
