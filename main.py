number = float(input('Enter the number: '))
base = float(input('Enter the base: '))
int_number = int(number)
fractional_number = number - int(number)
number_of_digits = 0
number_list = []

while int_number != 0:
    number_list.append(str(int(int_number % base)))
    int_number = (int_number // base)

number_list.append('.')
while fractional_number != 0 and number_of_digits <= 100:
    number_list.append(str(int(fractional_number * base)))
    fractional_number = (fractional_number * base - int(fractional_number * base))
    number_of_digits += 1

for i in number_list:
    print(i, end="")
