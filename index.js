function sendJSON(){
               
    let result = document.querySelector('.result');
    let nome = document.querySelector('#nome');
    let telefone = document.querySelector('#telefone');
    let cep = document.querySelector('#cep');
    let email = document.querySelector('#email');
    let endereco = document.querySelector('#endereco');
    let cidade = document.querySelector('#cidade');
    let estado = document.querySelector('#estado');
    let conta = document.querySelector('#conta');
    let demo = document.querySelector('#demo');
    let te = document.querySelector('#te');
    let tusd = document.querySelector('#tusd');
    // Creating a XHR object
    let xhr = new XMLHttpRequest();
    let url = "https://univesppi1.herokuapp.com/orcamentos";

    // open a connection
    xhr.open("PUT", url, true);

    // Set the request header i.e. which type of content you are sending
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        const myObj = JSON.parse(this.responseText);
        document.getElementById('texto').innerHTML = myObj[0].Investimento +"<br>"+myObj[0].Carbono +"<br>" +myObj[0].Retorno;
    };
    xhr.onload = function () {

    }
    // Converting JSON data to string
    var data = JSON.stringify(
    [{ 
        "ORC_ID": "",
        "ORC_NOME": nome.value,
        "ORC_CEP": cep.value,
        "ORC_EMAIL": email.value,
        "ORC_TELEFONE": telefone.value,
        "ORC_LAGITUDE": 0.00,
        "ORC_LONGITUDE": 0.00,
        "ORC_LOGRADOURO": endereco.value,
        "ORC_BAIRRO": "X",
        "ORC_NUMERO": "0",
        "ORC_CIDADE": cidade.value,
        "ORC_ESTADO": estado.value,
        "ORC_TE": te.value,
        "ORC_TUSD": tusd.value,
        "ORC_CONSUMO": conta.value 
    }]);
    // Sending data with the request
    console.log(data)
    xhr.send(data);
}