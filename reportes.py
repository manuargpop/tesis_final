import pickle
import os
from datetime import date
import time

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

import pickle

# for paciente in data:
#     for i, p in vars(paciente):
#         if p == 'medidas':
#             continue
#         print(i, p, ':', vars(paciente)[p])
#     print('------------------------')

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Add logo
        self.image('images/logo.png', 10, 7.5, 15)

        # Set font for the header
        self.set_font('Helvetica', 'B', 14)

        # Centered text
        self.cell(0, 10, 'Reporte de Pacientes', 0, 0, 'C')
        # Right-aligned date
        self.set_font('Arial', '', 10)
        self.cell(0, 5, "Fecha de Reporte:", 0, 0.1, 'R')
        self.set_font('Helvetica', 'B', 10)
        self.cell(0, 5, str(self.get_current_date()), 0, 0, 'R')

        # Line break
        self.ln(15)

    def get_current_date(self):
        return time.strftime('%d%m%Y-%H%M%S')

    def table_header(self):
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 7)
        self.set_fill_color(27, 38, 59)

        headers = ['ID', 'Nombre', 'Documento', 'Tipo', 'Sexo', 'Pais', 'Nacimiento',
                   'Citas', 'Deportes', 'Dirección']
        for header in headers:
            self.cell(19, 10, header, 1, 0, 'C', fill=True)

        self.ln()

    def add_data_row(self, data):
        self.set_text_color(0, 0, 0)
        self.set_font('Helvetica', '', 7)
        for p in data:
            for i, p in vars(p).items():
                if i == 'medidas':
                    p = len(p)
                if i == 'correo':
                    continue
                self.cell(19, 10, str(p), 1, 0, 'C')
            self.ln()



