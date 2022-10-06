# Ryan Lau Daniel Liu Wei Chen Liu
#SoftDev
#K07
#2022-10-03
#Time Spent: 


from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. Java. Similar Syntax to When You Create A New Object.
1. '/' represents a root of a file system Also, it is used to join file paths.
2. Name Is Printed in the Terminal.
3. Name is printed in the terminal(ex: __main__) every time request is made to the IP)
4. This will appear on the webpage of the relevant link of the IP address. We know because it is printed in the terminal as an http://
5. Run() is like a method of the class.
...
INVESTIGATIVE APPROACH:

 Flask needs to be installed via pip in terminal
 We ran the program
 We visted the http:// link that the Flask App is hosted on
'''