from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role,Review
from  flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# Creating app instance
app = create_app('development')
manager = Manager(app)
migrate = Migrate(app,db)
    #Initializing Flask Extensions
bootstrap.init_app(app)
db.init_app(app)
login_manager.init_app(app)    

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
if __name__ == '__main__':
    manager.run()
