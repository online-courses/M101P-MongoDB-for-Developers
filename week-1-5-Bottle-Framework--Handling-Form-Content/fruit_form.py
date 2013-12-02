import bottle


@bottle.route('/')
def home_page():
    my_things = ['apple', 'orange', 'banana', 'peach']
    return bottle.template('hello_world', {'username': 'Pahko',
                                           'things': my_things})


@bottle.post('/favourite-fruit')
def favourite_fruit():
    fruit = bottle.request.forms.get('fruit')
    if fruit is None or fruit == '':
        fruit = 'No Fruit Selected'

    return bottle.template('fruit_selection', {'fruit': fruit})


bottle.debug(True)
bottle.run(host='localhost', port=8080)
