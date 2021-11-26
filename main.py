from db import session
from models import Person


def main():
    persons = session.query(Person).all()
    for person in persons:
        print(person.first_name, person.last_name)
        for car in person.cars:
            print(f'\t{car.car.reg_no}, {car.car.brand}, {car.car.model}, {car.bought_date}')
        print('-'*10)


    bob = session.query(Person).filter(Person.first_name=='Bob').first()
    disa = session.query(Person).filter(Person.first_name=='Disa').first()

    car_obj = next(c for c in bob.cars if c.cars_reg_no == 'DEF 456')
    bob.cars.remove(car_obj)
    disa.cars.append(car_obj)
    session.add(bob)
    session.add(disa)
    session.commit()
    print()


if __name__ == '__main__':
    main()
