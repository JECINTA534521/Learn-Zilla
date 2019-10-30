from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,logout_user,login_required
#from . import auth
#from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db
from ..emails import mail_message