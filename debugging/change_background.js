document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("colorButton").addEventListener("click", function() {
        changeBackgroundColor();
    });

    function changeBackgroundColor() {
        var randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
        document.body.style.backgroundColor = randomColor;
    }
});
