

// 4 input fields - lowercase, uppercase, digits, punctuation
// "go" button to get the password
// element to show the generated password

// hide output element until the password is generated


function randomChar(letters) {
    // floor of random num * number of characters
    let random_index = Math.floor(Math.random() * letters.length)
    return letters[random_index]
}
// console.log(randomChar('abc')) // a, b, or c

function shuffle(array) {
    for (let i = 0; i < array.length; ++i) {
        let j = Math.floor(Math.random() * (array.length - i))
        let t = array[i]
        array[i] = array[j]
        array[j] = t
    }
}
// let array = ['a', 'b', 'c', 'd', 'e']
// shuffle(array)
// console.log(array)



function generatePassword(num_lower, num_upper, num_digits, num_punctuation) {

    let lower = "abcdefghijklmnopqrstuvwxyz"
    let upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let digits = "0123456789"
    let punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    let accumulation = []
    for (let i = 0; i < num_lower; i++) {
        accumulation.push(randomChar(lower))
    }
    for (let i = 0; i < num_upper; i++) {
        accumulation.push(randomChar(upper))
    }
    for (let i = 0; i < num_digits; i++) {
        accumulation.push(randomChar(digits))
    }
    for (let i = 0; i < num_punctuation; i++) {
        accumulation.push(randomChar(punctuation))
    }
    // console.log(accumulation)
    shuffle(accumulation)
    return accumulation.join('')
}

// console.log(generatePassword(2, 2, 2, 2)) // asYU23%^


let app = new Vue({
    el: '#app',
    data: {
        num_lowercase: '3',
        num_uppercase: '3',
        num_digits: '3',
        num_punctuation: '3',
        output_password: ''
    },
    methods: {
        generatePasswordClick: function() {
            // alert(this.num_lowercase + ' ' + this.num_uppercase + ' ' + this.num_digits + ' ' + this.num_punctuation)
            this.output_password = generatePassword(this.num_lowercase, this.num_uppercase, this.num_digits, this.num_punctuation)
        }
    }
})