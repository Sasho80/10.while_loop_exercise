num_unsatisfactory_grades = int(input())
average_score = 0.0
counter_task = 0
unsatisfactory_grade = 0
last_task = ""

while True:
    name_task = int(input())
    if name_task == "Enough":
        print(f"Average score: {average_score/counter_task:.2f}")
        print(f"Number of problems: {counter_task}")
        print(f"Last problem: {last_task}")
        break
    else:
        grade = input()
        average_score += grade
        if name_task != "Enough":
            last_task = name_task
    if grade <= 4:
        unsatisfactory_grade += 1
        if unsatisfactory_grade == num_unsatisfactory_grades:
            print(f"You need a break, {unsatisfactory_grade} poor grades.")
            break
    counter_task += 1
