from flask import Flask,render_template,request


app=Flask(__name__)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/predict',methods=['POST'])
def predict():
    
      return render_template("predict.html")

if __name__=="__main__":
    app.run(debug=True)
