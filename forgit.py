from flask import Flask,request,jsonify

app=Flask(__name__)
# def index():
    # pass

def addition(a,b):
    result=a+b
    return result

@app.route('/index',methods=['POST','GET'])
def index():

    return 'yes'
    



if __name__ == '__main__':
    app.run(debug=True)