from flask import Flask , request
from caesar import rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>

        <body>
            <!--create your form here-->
            <form action="" method="post">
                <label for="Rotate">Rotate By</label>
                <input name="rot" type="text" id="Rotate" value="0">
                <textarea id="text"></textarea>
                <button type="submit" id="btn">submit</button>
                
            </form>
            </body>
    </html>
"""
@app.route("/")
def index():
    return form
app.run()

@app.route("/" ,methods=['POST'])
def encrypt():
    local_rot = string(rot)
    local_text = string(text)
    rotated_string = rotate_character(text,rot)
    return rotated_string