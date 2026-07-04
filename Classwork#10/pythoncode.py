
users = {
    'adardon': {'password': '1234', 'role': 'student', 'name': 'Arcadio Dardón'},
    'irivas': {'password': '1234', 'role': 'student', 'name': 'Iván Rivas'},
    'kpool': {'password': '1234', 'role': 'student', 'name': 'Keyra Pool'},
    'ccalderon': {'password': '1234', 'role': 'student', 'name': 'Clarisa Calderón'},
    'lescalante': {'password': '1234', 'role': 'student', 'name': 'Luis Escalante'},
    'ahernandez': {'password': '1234', 'role': 'student', 'name': 'Alejandro Hernández'},
    'jpedrozo': {'password': '1234', 'role': 'teacher', 'name': 'Jorge Pedrozo'},
    'dgamboa': {'password': '1234', 'role': 'coordinator', 'name': 'Didier Gamboa'}
}

subjects = ('Prob&Stats', 'Comp&Serv Arch', 'Tutoring', 'DifCalculus', 'Programming', 'Dicrete Math', 'SocialE Skills', 'English')

grades = {
    'adardon': {'Prob&Stats': 8.0, 'Comp&Serv Arch': 7.0, 'Tutoring': 9.0, 'DifCalculus': 8.0, 'Programming': 8.5, 'Dicrete Math': 9.5, 'SocialE Skills': 10.0, 'English': 9.5},
    'irivas': {'Prob&Stats': 8.5, 'Comp&Serv Arch': 8.5, 'Tutoring': 8.0, 'DifCalculus': 8.0, 'Programming': 9.5, 'Dicrete Math': 8.0, 'SocialE Skills': 8.5, 'English': 8.5},
    'kpool': {'Prob&Stats': 7.5, 'Comp&Serv Arch': 8.0, 'Tutoring': 9.5, 'DifCalculus': 9.0, 'Programming': 10.0, 'Dicrete Math': 9.0, 'SocialE Skills': 9.0, 'English': 8.0},
    'ccalderon': {'Prob&Stats': 8.0, 'Comp&Serv Arch': 9.0, 'Tutoring': 9.5, 'DifCalculus': 8.0, 'Programming': 9.0, 'Dicrete Math': 8.5, 'SocialE Skills': 8.0, 'English': 9.5},
    'lescalante': {'Prob&Stats': 8.5, 'Comp&Serv Arch': 9.0, 'Tutoring': 8.0, 'DifCalculus': 8.5, 'Programming': 10.0, 'Dicrete Math': 9.5, 'SocialE Skills': 8.0, 'English': 7.5},
    'ahernandez': {'Prob&Stats': 8.0, 'Comp&Serv Arch': 10.0, 'Tutoring': 10.0, 'DifCalculus': 8.0, 'Programming': 8.5, 'Dicrete Math': 9.0, 'SocialE Skills': 10.0, 'English': 9.5}
}

# PROCESS
access_granted = False
current_user = ''

while access_granted == False:
    username = input('Username: ')
    password = input('Password: ')

    if username in users and users[username]['password'] == password:
        access_granted = True
        current_user = username
    else:
        # OUTPUT
        print('Invalid username or password. Please try again.\n')

current_name = users[current_user]['name']
current_role = users[current_user]['role']

# OUTPUT
print('\nWelcome, ' + current_name + ' (' + current_role.capitalize() + ')')
print('=' * 40)

# PROCESS
if current_role == 'student':

    print('Report Card for ' + current_name)
    print('-' * 40)

    passed_subjects = set()

    for subject in subjects:
        grade = grades[current_user][subject]
        print(subject + ': ' + str(grade))

        if grade >= 8.0:
            passed_subjects.add(subject)

    pending_subjects = set(subjects) - passed_subjects

    print('\nPassed subjects: ' + str(passed_subjects))
    print('Pending subjects: ' + str(pending_subjects))

elif current_role == 'teacher':

    print('Student List:')
    print('-' * 40)

    for username in users:
        if users[username]['role'] == 'student':
            print(username.ljust(10) + ' | ' + users[username]['name'])

    continue_grading = True

    while continue_grading == True:
        print()

        student = input('Student username (or type "Exit" to quit): ')

        if student == 'Exit':
            continue_grading = False
        else:
            if student in grades:

                subject = input('Subject: ')

                if subject in subjects:

                    current_grade = grades[student][subject]
                    new_grade = float(input('New grade: '))

                    print('Current grade: ' + str(current_grade))
                    print('New grade: ' + str(new_grade))
                    confirmation = input('Confirm change? (yes/no): ')

                    if confirmation == 'yes':
                        grades[student][subject] = new_grade
                        print('Grade updated.')
                    else:
                        print('Change canceled.')
                else:
                    print('Invalid subject.')
            else:
                print('Student not found.')

elif current_role == 'coordinator':

    print('Teacher List:')
    print('-' * 40)

    for username in users:
        if users[username]['role'] == 'teacher':
            print(username.ljust(10) + ' | ' + users[username]['name'])

    print('\nSubject List:')
    print('-' * 40)

    for subject in subjects:
        print(subject)

    print('\nStudent List with Grades:')
    print('-' * 90)

    header = 'Subject'.ljust(15)
    for username in grades:
        header = header + users[username]['name'].ljust(20)
    print(header)
    print('-' * 90)

    for subject in subjects:
        row = subject.ljust(15)
        for username in grades:
            grade = grades[username][subject]
            grade_text = str(grade)
            if grade < 8.0:
                grade_text = grade_text + ' (F)'
            row = row + grade_text.ljust(20)
        print(row)

else:
    print('Access type not recognized.')