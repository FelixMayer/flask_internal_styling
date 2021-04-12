from flask import Flask, render_template 
app = Flask(__name__) 

@app.route('/')
def welcome():
    return 'Welcome to Squares!!!'

@app.route('/play')
def squares():
    return render_template('squares.html', num_times=3)

@app.route('/play/<int:times>')
def multiply(times):
    return render_template('squares.html', num_times= int(times))

@app.route('/play/<int:times>/<string:color>')
def color(times, color):
    return render_template('squares.html', num_times= int(times), new_color=color)

if __name__=="__main__":  
    app.run(debug=True)