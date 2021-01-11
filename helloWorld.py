from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if id and request.method == 'GET':
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   elif id and request.method == 'DELETE':
       pass
   return users

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/userJobs')
def get_userJobs():
    search_job = request.args.get('job')
    search_name = request.args.get('name')

    if search_job and search_name:
        subdict = {'users_list': []}
        for user in users['users_list']:
            if user['job'] == search_job and user['name'] == search_name:
                subdict['users_list'].append(user)
        return subdict
    return users

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code.
      # 200 is the default code for a normal response
      return resp

@app.route('/')
def hello_world():
    return 'Hello, World!'
