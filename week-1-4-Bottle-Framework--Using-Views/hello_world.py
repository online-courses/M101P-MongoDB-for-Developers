import bottle


@bottle.route('/')
def home_page():
    my_things = ['apple', 'orange', 'banana', 'peach']
    return bottle.template('hello_world', {'username': 'Pahko',
                                           'things': my_things})


bottle.debug(True)
bottle.run(host='localhost', port=8080)
