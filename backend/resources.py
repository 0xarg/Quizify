from flask import jsonify, request, current_app as app
from flask_restful import Api,Resource,fields,marshal_with
from models import *
from flask_security import auth_required, current_user


from datetime import time


class TimeField(fields.Raw):
    def format(self, value):
        if isinstance(value, time):
            return value.strftime('%H:%M:%S')
        else:
            raise Exception('Unsupported TimeField')

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
    "quiz_id": fields.Integer,
    "user_id": fields.Integer,
    "total_score" : fields.String,
    "time" : fields.DateTime,
}
quiz_fields = {
    "id": fields.Integer,
    "date" : fields.DateTime,
    "duration" : TimeField,
    "remarks" : fields.String,
    "questions": fields.List(fields.Nested(question_fields)),
    "scores": fields.List(fields.Nested(score_fields)),
    
    
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
    
    
    @auth_required('token')
    def put(self, subject_id):
        data = request.get_json()    
        name = data.get("name")
        description = data.get("description")
        
        subject = Subject.query.get(subject_id)
        if not subject:
            return jsonify({'message': 'Subject not Found'}), 404
        
        subject.name = name
        subject.description = description   
        try:
            db.session.commit()
            return jsonify({'message':'Succesfully Edited Subject Details'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Error Editing Subject Details'}),500

    
    
    
    @auth_required('token')
    def delete(self, subject_id):
        subject  = Subject.query.get(subject_id)
        
        if not subject:
            return ({'message': 'Subject not Found'}), 404
        try:
            db.session.delete(subject)
            db.session.commit()
            return ({'message':'Subject Deleted'})
        except:
            db.session.rollback()
            return ({'message': 'Error Deleting subject'}), 500

    
    
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
            db.session.rollback()
            return jsonify({'message': 'Error Adding subject'}), 500
           
           
class ChapterAPI(Resource):
    @auth_required('token')
    @marshal_with(chapter_fields)
    def get(self, chapter_id):
        chapter = Chapter.query.get(chapter_id)

        if not chapter:
            print("Chapter not Found")
            return jsonify({'message': 'Chapter not Found'}), 404
        return chapter
    
    @auth_required('token')
    def delete(self, chapter_id):
        chapter = Chapter.query.get(chapter_id)

        if not chapter:
            return jsonify({'message': 'Subject not Found'}), 404
        try:
            db.session.delete(chapter)
            db.session.commit()
            return jsonify({'message': 'Chapter Deleted'})
        except:
            db.session.rollback()
            return jsonify({'message': 'Error Deleting Chapter'}), 500

    @auth_required('token')
    def put(self, chapter_id):
        data = request.get_json()
        name = data.get("name")
        description = data.get("desription")

        chapter = Chapter.query.get(chapter_id)
        if not chapter:
            return jsonify({'message': 'Chapter not Found'}), 404

        chapter.name = name
        chapter.description = description
        try:
            db.session.commit()
            return jsonify({'message': 'Succesfully Edited Chapter Details'})
        except:
            db.session.rollback()
            return jsonify({'message': 'Error Editing Chapter Details'}), 500

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
           db.session.rollback()
           return jsonify({'message': 'Error Adding Chapter'}), 500


class QuizAPI(Resource):
    @auth_required('token')
    @marshal_with(quiz_fields)
    def get(self, quiz_id):
        quiz = Quiz.query.get(quiz_id)

        if not quiz:
            print("Quiz not Found")
            return jsonify({'message': 'Quiz not Found'}), 404
        return quiz

    @auth_required('token')
    def delete(self, quiz_id):
        quiz = Quiz.query.get(quiz_id)

        if not quiz:
            return jsonify({'message': 'quiz not Found'}), 404
        try:
            db.session.delete(quiz)
            db.session.commit()
            return jsonify({'message': 'quiz Deleted'})
        except:
            db.session.rollback()
            return jsonify({'message': 'Error Deleting quiz'}), 500

    @auth_required('token')
    def put(self, quiz_id):
        data = request.get_json()
        name = data.get("name")
        description = data.get("desription")

        chapter = Quiz.query.get(quiz_id)
        if not chapter:
            return jsonify({'message': 'Chapter not Found'}), 404

        chapter.name = name
        chapter.description = description
        try:
            db.session.commit()
            return jsonify({'message': 'Succesfully Edited Chapter Details'})
        except:
            db.session.rollback()
            return jsonify({'message': 'Error Editing Chapter Details'}), 500


class QuizListAPI(Resource):
    @auth_required('token')
    @marshal_with(quiz_fields)
    def get(self, chapter_id):
        quizes = Quiz.query.filter_by(chapter_id=chapter_id).all()
        return quizes


    @auth_required('token')
    def post(self, chapter_id):
        data = request.get_json()
        remarks = data.get("remarks")
        duration = data.get("duration")
        duration = datetime.strptime(duration, '%H:%M:%S').time()

        quiz = Quiz(remarks=remarks, duration=duration,
                       chapter_id=chapter_id)

        try:
            db.session.add(quiz)
            db.session.commit()
            print(duration)
            print(remarks)
            return jsonify({'message': 'Quiz Added'})
        except:
            db.session.rollback()
            return jsonify({'message': 'Error Adding Quiz'}), 500


           
           

    
api.add_resource(SubjectAPI,"/subjects/<int:subject_id>")
api.add_resource(SubjectListAPI,"/subjects")


api.add_resource(ChapterAPI,"/chapter/<int:chapter_id>")
api.add_resource(ChapterListAPI,"/chapters/<int:subject_id>")
    

api.add_resource(QuizAPI,"/quiz/<int:quiz_id>")
api.add_resource(QuizListAPI,"/quizes/<int:chapter_id>")
    