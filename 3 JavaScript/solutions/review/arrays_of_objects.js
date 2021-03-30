



// app data
let contacts = []

// incoming api data
let api_data = {
    contacts: [{
        name: 'Bob',
        email: 'bob@gmail.com',
        age: 55
    },{
        name: 'Jane',
        email: 'jane@gmail.com',
        age: 56
    },{
        name: 'Andrew',
        email: 'andrew@gmail.com',
        age: 78
    }]
}

// contacts.name = api_data.contacts.name
// console.log(api_data.contacts.name)
console.log(api_data.contacts[0].name)
for (let i=0; i<api_data.contacts.length; ++i) {
    console.log(api_data.contacts[i].name)
}

for (let i=0; i<api_data.contacts.length; ++i) {
    contacts.push({
        name: api_data.contacts[i].name.toLowerCase(),
        age: api_data.contacts[i].age
    })
}
console.log(contacts)




