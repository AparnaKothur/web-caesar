from flask import Flask ,request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']=True

form="""
    <!DOCTYPE html>



    <html>

        <head>

            <style>

                form {{

                    background-color: #eee;

                    padding: 20px;

                    margin: 0 auto;

                    width: 540px;

                    font: 16px sans-serif;

                    border-radius: 10px;

                }}

                textarea {{

                    margin: 10px 0;

                    width: 540px;

                    height: 120px;

                }}

            </style>

        </head>
        <body>
            <form method="Post">

                <label>Rotate By:
                <input name= "rot" value="0" type="text" />
                </label>
                <label><br><br>
                <textarea name="text">{0}</textarea>
                </label>
                <input type="submit" value="Submit " />
            </form>
        </body>
    </html>
"""
@app.route("/")
def index():
    #return form.__format__('')
    return form
app.run()

@app.route("/", methods=['POST'])
def encrypt():
    local_rot = int(request.form['rot'])
    local_text = request.form['text']
    enc_string = rotate_string(local_text, local_rot)
    return enc_string
    #return form.format(rotate_string(local_text, local_rot))
    

