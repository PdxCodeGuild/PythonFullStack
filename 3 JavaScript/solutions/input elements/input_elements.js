

// callback function example
// function double(x) {
//     return x * 2
// }
// function performOperation(nums, func) {
//     let output = []
//     for (let i=0; i<nums.length; ++i) {
//         output.push(func(nums[i]))
//     }
//     return output
// }
// console.log(performOperation([1, 2, 3, 4], double))


// setTimeout(function(){
//     alert('!!!!')
// }, 2000)


// You can call a javascript function without passing the right number of parameters
// function add(a, b) {
//     console.log(a)
//     console.log(b)
//     return a + b
// }
// console.log(add(5, 2, 3))






let input_text = document.querySelector('#input_text')
let btn_show_text = document.querySelector('#btn_show_text')
let span_output_text = document.querySelector('#span_output_text')

btn_show_text.addEventListener('click', function(event) {
    span_output_text.innerText = input_text.value
})



let input_password = document.querySelector('#input_password')
let btn_show_password = document.querySelector('#btn_show_password')
let span_output_password = document.querySelector('#span_output_password')

btn_show_password.addEventListener('click', function() {
    span_output_password.innerText = input_password.value
})


let input_number = document.querySelector('#input_number')
let btn_show_number = document.querySelector('#btn_show_number')
let span_output_number = document.querySelector('#span_output_number')

btn_show_number.addEventListener('click', function(event) {
    span_output_number.innerText = input_number.value
})

let input_color = document.querySelector('#input_color')
let btn_show_color = document.querySelector('#btn_show_color')
let span_output_color = document.querySelector('#span_output_color')

btn_show_color.addEventListener('click', function(event) {
    span_output_color.innerText = input_color.value
})

let input_checkbox = document.querySelector('#input_checkbox')
let btn_show_checkbox = document.querySelector('#btn_show_checkbox')
let span_output_checkbox = document.querySelector('#span_output_checkbox')

btn_show_checkbox.addEventListener('click', function(event) {
    span_output_checkbox.innerText = input_checkbox.checked
})

let input_range = document.querySelector('#input_range')
let span_output_range = document.querySelector('#span_output_range')

input_range.addEventListener('input', function(event) {
    span_output_range.innerText = parseFloat(input_range.value)/input_range.max
})

let textarea_text = document.querySelector('#textarea_text')
let btn_show_textarea = document.querySelector('#btn_show_textarea')
let span_output_textarea = document.querySelector('#span_output_textarea')

btn_show_textarea.addEventListener('click', function() {
    span_output_textarea.innerText = textarea_text.value
})



let btn_show_radio = document.querySelector('#btn_show_radio')
let span_output_radio = document.querySelector('#span_output_radio')



btn_show_radio.addEventListener('click', function(event) {
    // let checked_radio_button = document.querySelector('input[name="fruits"]:checked')
    // span_output_radio.innerText = checked_radio_button.value


    span_output_radio.innerText = getSelectedRadioButtonValue('fruits')
})


let select_fruits = document.querySelector('#select_fruits')
let btn_show_select = document.querySelector('#btn_show_select')
let span_output_select = document.querySelector('#span_output_select')

btn_show_select.addEventListener('click', function() {
    span_output_select.innerText = select_fruits.value
})










// btn_click.onclick = function(evt) {
//     console.log('A')
// }
// btn_click.onclick = function(evt) {
//     console.log('B')
// }
// btn_click.addEventListener('click', function() {
//     alert('A')
// })
// btn_click.addEventListener('click', function() {
//     alert('B')
// })

// input_text.oninput = function(evt) {}
// input_text.addEventListener('input', function(evt) {
//     span_output_text.innerText = input_text.value
// })

let btn_click = document.querySelector('#btn_click')

btn_click.addEventListener('click', function() {
    alert('A')
})
