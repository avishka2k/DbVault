from flask import render_template
from config import app
import action
from file_manager import file_manager, file_manager_table


def route():
    @app.errorhandler(404)
    def page_not_found(e):
        print(e)
        return render_template('404.html')

    @app.route('/')
    def index():
        return action.index()

    @app.route('/edit/<int:cell_id>', methods=['POST'])
    def edit(cell_id):
        return action.edit(cell_id)

    @app.route('/insert', methods=['POST'])
    def insert():
        return action.insert()

    @app.route('/newCol', methods=['POST'])
    def new_col():
        return action.new_col()

    @app.route('/dropCol', methods=['POST'])
    def drop_col():
        return action.drop_col()

    @app.route('/dropRow', methods=['POST'])
    def drop_row():
        return action.drop_row()

    @app.route('/editRow/<int:row_id>', methods=['POST'])
    def edit_row(row_id):
        return action.edit_row(row_id)

    @app.route('/filter/<int:value>', methods=['GET'])
    def compare(value):
        return action.compare(value)

# ------------- file_manager routes -------------
    @app.route('/file')
    def file():
        return file_manager()

    @app.route('/file/table')
    def file_table():
        return file_manager_table()

    @app.route('/signup')
    def sign_up():
        return render_template('authentication/sign-up.html')
