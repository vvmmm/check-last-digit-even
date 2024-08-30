def is_last_digit_even(number):
    last_digit=int(str(number)[len(str(number))-1])
    return last_digit%2==0
