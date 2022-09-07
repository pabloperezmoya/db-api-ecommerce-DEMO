from flask import Flask, request, jsonify, session
from flask_restful import Resource, Api
from flask_cors import CORS

from _db_interface import Users, Passwords, Purchases, Carts, Invoices, Products

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)
app.secret_key = 'iXiTTxa4xv4bJKgNv5wXP1o8-BhSvJZPNNKbU-Igyss'
active_tokens = ["w0Ls2oYM468", "4GcfK3ENems"]


def choose_class(table):
    """Choose a class based on a string"""
    if table == 'users':
        return True, Users()
    elif table == 'passwords':
        return True, Passwords()
    elif table == 'purchases':
        return True, Purchases()
    elif table == 'carts':
        return True, Carts()
    elif table == 'invoices':
        return True, Invoices()
    elif table == 'products':
        return True, Products()
    else:
        return False, "Invalid table name"


class API(Resource):
    def __init__(self):
        self.json_data = request.get_json(force=True)
        self.data = self.json_data['data']
        self.table = self.json_data['table']
        self.class_ = choose_class(self.table)
        
    def post(self):
        try:
            if self.class_[0]:
                returned = self.class_[1].get_item(self.data)
                if returned[0]:
                    return jsonify({'status': 'success', 'data': returned[1]})
                else:
                    return jsonify({'status': 'failure', 'error': returned[1]})

            else:
                return jsonify({'status': 'failure', 'error': self.class_[1]})
        except Exception as e:
            return jsonify({'status': 'failure', 'error': str(e)})

    def put(self):
        if self.class_[0]:
            returned = self.class_[1].put_item(self.data)
            if returned[0]:
                return jsonify({'status': 'success', 'data': returned[1]})
            else:
                return jsonify({'status': 'failure', 'error': returned[1]})

        else:
            return jsonify({'status': 'failure', 'error': self.class_[1]})

    def patch(self):
        if self.class_[0]:
            returned = self.class_[1].update_item(self.data, self.data.pop("update_expression"), self.data.pop("expression_attribute_values"))
            if returned[0]:
                return jsonify({'status': 'success', 'data': returned[1]})
            else:
                return jsonify({'status': 'failure', 'error': returned[1]})

        else:
            return jsonify({'status': 'failure', 'error': self.class_[1]})

    def delete(self):
        if self.class_[0]:
            returned = self.class_[1].delete_item(self.data)
            if returned[0]:
                return jsonify({'status': 'success', 'data': returned[1]})
            else:
                return jsonify({'status': 'failure', 'error': returned[1]})
        else:
            return jsonify({'status': 'failure', 'error': self.class_[1]})


api.add_resource(API, '/api/v1/')

@app.route('/<token>')
def verify_status(token):
    if token == 'test-token':
        return jsonify({'status': 'All online'})
    else:
        return jsonify({'status': 'Token needed'})


if __name__ == '__main__':
    app.run(debug=True)