# kodekata/routes.py


from kodekata import app
from flask import request, render_template, abort
from subprocess import Popen, STDOUT, PIPE


@app.route('/kodekata/<string:language>', methods=['GET', 'POST'])
def kodekata(language):

	if request.method == 'GET':
		return render_template("base.html", language=language)
	elif request.method == 'POST':
		data = request.data
		print "DATA: " + data
		ret = python_exec(data)
		print "RET: " + ret
		return ret
	else:
		abort(404)



def python_exec(code):


	print "CODE --> " + code
	proc = Popen(["python"], stdin=PIPE, stderr=STDOUT, stdout=PIPE)
	proc.stdin.write(code)
	retval = proc.communicate()[0]
	#for line in retval:
	#	print "LINE --> " + line
	return retval

"""
	 import subprocess
>>> p1 = subprocess.Popen(["echo", "This_is_a_testing"], stdout=subprocess.PIPE)
>>> p2 = subprocess.Popen(["grep", "-c", "test"], stdin=p1.stdout)
>>> p1.stdout.close()
>>> p2.communicate()
"""

