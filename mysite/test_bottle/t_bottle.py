from bottle import route, run, template
from bottle import get, post, request # or route

# @route('/')
# @route('/hello/<name>')
# def greet(name='Stranger'):
#     return template('Hello {{name}}, how are you?', name=name)


@get('/nsm')  # or @route('/nsm')
def nsm():
    return '''
        <form action="/nsm" method="post">
            Enter your name: <input name="name" type="text" />
            Enter your surname: <input name="surname" type="text" />
            Enter your middle name: <input name="middle_name" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''

@post('/nsm')  # or @route('/nsm', method='POST')
def do_nsm():
    name = request.forms.get('name')
    surname = request.forms.get('surname')
    middle_name = request.forms.get('middle_name')
    if (name, surname, middle_name):
        return name, ' ', surname, ' ', middle_name
    else:
        return "<p>nsm failed.</p>"
run(host='localhost', port=8080)
