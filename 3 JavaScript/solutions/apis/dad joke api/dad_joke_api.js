


let app = new Vue({
    el: '#app',
    data: {
        output: '',
    },
    methods: {
        loadJoke: function() {
            axios({
                method: 'get',
                url: 'https://icanhazdadjoke.com/',
                headers: {
                    'Accept': 'application/json'
                }
            }).then(response => {
                let joke = response.data.joke
                this.output = joke
            })
        }
    },
    created: function() {
        this.loadJoke()
    }
})




