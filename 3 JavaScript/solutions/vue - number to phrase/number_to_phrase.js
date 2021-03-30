


let app = new Vue({
    el: '#app',
    data: {
        input_number: '',
        output_phrase: ''
    },
    methods: {
        numberToPhrase: function(num) {
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
        },
        convertNumber: function() {
            // remove any non-digit characters
            this.input_number = this.input_number.replace(/\D/g, "")
            // convert number to phrase
            this.output_phrase = this.numberToPhrase(this.input_number)
            // if we weren't successful, show an error
            if (this.output_phrase === null) {
                this.output_phrase = 'Please enter a valid number'
            }
        }
    }
})


