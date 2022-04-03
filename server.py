#web dev. framework
from flask import Flask, render_template, request
from flask import jsonify
#serializes data to JavaScript Object Notation (JSON) format

app = Flask(__name__)
 
@app.route("/")
def hello():
  return "Hello World!"



@app.route("/getimage/<page>")
def upload(page):
  return render_template(f"{page}.html")

@app.route('/uploadimage',methods=['GET'])
def requestResults():
    url = str(request.args["imageurl"])
    text = str(request.args['text'])
    filename = str(request.args['filename'])
    boilerplate = f'''
                 <head>
                  <meta name="twitter:card" content="summary" />
                 <meta name="twitter:site" content="@tapaway" />
                 <meta name="twitter:title" content="demo" />
                 <meta name="twitter:description" content="{text}" />
                 <meta name="twitter:image" content="{url}" />
                 <meta name="twitter:url" content="https://twitter.com" />
               </head>
               <body>
                <img src="{url}" />
               </body>
    '''
    file = open(f"templates//{filename}.html",'w')
    file.write(boilerplate)
    file.close()
    response = {
        "action_status":200
    }
    return jsonify(response)


if __name__ == "__main__":
  app.run()