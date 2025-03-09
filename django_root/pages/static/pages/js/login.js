// static/pages/js/login.js

document.addEventListener('DOMContentLoaded', function() {
    // Находим форму по её ID
    var loginForm = document.getElementById('loginForm');

    // Добавляем обработчик события отправки формы
    loginForm.addEventListener('submit', function(event) {
        // Получаем значения полей логина и пароля
        var login = document.getElementById('first').value.trim();
        var password = document.getElementById('password').value.trim();

        // Проверяем, что поля не пустые
        if (!login || !password) {
            alert('Пожалуйста, заполните все поля.'); // Показываем сообщение об ошибке
            event.preventDefault(); // Останавливаем отправку формы
        }
    });
});