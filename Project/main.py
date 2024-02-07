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

while True:
    try:
        # Getting credit input from user
        pass_credit = input("Please enter your Pass credits: \n")

        # Check if Pass credit is an integer
        while not pass_credit.isdigit():
            print("Integer required")
            pass_credit = input("Please enter your Pass credits: \n")

        defer_credit = input("Please enter your Defer credits: \n")

        # Check if Defer credit is an integer
        while not defer_credit.isdigit():
            print("Integer required")
            defer_credit = input("Please enter your Defer credits: \n")

        fail_credit = input("Please enter your Fail credits: \n")

        # Check if Fail credit is an integer
        while not fail_credit.isdigit():
            print("Integer required")
            fail_credit = input("Please enter your Fail credits: \n")

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
            progress_count += 1
            progress_result += '*'
            progress_list.append('Progress: ' + str(pass_credit) + ', ' + str(defer_credit) + ', ' + str(fail_credit))
        # Progress (Module Trailer):
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
        # Do not progress (Module retriever):
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
        # Exclude:
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

        # Total of credits must equal 120
        elif pass_credit + defer_credit + fail_credit != 120:
            print('Total incorrect')

        # Only allowing 0, 20, 40, 60, 80, 100 and 120 to be entered
        elif pass_credit not in range(0, 140, 20) or defer_credit not in range(0, 140, 20) or fail_credit not in range(
                0, 140, 20):
            print('Out of range. Credits can only be in the interval [0,120].')

        # Asking the user if they want to enter another set of data
        options = input(
            "\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: \n").lower()
        if options == 'q':
            break
        elif options != 'y':
            print('Invalid option entered. Please enter either \'y\' or \'q\'.')

    except ValueError as e:
        print(e)
        print('Please enter the credit again.')


# Horizontal Histogram:
# Determine the maximum length of the category names
# Horizontal Histogram:
def h_histogram():
    print('-' * 30)
    print('Horizontal Histogram: ')
    # Map outcome names to their respective counts
    counts = {
        'Progress': progress_count,
        'Trailing': trailer_count,
        'Retriever': retriever_count,
        'Excluded': exclude_count
    }
    # Use the maximum outcome name length to align the histogram
    max_length = max(len(name) for name in counts.keys())

    for outcome in progression_outcome:
        # Adjust the output based on the outcome name length
        print(f"{outcome.ljust(max_length)} {counts[outcome]} :", '* ' * counts[outcome])

    total_outcomes = sum(counts.values())
    print('\n')
    print(f"{total_outcomes} outcome(s) in total")
    print('-' * 30)


h_histogram()
print('\n')


# Vertical Histogram:
def v_histogram(progress_count, trailer_count, retriever_count, exclude_count):
    print('-' * 45)
    print('Vertical Histogram:')

    # Calculate the maximum count to determine the height of the histogram
    max_count = max(progress_count, trailer_count, retriever_count, exclude_count)

    # Create a list of the counts to iterate over
    counts = [progress_count, trailer_count, retriever_count, exclude_count]

    # Print the header
    print(f'{"Progress":>10} {"Trailing":>10} {"Retriever":>10} {"Excluded":>10}')

    # Print each row of the histogram
    for i in range(max_count, 0, -1):
        for count in counts:
            # Print an asterisk if the count is at least as large as the current row number
            print(f'{"*":>10}' if count >= i else f'{" ":>10}', end='')
        print()  # Move to the next line after printing all categories

    print('-' * 45)


# Call the function with the actual counts
v_histogram(progress_count, trailer_count, retriever_count, exclude_count)
print('\n')

# Part 3 (List/Tuple/Dictionary)
print('Part 3 (List/Tuple/Dictionary):')
print(progress_count + trailer_count + retriever_count + exclude_count, 'outcome(s) in total:')
with open('outcomes.txt', 'w') as txt_file:
    txt_file.write('Progression outcomes:\n')
    for progress_credit in progress_list:
        print(progress_credit)
        txt_file.write('\n' + progress_credit)
    for trailer_credit in trailer_list:
        print(trailer_credit)
        txt_file.write('\n' + trailer_credit)
    for retriever_credit in retriever_list:
        print(retriever_credit)
        txt_file.write('\n' + retriever_credit)
    for exclude_credit in exclude_list:
        print(exclude_credit)
        txt_file.write('\n' + exclude_credit)

# Part 4 (Text File):
print('\nPrinting user input from text file:')
with open('outcomes.txt', 'r') as txt_file:
    content = txt_file.read()
    print(content)
