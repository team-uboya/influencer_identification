#created by Steffen Schmidt on 5/24/2020
import SMS_Twilio_backend
import system_constants
from flask import Flask, request, redirect, render_template
import os

import werkzeug.utils as utils


#TODO: Fix to relative folder
UPLOAD_FOLDER = '/home/ubuntu/influencer_identification/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'rtf'}


app = Flask(__name__, static_folder= '/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def show_main():
    print('Website visited')
    return render_template('index_new.html')

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    backend=SMS_Twilio_backend.SMS_Twilio_backend()
    backend.receiveMessage(request)

@app.route("/demo", methods=['GET','POST'])
def show_demo():
    if request.method=='POST':
        if 'file' in request.files:

            file = request.files['file']
            file_name = utils.secure_filename(file.filename)
            #TODO: abfangen falls files mit gleichem Namen schon existieren
            #f = open(os.path.join(app.config['UPLOAD_FOLDER'], file_name),"w")
            #f.close()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        return return redirect(url_for('results'))


    return render_template('demo.html')



if __name__ == "__main__":
    app.run(debug=True)