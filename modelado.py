from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vedo import load, Plotter
from PyQt6 import QtCore, QtWidgets
import json
import random

script_path = './scripts/script_blender.py'
blender_path = 'c:/Program Files/Blender Foundation/Blender 3.4/blender.exe'
model_path = './test/exported_model.obj'
json_path = './scripts/datos_modelo.json'

def cambiar_ventana3d(self):
    if self.visor_3d is None:
        self.visor_3d = QVTKRenderWindowInteractor(parent=self.frame_visor3d)
        self.visor_3d.setObjectName("visor_3d")
        self.verticalLayout_43.addWidget(self.visor_3d)
    self.correr_subproceso(self.blender_path, self.script_path)

def cargarModelo(self, ruta):
    self.content.setCurrentIndex(3)
    model = load(ruta)
    scals = model.points()[:, 0] + 100  # pick x coordinates of vertices
    model.cmap("gray", scals)
    model.add_scalarbar(horizontal=True)
    vp = Plotter(qt_widget=self.visor_3d, pos=(0, 1))
    vp.add(model)
    vp.show(title='Modelo 3D', mode=1)


def correr_subproceso(self, blender, script):
    self.actualizar_json(self.json_path)
    self.dlg = QtWidgets.QMessageBox()
    self.dlg.setWindowTitle("Información")
    self.dlg.setText("El modelo está siendo creado")
    self.dlg.show()
    if self.p is None:
        self.p = QtCore.QProcess()
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        self.p.readyReadStandardError.connect(self.handle_stderr)
        self.p.finished.connect(self.modelo_terminado)
        self.p.start(str(blender), ['--background', '--python', str(script)])


def handle_stderr(self):
    data = self.p.readAllStandardError()
    stderr = bytes(data).decode("utf8")
    print(stderr)

def handle_stdout(self):
    data = self.p.readAllStandardOutput()
    stdout = bytes(data).decode("utf8")
    print(stdout)
    word = 'Progress'
    if word in stdout:
        stdout = int(float(stdout[stdout.find(word) + len(word) + 2: stdout.find(word) + len(word) + 8].strip()))


def modelo_terminado(self):
    self.cargarModelo(self.model_path)
    self.dlg.hide()
    self.p = None

def actualizar_json(self, ruta):
    with open(ruta, 'r', encoding='utf-8') as json_file:
        datos = json.load(json_file)

    datos['preset'] = 'm_la01'
    for key in datos:
        if key == 'preset':
            continue
        num_random = round(random.uniform(0.0, 1.0), 3)
        datos[key] = num_random

    with open(ruta, 'w', encoding='utf-8') as json_file:
        json.dump(datos, json_file)