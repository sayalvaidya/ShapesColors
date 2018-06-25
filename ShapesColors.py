import os

from os.path import realpath, dirname, join
from flask import Flask, render_template, app
from flask import request
from werkzeug.utils import secure_filename

from color_live import live_Color
from detect_color import color_det
from detect_shape import input_image
from shape_sound import sound

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/images')
SHAPE_OUTPUT = join(dirname(realpath(__file__)), 'static/shape_output')
COLOR_OUTPUT = join(dirname(realpath(__file__)), 'static/color_output')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

@app.route('/')
def project():
    return render_template('project.html')
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: img/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/quiz')
def learn():
    return render_template('quiz.html')


@app.route('/learnShape')
def learnShape():
    return render_template('learnShape.html')

@app.route('/learnColor')

def learnColor():
    return render_template('learnColor.html')

@app.route('/study')

def study():
    return render_template('quiz.html')


@app.route('/upload', methods=['POST'])
def upload_shape():
    file = request.files['inputImage']
    # print(file)
    # print(file.filename)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    input_image(file.filename)
    sd=sound(file.filename)

    return render_template('shapeResult.html', img=file.filename,out=filename,sound=sd)

@app.route('/uploada', methods=['POST'])
def upload_color():
    file = request.files['inputImage']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    color_det(file.filename)
    return render_template('colorResult.html', img=file.filename,output=filename)
@app.route('/liveColor/')

def liveColor():
    # return Response(gen(colorLive()),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')
    live_Color()
    return render_template('learnColor.html')




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




if __name__ == '__main__':

    app.secret_key = 'super secret key'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SHAPE_OUTPUT']= SHAPE_OUTPUT
    app.config['COLOR_OUTPUT']= COLOR_OUTPUT

    app.run()