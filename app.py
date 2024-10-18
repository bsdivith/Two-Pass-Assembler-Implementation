# app.py (Flask application)

from flask import Flask, render_template, request
from pass1 import pass1
from pass2 import pass2

app = Flask(__name__)

# Home route to display project overview and form for inputting assembly code
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        assembly_code = request.form['assembly_code'].split('\n')

        # Run Pass 1 to build the symbol table
        symbol_table = pass1(assembly_code)

        # Run Pass 2 to generate object code
        object_code = pass2(assembly_code, symbol_table)

        return render_template('project.html', assembly_code=assembly_code, symbol_table=symbol_table, object_code=object_code)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
