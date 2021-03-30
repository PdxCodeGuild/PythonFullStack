



/*
def rotn_approach2(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += n
        index %= len(alphabet)

        output += alphabet[index]
    return output
        
# print(rotn_approach2('hello', 10)) # rovvy
# print(rotn_approach2('rovvy', -10)) # hello
*/




function rotX(text, offset) {

    let alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet += alphabet.toUpperCase()
    alphabet += '0123456789'
    alphabet += '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    alphabet += ' \t\n'
    while (offset < 0) {
        offset += alphabet.length
    }
    // maybe convert text to lower case?
    let output = ''
    for (let i=0; i<text.length; i++) {
        let char = text[i]
        // console.log(i + ' ' + text[i])
        // console.log(alphabet.indexOf(char))
        let alphabet_index = alphabet.indexOf(char)
        if (alphabet_index == -1) {
            output += char
        } else {
            alphabet_index += offset
            alphabet_index %= alphabet.length
            // console.log(alphabet[alphabet_index])
            output += alphabet[alphabet_index]
        }
    }
    return output
}

console.log(rotX('hello', 13)) // uryyb

let input_text = document.querySelector('#input_text')
let input_rot_amount = document.querySelector('#input_rot_amount')
let btn_encrypt = document.querySelector('#btn_encrypt')
let div_cipher_output = document.querySelector('#div_cipher_output')
let div_cipher_decrypt = document.querySelector('#div_cipher_decrypt')

div_cipher_output.style.color = 'lightgrey'
div_cipher_decrypt.style.color = 'lightgrey'

btn_encrypt.addEventListener('click', function() {
    // let name = input_name.value
    // div_output.innerText = 'Hello, ' + name + '!'
    

    // get the text to encrypt from the text input
    let text_to_encrypt = input_text.value
    // get the offset
    let our_offset = parseInt(input_rot_amount.value)
    // call rotX
    let output = rotX(text_to_encrypt, our_offset)
    // show output
    div_cipher_output.innerText = output

    div_cipher_decrypt.innerText = rotX(output, -our_offset)

    div_cipher_output.style.color = 'black'
    div_cipher_decrypt.style.color = 'black'
})





