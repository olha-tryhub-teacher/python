<!DOCTYPE html>
<html>
<head>
    <title>Логін</title>
</head>
<body>
    <h2>Авторизація</h2>

    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Увійти</button>
    </form>
</body>
</html>
