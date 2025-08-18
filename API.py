from flask import Flask, jsonify, request

app = Flask(__name__)

# Главная страница API
@app.route("/")
def home():
    return "Привет! Это мой первый API 🚀"

# Простейший GET-запрос (получить данные)
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Привет, мир!"})

# Пример POST-запроса (отправить данные)
@app.route("/echo", methods=["POST"])
def echo():
    data = request.json  # ожидаем JSON
    return jsonify({"Вы отправили": data})

if __name__ == "__main__":
    app.run(debug=True)
