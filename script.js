document.getElementById('natalForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    const day = document.getElementById('day').value;
    const month = document.getElementById('month').value;
    const year = document.getElementById('year').value;
    const hour = document.getElementById('hour').value;
    const minute = document.getElementById('minute').value;
    const city = document.getElementById('city').value;


    fetch('/natal_chart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ day: day, month: month, year: year, hour: hour, minute: minute, city: city })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <h2>Результаты:</h2>
            <p>Знак зодиака: ${data.sun_sign}</p>
            <p>Дата рождения: ${data.birth_date}</p>
            <p>Город рождения: ${data.city}</p>
        `;
    })
    .catch(error => {
        console.error('Ошибка:', error);
        document.getElementById('result').innerHTML = '<p>Ошибка при расчете.</p>';
    });
});
