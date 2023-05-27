from flask import Flask, render_template,request,flash,session,redirect,url_for

from model import db, connect_to_db, User, Post

from forms import LoginForm, PostForm, NewUserForm

from jinja2 import StrictUndefined

from flask_login import UserMixin, login_user, logout_user, LoginManager, login_required, current_user

app = Flask(__name__)
app.secret_key = 'superdupersecret'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home():
    form = LoginForm()
    post_form = PostForm()
    return render_template('login.html', form = form, post_form = post_form)

@app.route('/new-user')
def new_user():
    add_form = NewUserForm()
    return render_template('new_user.html', add_form = add_form)

@app.route('/add-user', methods=['POST'])
def add_user():
    add_form = NewUserForm()

    if add_form.validate_on_submit():
        
        email = add_form.email.data
        username = add_form.username.data
        password = add_form.password.data
        repassword = add_form.repassword.data

        if password == repassword:

            new_user = User(email,username,password)
            db.session.add(new_user)
            db.session.commit()

        else:
            print('The passwords didnt match')

    return redirect(url_for('home'))

#Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['POST','GET'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():

        email = login_form.email.data
        username = login_form.username.data
        password = login_form.password.data
        
        user = User.query.filter_by(email=email).first()
        if not user or user.password != password:
            return flash('The credentials youve entered are incorrect, please try again.')
        
        else:
            flash('Login Successful!')
            login_user(user)
            return redirect(url_for('home'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/landing')
@login_required
def landing():
    # user = User.query.filter_by(email = session["email"]).first()
    post_form = PostForm()
    return render_template('landing.html', post_form = post_form)

@app.route('/blog')
@login_required
def blog():
    user = User.query.filter_by(email = current_user.email).first()
    return render_template('blog.html', user = user)

@app.route('/new_post', methods=['POST'])
def new_post():
    post_form = PostForm()

    user = User.query.filter_by(email = current_user.email).first()

    if post_form.validate_on_submit():

        header = post_form.header.data
        body = post_form.body.data

        post = Post(user.id, header, body)

        db.session.add(post)
        db.session.commit()
    
    return redirect(url_for('home'))

# @app.route('/delete_post', methods=['POST'])
# def delete_post():
#     db.session.delete()
    

# @app.route('/liked', methods=['POST'])
# def liked():
    
    


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)