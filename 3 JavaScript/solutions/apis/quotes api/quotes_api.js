
// function performOperation(arr, f) {
//     let output = []
//     for (let i=0; i<arr.length; ++i) {
//         output.push(f(arr[i]))
//     }
//     return output
// }
// let nums = performOperation([1, 2, 3], function(x) {
//     return Math.pow(x, 2)
// })
// console.log(nums)



// let nums = [1, 2, 102]
// nums.sort(function(a, b) {
//     if (a < b) {
//         return -1
//     } else if (a > b) {
//         return 1
//     } else {
//         return 0
//     }
// })
// nums.sort(function(a, b) {
//     return a - b
// })
// nums.sort((a, b) => a - b)
// console.log(nums)


// function sum(arr) {
//     let total = 0
//     for (let i=0; i<arr.length; ++i) {
//         total += arr[i]
//     }
//     return total
// }
//                    6         5        12      3
// let nums_lists = [[1, 2, 3], [4, 1], [3, 4, 5], [3]]
// nums_lists.sort(function(a, b) {
//     let a_sum = sum(a)
//     let b_sum = sum(b)
//     return a_sum - b_sum
// })
// console.log(nums_lists) // [[3], [4,1], [1,2,3], [3,4,5]]


// shuffle by returning a random number
// nums.sort((a, b) => Math.random() - 0.5)
// nums.sort(function(a, b) {
//     return Math.random() - 0.5
// })





// hoisted
// function x() {}
// not hoisted
// let x = function() {}
// not hoisted, preserves 'this'
// x = () => {}


// Array.prototype.myFunction = function() {
//     alert('hello!')
// }
// let nums = [1, 2, 3]
// nums.myFunction()


// Math.randint = function(a, b) {
//     return Math.floor(Math.random()*(b-a) + a)
// }
// console.log(Math.randint(5, 10))







let app = new Vue({
    el: '#app',
    data: {
        author: '',
        quote: ''
    },
    methods: {
        getQuote: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd'
            }).then(response => {
                // console.log(response)
                // console.log(response.data)
                console.log(this)
                this.author = response.data.quote.author
                this.quote = response.data.quote.body
            })
        }
    },
    created: function() {
        this.getQuote()
    }
})