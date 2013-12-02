import pymongo


def main():
    connection = pymongo.MongoClient('mongodb://localhost')

    db = connection.m101
    people = db.people

    person = {'name': 'Barack Obama', 'role': 'President',
              'address': {'address1': 'The White House',
              'street': '1600 Pennsylvania Avenue',
              'state': 'DC',
              'city': 'Washington'},
              'interests': ['goverment', 'basketball', 'the middle East']}

    people.insert(person)


main()
