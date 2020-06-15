from flask import Flask,render_template
from engine.app import code_run
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('./index.html')


@app.route('/8queens.html')
def queens():
    returnable = code_run()
    newmatrix = []
    best = returnable[1][0]
    for i in range(len(best)):
        newmatrix.append([0]*len(best))


    for item in range(len(best)):
        print('item: {}, best:{}'.format(item,best[item]))
        newmatrix[best[item]-1][item] = 1
        

    return render_template('./8queens.html',returnable=returnable,newmatrix=newmatrix)

""" @app.route('/<string:page_name>')
def pages(page_name):
    return render_template(page_name) """