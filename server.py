from flask import Flask, request
import ddddocr
app = Flask(__name__)


@app.route('/', methods=['POST'])
def result():
    print(request.form['foo'])
    ocr = ddddocr.DdddOcr(beta=True)
    with open("https://lds.yphs.tp.edu.tw/tea/validatecode.aspx", 'rb') as f:
        image = f.read()
    res = ocr.classification(image)
    return res.upper()  # response to your request.
