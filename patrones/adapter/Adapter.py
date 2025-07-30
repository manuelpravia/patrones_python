class MotorElectrico:
    def conectar(self):
        print("Motor eléctrico conectado.")

    def activar(self):
        print("Motor eléctrico activado.")

class MotorComun:
    def encender(self):
        print("Motor común encendido.")

# Adaptador
class MotorElectricoAdapter:
    def __init__(self, motor_electrico):
        self.motor_electrico = motor_electrico

    def encender(self):
        self.motor_electrico.conectar()
        self.motor_electrico.activar()

# Uso
motor_comun = MotorComun()
motor_comun.encender()

motor_electrico = MotorElectrico()
adaptador = MotorElectricoAdapter(motor_electrico)
adaptador.encender()