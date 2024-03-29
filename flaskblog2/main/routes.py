
from flask import render_template, request, Blueprint
from flaskblog2.models import Post
from flaskblog2.posts.forms import SearchForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('home.html', title='Home', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')




