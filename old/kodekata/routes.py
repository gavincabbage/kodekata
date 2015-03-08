from kodekata import app
from flask import request, render_template, abort
from subprocess import Popen, STDOUT, PIPE


PYTHON_CODE_FILE = "/Users/fkc930/Development/agile_programming/kodekata-app/kodekata/stubs/python.code"
PYTHON_TEST_FILE = "/Users/fkc930/Development/agile_programming/kodekata-app/kodekata/stubs/python.test"


@app.route('/kodekata/<string:language>', methods=['GET', 'POST'])
def kodekata(language):

	if request.method == 'GET':
		code_file = open(PYTHON_CODE_FILE, 'r')
		code = code_file.read()
		print code
		test_file = open(PYTHON_TEST_FILE, 'r')
		tests = test_file.read()
		print tests
		return render_template("base.html", language=language, code_content=code, test_content=tests)
	elif request.method == 'POST':
		return python_exec(request.data)
	else:
		abort(404)



def python_exec(code):
	proc = Popen(["python"], stdin=PIPE, stderr=STDOUT, stdout=PIPE)
	proc.stdin.write(code)
	return proc.communicate()[0]

