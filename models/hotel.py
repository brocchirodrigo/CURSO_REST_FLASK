from sql_alchemy import banco

class HotelModel(banco.Model):
    __tablename__= 'hoteis'
    
    hotel_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diarias = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(50))
    site_id = banco.Column(banco.Integer, banco.ForeignKey('sites.site_id'))
    
#class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diarias, cidade, site_id):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diarias = diarias
        self.cidade = cidade
        self.site_id = site_id
        
    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diarias': self.diarias,
            'cidade': self.cidade,
            'site_id': self.site_id
        }

    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None
    
    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()
        
    def update_hotel (self, nome, estrelas, diarias, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diarias = diarias
        self.cidade = cidade
        
    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()