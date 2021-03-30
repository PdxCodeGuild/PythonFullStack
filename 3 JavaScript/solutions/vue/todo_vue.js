


/*
TODO

title
input a new task
    text input
    button to add it
incomplete tasks
    text, italic?
    created date
    complete button
completed tasks
    greyed-out with a line through
    created date
    completed date
    delete button

stretch goals
    make sure it looks good on mobile
    fancy bootstrap datepicker
        https://bootstrap-datepicker.readthedocs.io/en/latest/
    accordian with editable notes
    priority? (high, medium, low)
    due date?
    save/load tasks from local storage
    move up + move down buttons / drag & drop
        https://github.com/SortableJS/Vue.Draggable
    progress bar showing the number of tasks completed / total tasks
*/


let app = new Vue({
    el: '#app',
    data: {
        todo_item_text: '',
        todo_items: [{
            text: 'Walk the dog',
            created_date: '1/20/2021'
        },{
            text: 'Wash the car',
            created_date: '1/20/2021'
        },{
            text: 'Drink water',
            created_date: '1/20/2021'
        }],
        completed_items: [{
            text: 'Water the plants',
            created_date: '1/19/2021',
            completion_date: '1/20/2021'
        },{
            text: 'Eat lunch',
            created_date: '1/18/2021',
            completion_date: '1/20/2021'
        }]
    },
    methods: {
        getCurrentDate: function() {
            let date = new Date()
            return (date.getMonth()+1) + '/' + date.getDate() + '/' + date.getFullYear()
        },
        addVuedo: function() {
            let todo = {
                text: this.todo_item_text,
                created_date: this.getCurrentDate()
            }
            this.todo_items.push(todo)
            this.todo_item_text = ''
            this.saveTodos()
        },
        completeVuedo: function(index) {
            // alert(index)
            // alert(JSON.stringify(this.todo_items[index], null, 2))
            // let complete = {
            //     text: item.text
            // }
            let todo_item = this.todo_items[index]
            todo_item.completion_date = this.getCurrentDate()
            // console.log(todo_item)
            // remove the element from the todo_items
            this.todo_items.splice(index, 1)
            // add the element to the completed_items
            this.completed_items.push(todo_item)
            this.saveTodos()
        },
        deleteVuedo: function(index) {
            this.completed_items.splice(index, 1)
            this.saveTodos()
        },
        saveTodos: function() {
            this.saveData('todo_items', this.todo_items)
            this.saveData('completed_items', this.completed_items)
        },
        loadData: function(name, default_value) {
            let data = localStorage.getItem(name)
            if (data == null) {
                return default_value
            } else {
                return JSON.parse(data)
            }
        },
        saveData: function(name, data) {
            localStorage.setItem(name, JSON.stringify(data))
        }
    },
    created: function() {
        this.todo_items = this.loadData('todo_items', [])
        this.completed_items = this.loadData('completed_items', [])
    }
})