"""
    Flask-Pages - Another? flask extension that provides dynamic pages.

    Author: Bill Schumacher <bill@servernet.co>
    License: LGPLv3
    Copyright: 2016 Bill Schumacher, Cerebral Power
** GNU Lesser General Public License Usage
** This file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPLv3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl.html.
"""
from flask import Flask, redirect, url_for
from flask_security import Security
from flask_pages import Pages
app = Flask(__name__)
app.config['SECRET_KEY'] = "SuperSecretTestingKey"
Security(app).init_app(app)
pages = Pages(app).init_app(app)


@app.route("/")
def hello():
    return redirect(url_for('pages.page', page="test"))


if __name__ == "__main__":
    page = pages.datastore.create_page(name="test", url_slug="test", content="Hello World! Flask-Pages test...")
    authenticated_page = pages.datastore.create_page(name="auth", url_slug="auth",
                                                     content="Hello World! Flask-Pages auth test...",
                                                     login_required=True)
    app.run(port=5502)
