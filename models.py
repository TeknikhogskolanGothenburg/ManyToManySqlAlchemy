from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import relationship

from db import Base


class PersonCars(Base):
    __tablename__ = 'persons_has_cars'

    persons_persons_id = Column(Integer, ForeignKey('persons.persons_id'), primary_key=True)
    cars_reg_no = Column(String(7), ForeignKey('cars.reg_no'), primary_key=True)
    bought_date = Column(Date)
    person = relationship('Person', back_populates='cars')
    car = relationship('Car', back_populates='owners')


class Person(Base):
    __tablename__ = 'persons'

    persons_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    cars = relationship('PersonCars', back_populates='person')


class Car(Base):
    __tablename__ = 'cars'

    reg_no = Column(String(7), primary_key=True)
    brand = Column(String(50))
    model = Column(String(50))
    owners = relationship('PersonCars', back_populates='car')
