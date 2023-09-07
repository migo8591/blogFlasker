var enzo = document.getElementById('demo')
enzo.style.color ="brown"

var titulo = document.querySelector('.title')
titulo.style.color="red"

setInterval(()=>{
    var change = titulo.style.color
    if(change=="red"){
        titulo.style.color="green"
    }else if(change=="green"){
        titulo.style.color="blue"
    }else if(change=="blue"){
        titulo.style.color="red"
    }
},2500)

setTimeout(function(){
    document.getElementById('flash-message').classList.remove('show');
    document.getElementById('flash-message').classList.add('hidden');
}, 3000); // Cambia 3000 a la cantidad de milisegundos que desees