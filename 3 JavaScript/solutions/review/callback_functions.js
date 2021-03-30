



// class Vue {
//     constructor(obj) {
//         console.log(obj.el)
//         console.log(obj.data)
//     }
// }

// let app = new Vue({
//     el: '#app',
//     data: {
//         message: 'hello world!'
//     },
//     methods: {
//         sayHello: function() {
//             alert(this.message)
//         }
//     }
// })




// get hoisted, does not preserve 'this'
// function x() {}

// does not get hoisted, does not preserve 'this'
// let x = function() {}

// does not get hoisted, preserves 'this'
// let x = () => {}





// callback functions / 'higher order functions'
// function that's passed as a parameter to another function

// function double(nums) {
//     let output = []
//     for (let i = 0; i < nums.length; ++i) {
//         output.push(nums[i] * 2)
//     }
//     return output
// }
// console.log(double([1, 2, 3, 4]))



// function performOperation(nums, f) {
//     let output = []
//     for (let i = 0; i < nums.length; ++i) {
//         output.push(f(nums[i]))
//     }
//     return output
// }
// let result = performOperation([1, 2, 3, 4], function(x) {
//     return x * 2
// })
// let result = performOperation([1, 2, 3, 4], x => Math.pow(x, 2))
// let result = performOperation([1, 2, 3, 4], x => {
//     return Math.pow(x, 2)
// })
// console.log(result)


// function square(x) {
//     return x*x
// }
// let result = performOperation([1, 2, 3, 4], square)









// function performOperation2(obj) {
//     let output = []
//     for (let i = 0; i < obj.nums.length; ++i) {
//         output.push(obj.f(nums[i]))
//     }
//     return output
// }
// let result = performOperation2({
//     nums: [1, 2, 3, 4],
//     f: x => x*2
// })


// timing functions ==================================

// setTimeout(function() {
//     console.log('hello!')
// }, 3000)

// setInterval(function() {
//     console.log(Math.random())
// }, 1000)


// event listeners =============================

// let mybtn = document.querySelector('#mybtn')
// mybtn.addEventListener('click', function() {
//     console.log('clicked!')
// })



// axios ==================================

// console.log('A')

// axios({
//     method: 'get',
//     url: 'https://favqs.com/api/qotd',
// }).then(response => {
//     console.log(response.data)
//     console.log('B')
// }).catch(error => {
//     console.log(error)
// })

// console.log('C')


// let data = null
// axios({
//     method: 'get',
//     url: 'https://favqs.com/api/qotd',
// }).then(response => {
//     data = response.data
// })
// console.log(data)


