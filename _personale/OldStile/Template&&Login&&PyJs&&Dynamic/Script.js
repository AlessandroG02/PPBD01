const myButton = document.getElementById('myButton');

myButton.addEventListener('mouseover', function() {
    myButton.style.backgroundColor = '#000';
    myButton.style.color = '#fff';
});

myButton.addEventListener('mouseout', function() {
    myButton.style.backgroundColor = '#fff';
    myButton.style.color = '#000';
});
