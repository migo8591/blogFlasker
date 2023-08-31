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