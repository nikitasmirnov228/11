from flask import Flask,request,jsonify

app = Flask(__name__)

db_users = []
db_music = []

class User:
    def __init__(self, name, password, email, group):
        self.name = name
        self.password = password
        self.email = email
        self.group = group

class Music:
    def __init__(self, name, executor, year):
        self.name = name
        self.executor = executor
        self.year = year



@app.route('/user', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        data = request.get_json()
        if (data == False and []):
            return "Данные не заполнены", 403
        if (data['name'] == ''):
            return "Имя не заполнено", 403

    
        
        name = data['name']
        password = data['password']
        email = data['email']
        group = data['group']
        user = User(name, password, email, group)

        db_users.append(user)

        return "Пользователь добавлен", 200
        return jsonify(data)

    if request.method == "GET":
        i = ''
        for u in db_users:
            user = u.name + " " + u.password + " " + u.email + " " + u.group
            i += user

        return i, 200


        

@app.route('/user/<int:id>', methods=['PUT', "DELETE"])

def user_id(id):
    if request.method == 'DELETE':
        db_users.pop(id)
        return "Пользователь удален", 200

    if request.method == "PUT":
        data = request.get_json();
        if data:
            if 'name' in data:
                db_users[id].name = data['name']
            if 'password' in data:
                db_users[id].password = data['password']
            if 'email' in data:
                db_users[id].email = data['email']
            if 'group' in data:
                db_users[id].group = data['group']

        else:
            return "Нет данных", 403

        return "Пользователь изменен", 200


@app.route('/music', methods=['POST', 'GET'])
def music():
    if request.method == 'POST':
        data = request.get_json()
        if (data == False and []):
            return "Данные не заполнены", 403
        if (data['name'] == ''):
            return "Имя не заполнено", 403

    
        
        name = data['name']
        executor = data['executor']
        year = data['year']
        music = Music(name, executor, year)

        db_music.append(music)

        return "Музыка добавлена", 200
        return jsonify(data)

    if request.method == "GET":
        i = ''
        for u in db_music:
            music = u.name + " " + u.executor + " " + u.year
            i += music

        return i, 200


@app.route('/music/<int:id>', methods=['PUT', "DELETE"])

def music_id(id):
    if request.method == 'DELETE':
        db_music.pop(id)
        return "Музыка удалена", 200

    if request.method == "PUT":
        data = request.get_json();
        if data:
            if 'name' in data:
                db_music[id].name = data['name']
            if 'executor' in data:
                db_music[id].password = data['executor']
            if 'year' in data:
                db_music[id].email = data['year']

        else:
            return "Нет данных", 403

        return "Музыка изменена", 200



if __name__ == "__main__":
    data = request.json()
    app.run(port=3005)