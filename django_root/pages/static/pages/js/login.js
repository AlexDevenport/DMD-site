document.addEventListener('DOMContentLoaded', function() {
    var loginForm = document.getElementById('loginForm');

    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            var login = document.getElementById('username').value.trim();
            var password = document.getElementById('password').value.trim();

            // Проверяем, что поля не пустые
            if (!login || !password) {
                // Показываем уведомление с кнопкой "ОК"
                alert('Пожалуйста, заполните все поля.');
                event.preventDefault(); // Останавливаем отправку формы
            }
        });
    }

    // Проверяем, есть ли сообщение об ошибке от Django
    var errorMessage = document.querySelector('.alert.alert-danger');
    if (errorMessage) {
        // Показываем уведомление с кнопкой "ОК"
        alert(errorMessage.textContent);
    }
});