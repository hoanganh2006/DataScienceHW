from flask import Flask, render_template, url_for, flash, redirect, session, request,logging, Response
from lessons import Lessons
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from keras.models import load_model
import numpy as np 
import os
from importlib import import_module
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
from keras.backend import tf
# from base_camera import VideoCamera

app = Flask(__name__)

#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mingo2006'
app.config['MYSQL_DB'] = 'project3'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init MySQL
mysql = MySQL(app)

Lessons = Lessons()
'''
'''
graph = tf.get_default_graph()
model = load_model('emojinator.h5')
cap = cv2.VideoCapture(0)


def gen():
    keras_predict(model, np.zeros((50, 50, 1), dtype=np.uint8))
    emojis = get_emojis()
    x, y, w, h = 300, 50, 350, 350
    """Video streaming generator function."""
    while (cap.isOpened()):
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask2 = cv2.inRange(hsv, np.array([2, 50, 60]), np.array([25, 150, 255]))
        res = cv2.bitwise_and(img, img, mask=mask2)
        gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        median = cv2.GaussianBlur(gray, (5, 5), 0)

        kernel_square = np.ones((5, 5), np.uint8)
        dilation = cv2.dilate(median, kernel_square, iterations=2)
        opening = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel_square)
        ret, thresh = cv2.threshold(opening, 30, 255, cv2.THRESH_BINARY)

        thresh = thresh[y:y + h, x:x + w]
        contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]
        if len(contours) > 0:
            contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(contour) > 2500:
                x, y, w1, h1 = cv2.boundingRect(contour)
                newImage = thresh[y:y + h1, x:x + w1]
                newImage = cv2.resize(newImage, (50, 50))
                pred_probab, pred_class = keras_predict(model, newImage)
                print(pred_class, pred_probab)
                img = overlay(img, emojis[pred_class], 400, 250, 90, 90)
        
        x, y, w, h = 300, 50, 350, 350
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite('t.jpg', img)
        # cv2.imwrite("Contours", thresh)
        yield (b'--img\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')
        k = cv2.waitKey(10)
        if k == 27:
            break

def get_emojis():
    emojis_folder = 'hand_emo/'
    emojis = []
    for emoji in range(len(os.listdir(emojis_folder))):
        print(emoji)
        emojis.append(cv2.imread(emojis_folder+str(emoji)+'.png', -1))
    return emojis

def keras_predict(model, image):
    processed = keras_process_image(image)
    global graph
    with graph.as_default():
        pred_probab = model.predict(processed)[0]
        pred_class = list(pred_probab).index(max(pred_probab))
        return max(pred_probab), pred_class

def keras_process_image(img):
    image_x = 50
    image_y = 50
    img = cv2.resize(img, (image_x, image_y))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img, (-1, image_x, image_y, 1))
    return img

def overlay(image, emoji, x,y,w,h):
    emoji = cv2.resize(emoji, (w, h))
    try:
        image[y:y+h, x:x+w] = blend_transparent(image[y:y+h, x:x+w], emoji)
    except:
        pass
    return image

def blend_transparent(face_img, overlay_t_img):
    # Split out the transparency mask from the colour info
    overlay_img = overlay_t_img[:,:,:3] # Grab the BRG planes
    overlay_mask = overlay_t_img[:,:,3:]  # And the alpha plane

    # Again calculate the inverse mask
    background_mask = 255 - overlay_mask

    # Turn the masks into three channel, so we can use them as weights
    overlay_mask = cv2.cvtColor(overlay_mask, cv2.COLOR_GRAY2BGR)
    background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)

    # Create a masked out face image, and masked out overlay
    # We convert the images to floating point in range 0.0 - 1.0
    face_part = (face_img * (1 / 255.0)) * (background_mask * (1 / 255.0))
    overlay_part = (overlay_img * (1 / 255.0)) * (overlay_mask * (1 / 255.0))

    # And finally just add them together, and rescale it back to an 8bit integer image
    return np.uint8(cv2.addWeighted(face_part, 255.0, overlay_part, 255.0, 0.0))
@app.route('/video_feed')
def video():
    return render_template('video_feed.html')

@app.route('/video_feed/on')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=img')
    # return render_template('video_feed.html')

'''
'''


@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html')

class MessageForm(Form):
    guest_name = StringField('Name', [validators.Length(min = 1, max = 50)])
    guest_email = StringField('Email', [validators.Length(min = 6, max = 50)])
    guest_message = TextAreaField('Message', [validators.Length(min=30)])

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = MessageForm(request.form)
    if request.method == 'POST' and form.validate():
        guest_name = form.guest_name.data
        guest_email = form.guest_email.data
        guest_message = form.guest_message.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO messages (name, email, messsage) VALUES(%s, %s, %s)", (guest_name, guest_email, guest_message))

        #Commit to DB
        mysql.connection.commit()

        #Close connection 
        cur.close()
        flash('Your message has been sent successful', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form = form)

@app.route('/lessons')
def lessons():
	return render_template('lessons.html', lessons = Lessons)
'''
'''

@app.route('/lesson/<string:id>/')
def lesson(id):
	return render_template('lesson.html', id = id)

@app.route('/studies', methods = ['GET', 'POST'])
def studies():
	return render_template('studies.html')

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min = 1, max = 50)])
    username = StringField('Username', [validators.Length(min = 5, max = 25)])
    email = StringField('Email', [validators.Length(min = 6, max = 50)])
    password = PasswordField('Password', [
    	validators.DataRequired(), 
    	validators.EqualTo('confirm', message = 'Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')
# Check if user login 
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
	app.secret_key = 'secretkey123'
	app.run(debug = True)

