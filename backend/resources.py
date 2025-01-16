from flask import jsonify, request, current_app as app
from flask_restful import Api,Resource,fields,marshal_with
from models import *
from flask_security import auth_required, current_user

api = Api(prefix="/api")

chapter_fields = {
    "id": fields.Integer,
    "name" : fields.String,
    "description" : fields.String,
    "subject_id": fields.Integer,
    "subject.name": fields.String,
}
subject_fields = {
    "id": fields.Integer,
    "name" : fields.String,
    "description" : fields.String,
    "chapters": fields.List(fields.Nested(chapter_fields))
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
            print("Subject not Found")
            return jsonify({'message':'Subject not Found'}),404
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
           
           
class ChapterAPI(Resource):
    @auth_required('token')
    @marshal_with(chapter_fields)
    def get(self, chapter_id):
        chapter = Chapter.query.get(chapter_id)

        if not chapter:
            print("Chapter not Found")
            return jsonify({'message': 'Chapter not Found'}), 404
        return chapter
    
class ChapterListAPI(Resource):
    @auth_required('token')
    @marshal_with(chapter_fields)
    def get(self, subject_id):
        chapters = Chapter.query.filter_by(subject_id = subject_id).all()
        return chapters
    
    
    def post(self, subject_id):
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        chapter = Chapter(name = name, description = description, subject_id = subject_id)
        
        
        try:
            db.session.add(chapter)
            db.session.commit()
            print(name)
            print(description)
            return jsonify({'message':'Chapter Added'})
        except:
           print('Error')
           
           
           

    
api.add_resource(SubjectAPI,"/subjects/<int:subject_id>")
api.add_resource(SubjectListAPI,"/subjects")


api.add_resource(ChapterAPI,"/chapter/<int:chapter_id>")
api.add_resource(ChapterListAPI,"/chapters/<int:subject_id>")
    