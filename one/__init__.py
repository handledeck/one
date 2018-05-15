from flask import Flask
app = Flask(__name__)

from flaskext.markdown import Markdown
Markdown(app)

import one.views

