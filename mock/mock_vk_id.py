from flask import Flask, jsonify, Response, json

app = Flask(__name__)

USER_LIST = {}
user_id = 100


@app.route('/all_users')
def get_all_users():
    return Response(content_type='application/json', status=200, response=json.dumps({'users': USER_LIST}))


@app.route('/add_user/<username>', methods=['POST'])
def post_create_new_user(username):
    global user_id
    if username in USER_LIST.keys():
        return Response(content_type='application/json', status=403, response=json.dumps({}))
    else:
        user_id += 1
        USER_LIST[username] = user_id
        return Response(
            content_type='application/json',
            status=201,
            response=json.dumps({"vk_id": str(USER_LIST[username])}))


@app.route('/vk_id/<username>')
def get_user_id(username):
    if username in USER_LIST.keys():
        return Response(
            content_type='application/json',
            status=200,
            response=json.dumps({"vk_id": str(USER_LIST[username])}))
    else:
        return Response(content_type='application/json', status=404, response=json.dumps({}))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

