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
    if direction == 'stop':
        # Turn all motors off
        GPIO.output(7, 0)
        GPIO.output(8, 0)
        GPIO.output(9, 0)
        GPIO.output(10, 0)
    
    if direction == 'up':
        # Turn the right motor forwards
        GPIO.output(9, 0)
        GPIO.output(10, 1)

        # Turn the left motor forwards
        GPIO.output(7, 0)
        GPIO.output(8, 1)
    
    if direction == 'down':
        # Turn the right motor backwards
        GPIO.output(9, 1)
        GPIO.output(10, 0)

        # Turn the left motor backwards
        GPIO.output(7, 1)
        GPIO.output(8, 0)
    
    if direction == 'left':
        # Turn the right motor forwards
        GPIO.output(9, 0)
        GPIO.output(10, 1)

        # Turn the left motor backwards
        GPIO.output(7, 1)
        GPIO.output(8, 0)
    
    if direction == 'right':
        # Turn the right motor backwards
        GPIO.output(9, 1)
        GPIO.output(10, 0)

        # Turn the left motor forwards
        GPIO.output(7, 0)
        GPIO.output(8, 1)
    
    return direction;

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
