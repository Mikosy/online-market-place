const subItems = document.getElementById('sub-items');
const rotateIcon = document.getElementById('rotate-icon');
const categoriesSection = document.getElementById('categories');


categoriesSection.addEventListener('mouseover', function(){
    console.log('My turn to display');
    subItems.style.transition = "1s";
    subItems.style.display = 'block';

});

categoriesSection.addEventListener('mouseleave', function(){
    subItems.style.transition = '0s';
    setTimeout(function() {
        subItems.style.display = 'none';
    }, 3000);
});


// Carousel

let scrollContainer = document.querySelector(".gallery");
let prevBtn = document.getElementById("prevBtn");
let nextBtn = document.getElementById("nextBtn");

scrollContainer.addEventListener("wheel", (evt) => {
    evt.preventDefault();

    scrollContainer.scrollLeft += evt.deltaY;   
    scrollContainer.style.scrollBehavior = "auto";

});

nextBtn.addEventListener("click", ()=>{
    scrollContainer.style.scrollBehavior = "smooth";
    scrollContainer.style.transition = ".3s"
    scrollContainer.scrollLeft += 1000;
});

prevBtn.addEventListener("click", ()=>{
    scrollContainer.style.scrollBehavior = "smooth";
    scrollContainer.style.scrollBehavior = "smooth";
    scrollContainer.scrollLeft -= 1000;
});