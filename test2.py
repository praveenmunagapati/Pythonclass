def getTopStudents(students):
    top_students = []

    for student in students:
        # Unpack the tuple
        name, math, science, english = student

        # Calculate average and round to 2 decimal places
        average = round((math + science + english) / 3, 2)

        # Filter condition: keep if average >= 75.00
        if average >= 75.00:
            top_students.append((name, average))

    return top_students


if __name__ == '__main__':
    try:
        # 1. Takes input from you and processes it the moment you press Enter
        raw_input = input().strip()

        if not raw_input:
            print("[]")
        else:
            # 2. eval() safely turns your pasted text into a real list of tuples
            students = eval(raw_input)

            # 3. Call the function
            result = getTopStudents(students)

            # 4. Print the output
            print(result)

    except EOFError:
        pass
    except Exception as e:
        print("Error processing input:", e)