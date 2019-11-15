# -*- coding: utf-8 -*-
"""
    web.app
"""
from flask import Flask, render_template, request
from process.reader import Reader
from process.refine import Refine
from process.util import remove_tag


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/refine', methods=['POST'])
def refine():
    reader = Reader(request.form['url'])
    refine = Refine(int(request.form['bundle_unit']))
    # 입력 받은 URL에 접근하여 HTML을 읽음
    html = reader.read()
    if request.form['type'] == 'remove_tag':
        html = remove_tag(html)
    return refine.obtain_result(refine.refine_text(html))


if __name__ == "__main__":
    app.run(host='localhost', port=8080)