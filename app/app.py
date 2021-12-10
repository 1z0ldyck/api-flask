from flask import (
    Flask, 
    jsonify, 
    request, 
    redirect, 
    url_for,
)
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from producer.producer import Producer

import json, os


app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['POSTGRESQL_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
producer = Producer()

class People(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(25), nullable=False) 
   age = db.Column(db.Integer, nullable=False)
   
   def to_json(self):
       return {
           "name": self.name,
           "age": int(self.age)
       }


db.create_all()
    
# views
@app.after_request
def redirect_user(response):
    """Verify if have 404 or 500 in status code of response, if true redirect user to index."""
    error_status_code = (True if response.status_code == 404 
                         or response.status_code == 500 else False)
    if(error_status_code):
        return redirect(url_for('index'))
    return response
        
@app.route('/get_users')
def index():
    """Get all person in database and return json response."""
    people = People.query.all()
    return jsonify({"users": [x.to_json() for x in people] 
                    if len(people) > 0 
                    else 'Nenhum dado encontrado.'})

@app.route('/post_people', methods=['POST'])
def post_people():
    """Receive post method and commit new content in database."""
    validate_data = ["name", "age"]
    content = json.loads(request.data)
    
    if content:
        verify_data = [data for data in validate_data 
                       if data in content.keys()]
        
        if validate_data == verify_data:
            producer.publish_data(request.data)
            data = {'success:' 'you send a data with success. Congratulations!'}
            return ''
        else:
            data = {'error': 'it was not possible to send the data.'}
            return jsonify(data), 500
        
if __name__ == '__main__':
    app.run()