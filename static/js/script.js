// const backgroundChangeOne = document.querySelector('.backgroundChange-one')
// var currentTime = new Date().getHours();


// function functionOverFunction() {

//     if (currentTime < 12 ) {
//         // Changing the color
//         backgroundChangeOne.style.backgroundColor = '#fff';
//         backgroundChangeOne.style.transition = '.5s';
//         backgroundChangeOne.style.color = '#222';


//     } else if (currentTime >= 12 && currentTime <= 18){
//         console.log('welcome');
//         backgroundChangeOne.style.backgroundColor = '#222';
//         backgroundChangeOne.style.color = '#fff';
//         backgroundChangeOne.style.transition = '.5s';
        

//     };
    
// }

// functionOverFunction();
  




var increaseCart = document.querySelector('#increase');
var i = 0;

function increaseBtn(){
    i++;
    increaseCart.innerHTML = i;
}

var i = 0;

function reduceBtn(){
    if(i > 0){
        i--;
        document.querySelector('#increase').innerHTML = i;

    }

};



// Returning customer

document.getElementById('returning-customer').addEventListener('click', function(){
    var firstDiv = document.getElementById('first-one');
    var secondDiv = document.getElementById('second-one');

    if(firstDiv.style.display !== 'none'){
        firstDiv.style.display = 'none';
        secondDiv.style.display = 'block';


    } else {
        firstDiv.style.display = 'block';
        secondDiv.style.display = 'none';
    }
});


// Dropdown
var subMenu = document.getElementById('subMenu');

function toggleMenu(){
    subMenu.classList.toggle("open");
}


