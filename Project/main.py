# List of progression outcomes
progression_outcome = ['Progress', 'Trailing', 'Retriever', 'Excluded']
progression_outcome2 = ['Progress', 'Progress (module trailer)', 'Do not Progress - module retriever', 'Exclude']

# Set count to 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

# Empty lists (Append credits into them)
progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []

# Empty strings (Append '*' into them)
progress_result = ''
trailer_result = ''
retriever_result = ''
exclude_result = ''

# Initiating a loop
while True:
    # Getting credit input from user
    pass_credit = input("Please enter your Pass credits: \n")
    defer_credit = input("Please enter your Defer credits: \n")
    fail_credit = input("Please enter your Fail credits: \n")
    # Adding try and except to only allow integers to be entered
    try:
        # Turning credits into integers
        pass_credit = int(pass_credit)
        defer_credit = int(defer_credit)
        fail_credit = int(fail_credit)
        # Progress:
        if pass_credit == 120 and defer_credit == 0 and fail_credit == 0:
            print('-_- ' * 10)
            print("Pass credit =", pass_credit)
            print("Defer credit =", defer_credit)
            print("Fail credit =", fail_credit)
            print("Progression outcome:", progression_outcome2[0])
            print('-_- ' * 10)
            # Adding one to Progress count each time this occurs
            progress_count += 1
            # Adding 1 asterisk each time this occurs
            progress_result += '*'
            # Appending user input into a list
            # Turning credits into strings so I can concatenate with other strings
            progress_list.append('Progress: ' + str(pass_credit) + ', ' + str(defer_credit) + ', ' + str(fail_credit))
            # Giving option to continue or quit
            options = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: \n").lower()
            if options == 'y':
                continue
            elif options == 'q':
                break
            else:
                print('Invalid option entered. Please enter your credits.')

        ## Progress (Module Trailer):
        elif pass_credit == 100 and defer_credit == 20 and fail_credit == 0 or pass_credit == 100 and defer_credit == 0 and fail_credit == 20:
            print('-_- ' * 15)
            print("Pass credit = ", pass_credit)
            print("Defer credit = ", defer_credit)
            print("Fail credit = ", fail_credit)
            print("Progression outcome:", progression_outcome2[1])
            print('-_- ' * 15)
            trailer_count += 1
            trailer_result += '*'
            trailer_list.append('Trailer: ' + str(pass_credit) + ', ' + str(defer_credit) + ', ' + str(fail_credit))
            options = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: \n").lower()
            if options == 'y':
                continue
            elif options == 'q':
                break
            else:
                print('Invalid option entered. Please enter your credits.')

        ## Do not progress (Module retriever):
        elif pass_credit in range(0, 100, 20) and defer_credit in range(0, 140, 20) and fail_credit in range(0, 80, 20):
            print('-_- ' * 18)
            print("Pass credit = ", pass_credit)
            print("Defer credit = ", defer_credit)
            print("Fail credit = ", fail_credit)
            print("Progression outcome:", progression_outcome2[2])
            print('-_- ' * 18)
            retriever_count += 1
            retriever_result += '*'
            retriever_list.append('Retriever: ' + str(pass_credit) + ', ' + str(defer_credit) + ', ' + str(fail_credit))
            options = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: \n").lower()
            if options == 'y':
                continue
            elif options == 'q':
                break
            else:
                print('Invalid option entered. Please enter your credits. ')

        ## Exclude:
        elif pass_credit in range(0, 60, 20) and defer_credit in range(0, 60, 20) and fail_credit in range(80, 140, 20):
            print('-_- ' * 10)
            print("Pass credit = ", pass_credit)
            print("Defer credit = ", defer_credit)
            print("Fail credit = ", fail_credit)
            print("Progression outcome:", progression_outcome2[3])
            print('-_- ' * 10)
            exclude_count += 1
            exclude_result += '*'
            exclude_list.append(
                'Exclude: ' + str(pass_credit) + ', ' + str(defer_credit) + ', ' + str(fail_credit))
            options = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: \n").lower()
            if options == 'y':
                continue
            elif options == 'q':
                break
            else:
                print('Invalid option entered. Please enter your credits. ')

        # Total of credits must equal 120
        elif pass_credit + defer_credit + fail_credit != 120:
            print('Total incorrect')

        # Only allowing 0, 20, 40, 60, 80, 100 and 120 to be entered
        elif pass_credit != range(0, 140, 20) or defer_credit != range(0, 140, 20) or fail_credit != range(0, 140, 20):
            print('Out of range. Credits can oan only be in the interval [0,120].')

    except ValueError:
        print('Integer required')

#Horizontal Histogram:
#h_histogram = Horizontal Histogram function
def h_histogram():
    print('-' * 30)
    print('Horizontal Histogram: ')
    print(progression_outcome[0], progress_count, ':', '* ' * progress_count)
    print(progression_outcome[1], trailer_count, ':', '* ' * trailer_count)
    print(progression_outcome[2], retriever_count, ':', '* ' * retriever_count)
    print(progression_outcome[3], exclude_count, ':', '* ' * exclude_count)
    print('\n')
    print(progress_count + trailer_count + retriever_count + exclude_count, 'outcome(s) in total')
    print('-' * 30)
h_histogram()
print('\n')

#Vertical Histogram:
#v_histogram = Vertical Histogram function

def v_histogram():
    print('-' * 45)
    print('Vertical Histogram:')

    print(f'{progression_outcome[0]:>4} {progression_outcome[1]:>10} {progression_outcome[2]:>12} {progression_outcome[3]:>10}')
    for progress in progress_result:
        print(f'{progress:>4}')
        for trailer in trailer_result:
            print(f'{trailer:>15}')
        for retriever in retriever_result:
            print(f'{retriever:>28}')
        for exclude in exclude_result:
            print(f'{exclude:>40}')
        print('\n')
        print(progress_count + trailer_count + retriever_count + exclude_count, 'outcome(s) in total')
        print('-' * 45)
v_histogram()

print('\n')
# Part 3 (List/Tuple/Dictionary)
print('Part 3 (List/Tuple/Dictionary):')
print(progress_count + trailer_count + retriever_count + exclude_count, 'outcome(s) in total:')
txt_file = open('outcomes.txt', 'w')
txt_file.write('Progression outcomes:\n')
txt_file.close()
for progress_credit in progress_list:
    print(progress_credit)
    txt_file = open('outcomes.txt', 'a')
    txt_file.write('\n' + progress_credit)
    txt_file.close()
for trailer_credit in trailer_list:
    print(trailer_credit)
    txt_file = open('outcomes.txt', 'a')
    txt_file.write('\n' + trailer_credit)
    txt_file.close()
for retriever_credit in retriever_list:
    print(retriever_credit)
    txt_file = open('outcomes.txt', 'a')
    txt_file.write('\n' + retriever_credit)
    txt_file.close()
for exclude_credit in exclude_list:
    print(exclude_credit)
    txt_file = open('outcomes.txt', 'a')
    txt_file.write('\n' + exclude_credit)
    txt_file.close()

# Part 4 (Text File):
print('\nPrinting user input from text file:')
txt_file = open('outcomes.txt', 'r')
content = txt_file.read()
print(content)
txt_file.close()