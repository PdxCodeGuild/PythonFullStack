


let input_name = document.querySelector('#input_name')
let input_email = document.querySelector('#input_email')
let input_dob = document.querySelector('#input_dob')
let btn_add = document.querySelector('#btn_add')
let table_contacts = document.querySelector('#table_contacts')
let div_alert = document.querySelector('#div_alert')



btn_add.addEventListener('click', function(event) {
    
    let name = input_name.value
    let email = input_email.value
    let dob = input_dob.value

    if (name === '' || email === '' || dob === '') {
        // alert('Please fill out all fields')
        div_alert.style.display = '' // show the alert
        setTimeout(function() { // wait 3 seconds
            div_alert.style.display = 'none' // hide the alert
        }, 3000)
        return
    }

    input_name.value = ''
    input_email.value = ''
    input_dob.value = ''

    dob = dob.split('-')
    dob = dob[1] + '/' + dob[2] + '/' + dob[0]

    // create tr element
    let tr = document.createElement('tr')

    // create the td for the name
    let td_name = document.createElement('td')
    td_name.innerText = name
    tr.appendChild(td_name)

    let td_email = document.createElement('td')
    td_email.innerText = email
    tr.appendChild(td_email)

    let td_dob = document.createElement('td')
    td_dob.innerText = dob
    tr.appendChild(td_dob)

    let td_btn_remove = document.createElement('td')
    let span_remove = document.createElement('span')
    span_remove.innerText = '✕'
    span_remove.classList.add('btn', 'btn-danger')
    span_remove.addEventListener('click', function(event) {
        table_contacts.removeChild(tr)
    })
    td_btn_remove.appendChild(span_remove)
    tr.appendChild(td_btn_remove)

    table_contacts.appendChild(tr)


})