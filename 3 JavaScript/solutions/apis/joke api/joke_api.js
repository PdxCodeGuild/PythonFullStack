
let app = new Vue({
    el: '#app',
    data: {
        joke: {
            setup: '',
            delivery: '',
        },
        selected_category: 'Any',
        categories: ['Any', 'Programming', 'Misc', 'Dark', 'Pun', 'Spooky', 'Christmas'],
        search_text: '',
        selected_language: 'en',
        languages: [{
            name: 'Czech',
            value: 'cs'
        }, {
            name: 'German',
            value: 'de'
        }, {
            name: 'English',
            value: 'en'
        }, {
            name: 'Spanish',
            value: 'es'
        }, {
            name: 'French',
            value: 'fr'
        }, {
            name: 'Portuguese',
            value: 'pt'
        }]
    },
    methods: {
        getJoke: function () {
            axios({
                method: 'get',
                url: 'https://v2.jokeapi.dev/joke/' + this.selected_category,
                params: {
                    blacklistFlags: 'nsfw,religious,political,racist,sexist,explicit',
                    lang: this.selected_language,
                    contains: this.search_text
                }
            }).then((response) => {
                console.log(response.data)
                if (response.data.type === 'single') {
                    this.joke.setup = response.data.joke
                    this.joke.delivery = 'Hahahaha'
                } else {
                    this.joke.setup = response.data.setup
                    this.joke.delivery = response.data.delivery
                }
            })
        }
    },
    created: function () {
        this.getJoke()
        // this.selected_category = this.categories[0]
    }
})





