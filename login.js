let loginpage = (e) =>{
    e.preventDefault()
    let span = document.querySelector('span')

    let emailfield = e.target[0]
    let pswdfield = e.target[1]

    let email = 'sameer9292@gmail.com';
    let password = 'Sameer@9292';

    if(emailfield.value===email && pswdfield.value===password){
        alert('welcome')
        window.location.href="./main.html"
    }
    else{
        alert("Invalid Credential")
        emailfield.style.border='solid 2px red'
        pswdfield.style.border='solid 2px red'
        span.innerText='email or password not matching'
        span.style.color='red'
    }

}