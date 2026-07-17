const micButton = document.getElementById("micbutton");

const popup = document.getElementById("popup");

const responseText = document.getElementById("responsetext");

const recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.lang = "en-US";

recognition.interimResults = false;

recognition.maxAlternatives = 1;

micButton.onclick = function(){

    recognition.start();

}

recognition.onresult = async function(event){

    const spokenText = event.results[0][0].transcript;

    try{

        const response = await fetch("/process",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                text:spokenText
            })

        });

        const data = await response.json();

        responseText.innerHTML = data.result;

        popup.style.display = "block";
        audio.style.display = "none";

    }

    catch(error){

        responseText.innerHTML = "Server Error";

        popup.style.display = "block";
        audio.style.display = "none";

    }

}

function closePopup(){

    popup.style.display = "none";
    audio.style.display = "block";

}

const navbarToggle = document.querySelector('.navbar-toggle');
const navbarMenu = document.querySelector('.navbar-menu');

navbarToggle.addEventListener('click', () => {
    navbarToggle.classList.toggle('active');
    navbarMenu.classList.toggle('active');

});


function closePopup(){
    document.getElementById("popup").style.display = "none";
    document.getElementById("audio").style.display = "block";
}