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

max_of_apps = int(input())
department = {'Mathematics': list(), 'Physics': list(), 'Biotech': list(), 'Chemistry': list(), 'Engineering': list()}
applicants = list()
with open("applicant_list.txt", "r") as apps:
    for line in apps:
        # app_items = line.split()
        applicants.append(line.split())

for person in applicants:
    department[person[3]].append([person[0], person[1], float(person[2])])


for key in department.keys():
    sorted_applicants = sorted(department[key], key = lambda x: (-x[2], x[0]))
    department[key] = sorted_applicants


