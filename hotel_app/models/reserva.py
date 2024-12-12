
class Reserva:
    def __init__(self, id, cliente_id, habitacion_id, fecha_reserva, fecha_entrada, fecha_salida, estado):
        self.id = id
        self.cliente_id = cliente_id
        self.habitacion_id = habitacion_id
        self.fecha_reserva = fecha_reserva
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.estado = estado

