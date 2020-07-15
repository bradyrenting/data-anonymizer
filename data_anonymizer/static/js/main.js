$(document).ready(function () {
    $('#select_all').on('click', function () {
        if (this.checked) {
            $('.switch').each(function () {
                this.checked = true;
            });
        } else {
            $('.switch').each(function () {
                this.checked = false;
            });
        }
    });

    $('.checkbox').on('click', function () {
        if ($('.switch:checked').length == $('.switch').length) {
            $('#select_all').prop('checked', true);
        } else {
            $('#select_all').prop('checked', false);
        }
    });
});

function checkFormValue(formValue, id) {
    const textInput = document.getElementById(id);
    enableInput = ["bool", "string", "int", "date"];

    textInput.disabled = !enableInput.includes(formValue);
}