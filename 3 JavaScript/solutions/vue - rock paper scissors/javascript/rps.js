

var app = new Vue({
    el: '#app',
    data: {
        user_score: 0,
        computer_score: 0,
        match_results: '',
        user_details: '',
        computer_details: ''
    },
    methods: {
        clickedButton: function(user_weapon) {
            let choices = ['rock', 'paper', 'scissors']
            // need a random selection for the computer to play against the user selection
            let computer_choice = Math.floor(Math.random() * choices.length)
            let computer_weapon = choices[computer_choice]
            //alert("Randomly selected: " + choices[computer_choice])
            // Then compare the 2 choices and determine a winner/loser
                
            if (user_weapon === 'rock' && computer_weapon === 'scissors') {  // user win
                this.match_results = "You win!"
                this.user_score += 1
            } else if (user_weapon === 'rock' && computer_weapon === 'paper') {
                this.match_results = "You lose!"
                this.computer_score += 1
            } else if (user_weapon === 'paper' && computer_weapon === 'rock') {
                this.match_results = "You win!"
                this.user_score += 1
            } else if (user_weapon === 'paper' && computer_weapon === 'scissors') {
                this.match_results = "You lose!"
                this.computer_score += 1
            } else if (user_weapon === 'scissors' && computer_weapon === 'paper') {
                this.match_results = "You win!"
                this.user_score += 1
            } else if (user_weapon === 'scissors' && computer_weapon === 'rock') {
                this.match_results = "You lose!"
                this.computer_score += 1
            } else {
                this.match_results = "Match was a tie!"
            }
            this.user_details = "You Selected: " + user_weapon
            this.computer_details = "Computer Selected: " + computer_weapon

            // update the results and overall score
            
        }
    }
})

