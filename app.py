from flask import Flask,request
import binascii
app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
    return 'This is good'
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)
