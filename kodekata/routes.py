# kodekata/routes.py


from kodekata import app
from flask import request, render_template, abort
from subprocess import Popen, STDOUT, PIPE


@app.route('/kodekata/<string:language>', methods=['GET', 'POST'])
def kodekata(language):

	if request.method == 'GET':
		code_file = open("kodekata/stubs/"+language+".code", 'w')
		code = code_file.read()
		test_file = open("kodekata/stubs/"+language+".test", 'w')
		tests = test_file.read()
		return render_template("base.html", language=language, code_content=code, test_content=tests)
	elif request.method == 'POST':
		return python_exec(request.data)
	else:
		abort(404)



def python_exec(code):
	proc = Popen(["python"], stdin=PIPE, stderr=STDOUT, stdout=PIPE)
	proc.stdin.write(code)
	return proc.communicate()[0]

