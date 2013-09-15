import flask, flask.views
import streaming as streaming
import os
from flask import session, request
import datetime

app = flask.Flask(__name__)
app.secret_key = "SCOPE"


class View(flask.views.MethodView):

    def get(self):
        min_time = request.args.get('min_time')
        print min_time, float(min_time)

        if min_time is None:
            min_time = datetime.datetime.now() + datetime.timedelta(minutes=-1)
            print min_time
        else:
            min_time = datetime.datetime.fromtimestamp(float(min_time))
            print min_time

        print "starting query"
        response = flask.make_response(streaming.stream(min_time))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self):
        flask.flash(streaming.stream())
        return flask.render_template('index.html')


app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
