from flask import Flask, render_template,request,flash,session,redirect,url_for

from model import db, connect_to_db, User, Post

from forms import LoginForm, PostForm, NewUserForm

from jinja2 import StrictUndefined

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

    return url_for('home')

@app.route('/login', methods=['POST','GET'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():

        email = login_form.email.data
        username = login_form.username.data
        password = login_form.password.data
        
        user = User.query.filter_by(email=email).first()
        if not user or user.password != password:
            return print('The credentials youve entered are incorrect, please try again.')
        
        session['email'] = user.email

    return redirect(url_for('user'))


@app.route('/user')
def user():
    user = User.query.filter_by(email = session["email"]).first()
    return render_template('user.html', user = user)

@app.route('/blog')
def blog():
    user = User.query.filter_by(email = session["email"]).first()
    return render_template('blog.html', user = user)

@app.route('/new_post', methods=['POST'])
def new_post():
    post_form = PostForm()

    user = User.query.filter_by(email = session["email"]).first()

    if post_form.validate_on_submit():

        header = post_form.header.data
        body = post_form.body.data

        post = Post(user.id, header, body)

        db.session.add(post)
        db.session.commit()
    
    return redirect(url_for('home'))



if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)