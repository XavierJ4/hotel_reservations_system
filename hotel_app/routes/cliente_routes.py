from flask import Blueprint, jsonify, request
from models import db

cliente_bp = Blueprint('clientes', __name__)

@cliente_bp.route('/', methods=['GET'])
def get_clientes():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()

    clientes = []
    for row in rows:
        cliente = {
            'id': row[0],
            'nombre': row[1],
            'direccion': row[2],
            'telefono': row[3],
            'email': row[4],
            'fecha_registro': row[5].strftime('%Y-%m-%d %H:%M:%S')
        }
        clientes.append(cliente)

    cursor.close()
    return jsonify(clientes)


@cliente_bp.route('/<int:id>', methods=['GET'])
def get_cliente(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
    row = cursor.fetchone()

    if row:
        cliente = {
            'id': row[0],
            'nombre': row[1],
            'direccion': row[2],
            'telefono': row[3],
            'email': row[4],
            'fecha_registro': row[5].strftime('%Y-%m-%d %H:%M:%S')
        }
        cursor.close()
        return jsonify(cliente)
    else:
        cursor.close()
        return jsonify({'message': 'Cliente no encontrado'}), 404


@cliente_bp.route('/', methods=['POST'])
def create_cliente():
    data = request.get_json()
    nombre = data['nombre']
    direccion = data.get('direccion', '')
    telefono = data.get('telefono', '')
    email = data['email']
    cursor = db.connection.cursor()


    cursor.execute("""
        INSERT INTO clientes (nombre, direccion, telefono, email)
        VALUES (%s, %s, %s, %s)
    """, (nombre, direccion, telefono, email))

    db.connection.commit()
    cursor.close()

    return jsonify({'message': 'Cliente creado exitosamente'}), 201


@cliente_bp.route('/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.get_json()

    nombre = data.get('nombre', '')
    direccion = data.get('direccion', '')
    telefono = data.get('telefono', '')
    email = data.get('email', '')

    cursor = db.connection.cursor()


    cursor.execute("""
        UPDATE clientes
        SET nombre = %s, direccion = %s, telefono = %s, email = %s
        WHERE id = %s
    """, (nombre, direccion, telefono, email, id))

    db.connection.commit()
    cursor.close()

    return jsonify({'message': 'Cliente actualizado exitosamente'})


@cliente_bp.route('/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    cursor = db.connection.cursor()


    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    db.connection.commit()
    cursor.close()

    return jsonify({'message': 'Cliente eliminado exitosamente'})

