fetch('/data-user')
.then(response => response.json())
.then((data) => {
    console.log(data)
    console.log(data['type_user'])
    if (data['type_user'] === 'user') {
        document.getElementById("banner").style.display = "none";
    }
}
);