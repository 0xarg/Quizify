from flask import jsonify, request, current_app as app
from flask_restful import Api,Resource,fields,marshal_with
from models import Subject, db
from flask_security import auth_required, current_user

api = Api(prefix="/api")

subject_fields = {
    "id": fields.Integer,
    "name" : fields.String,
    "description" : fields.String,
}
chapter_fields = {
    "id": fields.Integer,
    "name" : fields.String,
    "description" : fields.String,
}
quiz_fields = {
    "id": fields.Integer,
    "date" : fields.DateTime,
    "duration" : fields.DateTime,
    "remarks" : fields.String,
}
question_fields = {
    "id": fields.Integer,
    "statement" : fields.String,
    "option_1" : fields.String,
    "option_2" : fields.String,
    "option_3" : fields.String,
    "option_4" : fields.String,
    "correct_answer" : fields.String,
}
    
score_fields = {
    "id": fields.Integer,
    "total_score" : fields.String,
    "time" : fields.DateTime,
}
    
    
class SubjectAPI(Resource):
    @auth_required('token')
    @marshal_with(subject_fields)
    def get(self,subject_id):
        subject = Subject.query.get(subject_id)
        
        if not subject:
            return {'message':'Subject not Found'},404
        return subject
    
class SubjectListAPI(Resource):
    @auth_required('token')
    @marshal_with(subject_fields)
    def get(self):
        subjects = Subject.query.all()
        return subjects
    
    
    def post(self):
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        subject = Subject(name = name, description = description)
        
        
        try:
            db.session.add(subject)
            db.session.commit()
            print(name)
            print(description)
            return jsonify({'message':'Subject Added'})
        except:
           print('Error')
    
api.add_resource(SubjectAPI,"/subjects/<int:subject_id>")
api.add_resource(SubjectListAPI,"/subjects")
    