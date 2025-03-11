from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def calculate_sun_sign(day, month):
    """
    Упрощенное определение знака зодиака по дате.
    """
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Рыбы"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    return "Неизвестно"

@app.route('/natal_chart', methods=['POST'])
def natal_chart():
    data = request.get_json()
    day = int(data['day'])
    month = int(data['month'])
    year = int(data['year'])
    hour = int(data['hour'])
    minute = int(data['minute'])
    city = data['city']

    # Здесь можно добавить более сложные расчеты, требующие астрологических библиотек.
    sun_sign = calculate_sun_sign(day, month)

    return jsonify({
        'sun_sign': sun_sign,
        'birth_date': f"{day}/{month}/{year} {hour}:{minute}",
        'city': city
        # Добавьте другие параметры натальной карты сюда.
    })

if __name__ == '__main__':
    app.run(debug=True)
