number = float(input('Enter a number: '))
base = int(input('Enter a base: '))
number_of_digits = -1
number_list = []
each_digit = []
final_answer = 0
number_without_int = str(0)
int_number = int(number)
number_list_right = []
left_digits = []
full_number_list = []
is_wrong = False

for i in str(number):
    if i >= str(base):
        print("Numbers can't be above or equal to " + str(base) + ".")
        is_wrong = True
        break

if is_wrong == False:
    for i in str(int(number)):
        left_digits.append(i)
    length_left_digits = len(left_digits)

    for i in str(number):
        full_number_list.append(i)
    del full_number_list[0:length_left_digits]
    j = 0
    for i in full_number_list:
        full_number_list[j] = (i)
        j += 1

    for i in full_number_list:
        number_without_int = number_without_int + i
        number_without_int_float = float(number_without_int)

    if number_without_int_float != 0:
        for i in str(number_without_int_float):
            number_list_right.append(i)
        del number_list_right[0:2]
        j = 0
        for i in number_list_right:
            number_list_right[j] = int(i)
            j += 1

    for i in str(int_number):
        number_list.append(int(i))
        number_of_digits += 1

    for i in number_list_right:
        number_list.append(int(i))

    for i in number_list:
        each_digit.append(i * (base ** number_of_digits))
        number_of_digits -= 1

    for i in each_digit:
        final_answer += i

    print(final_answer)