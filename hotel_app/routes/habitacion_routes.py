
from flask import Blueprint, jsonify, request
from models import db
from models.habitacion import Habitacion

habitacion_bp = Blueprint('habitaciones', __name__)

@habitacion_bp.route('/', methods=['GET'])
def get_habitaciones():

    pass

@habitacion_bp.route('/<int:id>', methods=['GET'])
def get_habitacion(id):

    pass

@habitacion_bp.route('/', methods=['POST'])
def create_habitacion():

    pass

@habitacion_bp.route('/<int:id>', methods=['PUT'])
def update_habitacion(id):

    pass

@habitacion_bp.route('/<int:id>', methods=['DELETE'])
def delete_habitacion(id):

    pass

