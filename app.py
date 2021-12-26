from flask import Flask, render_template
import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the GPIO Pin mode
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move/<direction>')
def move(direction):    
    # Turn the right motor forwards
    GPIO.output(9, 0)
    GPIO.output(10, 1)

    # Turn the left motor forwards
    GPIO.output(7, 0)
    GPIO.output(8, 1)
    
    time.sleep(1)
    
    # Turn all motors off
    GPIO.output(7, 0)
    GPIO.output(8, 0)
    GPIO.output(9, 0)
    GPIO.output(10, 0)
    # GPIO.cleanup()
    
    return direction;

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
