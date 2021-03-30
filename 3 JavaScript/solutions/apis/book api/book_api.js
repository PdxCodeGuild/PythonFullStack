


let app = new Vue({
    el: '#app',
    data: {
        docs: [],
        searchQuery: 'lord of the rings',
        current_page: 1,
        num_pages: 0,
    },
    methods: {
        nextPage: function() {
            if (this.current_page < this.num_pages) {
                this.current_page += 1
                this.getBooks()
            }
        },
        previousPage: function() {
            if (this.current_page > 1) {
                this.current_page -= 1
                this.getBooks()
            }
        },
        setPage: function(page) {
            this.current_page = page
            this.getBooks()
        },
        getBooks: function() {
            axios({
                method: 'get',
                url: 'http://openlibrary.org/search.json',
                params: {
                    q: this.searchQuery,
                    page: this.current_page
                }
            }).then(response => {
                console.log(response.data)
                this.num_pages = Math.ceil(response.data.num_found/100)
                this.docs = []
                let api_data = response.data.docs
                for (let i=0; i<api_data.length; ++i) {
                    
                    let doc = {}
                    
                    if (api_data[i].title) {
                        doc.title = api_data[i].title
                    } else {
                        doc.title = ''
                    }

                    // if the book has author names, join them together
                    // if it doesn't, add the author as a blank string
                    if (api_data[i].author_name) {
                        doc.author = api_data[i].author_name.join(', ')
                    } else {
                        doc.author = ''
                    }

                    if (api_data[i].first_publish_year) {
                        doc.publish_year = api_data[i].first_publish_year
                    } else {
                        doc.publish_year = ''
                    }

                    if (api_data[i].cover_i) {
                        // http://covers.openlibrary.org/b/ID/9255566-L.jpg
                        doc.cover_url = `http://covers.openlibrary.org/b/ID/${api_data[i].cover_i}-L.jpg`
                    } else {
                        doc.cover_url = ''
                    }

                    this.docs.push(doc)
                }
                console.log(this.docs)
            })
        }
    },
    created: function() {
        // alert(app.message)
        // this.getBooks()
    }
})


// let x = 5
// let person = {
//     name: 'bob',
//     age: 44,
//     sayHello: function() {
//         alert('my name is bob')
//     }
// }
// alert(person.name)
// person.sayHello()











document.addEventListener('DOMContentLoaded', function() {
    let elems = document.querySelectorAll('.collapsible')
    let instances = M.Collapsible.init(elems, {})
});
