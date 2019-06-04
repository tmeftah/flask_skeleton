#  The MIT License (MIT)
#  Copyright (c) 2019 Tarek Meftah. Portions adopted from code by Miguel Grinberg,  Hack4Impact.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#
from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.account.forms import LoginForm
from app.models import User, Permission
from app.decorators import permission_required


blueprint = Blueprint('account', __name__, url_prefix='/account')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """ Log in an existing user."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.strip()).first()
        if user is not None and user.password_hash is not None and user.verify_password(form.password.data.strip()):
            login_user(user, form.remember_me.data)
            flash('You are now logged in. Welcom back!', 'succes')
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('account/login.html', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('account.login'))


@blueprint.route('/test')
@login_required
@permission_required(Permission.ADMINISTER)
def test():
    return 'only admin'
