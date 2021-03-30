


axios({
    method: 'get',
    url: 'https://api.openweathermap.org/data/2.5/onecall',
    params: {
        lat: 45.523064,
        lon: -122.676483,
        exclude: 'minutely,hourly,alerts',
        appid: openweathermap_api_key
    }
}).then(response => {
    console.log(response.data)
})

