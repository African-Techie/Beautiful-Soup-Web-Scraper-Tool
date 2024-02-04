from flask import Flask
from project.auth.auth import auth_bp
from project.views.views import views_bp
from project.models.models import db, login_manager
from project.scraper.scraper import sraper_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY NAME IS EDDIE OGYNER'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://eddie:root@localhost/orion1'

db.init_app(app)
login_manager.init_app(app)

# register the blueprints
app.register_scraper(scraper_bp, url_prefix='/scraper')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_views(views_bp, url_prefix='/views')

# Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
