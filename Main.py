from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/api/cep", methods = ["POST"])
def cep():
    data=request.json

    try:
        cep=data["cep"]

        response=requests.get(url=f"https://viacep.com.br/ws/{cep}/json/",params={})
        return response.json()        
    except:
        print("exception ocurred")

if __name__=="__main__":
    app.run(debug=True)