

// input_text
// input_rot_amount
// div_output


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

$('.list-item').text('Apple')
// $('.list-item').first().text('Apple')
$('.list-item').css({'color': 'red'})

// let items = document.querySelectorAll('.list-item')
// for (let i=0; i<items.length; i++) {
//     items[i].innerText = 'Apple'
//     items[i].style.color = 'red'
// }


// $('#btn').click(function() {})
$('#input_text').on('input', function() {
    let text = $('#input_text').val()
    let offset = $('#input_rot_amount').val()
    if (text.length === 0) {
        $('#div_output').hide()
        return
    }
    offset = parseInt(offset)
    let output = rotX(text, offset)

    $('#div_output').text(output)
    $('#div_output').show()


})





