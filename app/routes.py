from flask import (
  redirect,
  url_for,
  jsonify,
  request
)
from app.ext.people import People

import os, json

def init_app(app):
  """Routes of application"""
  
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

  @app.route('/post_person', methods=['POST'])
  def post_person():
      """Receive post method and commit new content in database."""
      validate_data = ["name", "age"]
      content = json.loads(request.data)
      
      if content:
          verify_data = [data for data in validate_data 
                        if data in content.keys()]
          
          if validate_data == verify_data:
              app.Producer.publish_data(request.data)
              message_api = {'success:' 'you send a data with success. Congratulations!'}
              return jsonify(message_api), 200
          else:
              message_api = {'error': 'it was not possible to send the data.'}
              return jsonify(message_api), 500