from flask import Flask, jsonify
from flask_cors import CORS
import run_model
import constants as CONST
from waitress import serve

# create flask app
app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(run_model.bp, url_prefix='/api')

@app.route("/")
def check_status():
    return jsonify({'status':'Success','data':[]})

if __name__ == "__main__":  #Local
    app.run(host="localhost", port="9999", debug=True, use_reloader=True,threaded=True)

else:     #Production (Heroku)
    port = int(os.environ.get('PORT', 33507))
    serve(app,port=port)