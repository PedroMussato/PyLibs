from sql_alchemy import banco


# modelo de classe para o objeto hotel
class HotelModel(banco.Model):
    __tablename__ = 'hoteis' # tabela
    hotel_id = banco.Column(banco.String, primary_key=True) # Coluna
    nome = banco.Column(banco.String(80)) # Coluna
    estrelas = banco.Column(banco.Float(precision=1)) # Coluna
    diaria = banco.Column(banco.Float(precision=2)) # Coluna
    cidade = banco.Column(banco.String(40)) # Coluna

    # metodo construtor
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    # métodos
    def json(self):
        """
        O método json retorna o objeto do hotel em formato json
        """
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }

    @classmethod
    def find_hotel(cls, hotel_id):
        """
        O método de classe find_hotel procura no database se há algum hotel com que o id é igual a hotel_id
        caso ache algum hotel no banco que seja coerente com hotel_id ele retorna o objeto
        caso não ache nenhum dado referente ao hotel_id no banco o retorno é None
        """
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        """
        aqui é realizado o salvamento dos dados alterados no banco.
        """
        banco.session.add(self)
        banco.session.commit()

    def update_hotel(self, nome, estrelas, diaria, cidade):
        """
        aqui é feito o update de algum dado que já consta na tabela segundo o hotel_id
        """
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def delete_hotel(self):
        """
        aqui é realizado o delete do dado na tabela segundo o hotel_id
        """
        banco.session.delete(self)
        banco.session.commit()
