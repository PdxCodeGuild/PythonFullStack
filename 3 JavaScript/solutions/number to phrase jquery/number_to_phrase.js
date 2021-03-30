



function numberToPhrase(num) {
    let ones_dict = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    let teens_dict = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }
    let tens_dict = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }
    if (num < 10) {
        return ones_dict[num]
    } else if (num < 20) {
        return teens_dict[num]
    } else if (num < 100) {
        let tens_digit = Math.floor(num/10)
        let ones_digit = num%10
        if (ones_digit == 0) {
            return tens_dict[tens_digit]
        } else {
            return tens_dict[tens_digit] + '-' + ones_dict[ones_digit]
        }
    } else if (num < 1000) {
        let hundreds_digit = Math.floor(num/100)
        let tens_digit = Math.floor(num/10)%10
        let ones_digit = num%10
        // return hundreds_digit + ' ' + tens_digit + ' ' + ones_digit
        if (tens_digit == 0 && ones_digit == 0) {
            return ones_dict[hundreds_digit] + ' hundred'
        } else if (tens_digit == 0) {
            return ones_dict[hundreds_digit] + ' hundred and ' + ones_dict[ones_digit]
        } else if (tens_digit == 1) {
            return ones_dict[hundreds_digit] + ' hundred and ' + teens_dict[ones_digit+10]
        } else if (ones_digit == 0) {
            return ones_dict[hundreds_digit] + ' hundred and ' + tens_dict[tens_digit]
        } else {
            return ones_dict[hundreds_digit] + ' hundred and ' + tens_dict[tens_digit] + '-' + ones_dict[ones_digit]
        }
    } else {
        return null
    }
}

// for (let i=0; i<100; ++i) {
//     console.log(i + ' ' + numberToPhrase(i))
// }

// input_number
// btn_go
// div_output

$('#btn_go').click(() => {
    // get the number the user entered and parse it as an integer
    let number = $('#input_number').val()
    number = parseInt(number)
    // check if the number is within a valid range
    if (number >= 0 && number < 1000) {
        // convert the number to a phrase
        let phrase = numberToPhrase(number)
        // set the phrase as the output text
        $('#div_output').text(phrase)
    } else {
        // show the user an error message
        $('#div_output').text('Enter a number between 0 and 1000')
        // clear the error message after 3 seconds
        setTimeout(function() {
            $('#div_output').text('')
        }, 3000)
    }
})


