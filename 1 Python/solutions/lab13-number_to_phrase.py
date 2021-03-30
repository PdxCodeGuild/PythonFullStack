



def number_to_phrase(num):
    #                0      1      2       3  ...
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num-10]
    elif num < 100:
        tens_digit = num//10
        ones_digit = num%10
        if ones_digit == 0:
            return tens[tens_digit-2]
        else:
            return tens[tens_digit-2] + '-' + ones[ones_digit]
    return None


for i in range(100):
    print(i, number_to_phrase(i))









