from flask import Flask
from flask import render_template
from flask import request
from weatherapi import WeatherAPI

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index.htm', methods=['GET', 'POST'])
def main():
    kw = request.args.get('keywords', '')
    if kw is None or kw == '':
        return render_template('index.htm')
    wapi = WeatherAPI()
    data = wapi.getCityWeatherData(c=kw.encode('utf-8','ignore'))
    return render_template('weather.htm', city=kw, data=data)


if __name__ == '__main__':
    app.run(debug=True)
