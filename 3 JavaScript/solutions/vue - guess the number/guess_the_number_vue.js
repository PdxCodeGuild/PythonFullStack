


/*
title
number buttons which are disabled after you press them
text showing warmer / colder
text showing higher / lower
text showing correct / incorrect
when they win
    show how many guesses it took
    show fireworks?
stretch goal: show their score history? with localstorage
*/


// hoisted, does not preserve this
// function add(a, b) {
//     return a + b
// }
// // not hoisted, does not preserve this
// let add = function(a, b) {
//     return a + b
// }
// // not hoisted, preserves this
// let add = (a, b) => {
//     return a + b
// }
// console.log(add(5, 2)) // 7



let app = new Vue({
    el: '#app',
    data: {
        max_guess: 10,
        output: '',
        correct_answer: 0,
        buttons: [],
        modal: null
    },
    methods: {
        initGame: function() {
            // build our array of booleans representing whether a button is disabled
            this.buttons = []
            for (let i=0; i<this.max_guess; i++) {
                this.buttons.push(false)
            }
            // set the correct answer to a random value
            this.correct_answer = Math.floor(Math.random()*this.max_guess+1)
            // reset the output
            this.output = ''
        },
        selectNumber: function(index) {
            this.output = index
            if (index == this.correct_answer) {
                // show a fireworks div?
                this.modal.open()
                // alert('correct!')
                // show 'correct' in the page
                this.output = index + ' is correct!'

                let modal_footer = document.querySelector('#modal_footer_text')
                modal_footer.innerText = index + ' is correct!'

                // disable all the buttons
                for (let i=0; i<this.buttons.length; i++) {
                    this.buttons[i] = true
                }
                // reset the game
                setTimeout(() => {
                    this.modal.close()
                    this.initGame()
                }, 3000)
            } else {
                // disable the button
                this.buttons[index-1] = true
                // set button array index to true
                // alert('incorrect!')
            }
        }
    },
    created: function() {
        this.initGame()
        let elems = document.querySelectorAll('.modal');
        let instances = M.Modal.init(elems, {
            opacity: 0.3,
            inDuration: 500,
            dismissible: false
        })
        this.modal = instances[0]
        // this.modal.open()
        
    }
})






