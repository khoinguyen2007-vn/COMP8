    student = []
    n=int(input())
    for i in range(n):
        name = input().strip()
        score = float(input())
        student.append([name,score])
    scores = sorted(set([score for name, score in student]))
    second_lowest = scores[1]
    names = [name for name, score in student if score == second_lowest]
    names.sort()
    for name in names:
        print(name)
    