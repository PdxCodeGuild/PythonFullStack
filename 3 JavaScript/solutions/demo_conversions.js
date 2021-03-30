



let num = '5.1'
num = parseInt(num)
console.log(num)
console.log(typeof num)

num = '5.1'
num = parseFloat(num)
console.log(num)
console.log(typeof num)



function stringToArray(text) {
    let output = []
    for (let i=0; i<text.length; ++i) {
        output.push(text[i])
    }
    return output
}



text = 'hello world!'
console.log(stringToArray(text))
// list(text) -> ['h', 'e', 'l', 'l', ...]
// text = [...text]
// console.log(text)



