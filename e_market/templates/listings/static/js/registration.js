const form = document.getElementById('form');
const username = document.getElementById('first_name');
const middle_name = document.getElementById('middle_name');
const last_name = document.getElementById('last_name');
const username = document.getElementById('username');
const email = document.getElementById('email');
const pwd = document.getElementById('pwd');
const pwd2 = document.getElementById('pwd2');

form.addEventListener('submit',(e)=>{
e.preventDefault();

checkInputs();

});


function checkInputs(){

const userNameValue = username.value.trim();
const middleNameValue = middle_name.value.trim();
const lastNameValue = last_name.value.trim();
const userNameValue = username.value.trim();
const emailValue = email.value.trim();
const pwdValue = pwd.value.trim();
const pwd2Value = pwd2.value.trim();

if(userNameValue===''){
document.write("Empty username");
} else {
document.write("")
}

}