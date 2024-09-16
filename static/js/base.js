var windowWidth = window.innerWidth;
console.log(windowWidth);
document.getElementById('width').value = windowWidth;
window.onload = function (){
    document.getElementById('blinker').style.display = 'block';
}