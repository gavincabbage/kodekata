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


	def test_foobar(self):
		self.assertEqual(1, 1)

if __name__ == "__main__":
	unittest.main()