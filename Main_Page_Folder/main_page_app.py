from flask import Flask, Blueprint, render_template

main_page = Blueprint('main_page', __name__, url_prefix='/mainpage',
                      static_folder='static', static_url_path='/Main_Page_Folder/static',
                      template_folder='templates')


@main_page.route('/')
def main_page_def():
    return render_template("Main_Page_HTML.html")
