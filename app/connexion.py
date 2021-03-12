import itertools
from cassandra.cluster import Cluster
from cassandra.query import dict_factory

class DB():

    @classmethod
    def open_con(cls):
        cls.cluster = Cluster(['cassandra-c01', 'cassandra-c02'], port=9042)
        # cls.cluster = Cluster(['localhost'], port=9042)

        cls.session = cls.cluster.connect('resto')

        cls.session.row_factory = dict_factory

    @classmethod
    def close_con(cls):
        cls.cluster.shutdown()



    @classmethod
    def get_info_by_id(cls, id_resto):
        cls.open_con()
        data = cls.session.execute(f"SELECT * FROM restaurant WHERE id={id_resto}").one() 
        cls.close_con()

        return {'info' : data}


    @classmethod
    def get_name_by_type(cls, type_cuisine):
        cls.open_con()
        data = cls.session.execute(f"SELECT * FROM restaurant WHERE cuisinetype='{type_cuisine}'").all()
        cls.close_con()

        return {'data': [resto['name'] for resto in data]}


    @classmethod
    def get_nb_inspec_by_id(cls, id_resto):
        cls.open_con()
        data = cls.session.execute(f"select * from restaurant where id = {id_resto}").one()
        number = len(cls.session.execute(f"select * from inspection where idrestaurant = {id_resto}").all())

        cls.close_con()
        return {'name': data['name'], 'nb_inspection': number }


# les noms des 10 premiers restaurants d'un grade donné.
    @classmethod
    def get_top_10(cls, grade):
        cls.open_con()

        data = cls.session.execute(f"select * from inspection where grade = '{grade}'").all()
        _ids = tuple(resto['idrestaurant'] for resto in data)[:100]
        top_10 = cls.session.execute(f"SELECT name FROM restaurant WHERE id IN {_ids}").all()
        cls.close_con()

        return {'grade': grade, 'restaurant': [resto['name'] for resto in top_10][:10]}

