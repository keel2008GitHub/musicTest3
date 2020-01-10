# coding=utf-8
import json
import os

from flask import Flask, render_template, request

from scorer import doScore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Note: You need to change this $pyPlayHomeDirectory$ to your Compass Project "music test 3 "'s directory.
MusicTest3Directory = '/Users/wangmeng/Projects/lab/python/audioMix2'
PlayShell = "./venv/bin/python ./mix_audio.py"


# windows cmd.
# MusicTest3Directory = 'D:\\MusicTest3D'
# PlayShell = ".\venv\Scripts\python.exe .\mix_audio.py"


@app.route('/', methods=['GET', 'POST'])
def index_html():
    return render_template('index.html', name='stronger')


@app.route('/speech', methods=['GET', 'POST'])
def speech():
    if request.method == 'POST':
        f = request.files['audioData']
        f.save(os.path.join('music', 'recorder.wav'))
        result = {"result": doScore()}
        return json.dumps(result)


@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        data = request.get_data()
        data2 = json.loads(data)
        print(data2['notes'])

        os.chdir(MusicTest3Directory)
        os.system(PlayShell + " \"" + data2['notes'] + "\"")
        return "sucess"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
