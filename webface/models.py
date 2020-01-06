from datetime import datetime
from pony.orm import *


db = Database()


class Uzivatel(db.Entity):
    id = PrimaryKey(int, auto=True)
    login = Required(str)
    heslo = Required(str)
    jmeno = Optional(str)
    rezervaces = Set('Rezervace')


class Rezervace(db.Entity):
    id = PrimaryKey(int, auto=True)
    uzivatel = Required(Uzivatel)
    zacatek = Required(datetime)
    konec = Required(datetime)
    sal = Required('Sal')


class Sal(db.Entity):
    id = PrimaryKey(int, auto=True)
    jmeno = Optional(str)
    kapacita = Required(int)
    Dostupnost = Optional(bool)
    rezervaces = Set(Rezervace)