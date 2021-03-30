




let app = new Vue({
    el: '#app',
    data: {
        input_currency: 'USD',
        input_amount: 0,
        output_currency: 'USD',
        output_amount: 0,
        currencies: [
            {
                country: 'Canada',
                code: 'CAD'
            },
            {
                country: 'Hong Kong',
                code: 'HKD'
            },
            {
                country: 'Iceland',
                code: 'ISK'
            },
            {
                country: 'Philippines',
                code: 'PHP'
            },
            {
                country: 'Denmark',
                code: 'DKK'
            },
            {
                country: 'Hungary',
                code: 'HUF'
            },
            {
                country: 'Czech Republic',
                code: 'CZK'
            },
            {
                country: 'Great Britain',
                code: 'GBP'
            },
            {
                country: 'Romania',
                code: 'RON'
            },
            {
                country: 'Sweden',
                code: 'SEK'
            },
            {
                country: 'Indonesia',
                code: 'IDR'
            },
            {
                country: 'Bhutan',
                code: 'INR'
            },
            {
                country: 'Brazil',
                code: 'BRL'
            },
            {
                country: 'Russia',
                code: 'RUB'
            },
            {
                country: 'Croatia',
                code: 'HRK'
            },
            {
                country: 'Japan',
                code: 'JPY'
            },
            {
                country: 'Thailand',
                code: 'THB'
            },
            {
                country: 'Liechtenstein',
                code: 'CHF'
            },
            {
                country: 'Europe',
                code: 'EUR'
            },
            {
                country: 'Malaysia',
                code: 'MYR'
            },
            {
                country: 'Bulgaria',
                code: 'BGN'
            },
            {
                country: 'Turkey',
                code: 'TRY'
            },
            {
                country: 'China',
                code: 'CNY'
            },
            {
                country: 'Bouvet Island',
                code: 'NOK'
            },
            {
                country: 'New Zealand',
                code: 'NZD'
            },
            {
                country: 'Lesotho',
                code: 'ZAR'
            },
            {
                country: 'United States',
                code: 'USD'
            },
            {
                country: 'Mexico',
                code: 'MXN'
            },
            {
                country: 'Singapore',
                code: 'SGD'
            },
            {
                country: 'Australia',
                code: 'AUD'
            },
            {
                country: 'Israel',
                code: 'ILS'
            },
            {
                country: 'Korea (Republic of)',
                code: 'KRW'
            },
            {
                country: 'Poland',
                code: 'PLN'
            }
        ]
    },
    methods: {
        getExchangedValue: function() {

            // https://api.exchangeratesapi.io/latest?base=USD
            axios({
                method: 'get',
                url: 'https://api.exchangeratesapi.io/latest',
                params: {
                    base: this.input_currency
                }
            }).then(response => {
                let rates = response.data.rates
                console.log(rates)
                let exchange_rate = rates[this.output_currency]
                // 5 USD = X EUR
                this.output_amount = exchange_rate*parseFloat(this.input_amount)
                this.output_amount = this.output_amount.toFixed(2)
            })
        }
    },
    created: function() {
        this.currencies.sort((a, b) => {
            if (a.country < b.country) {
                return -1
            } else if (a.country > b.country) {
                return 1
            } else {
                return 0
            }
        })
    }
})



