import pickle

class Patient:
    def __init__(self, id, name, doc, t_pac, sex, country, fnacimiento, fecha, hora, medidas, act_deporte):
        self.id = id
        self.name = name
        self.doc = doc
        self.t_pac = t_pac
        self.sex = sex
        self.country = country
        self.fnacimiento = fnacimiento
        self.fecha = fecha
        self.hora = hora
        self.medidas = medidas
        self.act_deporte = act_deporte

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_doc(self):
        return self.doc

    def get_t_pac(self):
        return self.t_pac

    def get_sex(self):
        return self.sex

    def get_country(self):
        return self.country

    def get_fnacimiento(self):
        return self.fnacimiento

    def get_fecha(self):
        return self.fecha

    def get_hora(self):
        return self.hora

    def get_medidas(self):
        return self.medidas

    def get_actdeporte(self):
        return self.act_deporte

data_row = []

with open(f'pacientes.txt', 'rb') as file_new_d:
    while True:
        try:
            info = pickle.load(file_new_d)
            data_row.append(info)
        except EOFError:
            break

print(len(data_row[6].get_medidas()[0]))
