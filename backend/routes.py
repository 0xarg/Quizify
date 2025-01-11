from flask import current_app as app, jsonify, request
from flask_security import auth_required, verify_password, hash_password, current_user

datastore = app.security.datastore
#---------Testing Point---------
@app.get('/protected')
@auth_required('token')
def proctected():
    return 'Only accessible by auth user'


#---------------------Login------------------
@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    
    email = data.get('email')           # To ignore error --> use get else direct data['email]
    password = data.get('password')
    
    
    if not email or not password:
        return jsonify({"message":"Invalid Inputs"}), 404
    
    user = datastore.find_user(email=email)
    
    if not user:
        return jsonify({"message":"Invalid Email"}),404
    
    if verify_password(password, user.password):
        
        roles = [role.name for role in user.roles]
        return jsonify({'token': user.get_auth_token(), 'email': user.email, 'roles': roles, 'id': user.id})
    return jsonify({"message":"Password Wrong"}), 400

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
