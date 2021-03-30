function getSelectedRadioButtonValue(name) {
    // let radio_buttons = document.querySelectorAll('input[name="fruits"]')
    let radio_buttons = document.getElementsByName(name)
    for (let i=0; i<radio_buttons.length; ++i) {
        if (radio_buttons[i].checked) {
            return radio_buttons[i].value
        }
    }
}

function randomInt(a, b) {
    return Math.floor(a + Math.random()*(b-a+1))
}

function randomChoice(arr) {
    let i = randint(0, arr.length-1)
    return arr[i]
}
