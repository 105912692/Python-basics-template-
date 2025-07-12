# PYTHON CODE TEMPLATES AND BASICS

# -----------------------------
# Commonly Used Libraries
# -----------------------------
import math  # Math functions and constants
import random  # Random number generation
import sys  # System-specific parameters and functions
import time  # Time access and conversions
import tkinter as tk # GUI toolkit for Python

#-- -----------------------------
#Import from other files
# -----------------------------
import input_functions #import file 'input_functions.py' for user input functions
result = input_functions.addition(5, 10)  # Example usage of a function from input_functions.py

#-------------------------------
#Import from other files from specific directory
# -----------------------------
from input_functions import addition, subtraction  # Import specific functions from input_functions.py
print(addition(5, 10))  # Call the addition function

#-- -----------------------------
#Basic Data Types
# -----------------------------
# Integer
a = 10  # Integer type
# Float
b = 3.14  # Float type
# String
c = "Hello, World!"  # String type
# Boolean
d = True  # Boolean type

# -----------------------------
# Basic Arithmetic Operations
# -----------------------------
print("Addition:", 1 + 2)  # Adds two numbers
print("Subtraction:", 3 - 1)  # Subtracts second number from first
print("Multiplication:", 2 * 4)  # Multiplies two numbers
print("Division:", 5 / 2)  # Divides first number by second (float result)
print("Floor Division:", 5 // 2)  # Divides and rounds down to nearest integer
print("Modulus:", 5 % 2)  # Remainder of division
print("Exponentiation:", 5 ** 2)  # Raises first number to the power of second

# -----------------------------
# Text User Input
# -----------------------------
# name = input("Enter your name: ")  # Get user input as a string
# print("Hello,", name)  # Print a greeting with the user's name

# -----------------------------
# Array Operations (using lists)
# -----------------------------
numbers = [1, 2, 3, 4, 5]  # Create a list of numbers
print("Original list:", numbers)  # Print the list
print("First element:", numbers[0])  # Access first element (index 0)
print("Slice [1:4]:", numbers[1:4])  # Get a sublist from index 1 to 3
print("Reversed list:", numbers[::-1])  # Reverse the list
print("Length:", len(numbers))  # Get the number of elements in the list

# -----------------------------
# List Operations
# -----------------------------
numbers.append(6)  # Add 6 to the end of the list
print("After append:", numbers)
numbers.insert(2, 99)  # Insert 99 at index 2
print("After insert at index 2:", numbers)
numbers.remove(3)  # Remove the first occurrence of 3
print("After removing 3:", numbers)
print("Pop last element:", numbers.pop())  # Remove and return the last element
numbers.sort()  # Sort the list in ascending order
print("Sorted list:", numbers)
numbers.reverse()  # Reverse the list in place
print("Reversed again:", numbers)

# -----------------------------
# String Operations
# -----------------------------
text = "  Hello, Python!  "  # Create a string with extra spaces
print("Original text:", text)  # Print the original string
print("Lowercase:", text.lower())  # Convert to lowercase
print("Uppercase:", text.upper())  # Convert to uppercase
print("Stripped:", text.strip())  # Remove leading/trailing whitespace
print("Replaced:", text.replace("Python", "World"))  # Replace substring
print("Split by comma:", text.split(","))  # Split string into list by comma

# -----------------------------
# Conditional Statements
# -----------------------------
x = 10  # Example variable
if x > 5:
    print("x is greater than 5")  # Executes if x > 5
elif x == 5:
    print("x is 5")  # Executes if x == 5
else:
    print("x is less than 5")  # Executes if x < 5

# -----------------------------
# Loops
# -----------------------------
print("For loop:")
for i in range(5):  # Loop from 0 to 4
    print(i)

print("While loop:")
count = 0
while count < 3:  # Loop while count is less than 3
    print("Count:", count)
    count += 1

# -----------------------------
# Functions
# -----------------------------
def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Call the function with argument

# -----------------------------
# Random Numbers
# -----------------------------
print("Random number 1-10:", random.randint(1, 10))  # Random integer between 1 and 10
print("Random float 0-1:", random.random())  # Random float between 0 and 1
print("Random choice:", random.choice(["apple", "banana", "cherry"]))  # Random element from list

# -----------------------------
# Math Functions
# -----------------------------
print("Square root of 16:", math.sqrt(16))  # Square root
print("Cosine of 0:", math.cos(0))  # Cosine of 0 radians
print("Pi value:", math.pi)  # Value of pi
print("Factorial of 5:", math.factorial(5))  # Factorial

# -----------------------------
# Try-Except (Error Handling)
# -----------------------------
try:
    result = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")  # Handle the error

# -----------------------------
# File Operations (Basic)
# -----------------------------
# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello File!\n")  # Write text to file

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()  # Read file content
    print("File content:", content)

# -----------------------------
# Classes and Objects
# -----------------------------
class Person:
    def __init__(self, name, age):
        self.name = name  # Set name attribute
        self.age = age    # Set age attribute

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old.")  # Print info

p1 = Person("Bob", 25)  # Create a Person object
p1.speak()  # Call the speak method
p2 = Person("Alice", 30)  # Create another Person object
p2.speak()  # Call the speak method for the second object

# -----------------------------
# Audio Playback Examples
# -----------------------------

# Option 1: Simple Playback using playsound
# pip install playsound
# This method is very simple and works for basic playback of mp3/wav files.
try:
    from playsound import playsound
    print("Playing audio using playsound...")
    # Replace with a valid file path like 'sound.mp3' or 'sound.wav'
    # playsound('example.mp3')  # Uncomment and provide a valid file to play
except ImportError:
    print("playsound module not installed.")

# Option 2: Using pydub and simpleaudio (more control over playback)
# pip install pydub simpleaudio
# This method allows you to manipulate audio (cut, slice, etc.) and play it back.
try:
    from pydub import AudioSegment
    from pydub.playback import play
    print("Playing audio using pydub...")
    # Load and play the first 5 seconds of a WAV file
    # sound = AudioSegment.from_wav("example.wav")  # Load audio file
    # short_clip = sound[:5000]  # Get first 5 seconds (5000 ms)
    # play(short_clip)  # Play the audio segment
except ImportError:
    print("pydub/simpleaudio not installed.")

# Option 3: Using pygame (game-style playback)
# pip install pygame
# This method is useful for games or apps needing more control over playback.
try:
    import pygame
    print("Playing audio using pygame...")
    pygame.mixer.init()  # Initialize the mixer module
    # pygame.mixer.music.load("example.wav")  # Load audio file
    # pygame.mixer.music.play()  # Start playback
    # while pygame.mixer.music.get_busy():  # Wait for playback to finish
    #     continue
except ImportError:
    print("pygame module not installed.")

# Option 4: Manually Read & Write Audio File in Binary
# This example shows how to read and write audio files as binary data.
try:
    print("Reading and copying audio file in binary...")
    with open("example.wav", "rb") as f:
        data = f.read()  # Read the entire file as bytes

    with open("copy.wav", "wb") as f:
        f.write(data)  # Write the bytes to a new file
except FileNotFoundError:
    print("example.wav not found for binary read/write.")

#-------------------------------
# Useful built-ijn functions
# -----------------------------
len()     # Get the length of an object (e.g., list, string)
type()    # Get the type of an object
print()   # Print to console
input()   # Get user input from console
range()   # Generate a sequence of numbers
sum()     # Calculate the sum of numbers in a list
max()     # Get the maximum value from a list
min()     # Get the minimum value from a list
sorted()  # Sort a list in ascending order

# ---------------------------------------------
# Basic GUI Display with Shapes and Button
# ---------------------------------------------
# Button Callback Function
# -----------------------------
def on_button_click():
    print("Button clicked! You can trigger any action here.")

# -----------------------------
# Window Setup
# -----------------------------
root = tk.Tk()
root.title("Basic GUI Display with Shapes")

# Define window dimensions
width = 800
height = 600
aspect_ratio = f"{width}:{height}"
print(f"Aspect Ratio: {aspect_ratio}")

# Set window size and background color
root.geometry(f"{width}x{height}")
root.configure(bg="lightgray")

# -----------------------------
# Canvas for Drawing
# -----------------------------
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

# -----------------------------
# Draw Shapes
# -----------------------------

# Rectangle (x1, y1, x2, y2)
canvas.create_rectangle(100, 100, 300, 200, fill="skyblue", outline="black", width=2)

# Oval (circle or ellipse)
canvas.create_oval(350, 100, 500, 250, fill="lightgreen", outline="darkgreen", width=2)

# Line (x1, y1, x2, y2)
canvas.create_line(50, 400, 750, 400, fill="red", width=3)

# Polygon (triangle)
canvas.create_polygon(600, 150, 700, 250, 500, 250, fill="yellow", outline="black", width=2)

# Text
canvas.create_text(400, 50, text="Canvas with Shapes", font=("Arial", 20), fill="purple")

# -----------------------------
# Button Below the Canvas
# -----------------------------
btn_action = tk.Button(root, text="Click Me!", font=("Arial", 14), bg="orange", command=on_button_click)
btn_action.pack(pady=20)

# -----------------------------
# Main Loop
# -----------------------------
root.mainloop()

#-------------------------------
#Pytest (Unit Testing)
#------------------------------

#-------------------------------
#Basic Assertions >
#-------------------------------
#terminal test: pytest test_fileName.py

#file name: test_fileName.py
import pytest
from fileName import functionName # import the function you want to test

def test_AssertionExample_Add(): 
    assert functionName(2, 3) == 5, "2 + 3 should equal 5"
    assert functionName(10, 0) == 10, "10 + 0 should equal 10" 
#   assert functionName(variables) == expected_result, "Error message"

#Fixtures >
#Creates a fresh instance of the function before each test, incase the result of one test affects the next. 
#Sometimes helpful when have backend  dataset database so it can simulate different scenarios.

import pytest 
from fileName import functionName

#Scenarios 1: Create a fresh instance of the function before each test
@pytest.fixture
def setup():
    """Creates a fresh instance of the function before each test"""
    return functionName()

#Scenarios 2: Creates a fresh instance of a database before each test
@pytest.fixture
def db():
    """Provides a fresh instance of a database class and cleans up after the test"""
    database = functionName() #new instance of database class
    yield database #Provide the fixture instance
    database.data_clear() # Clean up (not needed for in-memory, but useful for real DBs)

#Below is an example of how to use the fixture in both scenarios > 
def test_add_with_fixture(setup or db):
#   assert functionName(variables) == expected_result, "Error message"
#   assert functionName(variables) == expected_result, "Error message"
#   ...

def test_sub_with_fixture(setup or db):
#   assert functionName(variables) == expected_result, "Error message"
#   assert functionName(variables) == expected_result, "Error message"
#   ...

#-------------------------------
#Parametrized Tests >
#-------------------------------
#Allows tests to be run with different inputs based on fill in parameters.

import pytest
import fileName import functionName

@pytest.mark.parametrize("y, x, Expected_result", [
    (X1, Y1, expected_result),
    (X2, Y2, expected_result),
    (X3, Y3, expected_result),
    (X4, Y4, expected_result),
    #...
    ]) 
def test_functionName(x, y, expected_result):
    assert functionName(x, y) == expected_result
#   assert functionName(variables) == expected_result
# assert functionName(variables)

#-------------------------------
#Mocks/Mocking > 
# -----------------------------
 #Creates fake data functions that can be used in place of real functions during testing, generally in place of a backend database or API.
 # Mocks can be used to isolate modules, prevent side effects, and make tests more reliable.

#file name: fileName.py > 
import requests

def functionName(city):
    response = requests.get(f"https://fakewebsite.com/weather/{city}")
    if response.status_code == 200:
        data = response.json()
        return response.json()
    else:
        raise ValueError("Could not fetch weather data.")

#file name: test_fileName.py >
import pytest
from fileName import functionName

def test_functionName_with_mock(mocker):
    #Mock requests.get 
    mock_get = mocker.patch('fileName.requests.get')

    # Set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"Temperature": 25, "Condition": "Sunny"}

    #Call function
    result = get_weather("Dubai")

    #Assertions
    assert result == {"Temperature": 25, "Condition": "Sunny"}
    mock_get.assert_called_once_with("https://fakewebsite.com/weather/Dubai")
      
#-------------------------------
#Multi-thredding (Multi-tasking) >
#-----------------------------
# Used to perform multiple tasks concurrently in concurrently (multitasking)
# Good for I/O bound tasks like reading files or fetching data from APIs.
#     threading.Thread(target=function_name, args=(arg1, arg2)).start()

import threading  #used for multithreading
import time #used for example purposes

#This procedures takes the longest
def walk_dog(first):
    time.sleep(8) #time to simulate the task fetching data, NOT real example
    print(f"You finsihed walking {first}.")

#This procedure takes the shortest
def take_out_trash():
    time.sleep(2) #time to simulate the task fetching data, NOT real example
    print("You finsihed taking out the trash.")

#this procedure takes the medium amount of time
def get_mail(): 
    time.sleep(4) #time to simulate the task fetching data, NOT real example
    print("You finsihed getting mail.")

thread1 = threading.Thread(target=walk_dog, args=("Scooby",)) #for 1 parameter
thread1 = threading.Thread(target=walk_dog, args=("Scooby","Doo")) #for more then 1 parameter
thread1.start()

thread2 = threading.Thread(target=take_out_trash)
thread2.start()

thread3 = threading.Thread(target=get_mail)
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("All tasks have been completed.")

#--------------------------------------------
#MQTT - Message Queuing Telemetry Transport
#---------------------------------------------
#An open, light weight, and simple client server publish/subscribe message transport protocol designed for machine-to-machine communication between different devices in environments of high latency and low network bandwidth. 

#file name: mqtt_publish1.py 
#acts as publisher to send data of topic

import paho.mqtt.client as mqtt
from random import randrange, uniform
import times

mqttBroker = "mqtt.eclipseprojects.io/" #variable as mqtt Broker which will be used
client = mqtt.Client("Temperature_Inside") #create client with name "Temperature_Inside"
client.connect(mqttBroker) #connect client to broker

while True: 
    randNumber = unifrom(20.0, 21.0) #generate a random number between 20 and 21 
    client.publish("TEMPERATURE", randNumber) #publish randNumber to Topic of "TEMPERATURE"
    print("Just published" +str(randNumber) + " to Topic TEMPERATURE") #print to console
    time.sleep(1) #wait 1 sec

#file name: mqtt_publish2.py 
#acts as publisher to send data of topic

import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io/" #variable as mqtt Broker which will be used
client = mqtt.Client("Temperature_Outside") #create client with name "Temperature_Outside"
client.connect(mqttBroker) #connect client to broker

while True: 
    randNumber = randrange(10) #generate a random number between 0 and 10 
    client.publish("TEMPERATURE", randNumber) #publish randNumber to Topic of "TEMPERATURE"
    print("Just published" +str(randNumber) + " to Topic TEMPERATURE") #print to console
    time.sleep(1) #wait 1 sec

#file name: mqtt_subscribe.py 
#acts as subscriber to receive data of topic
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io/" #variable as mqtt Broker which will be used
client = mqtt.Client("Temperature_Outside") #create client with name "Smartphone"
client.connect(mqttBroker) #connect client to broker

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(30)
client.loop_end()


# End of Template
# -----------------------------