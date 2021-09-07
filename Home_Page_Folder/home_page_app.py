from flask import Flask, Blueprint, render_template

home_page = Blueprint('home_page', __name__, url_prefix='/homepage',
                      static_folder='static', static_url_path='/Home_Page_Folder/static',
                      template_folder='templates')


@home_page.route('/')
def home_page_def():
    return "LOL"
