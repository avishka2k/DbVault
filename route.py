from flask import render_template, session, redirect, url_for
import auth.action
from config import app
from auth import action
from file_manager import file_manager, FileManager, add_new_table, drop_table

file_list = FileManager()


def route():
    @app.errorhandler(404)
    def page_not_found(e):
        print(e)
        return render_template('404.html')

    # @app.route('/')
    # def index():
    #     return action.index()

    @app.route('/new_table', methods=['POST'])
    def new_table():
        return add_new_table()

    @app.route('/drop_table', methods=['GET', 'POST'])
    def remove_table():
        return drop_table()

    @app.route('/edit_cell/<int:cell_id>', methods=['POST'])
    def edit(cell_id):
        return file_list.edit_cell(cell_id)

    @app.route('/updateColName', methods=['POST'])
    def update_col():
        return file_list.edit_col_name()

    @app.route('/insert_row', methods=['POST'])
    def insert_row():
        return file_list.insert_row()

    @app.route('/newCol', methods=['POST'])
    def new_col():
        return file_list.new_col()

    @app.route('/dropCol', methods=['POST'])
    def drop_col():
        return file_list.drop_col()

    @app.route('/dropRow', methods=['POST'])
    def drop_row():
        return file_list.drop_row()

    @app.route('/editRow/<int:row_id>', methods=['POST'])
    def edit_row(row_id):
        return file_list.edit_row(row_id)

    @app.route('/filter/<int:value>', methods=['GET'])
    def compare(value):
        return file_list.compare(value)

    # ------------- file_manager routes -------------
    @app.route('/')
    def file():
        # if 'loggedin' in session:
        return file_manager()
        # return redirect(url_for('signin'))

    @app.route('/table/<string:table_name>')
    def file_table(table_name):
        return file_list.file_manager_table(table_name)

    @app.route('/signup')
    def sign_up():
        return render_template('authentication/sign-up.html')

    @app.route('/bin')
    def bin_table():
        return render_template('bin_tables.html')

    # -------------- login ----------------
    @app.route('/signin', methods=['GET', 'POST'])
    def signin():
        return auth.action.signin()

