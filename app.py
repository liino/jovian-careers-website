from flask import Flask, render_template, url_for, jsonify
import os

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Vienna',
  'salary': '100.000€'
}, {
  'id': 2,
  'title': 'Data Scientis',
  'location': 'Berchtesgaden',
  'salary': '150.000€'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Backand Engineer',
  'location': 'San Francisco, USA',
  'salary': '120.000€'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='MRKLNO')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
