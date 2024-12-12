
from flask import Blueprint, jsonify, request
from models import db
from models.reserva import Reserva

reserva_bp = Blueprint('reservas', __name__)

@reserva_bp.route('/', methods=['GET'])
def get_reservas():

    pass

@reserva_bp.route('/<int:id>', methods=['GET'])
def get_reserva(id):

    pass

@reserva_bp.route('/', methods=['POST'])
def create_reserva():

    pass

@reserva_bp.route('/<int:id>', methods=['PUT'])
def update_reserva(id):

    pass

@reserva_bp.route('/<int:id>', methods=['DELETE'])
def delete_reserva(id):

    pass

