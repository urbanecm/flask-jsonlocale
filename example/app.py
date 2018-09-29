# -*- coding: utf-8 -*-
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
__dir__ = os.path.dirname(__file__)

import sys
sys.path.append(os.path.join(__dir__, '..'))

import flask
from flask import redirect, request, jsonify, make_response, render_template, session, url_for
from flask import Flask
from flask_jsonlocale import Locales
import yaml

app = Flask(__name__)

# Load configuration from YAML file
app.config.update(
    yaml.safe_load(open(os.path.join(__dir__, 'config.yaml'))))


locales = Locales(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/python')
def python():
    return 'This was translated directly in app.py: %s' % locales.get_message('example')

@app.route('/change_language', methods=['GET', 'POST'])
def change_language():
    if request.method == 'GET':
        return render_template('change_language.html', locales=locales.get_locales(), permanent_locale=locales.get_permanent_locale())
    else:
        locales.set_locale(request.form['locale'])
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, threaded=True)