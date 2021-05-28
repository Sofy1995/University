# first_exam = int(input())
# second_exam = int(input())
# third_exam = int(input())
# mean_score = (first_exam + second_exam + third_exam) / 3
# print(mean_score)
# if mean_score >= 60:
#     print('Congratulations, you are accepted!')
# else:
#     print('We regret to inform you that we will not be able to offer you admission.')


# n = int(input()) # the total number of applicants
# m = int(input()) # the number of applicants that should be accepted
#
# applicants = list()
# for _ in range(n):
#     first, last, score = input().split()
#     applicants.append([first + " " + last, float(score)])
#
# sorted_applicants = sorted(applicants, key = lambda x: (-x[1], x[0]))
#
# print("Successful applicants:")
# for num in range(m):
#     print(sorted_applicants[num][0])

# 0 John 1 Ritchie 2 89 3 45 4 83 5 75 6 Physics 7 Engineering 8 Mathematics

def distribute_for_deps(priority):
    priority += 5
    scores = {'Biotech': 3, 'Chemistry': 3, 'Engineering': 5, 'Mathematics': 4, 'Physics': 2}
    temp_department = {'Biotech': list(), 'Chemistry': list(), 'Engineering': list(), 'Mathematics': list(), 'Physics': list()}
    for person in applicants:
        temp_department[person[priority]].append([person[0], person[1], person[scores[person[priority]]]])


def sort_deps():
    for key in department.keys():
        sorted_applicants = sorted(department[key], key=lambda x: (-x[2], x[0]))
        department[key] = sorted_applicants


def del_accepted_app():
    accepted = list()
    non_accepted = list()
    for key in department.keys():
        accepted += department[key][:min(max_of_apps, len(department[key]))]
    temp_accepted = [x[:2] for x in accepted]
    for applicant in applicants:
        if applicant[:2] not in temp_accepted:
            non_accepted.append(applicant)
    return non_accepted


def print_accepted():
    for key in department.keys():
        print(key)
        for i in range(min(max_of_apps, len(department[key]))):
            print(*department[key][i][:2], float(department[key][i][2]))
        print("")


max_of_apps = int(input())
department = {'Biotech': list(), 'Chemistry': list(), 'Engineering': list(), 'Mathematics': list(), 'Physics': list()}
applicants = list()


with open("applicants.txt", "r") as apps:
    for line in apps:
        app_items = line.split()
        temp = list()
        for item in app_items:
            try:
                temp.append(int(item))
            except ValueError:
                temp.append(item)

        applicants.append(temp)


for prioritet in [1,2,3]:
    # applicants = sorted(applicants, key=lambda x: (-x[2], x[0]))
    distribute_for_deps(prioritet)
    applicants = del_accepted_app()

sort_deps()
print_accepted()

