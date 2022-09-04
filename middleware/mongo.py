from mongoengine import connect


def setup():
    connect('recycledb')
