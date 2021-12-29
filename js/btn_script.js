function buttonClick() {
    $.ajax({
        url: '../controller.php',
        type: 'post',
        dataType: 'json',
        data: {},
        success: function (result) {
            document.getElementById('citation').innerText = result;
        }
    })

}