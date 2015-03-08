# tests.py

from kodekata import app, routes

import unittest
from flask import Flask


class KodekataTests(unittest.TestCase):

	def setUp(self):
		app.config.testing = True
		self.app_client = app.test_client()

	def tearDown(self):
		pass



	# Code Execution Tests

	def test_python_exec(self):
		test_code = "print 2+3"
		result = routes.python_exec(test_code)
		self.assertEqual(result.strip(), "5")

	def test_foobar(self):
		self.assertEqual(1, 1)

if __name__ == "__main__":
	unittest.main()