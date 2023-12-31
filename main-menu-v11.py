import pyqtgraph as pg
import time
import mysql.connector as m
import pickle
import locale
import pipes
from fpdf import FPDF
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vedo import load, Plotter
import json
from datetime import datetime, date
from functools import partial
from math import log10
import pickle
from PyQt6 import QtCore, QtGui, QtWidgets, Qt6
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QRegularExpression, QUrl
from PyQt6.QtWidgets import QMessageBox, QSpinBox, QHeaderView, QApplication
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QRegularExpressionValidator, QPixmap, QFont, QDesktopServices
from dateutil.relativedelta import relativedelta
from fpdf import FPDF

from animation_settings import *
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1320, 732)
        MainWindow.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainwindow = QtWidgets.QFrame(parent=self.centralwidget)
        self.mainwindow.setStyleSheet("background-color: rgb(226, 231, 255)")
        self.mainwindow.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainwindow.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainwindow.setMinimumSize(QtCore.QSize(0, 0))
        self.mainwindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainwindow.setObjectName("mainwindow")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainwindow)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu = QtWidgets.QFrame(parent=self.mainwindow)
        self.menu.setMinimumSize(QtCore.QSize(50, 0))
        self.menu.setMaximumSize(QtCore.QSize(0, 16777215))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.menu.setFont(font)
        self.menu.setStyleSheet("background-color: rgb(27, 38, 59);\n"
                                "color: white;")
        self.menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.options = QtWidgets.QFrame(parent=self.menu)
        self.options.setMinimumSize(QtCore.QSize(240, 0))
        self.options.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        self.options.setFont(font)
        self.options.setStyleSheet("QPushButton {\n"
                                   "border: 0px solid;\n"
                                   "color: white;\n"
                                   "text-align: left;\n"
                                   "padding-left: 9px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "background-color: rgb(0, 0, 30);\n"
                                   "color: white;\n"
                                   "border-left: 3px solid;\n"
                                   "border-color: rgb(255, 255, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QLabel {\n"
                                   "color: white;\n"
                                   "}")
        self.options.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.options.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.options.setObjectName("options")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.options)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_name_program = QtWidgets.QLabel(parent=self.options)
        self.lbl_name_program.setMinimumSize(QtCore.QSize(0, 80))
        self.lbl_name_program.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_name_program.setFont(font)
        self.lbl_name_program.setStyleSheet("color: white;")
        self.lbl_name_program.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_name_program.setObjectName("lbl_name_program")
        self.verticalLayout_3.addWidget(self.lbl_name_program, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.btn_menu = QtWidgets.QPushButton(parent=self.options)
        self.btn_menu.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_menu.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(12)
        self.btn_menu.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/menu-lockw.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(30, 30))
        self.btn_menu.setObjectName("btn_menu")
        self.verticalLayout_3.addWidget(self.btn_menu)
        self.btn_paciente = QtWidgets.QPushButton(parent=self.options)
        self.btn_paciente.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_paciente.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(12)
        self.btn_paciente.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/patient.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_paciente.setIcon(icon1)
        self.btn_paciente.setIconSize(QtCore.QSize(30, 30))
        self.btn_paciente.setObjectName("btn_paciente")
        self.verticalLayout_3.addWidget(self.btn_paciente)
        self.btn_estadistica_patient = QtWidgets.QPushButton(parent=self.options)
        self.btn_estadistica_patient.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_estadistica_patient.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(12)
        self.btn_estadistica_patient.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/analytics.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_estadistica_patient.setIcon(icon2)
        self.btn_estadistica_patient.setIconSize(QtCore.QSize(30, 30))
        self.btn_estadistica_patient.setObjectName("btn_estadistica_patient")
        self.verticalLayout_3.addWidget(self.btn_estadistica_patient)
        self.btn_report = QtWidgets.QPushButton(parent=self.options)
        self.btn_report.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_report.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(12)
        self.btn_report.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/report.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_report.setIcon(icon3)
        self.btn_report.setIconSize(QtCore.QSize(30, 30))
        self.btn_report.setObjectName("btn_report")
        self.verticalLayout_3.addWidget(self.btn_report)
        self.btn_db = QtWidgets.QPushButton(parent=self.options)
        self.btn_db.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_db.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(12)
        self.btn_db.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/db.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_db.setIcon(icon4)
        self.btn_db.setIconSize(QtCore.QSize(30, 30))
        self.btn_db.setObjectName("btn_db")
        self.verticalLayout_3.addWidget(self.btn_db)
        self.verticalLayout_2.addWidget(self.options, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.btn_settings = QtWidgets.QPushButton(parent=self.menu)
        self.btn_settings.setMinimumSize(QtCore.QSize(240, 50))
        self.btn_settings.setMaximumSize(QtCore.QSize(240, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(12)
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_settings.setStyleSheet("QPushButton {\n"
                                        "border: 0px solid;\n"
                                        "color: white;\n"
                                        "text-align: left;\n"
                                        "padding-left: 9px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(0, 0, 30);\n"
                                        "color: white;\n"
                                        "border-left: 3px solid;\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_settings.setIcon(icon5)
        self.btn_settings.setIconSize(QtCore.QSize(30, 30))
        self.btn_settings.setObjectName("btn_settings")
        self.verticalLayout_2.addWidget(self.btn_settings)
        self.horizontalLayout.addWidget(self.menu)
        self.content = QtWidgets.QStackedWidget(parent=self.mainwindow)
        self.content.setStyleSheet("background-color: rgb(226, 231, 255);")
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.Inicio = QtWidgets.QWidget()
        self.Inicio.setObjectName("Inicio")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Inicio)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fr_inicio = QtWidgets.QFrame(parent=self.Inicio)
        self.fr_inicio.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_inicio.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_inicio.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fr_inicio)
        self.verticalLayout_5.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_inicio = QtWidgets.QLabel(parent=self.fr_inicio)
        self.lbl_inicio.setObjectName("label")
        self.verticalLayout_5.addWidget(self.lbl_inicio)
        self.verticalLayout_4.addWidget(self.fr_inicio)
        self.content.addWidget(self.Inicio)
        self.Paciente = QtWidgets.QWidget()
        self.Paciente.setObjectName("Paciente")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Paciente)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.content_patient = QtWidgets.QStackedWidget(parent=self.Paciente)
        self.content_patient.setStyleSheet("QLineEdit {\n"
                                           "background-color: white;\n"
                                           "border: 1px solid;\n"
                                           "border-color: rgb(0, 0, 61);\n"
                                           "border-radius: 3px;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox {\n"
                                           "background-color: white;\n"
                                           "border: 1px solid;\n"
                                           "border-color: rgb(0, 0, 61);\n"
                                           "border-radius: 3px;\n"
                                           "}\n"
                                           "\n"
                                           "QDateEdit {\n"
                                           "background-color: white;\n"
                                           "border: 1px solid;\n"
                                           "border-color: rgb(0, 0, 61);\n"
                                           "border-radius: 3px;\n"
                                           "}")
        self.content_patient.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content_patient.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_patient.setObjectName("content_patient")
        self.Pacientes = QtWidgets.QWidget()
        self.Pacientes.setObjectName("Pacientes")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.Pacientes)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.fr_patient = QtWidgets.QFrame(parent=self.Pacientes)
        self.fr_patient.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_patient.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_patient.setObjectName("fr_patient")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.fr_patient)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.lbl_title_p = QtWidgets.QFrame(parent=self.fr_patient)
        self.lbl_title_p.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.lbl_title_p.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lbl_title_p.setObjectName("lbl_title_p")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.lbl_title_p)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.lbl_tablep = QtWidgets.QLabel(parent=self.lbl_title_p)
        self.lbl_tablep.setMinimumSize(QtCore.QSize(250, 80))
        self.lbl_tablep.setMaximumSize(QtCore.QSize(250, 80))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(19)
        font.setBold(True)
        self.lbl_tablep.setFont(font)
        self.lbl_tablep.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_tablep.setObjectName("lbl_tablep")
        self.verticalLayout_19.addWidget(self.lbl_tablep, 0,
                                         QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_17.addWidget(self.lbl_title_p, 0,
                                         QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.fr_tablep = QtWidgets.QFrame(parent=self.fr_patient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_tablep.sizePolicy().hasHeightForWidth())
        self.fr_tablep.setSizePolicy(sizePolicy)
        self.fr_tablep.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_tablep.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_tablep.setObjectName("fr_tablep")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.fr_tablep)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.table_patient = QtWidgets.QTableWidget(parent=self.fr_tablep)
        self.table_patient.setMinimumSize(QtCore.QSize(0, 0))
        self.table_patient.setStyleSheet("QTableWidget {\n"
                                         "background-color: white;\n"
                                         "border: 2px solid;\n"
                                         "border-color: rgb(0, 0, 61);\n"
                                         "border-radius: 5px;\n"
                                         "}")
        self.table_patient.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_patient.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_patient.setAlternatingRowColors(True)
        self.table_patient.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.table_patient.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        table_row = self.rows()
        self.table_patient.setRowCount(table_row)
        self.table_patient.setObjectName("table_patient")
        self.table_patient.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_patient.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_patient.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_patient.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_patient.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_patient.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_patient.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_patient.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_patient.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_patient.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_patient.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_patient.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_patient.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_patient.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        item.setFont(font)
        self.table_patient.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        item.setFont(font)
        self.table_patient.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        item.setFont(font)
        self.table_patient.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        item.setFont(font)
        self.table_patient.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        item.setFont(font)
        self.table_patient.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        item.setFont(font)
        self.table_patient.setItem(1, 5, item)
        self.items()
        self.table_patient.horizontalHeader().setVisible(False)
        self.table_patient.horizontalHeader().setCascadingSectionResizes(False)
        self.table_patient.horizontalHeader().setDefaultSectionSize(160)
        self.table_patient.horizontalHeader().setHighlightSections(True)
        self.table_patient.horizontalHeader().setSortIndicatorShown(False)
        self.table_patient.horizontalHeader().setStretchLastSection(False)
        self.table_patient.verticalHeader().setVisible(False)
        self.table_patient.verticalHeader().setCascadingSectionResizes(False)
        self.table_patient.verticalHeader().setSortIndicatorShown(False)
        self.table_patient.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_21.addWidget(self.table_patient)
        self.verticalLayout_17.addWidget(self.fr_tablep)
        self.fr_add = QtWidgets.QFrame(parent=self.fr_patient)
        self.fr_add.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_add.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_add.setObjectName("fr_add")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.fr_add)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.btn_add = QtWidgets.QPushButton(parent=self.fr_add)
        self.btn_add.setMinimumSize(QtCore.QSize(180, 50))
        self.btn_add.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(13)
        font.setBold(False)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("QPushButton {\n"
                                   "background-color: rgb(0, 0, 61);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border: 1px solid white;\n"
                                   "border-radius: 10px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "background-color: rgb(0, 0, 31);\n"
                                   "color: white;\n"
                                   "}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/add_patient.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_add.setIcon(icon6)
        self.btn_add.setIconSize(QtCore.QSize(22, 22))
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout_20.addWidget(self.btn_add, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_17.addWidget(self.fr_add)
        self.verticalLayout_18.addWidget(self.fr_patient)
        self.content_patient.addWidget(self.Pacientes)
        self.data_patient = QtWidgets.QWidget()
        self.data_patient.setStyleSheet("")
        self.data_patient.setObjectName("data_patient")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.data_patient)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.ingresar_patient = QtWidgets.QStackedWidget(parent=self.data_patient)
        self.ingresar_patient.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ingresar_patient.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ingresar_patient.setObjectName("ingresar_patient")
        self.data_personal = QtWidgets.QWidget()
        self.data_personal.setStyleSheet("#first_data {\n"
                                         "border: 2.5px solid;\n"
                                         "border-color: rgb(0, 0, 61);\n"
                                         "border-radius: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "#date_data {\n"
                                         "border: 2.5px solid;\n"
                                         "border-color: rgb(0, 0, 61);\n"
                                         "border-radius: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "#data_deporte {\n"
                                         "border: 2.5px solid;\n"
                                         "border-color: rgb(0, 0, 61);\n"
                                         "border-radius: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "#second_data {\n"
                                         "border: 2.5px solid;\n"
                                         "border-color: rgb(0, 0, 61);\n"
                                         "border-radius: 5px;\n"
                                         "}")
        self.data_personal.setObjectName("data_personal")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.data_personal)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.contenedor_data = QtWidgets.QFrame(parent=self.data_personal)
        self.contenedor_data.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.contenedor_data.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.contenedor_data.setObjectName("contenedor_data")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.contenedor_data)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_datos = QtWidgets.QFrame(parent=self.contenedor_data)
        self.frame_datos.setEnabled(True)
        self.frame_datos.setStyleSheet("")
        self.frame_datos.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_datos.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_datos.setObjectName("frame_datos")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_datos)
        self.verticalLayout_23.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_11 = QtWidgets.QFrame(parent=self.frame_datos)
        self.frame_11.setStyleSheet("background-color: white;\n"
                                    "font: 700 11pt \"Roboto\";\n"
                                    "color: black;\n"
                                    "border: 1px solid white;\n"
                                    "border-radius: 4;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_3.setStyleSheet("\n"
                                   "QLineEdit, QComboBox, QDateTimeEdit {\n"
                                   "    border-bottom: 1px solid rgb(213, 213, 213);\n"
                                   "    border-radius: 0;\n"
                                   "    font: 750 10pt \"Roboto\";    \n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QLineEdit[text=\"\"]  {\n"
                                   "    color: rgba(0,0,0, 1.0);\n"
                                   "    font: 750 10pt \"Roboto\";    \n"
                                   "}\n"
                                   "\n"
                                   "QComboBox {\n"
                                   "    color: black;\n"
                                   "    font: 750 10pt \"Roboto\";    \n"
                                   "}\n"
                                   "\n"
                                   "QComboBox::drop-down {\n"
                                   "    border:0px;\n"
                                   "}\n"
                                   "\n"
                                   "QDateTimeEdit {\n"
                                   "    color: gray;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QDateTimeEdit::drop-down {\n"
                                   "    border: 0;\n"
                                   "}\n"
                                   "\n"
                                   "QComboBox::down-arrow, QDateTimeEdit::down-arrow {\n"
                                   "    image: url(icons/keyboard_arrow_down_FILL0_wght400_GRAD0_opsz24.svg);\n"
                                   "    width: 64px;\n"
                                   "    height: 18px;\n"
                                   "    color: gray;\n"
                                   "}\n"
                                   "\n"
                                   "QComboBox::on {\n"
                                   "    border: 4px solid #c2dbfe;\n"
                                   "}\n"
                                   "\n"
                                   "QComboBox QListView {\n"
                                   "    font: 10pt \"Roboto\";\n"
                                   "    color: gray;\n"
                                   "    padding: 4px;\n"
                                   "    border: 1px solid rgba(0,0,0, 10%);\n"
                                   "    background-color: #fff;\n"
                                   "    outline: 0px;\n"
                                   "    border-radius: 0;\n"
                                   " }\n"
                                   "\n"
                                   "QComboBox QListView::item {\n"
                                   "    color: gray;\n"
                                   "    padding-top: 4px;\n"
                                   "    padding-left: 4px;\n"
                                   "}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(20)
        self.frame_3.setMidLineWidth(28)
        self.frame_3.setObjectName("frame_3")
        self.label_4_i = QtWidgets.QLabel(parent=self.frame_3)
        self.label_4_i.setGeometry(QtCore.QRect(80, 40, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label_4_i.setFont(font)
        self.label_4_i.setStyleSheet("color: rgb(27, 38, 59);\n"
                                   "font: 800 17.5pt \"Roboto\";")
        self.label_4_i.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4_i.setWordWrap(False)
        self.label_4_i.setObjectName("label_4_i")
        self.name = QtWidgets.QLineEdit(parent=self.frame_3)
        self.name.setGeometry(QtCore.QRect(50, 120, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        regex = QRegularExpression("[a-z-A-Z_]+")
        val = QRegularExpressionValidator(regex)
        self.name.setValidator(val)
        self.name.setFont(font)
        self.name.setStyleSheet("")
        self.name.setObjectName("name")
        self.apellido = QtWidgets.QLineEdit(parent=self.frame_3)
        self.apellido.setGeometry(QtCore.QRect(300, 120, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        regex = QRegularExpression("[a-z-A-Z_]+")
        val = QRegularExpressionValidator(regex)
        self.apellido.setValidator(val)
        self.apellido.setFont(font)
        self.apellido.setText("")
        self.apellido.setObjectName("apellido")
        self.tipo_pac = QtWidgets.QComboBox(parent=self.frame_3)
        self.tipo_pac.setGeometry(QtCore.QRect(53, 200, 458, 41))
        self.tipo_pac.setStyleSheet("QComboBox {\n"
                                    "    color: gray;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::drop-down {\n"
                                    "    border:0px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow {\n"
                                    "    image: url(icons/keyboard_arrow_down_FILL0_wght400_GRAD0_opsz24.svg);\n"
                                    "    width: 64px;\n"
                                    "    height: 18px;\n"
                                    "    color: gray;\n"
                                    "}")
        self.tipo_pac.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.tipo_pac.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.tipo_pac.setIconSize(QtCore.QSize(64, 64))
        self.tipo_pac.setFrame(True)
        self.tipo_pac.setObjectName("tipo_pac")
        self.tipo_pac.addItem("")
        self.tipo_pac.addItem("")
        self.tipo_pac.addItem("")
        self.sexo = QtWidgets.QComboBox(parent=self.frame_3)
        self.sexo.setGeometry(QtCore.QRect(53, 360, 458, 41))
        self.sexo.setStyleSheet("QComboBox {\n"
                                "    color: gray;\n"
                                "}\n"
                                "\n"
                                "QComboBox::drop-down {\n"
                                "    border:0px;\n"
                                "}\n"
                                "\n"
                                "QComboBox::down-arrow {\n"
                                "    image: url(icons/keyboard_arrow_down_FILL0_wght400_GRAD0_opsz24.svg);\n"
                                "    width: 64px;\n"
                                "    height: 18px;\n"
                                "    color: gray;\n"
                                "}")
        self.sexo.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.sexo.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.sexo.setIconSize(QtCore.QSize(64, 64))
        self.sexo.setFrame(True)
        self.sexo.setObjectName("sexo")
        self.sexo.addItem("")
        self.sexo.addItem("")
        self.fnacimiento = QtWidgets.QDateTimeEdit(parent=self.frame_3)
        self.fnacimiento.setGeometry(QtCore.QRect(53, 280, 458, 41))
        self.fnacimiento.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fnacimiento.setSpecialValueText("")
        self.fnacimiento.setMaximumDate(QtCore.QDate(2024, 12, 31))
        self.fnacimiento.setMinimumDate(QtCore.QDate(1940, 9, 14))
        self.fnacimiento.setCalendarPopup(True)
        self.fnacimiento.setObjectName("fnacimiento")
        self.act_deporte = QtWidgets.QLineEdit(parent=self.frame_3)
        self.act_deporte.setGeometry(QtCore.QRect(50, 440, 458, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        regex = QRegularExpression("[a-z-A-Z_]+")
        val = QRegularExpressionValidator(regex)
        self.act_deporte.setValidator(val)
        self.act_deporte.setFont(font)
        self.act_deporte.setStyleSheet("")
        self.act_deporte.setObjectName("act_deporte")
        self.btn_subir_foto = QtWidgets.QPushButton(parent=self.frame_3)
        self.btn_subir_foto.setGeometry(QtCore.QRect(240, 540, 111, 41))
        self.btn_subir_foto.setStyleSheet("QPushButton {\n"
                                          "    background-color:rgb(27, 38, 59);\n"
                                          "    border: 1px solid white;\n"
                                          "    border-radius: 10;\n"
                                          "    font: 750 9.5pt \"Roboto\";\n"
                                          "    color: white;\n"
                                          "}    \n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    font-size: 10pt;\n"
                                          "    background-color: black;\n"
                                          "}")
        self.btn_subir_foto.setObjectName("btn_subir_foto")
        self.lbl_info_foto = QtWidgets.QLabel(parent=self.frame_3)
        self.lbl_info_foto.setGeometry(QtCore.QRect(220, 500, 161, 31))
        self.lbl_info_foto.setStyleSheet("font: 9pt \"Roboto\";\n"
                                         "color: black;")
        self.lbl_info_foto.setText("")
        self.lbl_info_foto.setObjectName("lbl_info_foto")
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame_12 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_12.setStyleSheet("QFrame {\n"
                                    "    background-color: rgb(27, 38, 59);\n"
                                    "    border: 1px solid rgb(27, 38, 59);\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit, QComboBox {\n"
                                    "    border-bottom: 1px solid rgb(213, 213, 213);\n"
                                    "    border-left: none;\n"
                                    "    border-right: none;\n"
                                    "    border-top: none;\n"
                                    "    border-radius: 0;\n"
                                    "    font: 550 10pt \"Roboto\";    \n"
                                    "    background-color: rgb(27, 38, 59);\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit[text=\"\"], QComboBox[text=\"\"] {\n"
                                    "    color: white;\n"
                                    "    font: 550 10pt \"Roboto\";\n"
                                    "    background-color:  rgb(27, 38, 59);\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox {\n"
                                    "    color: white;\n"
                                    "    font: 550 10pt \"Roboto\";\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::drop-down {\n"
                                    "    border:0px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow {\n"
                                    "    image: url(icons/keyboard-down-white.svg);\n"
                                    "    width: 64px;\n"
                                    "    height: 18px;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QComboBox QListView {\n"
                                    "    font: 750 10pt \"Roboto\";\n"
                                    "    padding: 4px;\n"
                                    "    border: 1px solid rgba(0,0,0, 10%);\n"
                                    "    background-color: #fff;\n"
                                    "    outline: 0px;\n"
                                    "    border-radius: 0;\n"
                                    " }\n"
                                    "\n"
                                    "QComboBox QListView::item {\n"
                                    "    color: white;\n"
                                    "    padding-top: 4px;\n"
                                    "    padding-left: 4px;\n"
                                    "}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_5_i = QtWidgets.QLabel(parent=self.frame_12)
        self.label_5_i.setGeometry(QtCore.QRect(190, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label_5_i.setFont(font)
        self.label_5_i.setStyleSheet("color: white;\n"
                                   "font: 800 17.5pt \"Roboto\";\n"
                                   "border: none")
        self.label_5_i.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5_i.setObjectName("label_5_i")
        self.country = QtWidgets.QComboBox(parent=self.frame_12)
        self.country.setGeometry(QtCore.QRect(60, 120, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.country.setFont(font)
        self.country.setStyleSheet("QComboBox QListView {\n"
                                   "font-size: 12px;\n"
	"padding: 5px;\n"
	"background-color: rgb(27, 38, 59);\n"
	"color: black;\n"
"}\n"              
"QComboBox::drop-down {\n"
	"border:0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
	"image: url(icons/keyboard-down-white.svg);\n"
	"width: 64px;\n"
	"height: 18px;\n"
"}")
        self.country.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.country.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.country.setIconSize(QtCore.QSize(64, 64))
        self.country.setFrame(True)
        self.country.setObjectName("country")
        paises = ['Afghanistan',
                  'Albania',
                  'Algeria',
                  'Andorra',
                  'Angola',
                  'Antigua & Deps',
                  'Argentina',
                  'Armenia',
                  'Australia',
                  'Austria',
                  'Azerbaijan',
                  'Bahamas',
                  'Bahrain',
                  'Bangladesh',
                  'Barbados',
                  'Belarus',
                  'Belgium',
                  'Belize',
                  'Benin',
                  'Bhutan',
                  'Bolivia',
                  'Bosnia Herzegovina',
                  'Botswana',
                  'Brazil',
                  'Brunei',
                  'Bulgaria',
                  'Burkina',
                  'Burundi',
                  'Cambodia',
                  'Cameroon',
                  'Canada',
                  'Cape Verde',
                  'Central African Rep',
                  'Chad',
                  'Chile',
                  'China',
                  'Colombia',
                  'Comoros',
                  'Congo',
                  'Congo Democratic Rep',
                  'Costa Rica',
                  'Croatia',
                  'Cuba',
                  'Cyprus',
                  'Czech Republic',
                  'Denmark',
                  'Djibouti',
                  'Dominica',
                  'Dominican Republic',
                  'East Timor',
                  'Ecuador',
                  'Egypt',
                  'El Salvador',
                  'Equatorial Guinea',
                  'Eritrea',
                  'Estonia',
                  'Ethiopia',
                  'Fiji',
                  'Finland',
                  'France',
                  'Gabon',
                  'Gambia',
                  'Georgia',
                  'Germany',
                  'Ghana',
                  'Greece',
                  'Grenada',
                  'Guatemala',
                  'Guinea',
                  'Guinea-Bissau',
                  'Guyana',
                  'Haiti',
                  'Honduras',
                  'Hungary',
                  'Iceland',
                  'India',
                  'Indonesia',
                  'Iran',
                  'Iraq',
                  'Ireland Republic',
                  'Israel',
                  'Italy',
                  'Ivory Coast',
                  'Jamaica',
                  'Japan',
                  'Jordan',
                  'Kazakhstan',
                  'Kenya',
                  'Kiribati',
                  'Korea North',
                  'Korea South',
                  'Kosovo',
                  'Kuwait',
                  'Kyrgyzstan',
                  'Laos',
                  'Latvia',
                  'Lebanon',
                  'Lesotho',
                  'Liberia',
                  'Libya',
                  'Liechtenstein',
                  'Lithuania',
                  'Luxembourg',
                  'Macedonia',
                  'Madagascar',
                  'Malawi',
                  'Malaysia',
                  'Maldives',
                  'Mali',
                  'Malta',
                  'Marshall Islands',
                  'Mauritania',
                  'Mauritius',
                  'Mexico',
                  'Micronesia',
                  'Moldova',
                  'Monaco',
                  'Mongolia',
                  'Montenegro',
                  'Morocco',
                  'Mozambique',
                  'Myanmar, Burma',
                  'Namibia',
                  'Nauru',
                  'Nepal',
                  'Netherlands',
                  'New Zealand',
                  'Nicaragua',
                  'Niger',
                  'Nigeria',
                  'Norway',
                  'Oman',
                  'Pakistan',
                  'Palau',
                  'Panama',
                  'Papua New Guinea',
                  'Paraguay',
                  'Peru',
                  'Philippines',
                  'Poland',
                  'Portugal',
                  'Qatar',
                  'Romania',
                  'Russian Federation',
                  'Rwanda',
                  'St Kitts & Nevis',
                  'St Lucia',
                  'Saint Vincent & the Grenadines',
                  'Samcoa',
                  'San Marino',
                  'Sao Tome & Principe',
                  'Saudi Arabia',
                  'Senegal',
                  'Serbia',
                  'Seychelles',
                  'Sierra Leone',
                  'Singapore',
                  'Slovakia',
                  'Slovenia',
                  'Solomon Islands',
                  'Somalia',
                  'South Africa',
                  'South Sudan',
                  'Spain',
                  'Sri Lanka',
                  'Sudan',
                  'Suriname',
                  'Swaziland',
                  'Sweden',
                  'Switzerland',
                  'Syria',
                  'Taiwan',
                  'Tajikistan',
                  'Tanzania',
                  'Thailand',
                  'Togo',
                  'Tonga',
                  'Trinidad & Tobago',
                  'Tunisia',
                  'Turkey',
                  'Turkmenistan',
                  'Tuvalu',
                  'Uganda',
                  'Ukraine',
                  'United Arab Emirates',
                  'United Kingdom',
                  'United States',
                  'Uruguay',
                  'Uzbekistan',
                  'Vanuatu',
                  'Vatican City',
                  'Venezuela',
                  'Vietnam',
                  'Yemen',
                  'Zambia',
                  'Zimbabwe']
        for i in enumerate(paises):
            self.country.addItem("")
        self.documento = QtWidgets.QLineEdit(parent=self.frame_12)
        self.documento.setGeometry(QtCore.QRect(152, 200, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        regex = QRegularExpression("[0-9]{9}")
        val = QRegularExpressionValidator(regex)
        self.documento.setValidator(val)
        self.documento.setFont(font)
        self.documento.setStyleSheet("")
        self.documento.setText("")
        self.documento.setObjectName("documento")
        self.tipo_doc = QtWidgets.QComboBox(parent=self.frame_12)
        self.tipo_doc.setGeometry(QtCore.QRect(60, 200, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.tipo_doc.setFont(font)
        self.tipo_doc.setStyleSheet("QComboBox QListView {\n"
                                   "font-size: 12px;\n"
	"padding: 5px;\n"
	"background-color: rgb(27, 38, 59);\n"
	"color: black;\n"
"}\n"              
"QComboBox::drop-down {\n"
	"border:0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
	"image: url(icons/keyboard-down-white.svg);\n"
	"width: 64px;\n"
	"height: 18px;\n"
"}")
        self.tipo_doc.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.tipo_doc.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.tipo_doc.setIconSize(QtCore.QSize(64, 64))
        self.tipo_doc.setFrame(True)
        self.tipo_doc.setObjectName("tipo_doc")
        self.tipo_doc.addItem("")
        self.correo = QtWidgets.QLineEdit(parent=self.frame_12)
        self.correo.setGeometry(QtCore.QRect(60, 280, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.correo.setFont(font)
        self.correo.setText("")
        self.correo.setObjectName("correo")
        self.direccion = QtWidgets.QLineEdit(parent=self.frame_12)
        self.direccion.setGeometry(QtCore.QRect(60, 440, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.direccion.setFont(font)
        self.direccion.setText("")
        self.direccion.setObjectName("direccion")
        self.btn_sigR1 = QtWidgets.QPushButton(parent=self.frame_12)
        self.btn_sigR1.setGeometry(QtCore.QRect(230, 540, 151, 41))
        self.btn_sigR1.setStyleSheet("QPushButton {\n"
                                     "    background-color: white;\n"
                                     "    border: 1px solid rgb(27, 38, 59);\n"
                                     "    border-radius: 10;\n"
                                     "    font: 750 9.5pt \"Roboto\";\n"
                                     "    color: rgb(27, 38, 59);\n"
                                     "}    \n"
                                     "\n"
                                     "QPushButton::hover {\n"
                                     "    font: 750 10pt \"Roboto\";\n"
                                     "    background-color: rgb(0, 0, 61);\n"
                                     "    color: white;\n"
                                     "}")
        self.btn_sigR1.setObjectName("btn_sigR1")
        self.code_country = QtWidgets.QComboBox(parent=self.frame_12)
        self.code_country.setGeometry(QtCore.QRect(58, 360, 71, 41))
        self.code_country.setStyleSheet("QComboBox QListView {\n"
                                   "font-size: 12px;\n"
	"padding: 5px;\n"
	"background-color: rgb(27, 38, 59);\n"
	"color: black;\n"
"}\n"              
"QComboBox::drop-down {\n"
	"border:0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
	"image: url(icons/keyboard-down-white.svg);\n"
	"width: 64px;\n"
	"height: 18px;\n"
"}")
        self.code_country.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.code_country.setSizeAdjustPolicy(
            QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.code_country.setIconSize(QtCore.QSize(64, 64))
        self.code_country.setFrame(True)
        self.code_country.setObjectName("code_country")
        self.code_country.addItem("")
        self.telf = QtWidgets.QLineEdit(parent=self.frame_12)
        self.telf.setGeometry(QtCore.QRect(150, 360, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.direccion.setFont(font)
        regex = QRegularExpression("[0-9]{14}")
        val = QRegularExpressionValidator(regex)
        self.telf.setValidator(val)
        self.telf.setText("")
        self.telf.setObjectName("telf")
        self.horizontalLayout_3.addWidget(self.frame_12)
        self.verticalLayout_23.addWidget(self.frame_11)
        self.verticalLayout_23.setStretch(0, 10)
        self.horizontalLayout_2.addWidget(self.frame_datos)
        self.verticalLayout_32.addWidget(self.contenedor_data)
        self.ingresar_patient.addWidget(self.data_personal)
        self.Mediciones_adulto = QtWidgets.QWidget()
        self.Mediciones_adulto.setStyleSheet("QWidget {\n"
                                             "    background-color: rgb(226, 231, 255)\n"
                                             "}")
        self.Mediciones_adulto.setObjectName("Mediciones_adulto")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Mediciones_adulto)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scroll_medidas = QtWidgets.QScrollArea(parent=self.Mediciones_adulto)
        self.scroll_medidas.setStyleSheet("QScrollArea {border: 0px solid;}")
        self.scroll_medidas.setWidgetResizable(True)
        self.scroll_medidas.setObjectName("scroll_medidas")
        self.scrollArea_medidas = QtWidgets.QWidget()
        self.scrollArea_medidas.setGeometry(QtCore.QRect(0, 0, 1223, 1218))
        self.scrollArea_medidas.setObjectName("scrollArea_medidas")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollArea_medidas)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.grid_content = QtWidgets.QFrame(parent=self.scrollArea_medidas)
        self.grid_content.setMinimumSize(QtCore.QSize(1100, 1200))
        self.grid_content.setMaximumSize(QtCore.QSize(1250, 16777215))
        self.grid_content.setStyleSheet("QTableWidget {\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}")
        self.grid_content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.grid_content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.grid_content.setObjectName("grid_content")
        self.table_medidas = QtWidgets.QTableWidget(parent=self.grid_content)
        self.table_medidas.setGeometry(QtCore.QRect(50, 320, 1101, 181))
        self.table_medidas.setMinimumSize(QtCore.QSize(0, 180))
        self.table_medidas.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.table_medidas.setStyleSheet("")
        self.table_medidas.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.table_medidas.setLineWidth(0)
        self.table_medidas.setMidLineWidth(0)
        self.table_medidas.setAlternatingRowColors(False)
        self.table_medidas.setShowGrid(True)
        self.table_medidas.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.table_medidas.setObjectName("table_medidas")
        self.table_medidas.setColumnCount(5)
        self.table_medidas.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas.setItem(3, 4, item)
        self.table_medidas.horizontalHeader().setVisible(False)
        self.table_medidas.horizontalHeader().setDefaultSectionSize(214)
        self.table_medidas.horizontalHeader().setHighlightSections(True)
        self.table_medidas.horizontalHeader().setMinimumSectionSize(33)
        self.table_medidas.horizontalHeader().setStretchLastSection(True)
        self.table_medidas.verticalHeader().setVisible(False)
        self.table_medidas.verticalHeader().setDefaultSectionSize(37)
        self.table_medidas.verticalHeader().setHighlightSections(True)
        self.table_medidas.verticalHeader().setMinimumSectionSize(16)
        self.table_medidas.verticalHeader().setStretchLastSection(True)
        delegate = NumericDelegate(self.table_medidas)
        self.table_medidas.setItemDelegate(delegate)
        self.table_pliegues_cut = QtWidgets.QTableWidget(parent=self.grid_content)
        self.table_pliegues_cut.setGeometry(QtCore.QRect(50, 590, 1101, 191))
        self.table_pliegues_cut.setMinimumSize(QtCore.QSize(0, 180))
        self.table_pliegues_cut.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.table_pliegues_cut.setObjectName("table_pliegues_cut")
        self.table_pliegues_cut.setColumnCount(5)
        self.table_pliegues_cut.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut.setItem(4, 4, item)
        self.table_pliegues_cut.horizontalHeader().setVisible(False)
        self.table_pliegues_cut.horizontalHeader().setDefaultSectionSize(216)
        self.table_pliegues_cut.horizontalHeader().setMinimumSectionSize(40)
        self.table_pliegues_cut.horizontalHeader().setStretchLastSection(True)
        self.table_pliegues_cut.verticalHeader().setVisible(False)
        self.table_pliegues_cut.verticalHeader().setDefaultSectionSize(37)
        self.table_pliegues_cut.verticalHeader().setHighlightSections(True)
        self.table_pliegues_cut.verticalHeader().setMinimumSectionSize(0)
        self.table_pliegues_cut.verticalHeader().setStretchLastSection(True)
        delegate = NumericDelegate(self.table_pliegues_cut)
        self.table_pliegues_cut.setItemDelegate(delegate)
        self.table_perife_circun = QtWidgets.QTableWidget(parent=self.grid_content)
        self.table_perife_circun.setGeometry(QtCore.QRect(50, 870, 1101, 231))
        self.table_perife_circun.setMinimumSize(QtCore.QSize(852, 212))
        self.table_perife_circun.setMaximumSize(QtCore.QSize(1000000, 16777215))
        self.table_perife_circun.setRowCount(7)
        self.table_perife_circun.setColumnCount(5)
        self.table_perife_circun.setObjectName("table_perife_circun")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun.setItem(6, 4, item)
        self.table_perife_circun.horizontalHeader().setVisible(False)
        self.table_perife_circun.horizontalHeader().setDefaultSectionSize(216)
        self.table_perife_circun.horizontalHeader().setStretchLastSection(True)
        self.table_perife_circun.verticalHeader().setVisible(False)
        self.table_perife_circun.verticalHeader().setDefaultSectionSize(32)
        self.table_perife_circun.verticalHeader().setStretchLastSection(True)
        delegate = NumericDelegate(self.table_perife_circun)
        self.table_perife_circun.setItemDelegate(delegate)
        self.info_medidas = QtWidgets.QFrame(parent=self.grid_content)
        self.info_medidas.setGeometry(QtCore.QRect(40, 240, 1131, 71))
        self.info_medidas.setStyleSheet("QFrame {\n"
                                        "    background-color: rgb(0, 0, 61);\n"
                                        "    border-radius: 15;\n"
                                        "    color: white;\n"
                                        "}")
        self.info_medidas.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_medidas.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_medidas.setObjectName("info_medidas")
        self.label_medidas = QtWidgets.QLabel(parent=self.info_medidas)
        self.label_medidas.setGeometry(QtCore.QRect(30, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.label_medidas.setFont(font)
        self.label_medidas.setObjectName("label_medidas")
        self.info_pliegues = QtWidgets.QFrame(parent=self.grid_content)
        self.info_pliegues.setGeometry(QtCore.QRect(40, 510, 1141, 71))
        self.info_pliegues.setStyleSheet("QFrame {\n"
                                         "    background-color: rgb(0, 0, 61);\n"
                                         "    border-radius: 15;\n"
                                         "    color: white;\n"
                                         "}")
        self.info_pliegues.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_pliegues.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_pliegues.setObjectName("info_pliegues")
        self.label_pliegues = QtWidgets.QLabel(parent=self.info_pliegues)
        self.label_pliegues.setGeometry(QtCore.QRect(30, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.label_pliegues.setFont(font)
        self.label_pliegues.setObjectName("label_pliegues")
        self.info_perimetros = QtWidgets.QFrame(parent=self.grid_content)
        self.info_perimetros.setGeometry(QtCore.QRect(40, 790, 1141, 71))
        self.info_perimetros.setStyleSheet("QFrame {\n"
                                           "    background-color: rgb(0, 0, 61);\n"
                                           "    border-radius: 15;\n"
                                           "    color: white;\n"
                                           "}")
        self.info_perimetros.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_perimetros.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_perimetros.setObjectName("info_perimetros")
        self.label_perimetros = QtWidgets.QLabel(parent=self.info_perimetros)
        self.label_perimetros.setGeometry(QtCore.QRect(30, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.label_perimetros.setFont(font)
        self.label_perimetros.setObjectName("label_perimetros")
        self.btn_guardar_medidas = QtWidgets.QPushButton(parent=self.grid_content)
        self.btn_guardar_medidas.setGeometry(QtCore.QRect(530, 1120, 150, 50))
        self.btn_guardar_medidas.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_guardar_medidas.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(12)
        self.btn_guardar_medidas.setFont(font)
        self.btn_guardar_medidas.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(0, 0, 61);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border: 1px solid white;\n"
                                               "border-radius: 10px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "background-color: rgb(0, 0, 31);\n"
                                               "color: white;\n"
                                               "}")
        self.btn_guardar_medidas.setObjectName("btn_guardar_medidas")
        self.data_title_patient_s_2 = QtWidgets.QFrame(parent=self.grid_content)
        self.data_title_patient_s_2.setGeometry(QtCore.QRect(240, 10, 721, 200))
        self.data_title_patient_s_2.setMinimumSize(QtCore.QSize(500, 200))
        self.data_title_patient_s_2.setMaximumSize(QtCore.QSize(1000, 500))
        self.data_title_patient_s_2.setStyleSheet("#data_title_patient_s_2 {\n"
                                                  "    border: 1px solid black;\n"
                                                  "    font: 450 10pt \"Circular Std\";\n"
                                                  "}\n"
                                                  "\n"
                                                  "QFrame {\n"
                                                  "    background-color: rgb(221, 226, 249);\n"
                                                  "    border-radius: 10;\n"
                                                  "}")
        self.data_title_patient_s_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.data_title_patient_s_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.data_title_patient_s_2.setObjectName("data_title_patient_s_2")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.data_title_patient_s_2)
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_49.setSpacing(2)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.fr_photo_patient_s_3 = QtWidgets.QFrame(parent=self.data_title_patient_s_2)
        self.fr_photo_patient_s_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.fr_photo_patient_s_3.setStyleSheet("background-color: rgb(0, 0, 61);")
        self.fr_photo_patient_s_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_photo_patient_s_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_photo_patient_s_3.setObjectName("fr_photo_patient_s_3")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.fr_photo_patient_s_3)
        self.horizontalLayout_35.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_35.setSpacing(21)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.photo_patient_s_3 = QtWidgets.QLabel(parent=self.fr_photo_patient_s_3)
        self.photo_patient_s_3.setMinimumSize(QtCore.QSize(60, 60))
        self.photo_patient_s_3.setMaximumSize(QtCore.QSize(60, 60))
        self.photo_patient_s_3.setStyleSheet("border: 2px solid;\n"
                                             "border-color: white;")
        self.photo_patient_s_3.setText("")
        self.photo_patient_s_3.setPixmap(QtGui.QPixmap("../.designer/PycharmProjects/Tesis/images/foto-p.png"))
        self.photo_patient_s_3.setScaledContents(True)
        self.photo_patient_s_3.setObjectName("photo_patient_s_3")
        self.horizontalLayout_35.addWidget(self.photo_patient_s_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_49.addWidget(self.fr_photo_patient_s_3)
        self.fr_data_patient_s_3 = QtWidgets.QFrame(parent=self.data_title_patient_s_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fr_data_patient_s_3.setFont(font)
        self.fr_data_patient_s_3.setStyleSheet("#fr_data_patient_s {\n"
                                               "border: 3px solid;\n"
                                               "border-radius: 5px;\n"
                                               "border-color: rgb(0, 0, 31);\n"
                                               "}\n"
                                               "\n"
                                               "QFrame {\n"
                                               "background-color: white;\n"
                                               "}\n"
                                               "\n"
                                               "QLabel {\n"
                                               "background-color: white;\n"
                                               "color: rgb(0, 0, 31);\n"
                                               "}")
        self.fr_data_patient_s_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_data_patient_s_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_data_patient_s_3.setObjectName("fr_data_patient_s_3")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.fr_data_patient_s_3)
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.fr_name_s_3 = QtWidgets.QFrame(parent=self.fr_data_patient_s_3)
        self.fr_name_s_3.setMinimumSize(QtCore.QSize(0, 40))
        self.fr_name_s_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.fr_name_s_3.setStyleSheet("")
        self.fr_name_s_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_name_s_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_name_s_3.setObjectName("fr_name_s_3")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.fr_name_s_3)
        self.horizontalLayout_36.setSpacing(6)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.nombrec_s_3 = QtWidgets.QLabel(parent=self.fr_name_s_3)
        self.nombrec_s_3.setMinimumSize(QtCore.QSize(200, 20))
        self.nombrec_s_3.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.nombrec_s_3.setFont(font)
        self.nombrec_s_3.setStyleSheet("border-bottom: 2px solid;\n"
                                       "border-radius: 30px;\n"
                                       "border-color: rgb(0, 0, 31);")
        self.nombrec_s_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombrec_s_3.setObjectName("nombrec_s_3")
        self.horizontalLayout_36.addWidget(self.nombrec_s_3)
        self.verticalLayout_50.addWidget(self.fr_name_s_3)
        self.fr_datapatient_s_3 = QtWidgets.QFrame(parent=self.fr_data_patient_s_3)
        self.fr_datapatient_s_3.setStyleSheet("")
        self.fr_datapatient_s_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datapatient_s_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datapatient_s_3.setObjectName("fr_datapatient_s_3")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.fr_datapatient_s_3)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.fr_datap_s1_3 = QtWidgets.QFrame(parent=self.fr_datapatient_s_3)
        self.fr_datap_s1_3.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s1_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s1_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s1_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s1_3.setObjectName("fr_datap_s1_3")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.fr_datap_s1_3)
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.documento_s_3 = QtWidgets.QLabel(parent=self.fr_datap_s1_3)
        self.documento_s_3.setMinimumSize(QtCore.QSize(150, 20))
        self.documento_s_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(9)
        self.documento_s_3.setFont(font)
        self.documento_s_3.setStyleSheet("")
        self.documento_s_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.documento_s_3.setObjectName("documento_s_3")
        self.verticalLayout_51.addWidget(self.documento_s_3)
        self.tipo_patient_s_3 = QtWidgets.QLabel(parent=self.fr_datap_s1_3)
        self.tipo_patient_s_3.setMinimumSize(QtCore.QSize(150, 20))
        self.tipo_patient_s_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.tipo_patient_s_3.setFont(font)
        self.tipo_patient_s_3.setStyleSheet("")
        self.tipo_patient_s_3.setText("")
        self.tipo_patient_s_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tipo_patient_s_3.setObjectName("tipo_patient_s_3")
        self.verticalLayout_51.addWidget(self.tipo_patient_s_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_37.addWidget(self.fr_datap_s1_3)
        self.fr_datap_s2_3 = QtWidgets.QFrame(parent=self.fr_datapatient_s_3)
        self.fr_datap_s2_3.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s2_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s2_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s2_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s2_3.setObjectName("fr_datap_s2_3")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.fr_datap_s2_3)
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.sexo_s_3 = QtWidgets.QLabel(parent=self.fr_datap_s2_3)
        self.sexo_s_3.setMinimumSize(QtCore.QSize(150, 20))
        self.sexo_s_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(9)
        self.sexo_s_3.setFont(font)
        self.sexo_s_3.setStyleSheet("")
        self.sexo_s_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sexo_s_3.setObjectName("sexo_s_3")
        self.verticalLayout_52.addWidget(self.sexo_s_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.nombrec_s_7 = QtWidgets.QLabel(parent=self.fr_datap_s2_3)
        self.nombrec_s_7.setMinimumSize(QtCore.QSize(150, 20))
        self.nombrec_s_7.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.nombrec_s_7.setFont(font)
        self.nombrec_s_7.setStyleSheet("")
        self.nombrec_s_7.setText("")
        self.nombrec_s_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombrec_s_7.setObjectName("nombrec_s_7")
        self.verticalLayout_52.addWidget(self.nombrec_s_7)
        self.horizontalLayout_37.addWidget(self.fr_datap_s2_3)
        self.fr_datap_s3_3 = QtWidgets.QFrame(parent=self.fr_datapatient_s_3)
        self.fr_datap_s3_3.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s3_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s3_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s3_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s3_3.setObjectName("fr_datap_s3_3")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.fr_datap_s3_3)
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.telf_s_3 = QtWidgets.QLabel(parent=self.fr_datap_s3_3)
        self.telf_s_3.setMinimumSize(QtCore.QSize(150, 20))
        self.telf_s_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(9)
        self.telf_s_3.setFont(font)
        self.telf_s_3.setStyleSheet("")
        self.telf_s_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.telf_s_3.setObjectName("telf_s_3")
        self.verticalLayout_53.addWidget(self.telf_s_3)
        self.Act_fisica_s_3 = QtWidgets.QLabel(parent=self.fr_datap_s3_3)
        self.Act_fisica_s_3.setMinimumSize(QtCore.QSize(150, 20))
        self.Act_fisica_s_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.Act_fisica_s_3.setFont(font)
        self.Act_fisica_s_3.setStyleSheet("")
        self.Act_fisica_s_3.setText("")
        self.Act_fisica_s_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Act_fisica_s_3.setObjectName("Act_fisica_s_3")
        self.verticalLayout_53.addWidget(self.Act_fisica_s_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_37.addWidget(self.fr_datap_s3_3)
        self.fr_datap_s4_3 = QtWidgets.QFrame(parent=self.fr_datapatient_s_3)
        self.fr_datap_s4_3.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s4_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s4_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s4_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s4_3.setObjectName("fr_datap_s4_3")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.fr_datap_s4_3)
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.fnacimiento_s_3 = QtWidgets.QLabel(parent=self.fr_datap_s4_3)
        self.fnacimiento_s_3.setMinimumSize(QtCore.QSize(160, 20))
        self.fnacimiento_s_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(9)
        self.fnacimiento_s_3.setFont(font)
        self.fnacimiento_s_3.setStyleSheet("")
        self.fnacimiento_s_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fnacimiento_s_3.setObjectName("fnacimiento_s_3")
        self.verticalLayout_54.addWidget(self.fnacimiento_s_3)
        self.edad_s_3 = QtWidgets.QLabel(parent=self.fr_datap_s4_3)
        self.edad_s_3.setMinimumSize(QtCore.QSize(150, 20))
        self.edad_s_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.edad_s_3.setFont(font)
        self.edad_s_3.setStyleSheet("")
        self.edad_s_3.setText("")
        self.edad_s_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.edad_s_3.setObjectName("edad_s_3")
        self.verticalLayout_54.addWidget(self.edad_s_3)
        self.horizontalLayout_37.addWidget(self.fr_datap_s4_3)
        self.verticalLayout_50.addWidget(self.fr_datapatient_s_3)
        self.verticalLayout_49.addWidget(self.fr_data_patient_s_3)
        self.label_2 = QtWidgets.QLabel(parent=self.grid_content)
        self.label_2.setGeometry(QtCore.QRect(50, 1140, 451, 20))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 61);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.grid_content)
        self.label_3.setGeometry(QtCore.QRect(710, 1140, 441, 20))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 61);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.grid_content)
        self.scroll_medidas.setWidget(self.scrollArea_medidas)
        self.verticalLayout_8.addWidget(self.scroll_medidas)
        self.ingresar_patient.addWidget(self.Mediciones_adulto)
        self.Mediciones_atleta = QtWidgets.QWidget()
        self.Mediciones_atleta.setObjectName("Mediciones_atleta")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Mediciones_atleta)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scroll_medidas_atleta = QtWidgets.QScrollArea(parent=self.Mediciones_atleta)
        self.scroll_medidas_atleta.setStyleSheet("QScrollArea {border: 0px solid;}")
        self.scroll_medidas_atleta.setWidgetResizable(True)
        self.scroll_medidas_atleta.setObjectName("scroll_medidas_atleta")
        self.scrollArea_medidas_atleta = QtWidgets.QWidget()
        self.scrollArea_medidas_atleta.setGeometry(QtCore.QRect(0, 0, 1205, 1720))
        self.scrollArea_medidas_atleta.setObjectName("scrollArea_medidas_atleta")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.scrollArea_medidas_atleta)
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.grid_content_atleta = QtWidgets.QFrame(parent=self.scrollArea_medidas_atleta)
        self.grid_content_atleta.setMinimumSize(QtCore.QSize(1000, 2600))
        self.grid_content_atleta.setMaximumSize(QtCore.QSize(16777215, 2600))
        self.grid_content_atleta.setStyleSheet("QTableWidget {\n"
                                               "background-color: rgb(255, 255, 255);\n"
                                               "}")
        self.grid_content_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.grid_content_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.grid_content_atleta.setObjectName("grid_content_atleta")
        self.table_medidas_atleta = QtWidgets.QTableWidget(parent=self.grid_content_atleta)
        self.table_medidas_atleta.setGeometry(QtCore.QRect(60, 320, 1101, 261))
        self.table_medidas_atleta.setMinimumSize(QtCore.QSize(0, 261))
        self.table_medidas_atleta.setMaximumSize(QtCore.QSize(16777215, 261))
        self.table_medidas_atleta.setStyleSheet("")
        self.table_medidas_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.table_medidas_atleta.setLineWidth(0)
        self.table_medidas_atleta.setMidLineWidth(0)
        self.table_medidas_atleta.setAlternatingRowColors(False)
        self.table_medidas_atleta.setShowGrid(True)
        self.table_medidas_atleta.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.table_medidas_atleta.setObjectName("table_medidas_atleta")
        self.table_medidas_atleta.setColumnCount(5)
        self.table_medidas_atleta.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_medidas_atleta.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_medidas_atleta.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_medidas_atleta.setItem(6, 4, item)
        self.table_medidas_atleta.horizontalHeader().setVisible(False)
        self.table_medidas_atleta.horizontalHeader().setDefaultSectionSize(214)
        self.table_medidas_atleta.horizontalHeader().setHighlightSections(True)
        self.table_medidas_atleta.horizontalHeader().setMinimumSectionSize(33)
        self.table_medidas_atleta.horizontalHeader().setStretchLastSection(True)
        self.table_medidas_atleta.verticalHeader().setVisible(False)
        self.table_medidas_atleta.verticalHeader().setDefaultSectionSize(37)
        self.table_medidas_atleta.verticalHeader().setHighlightSections(True)
        self.table_medidas_atleta.verticalHeader().setMinimumSectionSize(16)
        self.table_medidas_atleta.verticalHeader().setStretchLastSection(True)
        delegate = NumericDelegate(self.table_medidas_atleta)
        self.table_medidas_atleta.setItemDelegate(delegate)
        self.table_pliegues_cut_atleta = QtWidgets.QTableWidget(parent=self.grid_content_atleta)
        self.table_pliegues_cut_atleta.setGeometry(QtCore.QRect(60, 670, 1101, 335))
        self.table_pliegues_cut_atleta.setMinimumSize(QtCore.QSize(0, 335))
        self.table_pliegues_cut_atleta.setMaximumSize(QtCore.QSize(16777215, 335))
        self.table_pliegues_cut_atleta.setObjectName("table_pliegues_cut_atleta")
        self.table_pliegues_cut_atleta.setColumnCount(5)
        self.table_pliegues_cut_atleta.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_pliegues_cut_atleta.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_pliegues_cut_atleta.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_pliegues_cut_atleta.setItem(8, 4, item)
        self.table_pliegues_cut_atleta.horizontalHeader().setVisible(False)
        self.table_pliegues_cut_atleta.horizontalHeader().setDefaultSectionSize(216)
        self.table_pliegues_cut_atleta.horizontalHeader().setMinimumSectionSize(40)
        self.table_pliegues_cut_atleta.horizontalHeader().setStretchLastSection(True)
        self.table_pliegues_cut_atleta.verticalHeader().setVisible(False)
        self.table_pliegues_cut_atleta.verticalHeader().setDefaultSectionSize(37)
        self.table_pliegues_cut_atleta.verticalHeader().setHighlightSections(True)
        self.table_pliegues_cut_atleta.verticalHeader().setMinimumSectionSize(0)
        self.table_pliegues_cut_atleta.verticalHeader().setStretchLastSection(True)
        delegate = NumericDelegate(self.table_pliegues_cut_atleta)
        self.table_pliegues_cut_atleta.setItemDelegate(delegate)
        self.table_perife_circun_atleta = QtWidgets.QTableWidget(parent=self.grid_content_atleta)
        self.table_perife_circun_atleta.setGeometry(QtCore.QRect(60, 1090, 1101, 546))
        self.table_perife_circun_atleta.setMinimumSize(QtCore.QSize(852, 546))
        self.table_perife_circun_atleta.setMaximumSize(QtCore.QSize(1000000, 546))
        self.table_perife_circun_atleta.setRowCount(17)
        self.table_perife_circun_atleta.setColumnCount(5)
        self.table_perife_circun_atleta.setObjectName("table_perife_circun_atleta")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(8, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(9, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(9, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(10, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(10, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(11, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(11, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(12, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(12, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(12, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(12, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(13, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(13, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(13, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(13, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(14, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(14, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(14, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(14, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(15, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(15, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(15, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(15, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(16, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_perife_circun_atleta.setItem(16, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(16, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_perife_circun_atleta.setItem(16, 4, item)
        self.table_perife_circun_atleta.horizontalHeader().setVisible(False)
        self.table_perife_circun_atleta.horizontalHeader().setDefaultSectionSize(216)
        self.table_perife_circun_atleta.horizontalHeader().setStretchLastSection(True)
        self.table_perife_circun_atleta.verticalHeader().setVisible(False)
        self.table_perife_circun_atleta.verticalHeader().setDefaultSectionSize(32)
        self.table_perife_circun_atleta.verticalHeader().setStretchLastSection(True)
        delegate = NumericDelegate(self.table_perife_circun_atleta)
        self.table_perife_circun_atleta.setItemDelegate(delegate)
        self.table_longitud_alt_atleta = QtWidgets.QTableWidget(parent=self.grid_content_atleta)
        self.table_longitud_alt_atleta.setGeometry(QtCore.QRect(60, 1720, 1101, 335))
        self.table_longitud_alt_atleta.setMinimumSize(QtCore.QSize(852, 335))
        self.table_longitud_alt_atleta.setMaximumSize(QtCore.QSize(1000000, 335))
        self.table_longitud_alt_atleta.setRowCount(9)
        self.table_longitud_alt_atleta.setColumnCount(5)
        self.table_longitud_alt_atleta.setObjectName("table_longitud_alt_atleta")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_longitud_alt_atleta.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_longitud_alt_atleta.setItem(8, 4, item)
        self.table_longitud_alt_atleta.horizontalHeader().setVisible(False)
        self.table_longitud_alt_atleta.horizontalHeader().setDefaultSectionSize(216)
        self.table_longitud_alt_atleta.horizontalHeader().setMinimumSectionSize(40)
        self.table_longitud_alt_atleta.horizontalHeader().setStretchLastSection(True)
        self.table_longitud_alt_atleta.verticalHeader().setVisible(False)
        self.table_longitud_alt_atleta.verticalHeader().setDefaultSectionSize(37)
        self.table_longitud_alt_atleta.verticalHeader().setMinimumSectionSize(0)
        self.table_longitud_alt_atleta.verticalHeader().setStretchLastSection(True)
        delegate = NumericDelegate(self.table_longitud_alt_atleta)
        self.table_longitud_alt_atleta.setItemDelegate(delegate)
        self.info_longitudes_atleta = QtWidgets.QFrame(parent=self.grid_content_atleta)
        self.info_longitudes_atleta.setGeometry(QtCore.QRect(50, 1640, 1121, 71))
        self.info_longitudes_atleta.setStyleSheet("QFrame {\n"
                                                  "    background-color: rgb(0, 0, 61);\n"
                                                  "    border-radius: 15;\n"
                                                  "    color: white;\n"
                                                  "}")
        self.info_longitudes_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_longitudes_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_longitudes_atleta.setObjectName("info_longitudes_atleta")
        self.label_longitudes_atleta = QtWidgets.QLabel(parent=self.info_longitudes_atleta)
        self.label_longitudes_atleta.setGeometry(QtCore.QRect(30, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.label_longitudes_atleta.setFont(font)
        self.label_longitudes_atleta.setObjectName("label_longitudes_atleta")
        self.info_longitudes_atleta_2 = QtWidgets.QFrame(parent=self.grid_content_atleta)
        self.info_longitudes_atleta_2.setGeometry(QtCore.QRect(50, 2060, 1121, 71))
        self.info_longitudes_atleta_2.setStyleSheet("QFrame {\n"
                                                    "    background-color: rgb(0, 0, 61);\n"
                                                    "    border-radius: 15;\n"
                                                    "    color: white;\n"
                                                    "}")
        self.info_longitudes_atleta_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_longitudes_atleta_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_longitudes_atleta_2.setObjectName("info_longitudes_atleta_2")
        self.label_longitudes_atleta_2 = QtWidgets.QLabel(parent=self.info_longitudes_atleta_2)
        self.label_longitudes_atleta_2.setGeometry(QtCore.QRect(30, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.label_longitudes_atleta_2.setFont(font)
        self.label_longitudes_atleta_2.setObjectName("label_longitudes_atleta_2")
        self.table_diametros_atleta = QtWidgets.QTableWidget(parent=self.grid_content_atleta)
        self.table_diametros_atleta.setGeometry(QtCore.QRect(60, 2140, 1101, 335))
        self.table_diametros_atleta.setMinimumSize(QtCore.QSize(852, 335))
        self.table_diametros_atleta.setMaximumSize(QtCore.QSize(1000000, 335))
        self.table_diametros_atleta.setRowCount(8)
        self.table_diametros_atleta.setColumnCount(5)
        self.table_diametros_atleta.setObjectName("table_diametros_atleta")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 31))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_diametros_atleta.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_diametros_atleta.setItem(7, 4, item)
        self.table_diametros_atleta.horizontalHeader().setVisible(False)
        self.table_diametros_atleta.horizontalHeader().setDefaultSectionSize(216)
        self.table_diametros_atleta.horizontalHeader().setMinimumSectionSize(40)
        self.table_diametros_atleta.horizontalHeader().setStretchLastSection(True)
        self.table_diametros_atleta.verticalHeader().setVisible(False)
        self.table_diametros_atleta.verticalHeader().setDefaultSectionSize(42)
        self.table_diametros_atleta.verticalHeader().setMinimumSectionSize(0)
        self.table_diametros_atleta.verticalHeader().setStretchLastSection(True)
        delegate = NumericDelegate(self.table_diametros_atleta)
        self.table_diametros_atleta.setItemDelegate(delegate)
        self.info_medidas_atleta = QtWidgets.QFrame(parent=self.grid_content_atleta)
        self.info_medidas_atleta.setGeometry(QtCore.QRect(50, 240, 1121, 71))
        self.info_medidas_atleta.setStyleSheet("QFrame {\n"
                                               "    background-color: rgb(0, 0, 61);\n"
                                               "    border-radius: 15;\n"
                                               "    color: white;\n"
                                               "}")
        self.info_medidas_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_medidas_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_medidas_atleta.setObjectName("info_medidas_atleta")
        self.label_medidas_atleta = QtWidgets.QLabel(parent=self.info_medidas_atleta)
        self.label_medidas_atleta.setGeometry(QtCore.QRect(30, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.label_medidas_atleta.setFont(font)
        self.label_medidas_atleta.setObjectName("label_medidas_atleta")
        self.info_pliegues_atleta = QtWidgets.QFrame(parent=self.grid_content_atleta)
        self.info_pliegues_atleta.setGeometry(QtCore.QRect(50, 590, 1121, 71))
        self.info_pliegues_atleta.setStyleSheet("QFrame {\n"
                                                "    background-color: rgb(0, 0, 61);\n"
                                                "    border-radius: 15;\n"
                                                "    color: white;\n"
                                                "}")
        self.info_pliegues_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_pliegues_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_pliegues_atleta.setObjectName("info_pliegues_atleta")
        self.label_pliegues_atleta = QtWidgets.QLabel(parent=self.info_pliegues_atleta)
        self.label_pliegues_atleta.setGeometry(QtCore.QRect(30, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.label_pliegues_atleta.setFont(font)
        self.label_pliegues_atleta.setObjectName("label_pliegues_atleta")
        self.info_perimetros_atleta = QtWidgets.QFrame(parent=self.grid_content_atleta)
        self.info_perimetros_atleta.setGeometry(QtCore.QRect(50, 1010, 1121, 71))
        self.info_perimetros_atleta.setStyleSheet("QFrame {\n"
                                                  "    background-color: rgb(0, 0, 61);\n"
                                                  "    border-radius: 15;\n"
                                                  "    color: white;\n"
                                                  "}")
        self.info_perimetros_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_perimetros_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_perimetros_atleta.setObjectName("info_perimetros_atleta")
        self.label_perimetros_atleta = QtWidgets.QLabel(parent=self.info_perimetros_atleta)
        self.label_perimetros_atleta.setGeometry(QtCore.QRect(30, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.label_perimetros_atleta.setFont(font)
        self.label_perimetros_atleta.setObjectName("label_perimetros_atleta")
        self.btn_guardar_medidas_atleta = QtWidgets.QPushButton(parent=self.grid_content_atleta)
        self.btn_guardar_medidas_atleta.setGeometry(QtCore.QRect(530, 2500, 150, 50))
        self.btn_guardar_medidas_atleta.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_guardar_medidas_atleta.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(12)
        self.btn_guardar_medidas_atleta.setFont(font)
        self.btn_guardar_medidas_atleta.setStyleSheet("QPushButton {\n"
                                                      "background-color: rgb(0, 0, 61);\n"
                                                      "color: rgb(255, 255, 255);\n"
                                                      "border: 1px solid white;\n"
                                                      "border-radius: 10px;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QPushButton:hover {\n"
                                                      "background-color: rgb(0, 0, 31);\n"
                                                      "color: white;\n"
                                                      "}")
        self.btn_guardar_medidas_atleta.setObjectName("btn_guardar_medidas_atleta")
        self.data_title_patient_s_atleta = QtWidgets.QFrame(parent=self.grid_content_atleta)
        self.data_title_patient_s_atleta.setGeometry(QtCore.QRect(230, 10, 840, 200))
        self.data_title_patient_s_atleta.setMinimumSize(QtCore.QSize(840, 200))
        self.data_title_patient_s_atleta.setMaximumSize(QtCore.QSize(1000, 500))
        self.data_title_patient_s_atleta.setStyleSheet("#data_title_patient_s_2 {\n"
                                                       "    border: 1px solid black;\n"
                                                       "    font: 450 10pt \"Circular Std\";\n"
                                                       "}\n"
                                                       "\n"
                                                       "QFrame {\n"
                                                       "    background-color: rgb(221, 226, 249);\n"
                                                       "    border-radius: 10;\n"
                                                       "}")
        self.data_title_patient_s_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.data_title_patient_s_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.data_title_patient_s_atleta.setObjectName("data_title_patient_s_atleta")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.data_title_patient_s_atleta)
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_57.setSpacing(2)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.fr_photo_patient_s_atleta = QtWidgets.QFrame(parent=self.data_title_patient_s_atleta)
        self.fr_photo_patient_s_atleta.setMaximumSize(QtCore.QSize(16777215, 80))
        self.fr_photo_patient_s_atleta.setStyleSheet("background-color: rgb(0, 0, 61);")
        self.fr_photo_patient_s_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_photo_patient_s_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_photo_patient_s_atleta.setObjectName("fr_photo_patient_s_atleta")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.fr_photo_patient_s_atleta)
        self.horizontalLayout_38.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_38.setSpacing(21)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.photo_patient_s_atleta = QtWidgets.QLabel(parent=self.fr_photo_patient_s_atleta)
        self.photo_patient_s_atleta.setMinimumSize(QtCore.QSize(60, 60))
        self.photo_patient_s_atleta.setMaximumSize(QtCore.QSize(60, 60))
        self.photo_patient_s_atleta.setStyleSheet("border: 2px solid;\n"
                                                  "border-color: white;")
        self.photo_patient_s_atleta.setText("")
        self.photo_patient_s_atleta.setPixmap(QtGui.QPixmap("../.designer/PycharmProjects/Tesis/images/foto-p.png"))
        self.photo_patient_s_atleta.setScaledContents(True)
        self.photo_patient_s_atleta.setObjectName("photo_patient_s_atleta")
        self.horizontalLayout_38.addWidget(self.photo_patient_s_atleta, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_57.addWidget(self.fr_photo_patient_s_atleta)
        self.fr_data_patient_s_atleta = QtWidgets.QFrame(parent=self.data_title_patient_s_atleta)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fr_data_patient_s_atleta.setFont(font)
        self.fr_data_patient_s_atleta.setStyleSheet("#fr_data_patient_s {\n"
                                                    "border: 3px solid;\n"
                                                    "border-radius: 5px;\n"
                                                    "border-color: rgb(0, 0, 31);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QFrame {\n"
                                                    "background-color: white;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QLabel {\n"
                                                    "background-color: white;\n"
                                                    "color: rgb(0, 0, 31);\n"
                                                    "}")
        self.fr_data_patient_s_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_data_patient_s_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_data_patient_s_atleta.setObjectName("fr_data_patient_s_atleta")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout(self.fr_data_patient_s_atleta)
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.fr_name_s_atleta = QtWidgets.QFrame(parent=self.fr_data_patient_s_atleta)
        self.fr_name_s_atleta.setMinimumSize(QtCore.QSize(0, 40))
        self.fr_name_s_atleta.setMaximumSize(QtCore.QSize(16777215, 40))
        self.fr_name_s_atleta.setStyleSheet("")
        self.fr_name_s_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_name_s_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_name_s_atleta.setObjectName("fr_name_s_atleta")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.fr_name_s_atleta)
        self.horizontalLayout_39.setSpacing(6)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.nombrec_s_atleta_2 = QtWidgets.QLabel(parent=self.fr_name_s_atleta)
        self.nombrec_s_atleta_2.setMinimumSize(QtCore.QSize(200, 20))
        self.nombrec_s_atleta_2.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.nombrec_s_atleta_2.setFont(font)
        self.nombrec_s_atleta_2.setStyleSheet("border-bottom: 2px solid;\n"
                                              "border-radius: 30px;\n"
                                              "border-color: rgb(0, 0, 31);")
        self.nombrec_s_atleta_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombrec_s_atleta_2.setObjectName("nombrec_s_atleta_2")
        self.horizontalLayout_39.addWidget(self.nombrec_s_atleta_2)
        self.verticalLayout_58.addWidget(self.fr_name_s_atleta)
        self.fr_datapatient_s_atleta = QtWidgets.QFrame(parent=self.fr_data_patient_s_atleta)
        self.fr_datapatient_s_atleta.setStyleSheet("")
        self.fr_datapatient_s_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datapatient_s_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datapatient_s_atleta.setObjectName("fr_datapatient_s_atleta")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.fr_datapatient_s_atleta)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.fr_datap_s1_atleta = QtWidgets.QFrame(parent=self.fr_datapatient_s_atleta)
        self.fr_datap_s1_atleta.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s1_atleta.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s1_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s1_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s1_atleta.setObjectName("fr_datap_s1_atleta")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout(self.fr_datap_s1_atleta)
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.documento_s_atleta = QtWidgets.QLabel(parent=self.fr_datap_s1_atleta)
        self.documento_s_atleta.setMinimumSize(QtCore.QSize(150, 20))
        self.documento_s_atleta.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(8)
        self.documento_s_atleta.setFont(font)
        self.documento_s_atleta.setStyleSheet("")
        self.documento_s_atleta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.documento_s_atleta.setObjectName("documento_s_atleta")
        self.verticalLayout_59.addWidget(self.documento_s_atleta)
        self.tipo_patient_s_atleta = QtWidgets.QLabel(parent=self.fr_datap_s1_atleta)
        self.tipo_patient_s_atleta.setMinimumSize(QtCore.QSize(150, 20))
        self.tipo_patient_s_atleta.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.tipo_patient_s_atleta.setFont(font)
        self.tipo_patient_s_atleta.setStyleSheet("")
        self.tipo_patient_s_atleta.setText("")
        self.tipo_patient_s_atleta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tipo_patient_s_atleta.setObjectName("tipo_patient_s_atleta")
        self.verticalLayout_59.addWidget(self.tipo_patient_s_atleta, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_40.addWidget(self.fr_datap_s1_atleta)
        self.fr_datap_s2_atleta = QtWidgets.QFrame(parent=self.fr_datapatient_s_atleta)
        self.fr_datap_s2_atleta.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s2_atleta.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s2_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s2_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s2_atleta.setObjectName("fr_datap_s2_atleta")
        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.fr_datap_s2_atleta)
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.sexo_s_atleta = QtWidgets.QLabel(parent=self.fr_datap_s2_atleta)
        self.sexo_s_atleta.setMinimumSize(QtCore.QSize(150, 20))
        self.sexo_s_atleta.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(8)
        self.sexo_s_atleta.setFont(font)
        self.sexo_s_atleta.setStyleSheet("")
        self.sexo_s_atleta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sexo_s_atleta.setObjectName("sexo_s_atleta")
        self.verticalLayout_60.addWidget(self.sexo_s_atleta, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.nombrec_s_atleta = QtWidgets.QLabel(parent=self.fr_datap_s2_atleta)
        self.nombrec_s_atleta.setMinimumSize(QtCore.QSize(150, 20))
        self.nombrec_s_atleta.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.nombrec_s_atleta.setFont(font)
        self.nombrec_s_atleta.setStyleSheet("")
        self.nombrec_s_atleta.setText("")
        self.nombrec_s_atleta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombrec_s_atleta.setObjectName("nombrec_s_atleta")
        self.verticalLayout_60.addWidget(self.nombrec_s_atleta)
        self.horizontalLayout_40.addWidget(self.fr_datap_s2_atleta)
        self.fr_datap_s3_atleta = QtWidgets.QFrame(parent=self.fr_datapatient_s_atleta)
        self.fr_datap_s3_atleta.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s3_atleta.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s3_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s3_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s3_atleta.setObjectName("fr_datap_s3_atleta")
        self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.fr_datap_s3_atleta)
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.telf_s_atleta = QtWidgets.QLabel(parent=self.fr_datap_s3_atleta)
        self.telf_s_atleta.setMinimumSize(QtCore.QSize(150, 20))
        self.telf_s_atleta.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(8)
        self.telf_s_atleta.setFont(font)
        self.telf_s_atleta.setStyleSheet("")
        self.telf_s_atleta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.telf_s_atleta.setObjectName("telf_s_atleta")
        self.verticalLayout_61.addWidget(self.telf_s_atleta)
        self.Act_fisica_s_atleta = QtWidgets.QLabel(parent=self.fr_datap_s3_atleta)
        self.Act_fisica_s_atleta.setMinimumSize(QtCore.QSize(150, 20))
        self.Act_fisica_s_atleta.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.Act_fisica_s_atleta.setFont(font)
        self.Act_fisica_s_atleta.setStyleSheet("")
        self.Act_fisica_s_atleta.setText("")
        self.Act_fisica_s_atleta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Act_fisica_s_atleta.setObjectName("Act_fisica_s_atleta")
        self.verticalLayout_61.addWidget(self.Act_fisica_s_atleta, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_40.addWidget(self.fr_datap_s3_atleta)
        self.fr_datap_s4_atleta = QtWidgets.QFrame(parent=self.fr_datapatient_s_atleta)
        self.fr_datap_s4_atleta.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s4_atleta.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s4_atleta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s4_atleta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s4_atleta.setObjectName("fr_datap_s4_atleta")
        self.verticalLayout_62 = QtWidgets.QVBoxLayout(self.fr_datap_s4_atleta)
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.fnacimiento_s_atleta = QtWidgets.QLabel(parent=self.fr_datap_s4_atleta)
        self.fnacimiento_s_atleta.setMinimumSize(QtCore.QSize(160, 20))
        self.fnacimiento_s_atleta.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(8)
        self.fnacimiento_s_atleta.setFont(font)
        self.fnacimiento_s_atleta.setStyleSheet("")
        self.fnacimiento_s_atleta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fnacimiento_s_atleta.setObjectName("fnacimiento_s_atleta")
        self.verticalLayout_62.addWidget(self.fnacimiento_s_atleta)
        self.edad_s_atleta = QtWidgets.QLabel(parent=self.fr_datap_s4_atleta)
        self.edad_s_atleta.setMinimumSize(QtCore.QSize(150, 20))
        self.edad_s_atleta.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.edad_s_atleta.setFont(font)
        self.edad_s_atleta.setStyleSheet("")
        self.edad_s_atleta.setText("")
        self.edad_s_atleta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.edad_s_atleta.setObjectName("edad_s_atleta")
        self.verticalLayout_62.addWidget(self.edad_s_atleta)
        self.horizontalLayout_40.addWidget(self.fr_datap_s4_atleta)
        self.verticalLayout_58.addWidget(self.fr_datapatient_s_atleta)
        self.verticalLayout_57.addWidget(self.fr_data_patient_s_atleta)
        self.label_4 = QtWidgets.QLabel(parent=self.grid_content_atleta)
        self.label_4.setGeometry(QtCore.QRect(60, 2520, 451, 20))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 61);\n"
                                   "border-radius: 2px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.grid_content_atleta)
        self.label_5.setGeometry(QtCore.QRect(700, 2520, 461, 20))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 61);\n"
                                   "border-radius: 2px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_56.addWidget(self.grid_content_atleta)
        self.scroll_medidas_atleta.setWidget(self.scrollArea_medidas_atleta)
        self.horizontalLayout_2.addWidget(self.scroll_medidas_atleta)
        self.ingresar_patient.addWidget(self.Mediciones_atleta)
        self.Salida = QtWidgets.QWidget()
        self.Salida.setObjectName("Salida")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Salida)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.fr_salida = QtWidgets.QFrame(parent=self.Salida)
        self.fr_salida.setMinimumSize(QtCore.QSize(0, 0))
        self.fr_salida.setMaximumSize(QtCore.QSize(16777215, 780))
        self.fr_salida.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_salida.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_salida.setObjectName("fr_salida")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.fr_salida)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.fr_datos_patient_s = QtWidgets.QFrame(parent=self.fr_salida)
        self.fr_datos_patient_s.setMinimumSize(QtCore.QSize(0, 200))
        self.fr_datos_patient_s.setMaximumSize(QtCore.QSize(16777215, 200))
        self.fr_datos_patient_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datos_patient_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datos_patient_s.setObjectName("fr_datos_patient_s")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.fr_datos_patient_s)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.hora_s = QtWidgets.QLabel(parent=self.fr_datos_patient_s)
        self.hora_s.setMinimumSize(QtCore.QSize(90, 60))
        self.hora_s.setMaximumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.hora_s.setFont(font)
        self.hora_s.setStyleSheet("background-color: white;\n"
                                  "color: rgb(0, 0, 31);\n"
                                  "border: 3px solid;\n"
                                  "border-radius: 5px;\n"
                                  "border-color: rgb(0, 0, 31);\n"
                                  "")
        self.hora_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hora_s.setObjectName("hora_s")
        self.horizontalLayout_16.addWidget(self.hora_s)
        self.data_title_patient_s = QtWidgets.QFrame(parent=self.fr_datos_patient_s)
        self.data_title_patient_s.setMinimumSize(QtCore.QSize(500, 200))
        self.data_title_patient_s.setMaximumSize(QtCore.QSize(1000, 200))
        self.data_title_patient_s.setStyleSheet("#data_title_patient {\n"
                                                "border: 1px solid;\n"
                                                "border-radius: 5px;\n"
                                                "border-color: rgb(0, 0, 61);\n"
                                                "}\n"
                                                "\n"
                                                "QFrame {\n"
                                                "background-color: rgb(221, 226, 249);\n"
                                                "}")
        self.data_title_patient_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.data_title_patient_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.data_title_patient_s.setObjectName("data_title_patient_s")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.data_title_patient_s)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.fr_photo_patient_s = QtWidgets.QFrame(parent=self.data_title_patient_s)
        self.fr_photo_patient_s.setMaximumSize(QtCore.QSize(16777215, 80))
        self.fr_photo_patient_s.setStyleSheet("background-color: rgb(0, 0, 31)")
        self.fr_photo_patient_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_photo_patient_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_photo_patient_s.setObjectName("fr_photo_patient_s")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fr_photo_patient_s)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.photo_patient_s = QtWidgets.QLabel(parent=self.fr_photo_patient_s)
        self.photo_patient_s.setMinimumSize(QtCore.QSize(60, 60))
        self.photo_patient_s.setMaximumSize(QtCore.QSize(60, 60))
        self.photo_patient_s.setStyleSheet("border: 2px solid;\n"
                                           "border-color: white;")
        self.photo_patient_s.setText("")
        self.photo_patient_s.setPixmap(QtGui.QPixmap("images/foto-p.png"))
        self.photo_patient_s.setScaledContents(True)
        self.photo_patient_s.setObjectName("photo_patient_s")
        self.horizontalLayout_7.addWidget(self.photo_patient_s, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_13.addWidget(self.fr_photo_patient_s)
        self.fr_data_patient_s = QtWidgets.QFrame(parent=self.data_title_patient_s)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fr_data_patient_s.setFont(font)
        self.fr_data_patient_s.setStyleSheet("#fr_data_patient_s {\n"
                                             "border: 3px solid;\n"
                                             "border-radius: 5px;\n"
                                             "border-color: rgb(0, 0, 31);\n"
                                             "}\n"
                                             "\n"
                                             "QFrame {\n"
                                             "background-color: white;\n"
                                             "}\n"
                                             "\n"
                                             "QLabel {\n"
                                             "background-color: white;\n"
                                             "color: rgb(0, 0, 31);\n"
                                             "}")
        self.fr_data_patient_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_data_patient_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_data_patient_s.setObjectName("fr_data_patient_s")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.fr_data_patient_s)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.fr_name_s = QtWidgets.QFrame(parent=self.fr_data_patient_s)
        self.fr_name_s.setMinimumSize(QtCore.QSize(0, 40))
        self.fr_name_s.setMaximumSize(QtCore.QSize(16777215, 40))
        self.fr_name_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_name_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_name_s.setObjectName("fr_name_s")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.fr_name_s)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.nombrec_s = QtWidgets.QLabel(parent=self.fr_name_s)
        self.nombrec_s.setMinimumSize(QtCore.QSize(200, 20))
        self.nombrec_s.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.nombrec_s.setFont(font)
        self.nombrec_s.setStyleSheet("border-bottom: 2px solid;\n"
                                     "border-radius: 30px;\n"
                                     "border-color: rgb(0, 0, 31);")
        self.nombrec_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombrec_s.setObjectName("nombrec_s")
        self.horizontalLayout_14.addWidget(self.nombrec_s)
        self.verticalLayout_14.addWidget(self.fr_name_s)
        self.fr_datapatient_s = QtWidgets.QFrame(parent=self.fr_data_patient_s)
        self.fr_datapatient_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datapatient_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datapatient_s.setObjectName("fr_datapatient_s")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.fr_datapatient_s)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.fr_datap_s1 = QtWidgets.QFrame(parent=self.fr_datapatient_s)
        self.fr_datap_s1.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s1.setObjectName("fr_datap_s1")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.fr_datap_s1)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.documento_s = QtWidgets.QLabel(parent=self.fr_datap_s1)
        self.documento_s.setMinimumSize(QtCore.QSize(150, 20))
        self.documento_s.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.documento_s.setFont(font)
        self.documento_s.setStyleSheet("")
        self.documento_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.documento_s.setObjectName("documento_s")
        self.verticalLayout_15.addWidget(self.documento_s, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.tipo_patient_s = QtWidgets.QLabel(parent=self.fr_datap_s1)
        self.tipo_patient_s.setMinimumSize(QtCore.QSize(150, 20))
        self.tipo_patient_s.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.tipo_patient_s.setFont(font)
        self.tipo_patient_s.setStyleSheet("")
        self.tipo_patient_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tipo_patient_s.setObjectName("tipo_patient_s")
        self.verticalLayout_15.addWidget(self.tipo_patient_s, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_15.addWidget(self.fr_datap_s1)
        self.fr_datap_s2 = QtWidgets.QFrame(parent=self.fr_datapatient_s)
        self.fr_datap_s2.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s2.setObjectName("fr_datap_s2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.fr_datap_s2)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.sexo_s = QtWidgets.QLabel(parent=self.fr_datap_s2)
        self.sexo_s.setMinimumSize(QtCore.QSize(150, 20))
        self.sexo_s.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.sexo_s.setFont(font)
        self.sexo_s.setStyleSheet("")
        self.sexo_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sexo_s.setObjectName("sexo_s")
        self.verticalLayout_16.addWidget(self.sexo_s, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.nombrec_s_5 = QtWidgets.QLabel(parent=self.fr_datap_s2)
        self.nombrec_s_5.setMinimumSize(QtCore.QSize(150, 20))
        self.nombrec_s_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.nombrec_s_5.setFont(font)
        self.nombrec_s_5.setStyleSheet("")
        self.nombrec_s_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombrec_s_5.setObjectName("nombrec_s_5")
        self.verticalLayout_16.addWidget(self.nombrec_s_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_15.addWidget(self.fr_datap_s2)
        self.fr_datap_s3 = QtWidgets.QFrame(parent=self.fr_datapatient_s)
        self.fr_datap_s3.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s3.setObjectName("fr_datap_s3")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.fr_datap_s3)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.telf_s = QtWidgets.QLabel(parent=self.fr_datap_s3)
        self.telf_s.setMinimumSize(QtCore.QSize(150, 20))
        self.telf_s.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.telf_s.setFont(font)
        self.telf_s.setStyleSheet("")
        self.telf_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.telf_s.setObjectName("telf_s")
        self.verticalLayout_36.addWidget(self.telf_s, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.Act_fisica_s = QtWidgets.QLabel(parent=self.fr_datap_s3)
        self.Act_fisica_s.setMinimumSize(QtCore.QSize(150, 20))
        self.Act_fisica_s.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.Act_fisica_s.setFont(font)
        self.Act_fisica_s.setStyleSheet("")
        self.Act_fisica_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Act_fisica_s.setObjectName("Act_fisica_s")
        self.verticalLayout_36.addWidget(self.Act_fisica_s, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_15.addWidget(self.fr_datap_s3)
        self.fr_datap_s4 = QtWidgets.QFrame(parent=self.fr_datapatient_s)
        self.fr_datap_s4.setMinimumSize(QtCore.QSize(170, 0))
        self.fr_datap_s4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fr_datap_s4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_datap_s4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_datap_s4.setObjectName("fr_datap_s4")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.fr_datap_s4)
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.fnacimiento_s = QtWidgets.QLabel(parent=self.fr_datap_s4)
        self.fnacimiento_s.setMinimumSize(QtCore.QSize(160, 20))
        self.fnacimiento_s.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.fnacimiento_s.setFont(font)
        self.fnacimiento_s.setStyleSheet("")
        self.fnacimiento_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fnacimiento_s.setObjectName("fnacimiento_s")
        self.verticalLayout_37.addWidget(self.fnacimiento_s)
        self.edad_s = QtWidgets.QLabel(parent=self.fr_datap_s4)
        self.edad_s.setMinimumSize(QtCore.QSize(150, 20))
        self.edad_s.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.edad_s.setFont(font)
        self.edad_s.setStyleSheet("")
        self.edad_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.edad_s.setObjectName("edad_s")
        self.verticalLayout_37.addWidget(self.edad_s)
        self.horizontalLayout_15.addWidget(self.fr_datap_s4)
        self.verticalLayout_14.addWidget(self.fr_datapatient_s)
        self.verticalLayout_13.addWidget(self.fr_data_patient_s)
        self.horizontalLayout_16.addWidget(self.data_title_patient_s)
        self.fecha_s = QtWidgets.QLabel(parent=self.fr_datos_patient_s)
        self.fecha_s.setMinimumSize(QtCore.QSize(90, 60))
        self.fecha_s.setMaximumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.fecha_s.setFont(font)
        self.fecha_s.setStyleSheet("background-color: white;\n"
                                   "color: rgb(0, 0, 31);\n"
                                   "border: 3px solid;\n"
                                   "border-radius: 5px;\n"
                                   "border-color: rgb(0, 0, 31);\n"
                                   "")
        self.fecha_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fecha_s.setObjectName("fecha_s")
        self.horizontalLayout_16.addWidget(self.fecha_s)
        self.verticalLayout_12.addWidget(self.fr_datos_patient_s, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.fr_calculos = QtWidgets.QFrame(parent=self.fr_salida)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_calculos.sizePolicy().hasHeightForWidth())
        self.fr_calculos.setSizePolicy(sizePolicy)
        self.fr_calculos.setMinimumSize(QtCore.QSize(0, 370))
        self.fr_calculos.setMaximumSize(QtCore.QSize(16777215, 370))
        self.fr_calculos.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_calculos.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_calculos.setObjectName("fr_calculos")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.fr_calculos)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fr_seccion_s = QtWidgets.QFrame(parent=self.fr_calculos)
        self.fr_seccion_s.setMinimumSize(QtCore.QSize(800, 0))
        self.fr_seccion_s.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.fr_seccion_s.setStyleSheet("#fr_seccion_s {\n"
                                        "border: 3px solid;\n"
                                        "border-radius: 5px;\n"
                                        "border-color: rgb(0, 0, 31);\n"
                                        "}\n"
                                        "\n"
                                        "QFrame {\n"
                                        "background-color: white;\n"
                                        "}")
        self.fr_seccion_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_seccion_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_seccion_s.setObjectName("fr_seccion_s")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.fr_seccion_s)
        self.verticalLayout_39.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.fr_title_s = QtWidgets.QFrame(parent=self.fr_seccion_s)
        self.fr_title_s.setMinimumSize(QtCore.QSize(0, 40))
        self.fr_title_s.setMaximumSize(QtCore.QSize(16777215, 40))
        self.fr_title_s.setStyleSheet("background-color: rgb(0, 0, 31);\n"
                                      "border-radius: 5px;")
        self.fr_title_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_title_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_title_s.setObjectName("fr_title_s")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.fr_title_s)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lbl_title_cal_s = QtWidgets.QLabel(parent=self.fr_title_s)
        self.lbl_title_cal_s.setMinimumSize(QtCore.QSize(848, 20))
        self.lbl_title_cal_s.setMaximumSize(QtCore.QSize(848, 16777215))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_title_cal_s.setFont(font)
        self.lbl_title_cal_s.setStyleSheet("color: white;")
        self.lbl_title_cal_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_title_cal_s.setObjectName("lbl_title_cal_s")
        self.horizontalLayout_17.addWidget(self.lbl_title_cal_s)
        self.verticalLayout_39.addWidget(self.fr_title_s)
        self.fr_content_s = QtWidgets.QFrame(parent=self.fr_seccion_s)
        self.fr_content_s.setStyleSheet("#fr_content_s {\n"
                                        "background-color: rgb(72, 18, 178);\n"
                                        "border-radius: 5px;\n"
                                        "}")
        self.fr_content_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_content_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_content_s.setObjectName("fr_content_s")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.fr_content_s)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.fr_salida1 = QtWidgets.QFrame(parent=self.fr_content_s)
        self.fr_salida1.setStyleSheet("#fr_salida1 {\n"
                                      "background-color: rgb(0, 0, 61);\n"
                                      "border: 1px solid;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: rgb(0, 0, 31);\n"
                                      "}")
        self.fr_salida1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_salida1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_salida1.setObjectName("fr_salida1")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.fr_salida1)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.fr_imc = QtWidgets.QFrame(parent=self.fr_salida1)
        self.fr_imc.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_imc.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_imc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_imc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_imc.setObjectName("fr_imc")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.fr_imc)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lbl_icon = QtWidgets.QLabel(parent=self.fr_imc)
        self.lbl_icon.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon.setText("")
        self.lbl_icon.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon.setScaledContents(True)
        self.lbl_icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon.setObjectName("lbl_icon")
        self.horizontalLayout_19.addWidget(self.lbl_icon)
        self.lbl_imc = QtWidgets.QLabel(parent=self.fr_imc)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_imc.setFont(font)
        self.lbl_imc.setObjectName("lbl_imc")
        self.horizontalLayout_19.addWidget(self.lbl_imc)
        self.verticalLayout_38.addWidget(self.fr_imc)
        self.fr_icc = QtWidgets.QFrame(parent=self.fr_salida1)
        self.fr_icc.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_icc.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_icc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_icc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_icc.setObjectName("fr_icc")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.fr_icc)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lbl_icon_2 = QtWidgets.QLabel(parent=self.fr_icc)
        self.lbl_icon_2.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon_2.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon_2.setText("")
        self.lbl_icon_2.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon_2.setScaledContents(True)
        self.lbl_icon_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon_2.setObjectName("lbl_icon_2")
        self.horizontalLayout_20.addWidget(self.lbl_icon_2)
        self.lbl_icc = QtWidgets.QLabel(parent=self.fr_icc)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_icc.setFont(font)
        self.lbl_icc.setObjectName("lbl_icc")
        self.horizontalLayout_20.addWidget(self.lbl_icc)
        self.verticalLayout_38.addWidget(self.fr_icc)
        self.fr_ice = QtWidgets.QFrame(parent=self.fr_salida1)
        self.fr_ice.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_ice.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_ice.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_ice.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_ice.setObjectName("fr_ice")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.fr_ice)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.lbl_icon_3 = QtWidgets.QLabel(parent=self.fr_ice)
        self.lbl_icon_3.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon_3.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon_3.setText("")
        self.lbl_icon_3.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon_3.setScaledContents(True)
        self.lbl_icon_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon_3.setObjectName("lbl_icon_3")
        self.horizontalLayout_21.addWidget(self.lbl_icon_3)
        self.lbl_ice = QtWidgets.QLabel(parent=self.fr_ice)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_ice.setFont(font)
        self.lbl_ice.setObjectName("lbl_ice")
        self.horizontalLayout_21.addWidget(self.lbl_ice)
        self.verticalLayout_38.addWidget(self.fr_ice)
        self.fr_porcent_grasa = QtWidgets.QFrame(parent=self.fr_salida1)
        self.fr_porcent_grasa.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_porcent_grasa.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_porcent_grasa.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_porcent_grasa.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_porcent_grasa.setObjectName("fr_porcent_grasa")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.fr_porcent_grasa)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.lbl_icon_4 = QtWidgets.QLabel(parent=self.fr_porcent_grasa)
        self.lbl_icon_4.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon_4.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon_4.setText("")
        self.lbl_icon_4.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon_4.setScaledContents(True)
        self.lbl_icon_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon_4.setObjectName("lbl_icon_4")
        self.horizontalLayout_22.addWidget(self.lbl_icon_4)
        self.lbl_porcent_grasa = QtWidgets.QLabel(parent=self.fr_porcent_grasa)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_porcent_grasa.setFont(font)
        self.lbl_porcent_grasa.setObjectName("lbl_porcent_grasa")
        self.horizontalLayout_22.addWidget(self.lbl_porcent_grasa)
        self.verticalLayout_38.addWidget(self.fr_porcent_grasa)
        self.horizontalLayout_18.addWidget(self.fr_salida1)
        self.fr_salida2 = QtWidgets.QFrame(parent=self.fr_content_s)
        self.fr_salida2.setStyleSheet("#fr_salida2 {\n"
                                      "background-color: rgb(0, 0, 61);\n"
                                      "border: 1px solid;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: rgb(0, 0, 31);\n"
                                      "}")
        self.fr_salida2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_salida2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_salida2.setObjectName("fr_salida2")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.fr_salida2)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.fr_pde_grasa = QtWidgets.QFrame(parent=self.fr_salida2)
        self.fr_pde_grasa.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_pde_grasa.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_pde_grasa.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_pde_grasa.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_pde_grasa.setObjectName("fr_pde_grasa")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.fr_pde_grasa)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.lbl_icon_5 = QtWidgets.QLabel(parent=self.fr_pde_grasa)
        self.lbl_icon_5.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon_5.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon_5.setText("")
        self.lbl_icon_5.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon_5.setScaledContents(True)
        self.lbl_icon_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon_5.setObjectName("lbl_icon_5")
        self.horizontalLayout_23.addWidget(self.lbl_icon_5)
        self.lbl_p_degrasa = QtWidgets.QLabel(parent=self.fr_pde_grasa)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_p_degrasa.setFont(font)
        self.lbl_p_degrasa.setObjectName("lbl_p_degrasa")
        self.horizontalLayout_23.addWidget(self.lbl_p_degrasa)
        self.verticalLayout_40.addWidget(self.fr_pde_grasa)
        self.fr_p_degrasa_percentil = QtWidgets.QFrame(parent=self.fr_salida2)
        self.fr_p_degrasa_percentil.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_p_degrasa_percentil.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_p_degrasa_percentil.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_p_degrasa_percentil.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_p_degrasa_percentil.setObjectName("fr_p_degrasa_percentil")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.fr_p_degrasa_percentil)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.lbl_icon_6 = QtWidgets.QLabel(parent=self.fr_p_degrasa_percentil)
        self.lbl_icon_6.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon_6.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon_6.setText("")
        self.lbl_icon_6.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon_6.setScaledContents(True)
        self.lbl_icon_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon_6.setObjectName("lbl_icon_6")
        self.horizontalLayout_24.addWidget(self.lbl_icon_6)
        self.lbl_p_degrasa_percentil = QtWidgets.QLabel(parent=self.fr_p_degrasa_percentil)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_p_degrasa_percentil.setFont(font)
        self.lbl_p_degrasa_percentil.setObjectName("lbl_p_degrasa_percentil")
        self.horizontalLayout_24.addWidget(self.lbl_p_degrasa_percentil)
        self.verticalLayout_40.addWidget(self.fr_p_degrasa_percentil)
        self.fr_indice_mlg = QtWidgets.QFrame(parent=self.fr_salida2)
        self.fr_indice_mlg.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_indice_mlg.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_indice_mlg.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_indice_mlg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_indice_mlg.setObjectName("fr_indice_mlg")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.fr_indice_mlg)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.lbl_icon_7 = QtWidgets.QLabel(parent=self.fr_indice_mlg)
        self.lbl_icon_7.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon_7.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon_7.setText("")
        self.lbl_icon_7.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon_7.setScaledContents(True)
        self.lbl_icon_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon_7.setObjectName("lbl_icon_7")
        self.horizontalLayout_25.addWidget(self.lbl_icon_7)
        self.lbl_indice_mlg = QtWidgets.QLabel(parent=self.fr_indice_mlg)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_indice_mlg.setFont(font)
        self.lbl_indice_mlg.setObjectName("lbl_indice_mlg")
        self.horizontalLayout_25.addWidget(self.lbl_indice_mlg)
        self.verticalLayout_40.addWidget(self.fr_indice_mlg)
        self.fr_camb = QtWidgets.QFrame(parent=self.fr_salida2)
        self.fr_camb.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_camb.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_camb.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_camb.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_camb.setObjectName("fr_camb")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.fr_camb)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.lbl_icon_8 = QtWidgets.QLabel(parent=self.fr_camb)
        self.lbl_icon_8.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon_8.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon_8.setText("")
        self.lbl_icon_8.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon_8.setScaledContents(True)
        self.lbl_icon_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon_8.setObjectName("lbl_icon_8")
        self.horizontalLayout_26.addWidget(self.lbl_icon_8)
        self.lbl_camb = QtWidgets.QLabel(parent=self.fr_camb)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_camb.setFont(font)
        self.lbl_camb.setObjectName("lbl_camb")
        self.horizontalLayout_26.addWidget(self.lbl_camb)
        self.verticalLayout_40.addWidget(self.fr_camb)
        self.horizontalLayout_18.addWidget(self.fr_salida2)
        self.fr_salida3 = QtWidgets.QFrame(parent=self.fr_content_s)
        self.fr_salida3.setStyleSheet("#fr_salida3 {\n"
                                      "background-color: rgb(0, 0, 61);\n"
                                      "border: 1px solid;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: rgb(0, 0, 31);\n"
                                      "}")
        self.fr_salida3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_salida3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_salida3.setObjectName("fr_salida3")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.fr_salida3)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.fr_iamb = QtWidgets.QFrame(parent=self.fr_salida3)
        self.fr_iamb.setMinimumSize(QtCore.QSize(0, 70))
        self.fr_iamb.setMaximumSize(QtCore.QSize(16777215, 70))
        self.fr_iamb.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_iamb.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_iamb.setObjectName("fr_iamb")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.fr_iamb)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.lbl_icon_9 = QtWidgets.QLabel(parent=self.fr_iamb)
        self.lbl_icon_9.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon_9.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon_9.setText("")
        self.lbl_icon_9.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon_9.setScaledContents(True)
        self.lbl_icon_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon_9.setObjectName("lbl_icon_9")
        self.horizontalLayout_28.addWidget(self.lbl_icon_9)
        self.lbl_iamb = QtWidgets.QLabel(parent=self.fr_iamb)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_iamb.setFont(font)
        self.lbl_iamb.setObjectName("lbl_iamb")
        self.horizontalLayout_28.addWidget(self.lbl_iamb)
        self.verticalLayout_41.addWidget(self.fr_iamb)
        self.fr_complex = QtWidgets.QFrame(parent=self.fr_salida3)
        self.fr_complex.setMinimumSize(QtCore.QSize(0, 70))
        self.fr_complex.setMaximumSize(QtCore.QSize(16777215, 70))
        self.fr_complex.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_complex.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_complex.setObjectName("fr_complex")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.fr_complex)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.lbl_icon_10 = QtWidgets.QLabel(parent=self.fr_complex)
        self.lbl_icon_10.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon_10.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon_10.setText("")
        self.lbl_icon_10.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon_10.setScaledContents(True)
        self.lbl_icon_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon_10.setObjectName("lbl_icon_10")
        self.horizontalLayout_29.addWidget(self.lbl_icon_10)
        self.lbl_complex = QtWidgets.QLabel(parent=self.fr_complex)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_complex.setFont(font)
        self.lbl_complex.setObjectName("lbl_complex")
        self.horizontalLayout_29.addWidget(self.lbl_complex)
        self.verticalLayout_41.addWidget(self.fr_complex)
        self.fr_peso_ideal = QtWidgets.QFrame(parent=self.fr_salida3)
        self.fr_peso_ideal.setMinimumSize(QtCore.QSize(0, 70))
        self.fr_peso_ideal.setMaximumSize(QtCore.QSize(16777215, 70))
        self.fr_peso_ideal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_peso_ideal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_peso_ideal.setObjectName("fr_peso_ideal")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.fr_peso_ideal)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.lbl_icon_11 = QtWidgets.QLabel(parent=self.fr_peso_ideal)
        self.lbl_icon_11.setMinimumSize(QtCore.QSize(25, 25))
        self.lbl_icon_11.setMaximumSize(QtCore.QSize(25, 25))
        self.lbl_icon_11.setText("")
        self.lbl_icon_11.setPixmap(QtGui.QPixmap("icons/icon_lista.png"))
        self.lbl_icon_11.setScaledContents(True)
        self.lbl_icon_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_icon_11.setObjectName("lbl_icon_11")
        self.horizontalLayout_30.addWidget(self.lbl_icon_11)
        self.lbl_peso_ideal = QtWidgets.QLabel(parent=self.fr_peso_ideal)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.lbl_peso_ideal.setFont(font)
        self.lbl_peso_ideal.setObjectName("lbl_peso_ideal")
        self.horizontalLayout_30.addWidget(self.lbl_peso_ideal)
        self.verticalLayout_41.addWidget(self.fr_peso_ideal)
        self.horizontalLayout_18.addWidget(self.fr_salida3)
        self.verticalLayout_39.addWidget(self.fr_content_s)
        self.horizontalLayout_6.addWidget(self.fr_seccion_s)
        self.verticalLayout_12.addWidget(self.fr_calculos)
        self.fr_buttons_s = QtWidgets.QFrame(parent=self.fr_salida)
        self.fr_buttons_s.setMinimumSize(QtCore.QSize(0, 85))
        self.fr_buttons_s.setMaximumSize(QtCore.QSize(16777215, 85))
        self.fr_buttons_s.setStyleSheet("background-color: None;")
        self.fr_buttons_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_buttons_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_buttons_s.setObjectName("fr_buttons_s")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fr_buttons_s)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fr_btn_patient_s = QtWidgets.QFrame(parent=self.fr_buttons_s)
        self.fr_btn_patient_s.setMinimumSize(QtCore.QSize(0, 70))
        self.fr_btn_patient_s.setMaximumSize(QtCore.QSize(16777215, 70))
        self.fr_btn_patient_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_btn_patient_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_btn_patient_s.setObjectName("fr_btn_patient_s")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.fr_btn_patient_s)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.btn_patient_s = QtWidgets.QPushButton(parent=self.fr_btn_patient_s)
        self.btn_patient_s.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_patient_s.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(13)
        self.btn_patient_s.setFont(font)
        self.btn_patient_s.setStyleSheet("QPushButton {\n"
                                         "background-color: rgb(0, 0, 61);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 1px solid white;\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background-color: rgb(0, 0, 31);\n"
                                         "color: white;\n"
                                         "}")
        self.btn_patient_s.setObjectName("btn_patient_s")
        self.verticalLayout_33.addWidget(self.btn_patient_s)
        self.horizontalLayout_5.addWidget(self.fr_btn_patient_s, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.fr_btn_inform_s = QtWidgets.QFrame(parent=self.fr_buttons_s)
        self.fr_btn_inform_s.setMinimumSize(QtCore.QSize(0, 70))
        self.fr_btn_inform_s.setMaximumSize(QtCore.QSize(16777215, 70))
        self.fr_btn_inform_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_btn_inform_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_btn_inform_s.setObjectName("fr_btn_inform_s")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.fr_btn_inform_s)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.btn_inform_s = QtWidgets.QPushButton(parent=self.fr_btn_inform_s)
        self.btn_inform_s.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_inform_s.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(13)
        self.btn_inform_s.setFont(font)
        self.btn_inform_s.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(0, 0, 61);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 1px solid white;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(0, 0, 31);\n"
                                        "color: white;\n"
                                        "}")
        self.btn_inform_s.setObjectName("btn_inform_s")
        self.verticalLayout_34.addWidget(self.btn_inform_s)
        self.horizontalLayout_5.addWidget(self.fr_btn_inform_s, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.fr_btn_model3D_s = QtWidgets.QFrame(parent=self.fr_buttons_s)
        self.fr_btn_model3D_s.setMinimumSize(QtCore.QSize(0, 70))
        self.fr_btn_model3D_s.setMaximumSize(QtCore.QSize(16777215, 70))
        self.fr_btn_model3D_s.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_btn_model3D_s.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_btn_model3D_s.setObjectName("fr_btn_model3D_s")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.fr_btn_model3D_s)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.btn_model3D_s = QtWidgets.QPushButton(parent=self.fr_btn_model3D_s)
        self.btn_model3D_s.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_model3D_s.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(13)
        self.btn_model3D_s.setFont(font)
        self.btn_model3D_s.setStyleSheet("QPushButton {\n"
                                         "background-color: rgb(0, 0, 61);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 1px solid white;\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background-color: rgb(0, 0, 31);\n"
                                         "color: white;\n"
                                         "}")
        self.btn_model3D_s.setObjectName("btn_model3D_s")
        self.verticalLayout_35.addWidget(self.btn_model3D_s)
        self.horizontalLayout_5.addWidget(self.fr_btn_model3D_s, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_12.addWidget(self.fr_buttons_s, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout_11.addWidget(self.fr_salida)
        self.ingresar_patient.addWidget(self.Salida)
        self.citas = QtWidgets.QWidget()
        self.citas.setStyleSheet("")
        self.citas.setObjectName("citas")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.citas)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.frame_2 = QtWidgets.QFrame(parent=self.citas)
        self.frame_2.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 31);\n"
                                   "color: white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.photo_patient_s_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.photo_patient_s_2.setMinimumSize(QtCore.QSize(80, 80))
        self.photo_patient_s_2.setMaximumSize(QtCore.QSize(80, 80))
        self.photo_patient_s_2.setStyleSheet("border: 5px solid;\n"
                                             "border-radius: 35px;\n"
                                             "border-color: rgb(0, 0, 100);")
        self.photo_patient_s_2.setText("")
        self.photo_patient_s_2.setPixmap(QtGui.QPixmap("images/foto-p.png"))
        self.photo_patient_s_2.setScaledContents(True)
        self.photo_patient_s_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.photo_patient_s_2.setObjectName("photo_patient_s_2")
        self.verticalLayout_45.addWidget(self.photo_patient_s_2, 0,
                                         QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_46.addWidget(self.frame_3)
        self.fr_dpatient_cita = QtWidgets.QFrame(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)

        self.fr_dpatient_cita.setFont(font)
        self.fr_dpatient_cita.setStyleSheet("QLineEdit {\n"
                                            "background-color: white;\n"
                                            "border: 3px solid;\n"
                                            "border-color: rgb(227, 227, 227);\n"
                                            "border-radius: 8px;\n"
                                            "color: rgb(0, 0, 61);\n"
                                            "padding-left: 5px;\n"
                                            "}")
        self.fr_dpatient_cita.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_dpatient_cita.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_dpatient_cita.setObjectName("fr_dpatient_cita")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.fr_dpatient_cita)
        self.verticalLayout_47.setContentsMargins(-1, -1, -1, 50)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.lbl_name_c = QtWidgets.QLabel(parent=self.fr_dpatient_cita)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.lbl_name_c.setFont(font)
        self.lbl_name_c.setObjectName("lbl_name_c")
        self.verticalLayout_47.addWidget(self.lbl_name_c)
        self.name_cita = QtWidgets.QLineEdit(parent=self.fr_dpatient_cita)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.name_cita.setFont(font)
        self.name_cita.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.name_cita.setReadOnly(True)
        self.name_cita.setObjectName("name_cita")
        self.verticalLayout_47.addWidget(self.name_cita)
        self.lbl_edad_c = QtWidgets.QLabel(parent=self.fr_dpatient_cita)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.lbl_edad_c.setFont(font)
        self.lbl_edad_c.setObjectName("lbl_edad_c")
        self.verticalLayout_47.addWidget(self.lbl_edad_c)
        self.edad_cita = QtWidgets.QLineEdit(parent=self.fr_dpatient_cita)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.edad_cita.setFont(font)
        self.edad_cita.setReadOnly(True)
        self.edad_cita.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.edad_cita.setObjectName("edad_cita")
        self.verticalLayout_47.addWidget(self.edad_cita)
        self.lbl_tpatient_c = QtWidgets.QLabel(parent=self.fr_dpatient_cita)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.lbl_tpatient_c.setFont(font)
        self.lbl_tpatient_c.setObjectName("lbl_tpatient_c")
        self.verticalLayout_47.addWidget(self.lbl_tpatient_c)
        self.tpaciente_cita = QtWidgets.QLineEdit(parent=self.fr_dpatient_cita)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.tpaciente_cita.setFont(font)
        self.tpaciente_cita.setReadOnly(True)
        self.tpaciente_cita.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tpaciente_cita.setObjectName("tpaciente_cita")
        self.verticalLayout_47.addWidget(self.tpaciente_cita)
        self.lbl_sexo_c = QtWidgets.QLabel(parent=self.fr_dpatient_cita)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.lbl_sexo_c.setFont(font)
        self.lbl_sexo_c.setObjectName("lbl_sexo_c")
        self.verticalLayout_47.addWidget(self.lbl_sexo_c)
        self.sexo_cita = QtWidgets.QLineEdit(parent=self.fr_dpatient_cita)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.sexo_cita.setFont(font)
        self.sexo_cita.setReadOnly(True)
        self.sexo_cita.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.sexo_cita.setObjectName("sexo_cita")
        self.verticalLayout_47.addWidget(self.sexo_cita)
        self.lbl_pais_c = QtWidgets.QLabel(parent=self.fr_dpatient_cita)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.lbl_pais_c.setFont(font)
        self.lbl_pais_c.setObjectName("lbl_pais_c")
        self.verticalLayout_47.addWidget(self.lbl_pais_c)
        self.pais_cita = QtWidgets.QLineEdit(parent=self.fr_dpatient_cita)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.pais_cita.setFont(font)
        self.pais_cita.setReadOnly(True)
        self.pais_cita.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.pais_cita.setObjectName("pais_cita")
        self.verticalLayout_47.addWidget(self.pais_cita)
        self.verticalLayout_46.addWidget(self.fr_dpatient_cita)
        self.horizontalLayout_31.addWidget(self.frame_2)
        self.fr_content_citas = QtWidgets.QFrame(parent=self.citas)
        self.fr_content_citas.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_content_citas.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_content_citas.setObjectName("fr_content_citas")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.fr_content_citas)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.fr_fecha_hora_c = QtWidgets.QFrame(parent=self.fr_content_citas)
        self.fr_fecha_hora_c.setMinimumSize(QtCore.QSize(0, 60))
        self.fr_fecha_hora_c.setMaximumSize(QtCore.QSize(16777215, 60))
        self.fr_fecha_hora_c.setStyleSheet("background-color: white;\n"
                                           "border-color: rgb(0, 0, 61);\n"
                                           "border: 3px solid;\n"
                                           "border-radius: 5px;")
        self.fr_fecha_hora_c.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_fecha_hora_c.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_fecha_hora_c.setObjectName("fr_fecha_hora_c")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.fr_fecha_hora_c)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.lbl_fecha_hora = QtWidgets.QLabel(parent=self.fr_fecha_hora_c)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(11)
        self.lbl_fecha_hora.setFont(font)
        self.lbl_fecha_hora.setStyleSheet("border: 0px solid;")
        self.lbl_fecha_hora.setObjectName("lbl_fecha_hora")
        self.verticalLayout_50.addWidget(self.lbl_fecha_hora)
        self.verticalLayout_43.addWidget(self.fr_fecha_hora_c)
        self.fr_tcitas = QtWidgets.QFrame(parent=self.fr_content_citas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_tcitas.sizePolicy().hasHeightForWidth())
        self.fr_tcitas.setSizePolicy(sizePolicy)
        self.fr_tcitas.setStyleSheet("QLineEdit {\n"
                                     "border: 3px solid;\n"
                                     "border-color: rgb(0, 0, 61);\n"
                                     "border-bottom-left-radius: 5px;\n"
                                     "border-bottom-right-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QLabel {\n"
                                     "border-top-left-radius: 5px;\n"
                                     "border-top-right-radius: 5px;\n"
                                     "color: white;\n"
                                     "background-color: rgb(0, 0, 61);\n"
                                     "}")
        self.fr_tcitas.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_tcitas.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_tcitas.setObjectName("fr_tcitas")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.fr_tcitas)
        self.horizontalLayout_33.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.table_citas = QtWidgets.QTableWidget(parent=self.fr_tcitas)
        self.table_citas.setStyleSheet("QTableWidget {\n"
                                       "background-color: white;\n"
                                       "border-color: rgb(0, 0, 61);\n"
                                       "border: 3px solid;\n"
                                       "border-radius: 5px;\n"
                                       "}")
        self.table_citas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_citas.setAlternatingRowColors(True)
        self.table_citas.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.table_citas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_citas.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.table_citas.setObjectName("table_citas")
        self.table_citas.setRowCount(1)
        self.table_citas.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_citas.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_citas.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_citas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_citas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_citas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_citas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_citas.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_citas.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_citas.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        item.setFlags(
            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.table_citas.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        self.table_citas.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_citas.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_citas.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_citas.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 61))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.table_citas.setItem(1, 4, item)
        self.table_citas.horizontalHeader().setVisible(False)
        self.table_citas.horizontalHeader().setDefaultSectionSize(127)
        self.table_citas.verticalHeader().setVisible(False)
        self.horizontalLayout_33.addWidget(self.table_citas)
        self.verticalLayout_43.addWidget(self.fr_tcitas)
        self.fr_btn_citas = QtWidgets.QFrame(parent=self.fr_content_citas)
        self.fr_btn_citas.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_btn_citas.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_btn_citas.setObjectName("fr_btn_citas")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.fr_btn_citas)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.btn_volver_patient_cita = QtWidgets.QPushButton(parent=self.fr_btn_citas)
        self.btn_volver_patient_cita.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_volver_patient_cita.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(12)
        self.btn_volver_patient_cita.setFont(font)
        self.btn_volver_patient_cita.setStyleSheet("QPushButton {\n"
                                                   "background-color: rgb(0, 0, 61);\n"
                                                   "color: rgb(255, 255, 255);\n"
                                                   "border: 1px solid white;\n"
                                                   "border-radius: 10px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover {\n"
                                                   "background-color: rgb(0, 0, 31);\n"
                                                   "color: white;\n"
                                                   "}")
        self.btn_volver_patient_cita.setObjectName("btn_volver_patient_cita")
        self.horizontalLayout_32.addWidget(self.btn_volver_patient_cita)

        self.btn_crear_modelo_cita = QtWidgets.QPushButton(parent=self.fr_btn_citas)
        self.btn_crear_modelo_cita.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_crear_modelo_cita.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(12)
        self.btn_crear_modelo_cita.setFont(font)
        self.btn_crear_modelo_cita.setStyleSheet("QPushButton {\n"
                                                   "background-color: rgb(0, 0, 61);\n"
                                                   "color: rgb(255, 255, 255);\n"
                                                   "border: 1px solid white;\n"
                                                   "border-radius: 10px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover {\n"
                                                   "background-color: rgb(0, 0, 31);\n"
                                                   "color: white;\n"
                                                   "}")
        self.btn_crear_modelo_cita.setObjectName("btn_crear_modelo_cita")
        self.horizontalLayout_32.addWidget(self.btn_crear_modelo_cita)


        self.btn_agregar_cita = QtWidgets.QPushButton(parent=self.fr_btn_citas)
        self.btn_agregar_cita.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_agregar_cita.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(12)
        self.btn_agregar_cita.setFont(font)
        self.btn_agregar_cita.setStyleSheet("QPushButton {\n"
                                            "background-color: rgb(0, 0, 61);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border: 1px solid white;\n"
                                            "border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "background-color: rgb(0, 0, 31);\n"
                                            "color: white;\n"
                                            "}")
        self.btn_agregar_cita.setObjectName("btn_agregar_cita")
        self.horizontalLayout_32.addWidget(self.btn_agregar_cita)
        self.btn_verinfo_cita = QtWidgets.QPushButton(parent=self.fr_btn_citas)
        self.btn_verinfo_cita.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_verinfo_cita.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(12)
        self.btn_verinfo_cita.setFont(font)
        self.btn_verinfo_cita.setStyleSheet("QPushButton {\n"
                                            "background-color: rgb(0, 0, 61);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border: 1px solid white;\n"
                                            "border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "background-color: rgb(0, 0, 31);\n"
                                            "color: white;\n"
                                            "}")
        self.btn_verinfo_cita.setObjectName("btn_verinfo_cita")
        self.horizontalLayout_32.addWidget(self.btn_verinfo_cita)
        self.verticalLayout_43.addWidget(self.fr_btn_citas, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.horizontalLayout_31.addWidget(self.fr_content_citas)
        self.ingresar_patient.addWidget(self.citas)
        self.verticalLayout_22.addWidget(self.ingresar_patient)
        self.content_patient.addWidget(self.data_patient)
        self.analytics = QtWidgets.QWidget()
        self.analytics.setStyleSheet("#first_data {\n"
                                     "border: 2.5px solid;\n"
                                     "border-color: rgb(0, 0, 61);\n"
                                     "border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "#date_data {\n"
                                     "border: 2.5px solid;\n"
                                     "border-color: rgb(0, 0, 61);\n"
                                     "border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "#second_data {\n"
                                     "border: 2.5px solid;\n"
                                     "border-color: rgb(0, 0, 61);\n"
                                     "border-radius: 5px;\n"
                                     "}")
        self.analytics.setObjectName("analytics")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.analytics)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.content_patient.addWidget(self.analytics)
        self.verticalLayout_6.addWidget(self.content_patient)
        self.content.addWidget(self.Paciente)
        self.Estadisticas = QtWidgets.QWidget()
        self.Estadisticas.setObjectName("Estadisticas")
        self.verticalLayout_440 = QtWidgets.QVBoxLayout(self.Estadisticas)
        self.verticalLayout_440.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_440.setSpacing(0)
        self.verticalLayout_440.setObjectName("verticalLayout_440")
        self.content_estadisticas = QtWidgets.QStackedWidget(parent=self.Estadisticas)
        self.content_estadisticas.setObjectName("content_estadisticas")
        self.est_generales = QtWidgets.QWidget()
        self.est_generales.setObjectName("est_generales")
        self.verticalLayout_560 = QtWidgets.QVBoxLayout(self.est_generales)
        self.verticalLayout_560.setObjectName("verticalLayout_560")
        self.est_scrollArea = QtWidgets.QScrollArea(parent=self.est_generales)
        self.est_scrollArea.setStyleSheet("border: none;")
        self.est_scrollArea.setWidgetResizable(True)
        self.est_scrollArea.setObjectName("est_scrollArea")
        self.est_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.est_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1209, 1098))
        self.est_scrollAreaWidgetContents.setObjectName("est_scrollAreaWidgetContents")
        self.verticalLayout_480 = QtWidgets.QVBoxLayout(self.est_scrollAreaWidgetContents)
        self.verticalLayout_480.setObjectName("verticalLayout_480")
        self.frame_est_general = QtWidgets.QFrame(parent=self.est_scrollAreaWidgetContents)
        self.frame_est_general.setMinimumSize(QtCore.QSize(1000, 1080))
        self.frame_est_general.setMaximumSize(QtCore.QSize(16777215, 1080))
        self.frame_est_general.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_est_general.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_est_general.setObjectName("frame_est_general")
        self.verticalLayout_490 = QtWidgets.QVBoxLayout(self.frame_est_general)
        self.verticalLayout_490.setObjectName("verticalLayout_490")
        self.fr_estadisticas_1 = QtWidgets.QFrame(parent=self.frame_est_general)
        self.fr_estadisticas_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_estadisticas_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_estadisticas_1.setObjectName("fr_estadisticas_1")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.fr_estadisticas_1)
        self.gridLayout_40.setContentsMargins(-1, -1, -1, 9)
        self.gridLayout_40.setVerticalSpacing(6)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.frame_cant_hombres = QtWidgets.QFrame(parent=self.fr_estadisticas_1)
        self.frame_cant_hombres.setMinimumSize(QtCore.QSize(0, 104))
        self.frame_cant_hombres.setMaximumSize(QtCore.QSize(16777215, 104))
        self.frame_cant_hombres.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border: 2px solid rgb(0, 0, 61);\n"
                                              "border-radius: 10px;")
        self.frame_cant_hombres.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cant_hombres.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cant_hombres.setObjectName("frame_cant_hombres")
        self.horizontalLayout_430 = QtWidgets.QHBoxLayout(self.frame_cant_hombres)
        self.horizontalLayout_430.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_430.setSpacing(0)
        self.horizontalLayout_430.setObjectName("horizontalLayout_430")
        self.label_cant_hombres_icono = QtWidgets.QLabel(parent=self.frame_cant_hombres)
        self.label_cant_hombres_icono.setMinimumSize(QtCore.QSize(100, 100))
        self.label_cant_hombres_icono.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.label_cant_hombres_icono.setFont(font)
        self.label_cant_hombres_icono.setStyleSheet("border: none;\n"
                                                    "border-radius: 0px;\n"
                                                    "border-top-left-radius: 10px;\n"
                                                    "border-bottom-left-radius: 10px;\n"
                                                    "background-color: rgb(170, 0, 0);\n"
                                                    "padding: 10px;")
        self.label_cant_hombres_icono.setText("")
        self.label_cant_hombres_icono.setPixmap(QtGui.QPixmap("icons/men.png"))
        self.label_cant_hombres_icono.setScaledContents(False)
        self.label_cant_hombres_icono.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cant_hombres_icono.setObjectName("label_cant_hombres_icono")
        self.horizontalLayout_430.addWidget(self.label_cant_hombres_icono)
        self.frame_cant_hombres_titulo = QtWidgets.QFrame(parent=self.frame_cant_hombres)
        self.frame_cant_hombres_titulo.setStyleSheet("border: none;")
        self.frame_cant_hombres_titulo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cant_hombres_titulo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cant_hombres_titulo.setObjectName("frame_cant_hombres_titulo")
        self.verticalLayout_660 = QtWidgets.QVBoxLayout(self.frame_cant_hombres_titulo)
        self.verticalLayout_660.setObjectName("verticalLayout_660")
        self.label_cant_hombres_titulo = QtWidgets.QLabel(parent=self.frame_cant_hombres_titulo)
        self.label_cant_hombres_titulo.setMinimumSize(QtCore.QSize(200, 23))
        self.label_cant_hombres_titulo.setMaximumSize(QtCore.QSize(200, 23))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.label_cant_hombres_titulo.setFont(font)
        self.label_cant_hombres_titulo.setStyleSheet("border: none;\n"
                                                     "border-radius: none;\n"
                                                     "border-bottom: 1px solid rgb(100, 100, 100);\n"
                                                     "color: rgb(100, 100, 100);")
        self.label_cant_hombres_titulo.setObjectName("label_cant_hombres_titulo")
        self.verticalLayout_660.addWidget(self.label_cant_hombres_titulo)
        self.horizontalLayout_430.addWidget(self.frame_cant_hombres_titulo, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_cant_hombres_num = QtWidgets.QFrame(parent=self.frame_cant_hombres)
        self.frame_cant_hombres_num.setStyleSheet("border: none;")
        self.frame_cant_hombres_num.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cant_hombres_num.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cant_hombres_num.setObjectName("frame_cant_hombres_num")
        self.verticalLayout_650 = QtWidgets.QVBoxLayout(self.frame_cant_hombres_num)
        self.verticalLayout_650.setObjectName("verticalLayout_650")
        self.lbl_cant_hombres = QtWidgets.QLabel(parent=self.frame_cant_hombres_num)
        self.lbl_cant_hombres.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_cant_hombres.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.lbl_cant_hombres.setFont(font)
        self.lbl_cant_hombres.setStyleSheet("border: none;")
        self.lbl_cant_hombres.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_cant_hombres.setObjectName("lbl_cant_hombres")
        self.verticalLayout_650.addWidget(self.lbl_cant_hombres)
        self.horizontalLayout_430.addWidget(self.frame_cant_hombres_num)
        self.gridLayout_40.addWidget(self.frame_cant_hombres, 2, 2, 1, 1)
        self.frame_edadprom = QtWidgets.QFrame(parent=self.fr_estadisticas_1)
        self.frame_edadprom.setMinimumSize(QtCore.QSize(0, 104))
        self.frame_edadprom.setMaximumSize(QtCore.QSize(16777215, 104))
        self.frame_edadprom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border: 2px solid rgb(0, 0, 61);\n"
                                          "border-radius: 10px;")
        self.frame_edadprom.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_edadprom.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_edadprom.setObjectName("frame_edadprom")
        self.horizontalLayout_410 = QtWidgets.QHBoxLayout(self.frame_edadprom)
        self.horizontalLayout_410.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_410.setSpacing(0)
        self.horizontalLayout_410.setObjectName("horizontalLayout_410")
        self.label_edadprom_icono = QtWidgets.QLabel(parent=self.frame_edadprom)
        self.label_edadprom_icono.setMinimumSize(QtCore.QSize(100, 100))
        self.label_edadprom_icono.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.label_edadprom_icono.setFont(font)
        self.label_edadprom_icono.setStyleSheet("border: none;\n"
                                                "border-radius: 0px;\n"
                                                "border-top-left-radius: 10px;\n"
                                                "border-bottom-left-radius: 10px;\n"
                                                "background-color: rgb(0, 255, 127);\n"
                                                "padding: 10px;")
        self.label_edadprom_icono.setText("")
        self.label_edadprom_icono.setPixmap(QtGui.QPixmap("icons/age-group.png"))
        self.label_edadprom_icono.setScaledContents(False)
        self.label_edadprom_icono.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_edadprom_icono.setObjectName("label_edadprom_icono")
        self.horizontalLayout_410.addWidget(self.label_edadprom_icono)
        self.frame_edadprom_titulo = QtWidgets.QFrame(parent=self.frame_edadprom)
        self.frame_edadprom_titulo.setStyleSheet("border: none;")
        self.frame_edadprom_titulo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_edadprom_titulo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_edadprom_titulo.setObjectName("frame_edadprom_titulo")
        self.verticalLayout_700 = QtWidgets.QVBoxLayout(self.frame_edadprom_titulo)
        self.verticalLayout_700.setObjectName("verticalLayout_700")
        self.label_edadprom_titulo = QtWidgets.QLabel(parent=self.frame_edadprom_titulo)
        self.label_edadprom_titulo.setMinimumSize(QtCore.QSize(200, 23))
        self.label_edadprom_titulo.setMaximumSize(QtCore.QSize(200, 23))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.label_edadprom_titulo.setFont(font)
        self.label_edadprom_titulo.setStyleSheet("border: none;\n"
                                                 "border-radius: none;\n"
                                                 "border-bottom: 1px solid rgb(100, 100, 100);\n"
                                                 "color: rgb(100, 100, 100);")
        self.label_edadprom_titulo.setObjectName("label_edadprom_titulo")
        self.verticalLayout_700.addWidget(self.label_edadprom_titulo)
        self.horizontalLayout_410.addWidget(self.frame_edadprom_titulo, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_edadprom_num = QtWidgets.QFrame(parent=self.frame_edadprom)
        self.frame_edadprom_num.setStyleSheet("border: none;")
        self.frame_edadprom_num.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_edadprom_num.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_edadprom_num.setObjectName("frame_edadprom_num")
        self.verticalLayout_690 = QtWidgets.QVBoxLayout(self.frame_edadprom_num)
        self.verticalLayout_690.setObjectName("verticalLayout_690")
        self.lbl_edad_promedio = QtWidgets.QLabel(parent=self.frame_edadprom_num)
        self.lbl_edad_promedio.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_edad_promedio.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.lbl_edad_promedio.setFont(font)
        self.lbl_edad_promedio.setStyleSheet("border: none;")
        self.lbl_edad_promedio.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_edad_promedio.setObjectName("lbl_edad_promedio")
        self.verticalLayout_690.addWidget(self.lbl_edad_promedio)
        self.horizontalLayout_410.addWidget(self.frame_edadprom_num)
        self.gridLayout_40.addWidget(self.frame_edadprom, 2, 0, 1, 1)
        self.frame_cant_mujeres = QtWidgets.QFrame(parent=self.fr_estadisticas_1)
        self.frame_cant_mujeres.setMinimumSize(QtCore.QSize(0, 104))
        self.frame_cant_mujeres.setMaximumSize(QtCore.QSize(16777215, 104))
        self.frame_cant_mujeres.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border: 2px solid rgb(0, 0, 61);\n"
                                              "border-radius: 10px;")
        self.frame_cant_mujeres.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cant_mujeres.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cant_mujeres.setObjectName("frame_cant_mujeres")
        self.horizontalLayout_420 = QtWidgets.QHBoxLayout(self.frame_cant_mujeres)
        self.horizontalLayout_420.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_420.setSpacing(0)
        self.horizontalLayout_420.setObjectName("horizontalLayout_420")
        self.label_cant_mujeres_icono = QtWidgets.QLabel(parent=self.frame_cant_mujeres)
        self.label_cant_mujeres_icono.setMinimumSize(QtCore.QSize(100, 100))
        self.label_cant_mujeres_icono.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.label_cant_mujeres_icono.setFont(font)
        self.label_cant_mujeres_icono.setStyleSheet("border: none;\n"
                                                    "border-radius: 0px;\n"
                                                    "border-top-left-radius: 10px;\n"
                                                    "border-bottom-left-radius: 10px;\n"
                                                    "background-color: rgb(85, 0, 127);\n"
                                                    "padding: 10px;")
        self.label_cant_mujeres_icono.setText("")
        self.label_cant_mujeres_icono.setPixmap(QtGui.QPixmap("icons/woman.png"))
        self.label_cant_mujeres_icono.setScaledContents(False)
        self.label_cant_mujeres_icono.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cant_mujeres_icono.setObjectName("label_cant_mujeres_icono")
        self.horizontalLayout_420.addWidget(self.label_cant_mujeres_icono)
        self.frame_cant_mujeres_titulo = QtWidgets.QFrame(parent=self.frame_cant_mujeres)
        self.frame_cant_mujeres_titulo.setStyleSheet("border: none;")
        self.frame_cant_mujeres_titulo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cant_mujeres_titulo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cant_mujeres_titulo.setObjectName("frame_cant_mujeres_titulo")
        self.verticalLayout_680 = QtWidgets.QVBoxLayout(self.frame_cant_mujeres_titulo)
        self.verticalLayout_680.setObjectName("verticalLayout_680")
        self.label_cant_mujeres_titulo = QtWidgets.QLabel(parent=self.frame_cant_mujeres_titulo)
        self.label_cant_mujeres_titulo.setMinimumSize(QtCore.QSize(200, 23))
        self.label_cant_mujeres_titulo.setMaximumSize(QtCore.QSize(200, 23))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.label_cant_mujeres_titulo.setFont(font)
        self.label_cant_mujeres_titulo.setStyleSheet("border: none;\n"
                                                     "border-radius: none;\n"
                                                     "border-bottom: 1px solid rgb(100, 100, 100);\n"
                                                     "color: rgb(100, 100, 100);")
        self.label_cant_mujeres_titulo.setObjectName("label_cant_mujeres_titulo")
        self.verticalLayout_680.addWidget(self.label_cant_mujeres_titulo)
        self.horizontalLayout_420.addWidget(self.frame_cant_mujeres_titulo, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_cant_mujeres_num = QtWidgets.QFrame(parent=self.frame_cant_mujeres)
        self.frame_cant_mujeres_num.setStyleSheet("border: none;")
        self.frame_cant_mujeres_num.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cant_mujeres_num.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cant_mujeres_num.setObjectName("frame_cant_mujeres_num")
        self.verticalLayout_670 = QtWidgets.QVBoxLayout(self.frame_cant_mujeres_num)
        self.verticalLayout_670.setObjectName("verticalLayout_670")
        self.lbl_cant_mujeres = QtWidgets.QLabel(parent=self.frame_cant_mujeres_num)
        self.lbl_cant_mujeres.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_cant_mujeres.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.lbl_cant_mujeres.setFont(font)
        self.lbl_cant_mujeres.setStyleSheet("border: none;")
        self.lbl_cant_mujeres.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_cant_mujeres.setObjectName("lbl_cant_mujeres")
        self.verticalLayout_670.addWidget(self.lbl_cant_mujeres)
        self.horizontalLayout_420.addWidget(self.frame_cant_mujeres_num)
        self.gridLayout_40.addWidget(self.frame_cant_mujeres, 2, 1, 1, 1)
        self.fr_patient_total = QtWidgets.QFrame(parent=self.fr_estadisticas_1)
        self.fr_patient_total.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_patient_total.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_patient_total.setObjectName("fr_patient_total")
        self.horizontalLayout_350 = QtWidgets.QHBoxLayout(self.fr_patient_total)
        self.horizontalLayout_350.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_350.setSpacing(6)
        self.horizontalLayout_350.setObjectName("horizontalLayout_350")
        self.frame_pacientetotal = QtWidgets.QFrame(parent=self.fr_patient_total)
        self.frame_pacientetotal.setMinimumSize(QtCore.QSize(0, 104))
        self.frame_pacientetotal.setMaximumSize(QtCore.QSize(16777215, 104))
        self.frame_pacientetotal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "border: 2px solid rgb(0, 0, 61);\n"
                                               "border-radius: 10px;")
        self.frame_pacientetotal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_pacientetotal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_pacientetotal.setObjectName("frame_pacientetotal")
        self.horizontalLayout_360 = QtWidgets.QHBoxLayout(self.frame_pacientetotal)
        self.horizontalLayout_360.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_360.setSpacing(0)
        self.horizontalLayout_360.setObjectName("horizontalLayout_360")
        self.label_pacientetotal_icono = QtWidgets.QLabel(parent=self.frame_pacientetotal)
        self.label_pacientetotal_icono.setMinimumSize(QtCore.QSize(100, 100))
        self.label_pacientetotal_icono.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.label_pacientetotal_icono.setFont(font)
        self.label_pacientetotal_icono.setStyleSheet("border: none;\n"
                                                     "border-radius: 0px;\n"
                                                     "border-top-left-radius: 10px;\n"
                                                     "border-bottom-left-radius: 10px;\n"
                                                     "background-color: rgb(255, 85, 0);\n"
                                                     "padding: 10px;")
        self.label_pacientetotal_icono.setText("")
        self.label_pacientetotal_icono.setPixmap(QtGui.QPixmap("icons/persona.png"))
        self.label_pacientetotal_icono.setScaledContents(True)
        self.label_pacientetotal_icono.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_pacientetotal_icono.setObjectName("label_pacientetotal_icono")
        self.horizontalLayout_360.addWidget(self.label_pacientetotal_icono)
        self.frame_pacientetotal_center = QtWidgets.QFrame(parent=self.frame_pacientetotal)
        self.frame_pacientetotal_center.setStyleSheet("border: none;")
        self.frame_pacientetotal_center.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_pacientetotal_center.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_pacientetotal_center.setObjectName("frame_pacientetotal_center")
        self.gridLayout_60 = QtWidgets.QGridLayout(self.frame_pacientetotal_center)
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.lbl_patient_adulto = QtWidgets.QLabel(parent=self.frame_pacientetotal_center)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        self.lbl_patient_adulto.setFont(font)
        self.lbl_patient_adulto.setStyleSheet("border: none;\n"
                                              "border-radius: none;\n"
                                              "color: rgb(100, 100, 100);")
        self.lbl_patient_adulto.setObjectName("lbl_patient_adulto")
        self.gridLayout_60.addWidget(self.lbl_patient_adulto, 1, 0, 1, 1)
        self.label_pacientetotal_titulo = QtWidgets.QLabel(parent=self.frame_pacientetotal_center)
        self.label_pacientetotal_titulo.setMinimumSize(QtCore.QSize(250, 23))
        self.label_pacientetotal_titulo.setMaximumSize(QtCore.QSize(250, 23))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.label_pacientetotal_titulo.setFont(font)
        self.label_pacientetotal_titulo.setStyleSheet("border: none;\n"
                                                      "border-radius: none;\n"
                                                      "border-bottom: 1px solid rgb(100, 100, 100);\n"
                                                      "color: rgb(100, 100, 100);")
        self.label_pacientetotal_titulo.setObjectName("label_pacientetotal_titulo")
        self.gridLayout_60.addWidget(self.label_pacientetotal_titulo, 0, 0, 1, 1)
        self.lbl_patient_atleta = QtWidgets.QLabel(parent=self.frame_pacientetotal_center)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        self.lbl_patient_atleta.setFont(font)
        self.lbl_patient_atleta.setStyleSheet("border: none;\n"
                                              "border-radius: none;\n"
                                              "color: rgb(100, 100, 100);")
        self.lbl_patient_atleta.setObjectName("lbl_patient_atleta")
        self.gridLayout_60.addWidget(self.lbl_patient_atleta, 2, 0, 1, 1)
        self.lbl_patient_adulto_count = QtWidgets.QLabel(parent=self.frame_pacientetotal_center)
        self.lbl_patient_adulto_count.setMinimumSize(QtCore.QSize(50, 0))
        self.lbl_patient_adulto_count.setObjectName("lbl_patient_adulto_count")
        self.gridLayout_60.addWidget(self.lbl_patient_adulto_count, 1, 1, 1, 1)
        self.lbl_patient_atleta_count = QtWidgets.QLabel(parent=self.frame_pacientetotal_center)
        self.lbl_patient_atleta_count.setMinimumSize(QtCore.QSize(50, 0))
        self.lbl_patient_atleta_count.setObjectName("lbl_patient_atleta_count")
        self.gridLayout_60.addWidget(self.lbl_patient_atleta_count, 2, 1, 1, 1)
        self.horizontalLayout_360.addWidget(self.frame_pacientetotal_center)
        self.frame_pacientetotal_numero = QtWidgets.QFrame(parent=self.frame_pacientetotal)
        self.frame_pacientetotal_numero.setStyleSheet("border: none;")
        self.frame_pacientetotal_numero.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_pacientetotal_numero.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_pacientetotal_numero.setObjectName("frame_pacientetotal_numero")
        self.verticalLayout_530 = QtWidgets.QVBoxLayout(self.frame_pacientetotal_numero)
        self.verticalLayout_530.setObjectName("verticalLayout_530")
        self.lbl_patient_total = QtWidgets.QLabel(parent=self.frame_pacientetotal_numero)
        self.lbl_patient_total.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_patient_total.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.lbl_patient_total.setFont(font)
        self.lbl_patient_total.setStyleSheet("border: none;")
        self.lbl_patient_total.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_patient_total.setObjectName("lbl_patient_total")
        self.verticalLayout_530.addWidget(self.lbl_patient_total)
        self.horizontalLayout_360.addWidget(self.frame_pacientetotal_numero)
        self.horizontalLayout_350.addWidget(self.frame_pacientetotal)
        self.fr_cita_total = QtWidgets.QFrame(parent=self.fr_patient_total)
        self.fr_cita_total.setMinimumSize(QtCore.QSize(0, 104))
        self.fr_cita_total.setMaximumSize(QtCore.QSize(16777215, 104))
        self.fr_cita_total.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border: 2px solid rgb(0, 0, 61);\n"
                                         "border-radius: 10px;")
        self.fr_cita_total.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_cita_total.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_cita_total.setObjectName("fr_cita_total")
        self.horizontalLayout_370 = QtWidgets.QHBoxLayout(self.fr_cita_total)
        self.horizontalLayout_370.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_370.setSpacing(0)
        self.horizontalLayout_370.setObjectName("horizontalLayout_370")
        self.label_citatotal_icono = QtWidgets.QLabel(parent=self.fr_cita_total)
        self.label_citatotal_icono.setMinimumSize(QtCore.QSize(100, 100))
        self.label_citatotal_icono.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.label_citatotal_icono.setFont(font)
        self.label_citatotal_icono.setStyleSheet("border: none;\n"
                                                 "border-radius: 0px;\n"
                                                 "border-top-left-radius: 10px;\n"
                                                 "border-bottom-left-radius: 10px;\n"
                                                 "background-color: rgb(85, 0, 255);\n"
                                                 "padding: 10px;")
        self.label_citatotal_icono.setText("")
        self.label_citatotal_icono.setPixmap(QtGui.QPixmap("icons/information-button.png"))
        self.label_citatotal_icono.setScaledContents(True)
        self.label_citatotal_icono.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_citatotal_icono.setObjectName("label_citatotal_icono")
        self.horizontalLayout_370.addWidget(self.label_citatotal_icono)
        self.frame_citatotal_label = QtWidgets.QFrame(parent=self.fr_cita_total)
        self.frame_citatotal_label.setStyleSheet("border: none;")
        self.frame_citatotal_label.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_citatotal_label.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_citatotal_label.setObjectName("frame_citatotal_label")
        self.verticalLayout_570 = QtWidgets.QVBoxLayout(self.frame_citatotal_label)
        self.verticalLayout_570.setObjectName("verticalLayout_570")
        self.label_citatota_titulo = QtWidgets.QLabel(parent=self.frame_citatotal_label)
        self.label_citatota_titulo.setMinimumSize(QtCore.QSize(250, 23))
        self.label_citatota_titulo.setMaximumSize(QtCore.QSize(250, 23))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.label_citatota_titulo.setFont(font)
        self.label_citatota_titulo.setStyleSheet("border: none;\n"
                                                 "border-radius: none;\n"
                                                 "border-bottom: 1px solid rgb(100, 100, 100);\n"
                                                 "color: rgb(100, 100, 100);")
        self.label_citatota_titulo.setObjectName("label_citatota_titulo")
        self.verticalLayout_570.addWidget(self.label_citatota_titulo)
        self.horizontalLayout_370.addWidget(self.frame_citatotal_label, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_citatotal_numero = QtWidgets.QFrame(parent=self.fr_cita_total)
        self.frame_citatotal_numero.setStyleSheet("border: none;")
        self.frame_citatotal_numero.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_citatotal_numero.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_citatotal_numero.setObjectName("frame_citatotal_numero")
        self.verticalLayout_580 = QtWidgets.QVBoxLayout(self.frame_citatotal_numero)
        self.verticalLayout_580.setObjectName("verticalLayout_580")
        self.lbl_cita_total = QtWidgets.QLabel(parent=self.frame_citatotal_numero)
        self.lbl_cita_total.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_cita_total.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.lbl_cita_total.setFont(font)
        self.lbl_cita_total.setStyleSheet("border: none;")
        self.lbl_cita_total.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_cita_total.setObjectName("lbl_cita_total")
        self.verticalLayout_580.addWidget(self.lbl_cita_total)
        self.horizontalLayout_370.addWidget(self.frame_citatotal_numero)
        self.horizontalLayout_350.addWidget(self.fr_cita_total)
        self.gridLayout_40.addWidget(self.fr_patient_total, 1, 0, 1, 3)
        self.verticalLayout_490.addWidget(self.fr_estadisticas_1)
        self.fra_graphics = QtWidgets.QFrame(parent=self.frame_est_general)
        self.fra_graphics.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fra_graphics.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_graphics.setObjectName("fra_graphics")
        self.horizontalLayout_340 = QtWidgets.QHBoxLayout(self.fra_graphics)
        self.horizontalLayout_340.setObjectName("horizontalLayout_340")
        self.fra_grap1 = QtWidgets.QFrame(parent=self.fra_graphics)
        self.fra_grap1.setMinimumSize(QtCore.QSize(0, 200))
        self.fra_grap1.setMaximumSize(QtCore.QSize(16777215, 200))
        self.fra_grap1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border: 2px solid rgb(0, 0, 61);\n"
                                     "border-radius: 10px;")
        self.fra_grap1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fra_grap1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_grap1.setObjectName("fra_grap1")
        self.horizontalLayout_340.addWidget(self.fra_grap1)
        self.fra_grap2 = QtWidgets.QFrame(parent=self.fra_graphics)
        self.fra_grap2.setMinimumSize(QtCore.QSize(0, 200))
        self.fra_grap2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.fra_grap2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border: 2px solid rgb(0, 0, 61);\n"
                                     "border-radius: 10px;")
        self.fra_grap2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fra_grap2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_grap2.setObjectName("fra_grap2")
        self.horizontalLayout_340.addWidget(self.fra_grap2)
        self.fra_grap3 = QtWidgets.QFrame(parent=self.fra_graphics)
        self.fra_grap3.setMinimumSize(QtCore.QSize(0, 200))
        self.fra_grap3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.fra_grap3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border: 2px solid rgb(0, 0, 61);\n"
                                     "border-radius: 10px;")
        self.fra_grap3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fra_grap3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fra_grap3.setObjectName("fra_grap3")
        self.horizontalLayout_340.addWidget(self.fra_grap3)
        self.verticalLayout_490.addWidget(self.fra_graphics, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_estadisticasp_titulo = QtWidgets.QFrame(parent=self.frame_est_general)
        self.frame_estadisticasp_titulo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_estadisticasp_titulo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_estadisticasp_titulo.setObjectName("frame_estadisticasp_titulo")
        self.xd = QtWidgets.QHBoxLayout(self.frame_estadisticasp_titulo)
        self.xd.setObjectName("0")
        self.label_estadp_titulo = QtWidgets.QLabel(parent=self.frame_estadisticasp_titulo)
        self.label_estadp_titulo.setMaximumSize(QtCore.QSize(1250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(19)
        self.label_estadp_titulo.setFont(font)
        self.label_estadp_titulo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "border: 2px solid rgb(0, 0, 61);")
        self.label_estadp_titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_estadp_titulo.setObjectName("label_estadp_titulo")
        self.xd.addWidget(self.label_estadp_titulo)
        self.verticalLayout_490.addWidget(self.frame_estadisticasp_titulo)
        self.frame_comp_combo = QtWidgets.QFrame(parent=self.frame_est_general)
        self.frame_comp_combo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_comp_combo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_comp_combo.setObjectName("frame_comp_combo")
        self.gridLayout_50 = QtWidgets.QGridLayout(self.frame_comp_combo)
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.fr_est_tablep = QtWidgets.QFrame(parent=self.frame_comp_combo)
        self.fr_est_tablep.setMinimumSize(QtCore.QSize(0, 230))
        self.fr_est_tablep.setMaximumSize(QtCore.QSize(1250, 300))
        self.fr_est_tablep.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border: 2px solid rgb(0, 0, 61);")
        self.fr_est_tablep.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_est_tablep.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_est_tablep.setObjectName("fr_est_tablep")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.fr_est_tablep)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_paciente = QtWidgets.QLabel(parent=self.fr_est_tablep)
        self.label_paciente.setMinimumSize(QtCore.QSize(0, 50))
        self.label_paciente.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.label_paciente.setFont(font)
        self.label_paciente.setStyleSheet("border: 2px solid rgb(0, 0, 61);\n"
                                          "border-radius: 10px;\n"
                                          "background-color: rgb(0, 0, 61);\n"
                                          "color: white")
        self.label_paciente.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_paciente.setObjectName("label_paciente")
        self.gridLayout_20.addWidget(self.label_paciente, 1, 2, 1, 1)
        self.frame_void_2 = QtWidgets.QFrame(parent=self.fr_est_tablep)
        self.frame_void_2.setMaximumSize(QtCore.QSize(30, 2000))
        self.frame_void_2.setStyleSheet("border: none")
        self.frame_void_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_void_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_void_2.setObjectName("frame_void_2")
        self.gridLayout_20.addWidget(self.frame_void_2, 3, 0, 1, 1)
        self.label_cita1 = QtWidgets.QLabel(parent=self.fr_est_tablep)
        self.label_cita1.setMinimumSize(QtCore.QSize(0, 50))
        self.label_cita1.setMaximumSize(QtCore.QSize(16777215, 4000))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.label_cita1.setFont(font)
        self.label_cita1.setStyleSheet("border: 2px solid rgb(0, 0, 61);\n"
                                       "border-radius: 10px;\n"
                                       "background-color: rgb(0, 0, 61);\n"
                                       "color: white")
        self.label_cita1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cita1.setObjectName("label_cita1")
        self.gridLayout_20.addWidget(self.label_cita1, 3, 1, 1, 1)
        self.frame_void = QtWidgets.QFrame(parent=self.fr_est_tablep)
        self.frame_void.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_void.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_void.setStyleSheet("border: None")
        self.frame_void.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_void.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_void.setObjectName("frame_void")
        self.gridLayout_20.addWidget(self.frame_void, 5, 3, 1, 1)
        self.combobox_cita1 = QtWidgets.QComboBox(parent=self.fr_est_tablep)
        self.combobox_cita1.setMinimumSize(QtCore.QSize(0, 30))
        self.combobox_cita1.setMaximumSize(QtCore.QSize(500, 35))
        self.combobox_cita1.setStyleSheet("border: 2px solid rgb(0, 0, 61);\n"
                                          "border-radius: 3px;\n"
                                          "border-color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "")
        self.combobox_cita1.setObjectName("combobox_cita1")
        self.gridLayout_20.addWidget(self.combobox_cita1, 4, 1, 1, 1)
        self.frame_void_3 = QtWidgets.QFrame(parent=self.fr_est_tablep)
        self.frame_void_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_void_3.setStyleSheet("border: none")
        self.frame_void_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_void_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_void_3.setObjectName("frame_void_3")
        self.gridLayout_20.addWidget(self.frame_void_3, 3, 5, 1, 1)
        self.label_cita2 = QtWidgets.QLabel(parent=self.fr_est_tablep)
        self.label_cita2.setMinimumSize(QtCore.QSize(0, 50))
        self.label_cita2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.label_cita2.setFont(font)
        self.label_cita2.setStyleSheet("border: 2px solid rgb(0, 0, 61);\n"
                                       "border-radius: 10px;\n"
                                       "background-color: rgb(0, 0, 61);\n"
                                       "color: white")
        self.label_cita2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cita2.setObjectName("label_cita2")
        self.gridLayout_20.addWidget(self.label_cita2, 3, 2, 1, 1)
        self.comboBox__paciente1 = QtWidgets.QComboBox(parent=self.fr_est_tablep)
        self.comboBox__paciente1.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox__paciente1.setMaximumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(10)
        self.comboBox__paciente1.setFont(font)
        self.comboBox__paciente1.setStyleSheet("border: 2px solid rgb(0, 0, 61);\n"
                                               "border-radius: 3px;\n"
                                               "border-color: rgb(0, 0, 0);\n"
                                               "background-color: rgb(255, 255, 255);\n"
                                               "")
        self.comboBox__paciente1.setObjectName("comboBox__paciente1")
        self.comboBox__paciente1.addItem("---")
        self.gridLayout_20.addWidget(self.comboBox__paciente1, 2, 2, 1, 1)
        self.combobox_cita2 = QtWidgets.QComboBox(parent=self.fr_est_tablep)
        self.combobox_cita2.setMinimumSize(QtCore.QSize(0, 30))
        self.combobox_cita2.setMaximumSize(QtCore.QSize(500, 35))
        self.combobox_cita2.setStyleSheet("border: 2px solid rgb(0, 0, 61);\n"
                                          "border-radius: 3px;\n"
                                          "border-color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "")
        self.combobox_cita2.setObjectName("combobox_cita2")
        self.gridLayout_20.addWidget(self.combobox_cita2, 4, 2, 1, 1)
        self.label_dato = QtWidgets.QLabel(parent=self.fr_est_tablep)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.label_dato.setFont(font)
        self.label_dato.setStyleSheet("border: 2px solid rgb(0, 0, 61);\n"
                                      "border-radius: 10px;\n"
                                      "background-color: rgb(0, 0, 61);\n"
                                      "color: white")
        self.label_dato.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_dato.setObjectName("label_dato")
        self.gridLayout_20.addWidget(self.label_dato, 3, 3, 1, 1)
        self.combobox_dato = QtWidgets.QComboBox(parent=self.fr_est_tablep)
        self.combobox_dato.setMinimumSize(QtCore.QSize(0, 30))
        self.combobox_dato.setStyleSheet("border: 2px solid rgb(0, 0, 61);\n"
                                         "border-radius: 3px;\n"
                                         "border-color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "")
        self.combobox_dato.setObjectName("combobox_dato")
        self.gridLayout_20.addWidget(self.combobox_dato, 4, 3, 1, 1)
        self.gridLayout_50.addWidget(self.fr_est_tablep, 0, 0, 1, 1)
        self.verticalLayout_490.addWidget(self.frame_comp_combo)
        self.frame_btn_comparar = QtWidgets.QFrame(parent=self.frame_est_general)
        self.frame_btn_comparar.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_btn_comparar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_btn_comparar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_btn_comparar.setObjectName("frame_btn_comparar")
        self.btn_comparar = QtWidgets.QPushButton(parent=self.frame_btn_comparar)
        self.btn_comparar.setGeometry(QtCore.QRect(430, 0, 300, 50))
        self.btn_comparar.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_comparar.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(13)
        self.btn_comparar.setFont(font)
        self.btn_comparar.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(0, 0, 61);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 1px solid white;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(0, 0, 31);\n"
                                        "color: white;\n"
                                        "}")
        self.btn_comparar.setObjectName("btn_comparar")
        self.verticalLayout_490.addWidget(self.frame_btn_comparar)
        self.fr_est_citas = QtWidgets.QFrame(parent=self.frame_est_general)
        self.fr_est_citas.setMinimumSize(QtCore.QSize(0, 250))
        self.fr_est_citas.setMaximumSize(QtCore.QSize(16777215, 250))
        self.fr_est_citas.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fr_est_citas.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fr_est_citas.setObjectName("fr_est_citas")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.fr_est_citas)
        self.gridLayout_30.setHorizontalSpacing(6)
        self.gridLayout_30.setObjectName("gridLayout_30")

        self.plot = pg.plot()
        self.plot.setBackground("w")
        self.gridLayout_30.addWidget(self.plot, 0, 2, 1, 1)

        self.frame_comparacion = QtWidgets.QFrame(parent=self.fr_est_citas)
        self.frame_comparacion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border: 2px solid rgb(0, 0, 61);")
        self.frame_comparacion.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_comparacion.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_comparacion.setObjectName("frame_comparacion")
        self.verticalLayout0 = QtWidgets.QVBoxLayout(self.frame_comparacion)
        self.verticalLayout0.setObjectName("verticalLayout0")
        self.frame_comparacion_inter = QtWidgets.QFrame(parent=self.frame_comparacion)
        self.frame_comparacion_inter.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "border: none")
        self.frame_comparacion_inter.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_comparacion_inter.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_comparacion_inter.setObjectName("frame_comparacion_inter")
        self.horizontalLayout_440 = QtWidgets.QHBoxLayout(self.frame_comparacion_inter)
        self.horizontalLayout_440.setObjectName("horizontalLayout_440")
        self.frame_comparacion_color1 = QtWidgets.QFrame(parent=self.frame_comparacion_inter)
        self.frame_comparacion_color1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_comparacion_color1.setMinimumSize(QtCore.QSize(90, 90))
        self.frame_comparacion_color1.setStyleSheet("background-color: rgb(031, 119, 180);\n"
                                                    "border: 2px solid rgb(0, 0, 61);")
        self.frame_comparacion_color1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_comparacion_color1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_comparacion_color1.setObjectName("frame_comparacion_color1")
        self.horizontalLayout_440.addWidget(self.frame_comparacion_color1)
        self.frame_comparacion_up_r = QtWidgets.QFrame(parent=self.frame_comparacion_inter)
        self.frame_comparacion_up_r.setStyleSheet("border: none")
        self.frame_comparacion_up_r.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_comparacion_up_r.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_comparacion_up_r.setObjectName("frame_comparacion_up_r")
        self.verticalLayout_520 = QtWidgets.QVBoxLayout(self.frame_comparacion_up_r)
        self.verticalLayout_520.setObjectName("verticalLayout_520")
        self.label_dato1 = QtWidgets.QLabel(parent=self.frame_comparacion_up_r)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.label_dato1.setFont(font)
        self.label_dato1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border: 2px solid rgb(0, 0, 61);")
        self.label_dato1.setObjectName("label_dato1")
        self.verticalLayout_520.addWidget(self.label_dato1)
        self.horizontalLayout_440.addWidget(self.frame_comparacion_up_r)
        self.verticalLayout0.addWidget(self.frame_comparacion_inter)
        self.frame_comparacion_down = QtWidgets.QFrame(parent=self.frame_comparacion)
        self.frame_comparacion_down.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "border: none")
        self.frame_comparacion_down.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_comparacion_down.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_comparacion_down.setObjectName("frame_comparacion_down")
        self.horizontalLayout_450 = QtWidgets.QHBoxLayout(self.frame_comparacion_down)
        self.horizontalLayout_450.setObjectName("horizontalLayout_450")
        self.frame_comparacion_color2 = QtWidgets.QFrame(parent=self.frame_comparacion_down)
        self.frame_comparacion_color2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_comparacion_color2.setMinimumSize(QtCore.QSize(90, 90))
        self.frame_comparacion_color2.setStyleSheet("background-color: rgb(255, 127, 014);\n"
                                                    "border: 2px solid rgb(0, 0, 61);")
        self.frame_comparacion_color2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_comparacion_color2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_comparacion_color2.setObjectName("frame_comparacion_color2")
        self.horizontalLayout_450.addWidget(self.frame_comparacion_color2)
        self.frame_comparacion_down_r = QtWidgets.QFrame(parent=self.frame_comparacion_down)
        self.frame_comparacion_down_r.setStyleSheet("border: none")
        self.frame_comparacion_down_r.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_comparacion_down_r.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_comparacion_down_r.setObjectName("frame_comparacion_down_r")
        self.verticalLayout_600 = QtWidgets.QVBoxLayout(self.frame_comparacion_down_r)
        self.verticalLayout_600.setObjectName("verticalLayout_600")
        self.label_dato2 = QtWidgets.QLabel(parent=self.frame_comparacion_down_r)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.label_dato2.setFont(font)
        self.label_dato2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border: 2px solid rgb(0, 0, 61);")
        self.label_dato2.setObjectName("label_dato2")
        self.verticalLayout_600.addWidget(self.label_dato2)
        self.horizontalLayout_450.addWidget(self.frame_comparacion_down_r)
        self.verticalLayout0.addWidget(self.frame_comparacion_down)
        self.gridLayout_30.addWidget(self.frame_comparacion, 0, 0, 1, 1)
        self.frame_comparacion_dif = QtWidgets.QFrame(parent=self.fr_est_citas)
        self.frame_comparacion_dif.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_comparacion_dif.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "border: 2px solid rgb(0, 0, 61);")
        self.frame_comparacion_dif.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_comparacion_dif.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_comparacion_dif.setObjectName("frame_comparacion_dif")
        self.verticalLayout_610 = QtWidgets.QVBoxLayout(self.frame_comparacion_dif)
        self.verticalLayout_610.setObjectName("verticalLayout_610")
        self.label_comparacion_dif1 = QtWidgets.QLabel(parent=self.frame_comparacion_dif)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.label_comparacion_dif1.setFont(font)
        self.label_comparacion_dif1.setObjectName("label_comparacion_dif1")
        self.verticalLayout_610.addWidget(self.label_comparacion_dif1)
        self.label_comparacion_dif2 = QtWidgets.QLabel(parent=self.frame_comparacion_dif)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.label_comparacion_dif2.setFont(font)
        self.label_comparacion_dif2.setObjectName("label_comparacion_dif2")
        self.verticalLayout_610.addWidget(self.label_comparacion_dif2)
        self.label_comparacion_diftotal = QtWidgets.QLabel(parent=self.frame_comparacion_dif)
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(19)
        self.label_comparacion_diftotal.setFont(font)
        self.label_comparacion_diftotal.setObjectName("label_comparacion_diftotal")
        self.verticalLayout_610.addWidget(self.label_comparacion_diftotal)
        self.gridLayout_30.addWidget(self.frame_comparacion_dif, 0, 4, 1, 1)
        self.frame_void_5 = QtWidgets.QFrame(parent=self.fr_est_citas)
        self.frame_void_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_void_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_void_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_void_5.setObjectName("frame_void_5")
        self.gridLayout_30.addWidget(self.frame_void_5, 0, 1, 1, 1)
        self.frame_void_4 = QtWidgets.QFrame(parent=self.fr_est_citas)
        self.frame_void_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_void_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_void_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_void_4.setObjectName("frame_void_4")
        self.gridLayout_30.addWidget(self.frame_void_4, 0, 3, 1, 1)
        self.verticalLayout_490.addWidget(self.fr_est_citas)
        self.verticalLayout_480.addWidget(self.frame_est_general)
        self.est_scrollArea.setWidget(self.est_scrollAreaWidgetContents)
        self.verticalLayout_560.addWidget(self.est_scrollArea)
        self.content_estadisticas.addWidget(self.est_generales)
        self.verticalLayout_440.addWidget(self.content_estadisticas)
        self.content.addWidget(self.Estadisticas)
        self.Model3D = QtWidgets.QWidget()
        self.Model3D.setStyleSheet("")
        self.Model3D.setObjectName("Model3D")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Model3D)
        self.horizontalLayout_8.setContentsMargins(1, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_contenedor_izquierda = QtWidgets.QFrame(parent=self.Model3D)
        self.frame_contenedor_izquierda.setStyleSheet("background-color: rgb(27, 38, 59);\n"
                                                      "font: 650 10pt \"Roboto\";\n"
                                                      "color: white;\n"
                                                      "border: 1px solid rgb(27, 38, 59);\n"
                                                      "")
        self.frame_contenedor_izquierda.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_contenedor_izquierda.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_contenedor_izquierda.setObjectName("frame_contenedor_izquierda")
        self.lbl_foto = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.lbl_foto.setGeometry(QtCore.QRect(92, 50, 91, 91))
        self.lbl_foto.setStyleSheet("border: 1px solid black;\n"
                                    "border-radius: 600")
        self.lbl_foto.setText("")
        self.lbl_foto.setPixmap(QtGui.QPixmap("images/foto-p.png"))
        self.lbl_foto.setScaledContents(True)
        self.lbl_foto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_foto.setObjectName("lbl_foto")
        self.lbl_nombre = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.lbl_nombre.setGeometry(QtCore.QRect(64, 150, 141, 31))
        self.lbl_nombre.setStyleSheet("color: white;\n"
                                      "font: 650 10.5pt \"Roboto\";")
        self.lbl_nombre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.btn_tipo_paciente = QtWidgets.QPushButton(parent=self.frame_contenedor_izquierda)
        self.btn_tipo_paciente.setGeometry(QtCore.QRect(100, 187, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.btn_tipo_paciente.setFont(font)
        self.btn_tipo_paciente.setStyleSheet("background-color: rgb(154, 154, 231);\n"
                                             "color: white;\n"
                                             "border: 1px solid rgb(154, 154, 231);\n"
                                             "border-radius: 7;\n"
                                             "font: 700 9pt \"Roboto\";")
        self.btn_tipo_paciente.setObjectName("btn_tipo_paciente")
        self.lbl_linea = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.lbl_linea.setGeometry(QtCore.QRect(30, 210, 221, 20))
        self.lbl_linea.setStyleSheet("border-bottom: 1px solid gray;\n"
                                     "border-radius: 0")
        self.lbl_linea.setText("")
        self.lbl_linea.setObjectName("lbl_linea")
        self.lbl_info = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.lbl_info.setGeometry(QtCore.QRect(70, 236, 141, 31))
        self.lbl_info.setStyleSheet("color: white;\n"
                                    "font: 750 10pt \"Roboto\";")
        self.lbl_info.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_info.setObjectName("lbl_info")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_contenedor_izquierda)
        self.frame_2.setGeometry(QtCore.QRect(70, 282, 181, 33))
        self.frame_2.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setContentsMargins(2, 1, -1, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lbl_desc1 = QtWidgets.QLabel(parent=self.frame_2)
        self.lbl_desc1.setStyleSheet("font: 650 9pt \"Roboto\";\n"
                                     "color: rgb(207, 207, 207);")
        self.lbl_desc1.setObjectName("lbl_desc1")
        self.verticalLayout_10.addWidget(self.lbl_desc1)
        self.lbl_fecha = QtWidgets.QLabel(parent=self.frame_2)
        self.lbl_fecha.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.lbl_fecha.setObjectName("lbl_fecha")
        self.verticalLayout_10.addWidget(self.lbl_fecha)
        self.ico_fecha = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.ico_fecha.setGeometry(QtCore.QRect(30, 280, 36, 36))
        self.ico_fecha.setStyleSheet("border: 1px solid rgba(0, 232, 159, 0.4);\n"
                                     "border-radius: 18;\n"
                                     "background-color: rgba(0, 232, 159, 0.2);")
        self.ico_fecha.setText("")
        self.ico_fecha.setPixmap(QtGui.QPixmap("icons/calendar.svg"))
        self.ico_fecha.setScaledContents(True)
        self.ico_fecha.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ico_fecha.setIndent(-9)
        self.ico_fecha.setMargin(7)
        self.ico_fecha.setObjectName("ico_fecha")
        self.ico_documento = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.ico_documento.setGeometry(QtCore.QRect(30, 337, 36, 36))
        self.ico_documento.setStyleSheet("border: 1px solid  rgba(216, 160, 15, 0.4);\n"
                                         "border-radius: 18;\n"
                                         "background-color: rgba(216, 160, 15, 0.2);")
        self.ico_documento.setText("")
        self.ico_documento.setPixmap(QtGui.QPixmap("icons/document.svg"))
        self.ico_documento.setScaledContents(True)
        self.ico_documento.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ico_documento.setIndent(-9)
        self.ico_documento.setMargin(7)
        self.ico_documento.setObjectName("ico_documento")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_contenedor_izquierda)
        self.frame_4.setGeometry(QtCore.QRect(70, 338, 181, 33))
        self.frame_4.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_43.setContentsMargins(2, 1, -1, 0)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.lbl_desc2 = QtWidgets.QLabel(parent=self.frame_4)
        self.lbl_desc2.setStyleSheet("font: 650 9pt \"Roboto\";\n"
                                     "color: rgb(207, 207, 207);")
        self.lbl_desc2.setObjectName("lbl_desc2")
        self.verticalLayout_43.addWidget(self.lbl_desc2)
        self.lbl_documento = QtWidgets.QLabel(parent=self.frame_4)
        self.lbl_documento.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.lbl_documento.setObjectName("lbl_documento")
        self.verticalLayout_43.addWidget(self.lbl_documento)
        self.ico_edad = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.ico_edad.setGeometry(QtCore.QRect(30, 394, 36, 36))
        self.ico_edad.setStyleSheet("border: 1px solid rgba(0, 91, 186, 0.4);\n"
                                    "border-radius: 18;\n"
                                    "background-color: rgba(0, 91, 186, 0.2);")
        self.ico_edad.setText("")
        self.ico_edad.setPixmap(QtGui.QPixmap("icons/age.svg"))
        self.ico_edad.setScaledContents(True)
        self.ico_edad.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ico_edad.setIndent(-9)
        self.ico_edad.setMargin(7)
        self.ico_edad.setObjectName("ico_edad")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_contenedor_izquierda)
        self.frame_5.setGeometry(QtCore.QRect(70, 397, 181, 33))
        self.frame_5.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_44.setContentsMargins(2, 1, -1, 0)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.lbl_desc3 = QtWidgets.QLabel(parent=self.frame_5)
        self.lbl_desc3.setStyleSheet("font: 650 9pt \"Roboto\";\n"
                                     "color: rgb(207, 207, 207);")
        self.lbl_desc3.setObjectName("lbl_desc3")
        self.verticalLayout_44.addWidget(self.lbl_desc3)
        self.lbl_edad = QtWidgets.QLabel(parent=self.frame_5)
        self.lbl_edad.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.lbl_edad.setObjectName("lbl_edad")
        self.verticalLayout_44.addWidget(self.lbl_edad)
        self.ico_peso = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.ico_peso.setGeometry(QtCore.QRect(30, 452, 36, 36))
        self.ico_peso.setStyleSheet("border: 1px solid rgba(109, 87, 222, 0.2);\n"
                                    "border-radius: 18;\n"
                                    "background-color: rgba(109, 87, 222, 0.2);")
        self.ico_peso.setText("")
        self.ico_peso.setPixmap(QtGui.QPixmap("icons/weight.svg"))
        self.ico_peso.setScaledContents(True)
        self.ico_peso.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ico_peso.setIndent(-9)
        self.ico_peso.setMargin(7)
        self.ico_peso.setObjectName("ico_peso")
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_contenedor_izquierda)
        self.frame_6.setGeometry(QtCore.QRect(70, 456, 181, 33))
        self.frame_6.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_45.setContentsMargins(2, 0, -1, 1)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.lbl_desc4 = QtWidgets.QLabel(parent=self.frame_6)
        self.lbl_desc4.setStyleSheet("font: 650 9pt \"Roboto\";\n"
                                     "color: rgb(207, 207, 207);")
        self.lbl_desc4.setObjectName("lbl_desc4")
        self.verticalLayout_45.addWidget(self.lbl_desc4)
        self.lbl_peso = QtWidgets.QLabel(parent=self.frame_6)
        self.lbl_peso.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.lbl_peso.setObjectName("lbl_peso")
        self.verticalLayout_45.addWidget(self.lbl_peso)
        self.ico_estatura = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.ico_estatura.setGeometry(QtCore.QRect(30, 512, 36, 36))
        self.ico_estatura.setStyleSheet("border: 1px solid rgba(222, 38, 136, 0.4);\n"
                                        "border-radius: 18;\n"
                                        "background-color: rgba(222, 38, 136, 0.2);")
        self.ico_estatura.setText("")
        self.ico_estatura.setPixmap(QtGui.QPixmap("icons/height.svg"))
        self.ico_estatura.setScaledContents(True)
        self.ico_estatura.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ico_estatura.setIndent(-9)
        self.ico_estatura.setMargin(7)
        self.ico_estatura.setObjectName("ico_estatura")
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_contenedor_izquierda)
        self.frame_7.setGeometry(QtCore.QRect(70, 514, 181, 33))
        self.frame_7.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_46.setContentsMargins(2, 1, -1, 0)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.lbl_desc5 = QtWidgets.QLabel(parent=self.frame_7)
        self.lbl_desc5.setStyleSheet("font: 650 9pt \"Roboto\";\n"
                                     "color: rgb(207, 207, 207);")
        self.lbl_desc5.setObjectName("lbl_desc5")
        self.verticalLayout_46.addWidget(self.lbl_desc5)
        self.lbl_estatura = QtWidgets.QLabel(parent=self.frame_7)
        self.lbl_estatura.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.lbl_estatura.setObjectName("lbl_estatura")
        self.verticalLayout_46.addWidget(self.lbl_estatura)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_contenedor_izquierda)
        self.frame_8.setGeometry(QtCore.QRect(70, 572, 181, 33))
        self.frame_8.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_47.setContentsMargins(2, 1, -1, 0)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.lbl_desc6 = QtWidgets.QLabel(parent=self.frame_8)
        self.lbl_desc6.setStyleSheet("font: 650 9pt \"Roboto\";\n"
                                     "color: rgb(207, 207, 207);")
        self.lbl_desc6.setObjectName("lbl_desc6")
        self.verticalLayout_47.addWidget(self.lbl_desc6)
        self.lbl_telefono = QtWidgets.QLabel(parent=self.frame_8)
        self.lbl_telefono.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.lbl_telefono.setObjectName("lbl_telefono")
        self.verticalLayout_47.addWidget(self.lbl_telefono)
        self.ico_telefono = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.ico_telefono.setGeometry(QtCore.QRect(30, 570, 36, 36))
        self.ico_telefono.setStyleSheet("border: 1px solid rgba(198, 87, 59, 0.2);\n"
                                        "border-radius: 18;\n"
                                        "background-color: rgba(198, 87, 59, 0.2);")
        self.ico_telefono.setText("")
        self.ico_telefono.setPixmap(QtGui.QPixmap("icons/phone.svg"))
        self.ico_telefono.setScaledContents(True)
        self.ico_telefono.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ico_telefono.setIndent(-9)
        self.ico_telefono.setMargin(7)
        self.ico_telefono.setObjectName("ico_telefono")
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_contenedor_izquierda)
        self.frame_9.setGeometry(QtCore.QRect(220, 773, 181, 31))
        self.frame_9.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_48.setContentsMargins(2, 1, -1, 0)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.label_26 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_26.setStyleSheet("font: 650 9pt \"Roboto\";\n"
                                    "color: rgb(207, 207, 207);")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_48.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_27.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_48.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.label_28.setGeometry(QtCore.QRect(180, 770, 36, 36))
        self.label_28.setStyleSheet("border: 1px solid rgba(0, 232, 159, 0.4);\n"
                                    "border-radius: 18;\n"
                                    "background-color: rgba(0, 232, 159, 0.2);")
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("icons/calendar.svg"))
        self.label_28.setScaledContents(True)
        self.label_28.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_28.setIndent(-9)
        self.label_28.setObjectName("label_28")
        self.frame_10 = QtWidgets.QFrame(parent=self.frame_contenedor_izquierda)
        self.frame_10.setGeometry(QtCore.QRect(70, 628, 181, 33))
        self.frame_10.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_55.setContentsMargins(2, 1, -1, 0)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.lbl_desc7 = QtWidgets.QLabel(parent=self.frame_10)
        self.lbl_desc7.setStyleSheet("font: 650 9pt \"Roboto\";\n"
                                     "color: rgb(207, 207, 207);\n"
                                     "")
        self.lbl_desc7.setObjectName("lbl_desc7")
        self.verticalLayout_55.addWidget(self.lbl_desc7)
        self.lbl_actividad_fisica = QtWidgets.QLabel(parent=self.frame_10)
        self.lbl_actividad_fisica.setStyleSheet("font: 750 9pt \"Roboto\";")
        self.lbl_actividad_fisica.setObjectName("lbl_actividad_fisica")
        self.verticalLayout_55.addWidget(self.lbl_actividad_fisica)
        self.ico_actividad = QtWidgets.QLabel(parent=self.frame_contenedor_izquierda)
        self.ico_actividad.setGeometry(QtCore.QRect(30, 626, 36, 36))
        self.ico_actividad.setStyleSheet("border: 1px solid rgba(58, 141, 123, 0.4);\n"
                                         "border-radius: 18;\n"
                                         "background-color: rgba(58, 141, 123, 0.2);")
        self.ico_actividad.setText("")
        self.ico_actividad.setPixmap(QtGui.QPixmap("icons/fitness.svg"))
        self.ico_actividad.setScaledContents(True)
        self.ico_actividad.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ico_actividad.setIndent(-9)
        self.ico_actividad.setMargin(8)
        self.ico_actividad.setObjectName("ico_actividad")
        self.horizontalLayout_8.addWidget(self.frame_contenedor_izquierda)
        self.frame_visor3d = QtWidgets.QFrame(parent=self.Model3D)
        self.frame_visor3d.setStyleSheet("")
        self.frame_visor3d.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_visor3d.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_visor3d.setObjectName("frame_visor3d")
        self.verticalLayout_frame3d = QtWidgets.QVBoxLayout(self.frame_visor3d)
        self.verticalLayout_frame3d.setObjectName("verticalLayout_frame3d")
        self.horizontalLayout_8.addWidget(self.frame_visor3d)
        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 10)
        self.content.addWidget(self.Model3D)
        self.Export = QtWidgets.QWidget()
        self.Export.setObjectName("Export")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.Export)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_bdd = QtWidgets.QFrame(parent=self.Export)
        self.frame_bdd.setStyleSheet("QFrame {\n"
                                     "    font: 11pt \"Roboto\";\n"
                                     "}")
        self.frame_bdd.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_bdd.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_bdd.setObjectName("frame_bdd")
        self.top_frame = QtWidgets.QFrame(parent=self.frame_bdd)
        self.top_frame.setGeometry(QtCore.QRect(0, 0, 1241, 61))
        self.top_frame.setStyleSheet("QFrame {\n"
                                     "    background-color: white;\n"
                                     "    border: 1px solid rgba(0,0,0, 0.3);\n"
                                     "    border-bottom:2px solid rgba(0,0,0, 0.3);\n"
                                     "}")
        self.top_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.top_frame.setObjectName("top_frame")
        self.label_7 = QtWidgets.QLabel(parent=self.top_frame)
        self.label_7.setGeometry(QtCore.QRect(80, 20, 171, 21))
        self.label_7.setStyleSheet("font-weight: 650;\n"
                                   "font-size: 13.5pt;\n"
                                   "color: rgba(0,0,0, 0.7);\n"
                                   "border: none;")
        self.label_7.setObjectName("label_7")
        self.btn_bdd_backup = QtWidgets.QPushButton(parent=self.top_frame)
        self.btn_bdd_backup.setGeometry(QtCore.QRect(870, 10, 151, 41))
        self.btn_bdd_backup.setStyleSheet("QPushButton {\n"
                                          "    color:     white;\n"
                                          "    font-weight: 550;\n"
                                          "    background-color: rgb(27, 38, 59);\n"
                                          "    border-radius: 5px;\n"
                                          "    font-size: 9.5pt;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgb(0, 0, 61);\n"
                                          "}"
                                          )
        self.btn_bdd_backup.setObjectName("btn_bdd_backup")
        self.btn_bdd_restaurar = QtWidgets.QPushButton(parent=self.top_frame)
        self.btn_bdd_restaurar.setGeometry(QtCore.QRect(1040, 10, 131, 41))
        self.btn_bdd_restaurar.setStyleSheet("QPushButton {\n"
                                             "    color:     white;\n"
                                             "    font-weight: 550;\n"
                                             "    \n"
                                             "    background-color: rgb(170, 170, 255);\n"
                                             "    border-radius: 5px;\n"
                                             "    font-size: 9.5pt;\n"
                                             "}\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgb(0, 0, 61);\n"
                                          "}"
                                            )
        self.btn_bdd_restaurar.setObjectName("btn_bdd_restaurar")
        self.ico_reportes_principal_2 = QtWidgets.QLabel(parent=self.top_frame)
        self.ico_reportes_principal_2.setGeometry(QtCore.QRect(30, 12, 36, 36))
        self.ico_reportes_principal_2.setStyleSheet("border: 1px solid rgba(0, 91, 186, 0.4);\n"
                                                    "background-color: rgba(27, 38, 59, 0.9);\n"
                                                    "border-radius: 5px;")
        self.ico_reportes_principal_2.setText("")
        self.ico_reportes_principal_2.setPixmap(QtGui.QPixmap("icons/database_icon.svg"))
        self.ico_reportes_principal_2.setScaledContents(True)
        self.ico_reportes_principal_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ico_reportes_principal_2.setIndent(-9)
        self.ico_reportes_principal_2.setMargin(5)
        self.ico_reportes_principal_2.setObjectName("ico_reportes_principal_2")
        self.frame_bdd_info_2 = QtWidgets.QFrame(parent=self.frame_bdd)
        self.frame_bdd_info_2.setGeometry(QtCore.QRect(380, 100, 181, 181))
        self.frame_bdd_info_2.setStyleSheet("background-color: white;\n"
                                            "border-radius: 10px;\n"
                                            "border: 1px solid rgba(0,0,0, 0.1)")
        self.frame_bdd_info_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_bdd_info_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_bdd_info_2.setLineWidth(3)
        self.frame_bdd_info_2.setObjectName("frame_bdd_info_2")
        self.label_fecha_bdd = QtWidgets.QLabel(parent=self.frame_bdd_info_2)
        self.label_fecha_bdd.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.label_fecha_bdd.setStyleSheet("font-size: 16pt;\n"
                                           "font-weight: 550;\n"
                                           "border: none;")
        self.label_fecha_bdd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_fecha_bdd.setObjectName("label_fecha_bdd")
        self.lbl_pacientes_s_6 = QtWidgets.QLabel(parent=self.frame_bdd_info_2)
        self.lbl_pacientes_s_6.setGeometry(QtCore.QRect(20, 128, 141, 20))
        self.lbl_pacientes_s_6.setStyleSheet("font-size: 10pt;\n"
                                             "color: rgba(0,0, 0, 0.7);\n"
                                             "border: none;")
        self.lbl_pacientes_s_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_pacientes_s_6.setObjectName("lbl_pacientes_s_6")
        self.lbl_icono_bdd_2 = QtWidgets.QLabel(parent=self.frame_bdd_info_2)
        self.lbl_icono_bdd_2.setGeometry(QtCore.QRect(53, 30, 71, 61))
        self.lbl_icono_bdd_2.setStyleSheet("border: none;")
        self.lbl_icono_bdd_2.setText("")
        self.lbl_icono_bdd_2.setPixmap(QtGui.QPixmap("icons/calendario_rojo.png"))
        self.lbl_icono_bdd_2.setScaledContents(True)
        self.lbl_icono_bdd_2.setObjectName("lbl_icono_bdd_2")
        self.frame_reportes_info_7 = QtWidgets.QFrame(parent=self.frame_bdd)
        self.frame_reportes_info_7.setGeometry(QtCore.QRect(670, 100, 181, 181))
        self.frame_reportes_info_7.setStyleSheet("background-color: white;\n"
                                                 "border-radius: 10px;\n"
                                                 "border: 1px solid rgba(0,0,0, 0.1)")
        self.frame_reportes_info_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_reportes_info_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_reportes_info_7.setLineWidth(3)
        self.frame_reportes_info_7.setObjectName("frame_reportes_info_7")
        self.label_pacientes_totales = QtWidgets.QLabel(parent=self.frame_reportes_info_7)
        self.label_pacientes_totales.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.label_pacientes_totales.setStyleSheet("font-size: 16pt;\n"
                                                   "font-weight: 550;\n"
                                                   "border: none;")
        self.label_pacientes_totales.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_pacientes_totales.setObjectName("label_pacientes_totales")
        self.lbl_pacientes_s_8 = QtWidgets.QLabel(parent=self.frame_reportes_info_7)
        self.lbl_pacientes_s_8.setGeometry(QtCore.QRect(20, 128, 141, 21))
        self.lbl_pacientes_s_8.setStyleSheet("font-size: 10pt;\n"
                                             "color: rgba(0,0, 0, 0.7);\n"
                                             "border: none;")
        self.lbl_pacientes_s_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_pacientes_s_8.setObjectName("lbl_pacientes_s_8")
        self.lbl_icono_bdd_3 = QtWidgets.QLabel(parent=self.frame_reportes_info_7)
        self.lbl_icono_bdd_3.setGeometry(QtCore.QRect(60, 34, 61, 61))
        self.lbl_icono_bdd_3.setStyleSheet("border: none;")
        self.lbl_icono_bdd_3.setText("")
        self.lbl_icono_bdd_3.setPixmap(QtGui.QPixmap("icons/age.svg"))
        self.lbl_icono_bdd_3.setScaledContents(True)
        self.lbl_icono_bdd_3.setObjectName("lbl_icono_bdd_3")
        self.frame_reportes_info_9 = QtWidgets.QFrame(parent=self.frame_bdd)
        self.frame_reportes_info_9.setGeometry(QtCore.QRect(940, 100, 181, 181))
        self.frame_reportes_info_9.setStyleSheet("background-color: white;\n"
                                                 "border-radius: 10px;\n"
                                                 "border: 1px solid rgba(0,0,0, 0.1)")
        self.frame_reportes_info_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_reportes_info_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_reportes_info_9.setLineWidth(3)
        self.frame_reportes_info_9.setObjectName("frame_reportes_info_9")
        self.label_contador_bdd_2 = QtWidgets.QLabel(parent=self.frame_reportes_info_9)
        self.label_contador_bdd_2.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.label_contador_bdd_2.setStyleSheet("font-size: 16pt;\n"
                                                "font-weight: 550;\n"
                                                "border: none;")
        self.label_contador_bdd_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_contador_bdd_2.setObjectName("label_contador_bdd_2")
        self.lbl_pacientes_s_10 = QtWidgets.QLabel(parent=self.frame_reportes_info_9)
        self.lbl_pacientes_s_10.setGeometry(QtCore.QRect(10, 130, 161, 20))
        self.lbl_pacientes_s_10.setStyleSheet("font-size: 10pt;\n"
                                              "color: rgba(0,0, 0, 0.7);\n"
                                              "border: none;")
        self.lbl_pacientes_s_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_pacientes_s_10.setObjectName("lbl_pacientes_s_10")
        self.lbl_icono_bdd_4 = QtWidgets.QLabel(parent=self.frame_reportes_info_9)
        self.lbl_icono_bdd_4.setGeometry(QtCore.QRect(59, 36, 61, 61))
        self.lbl_icono_bdd_4.setStyleSheet("border: none;")
        self.lbl_icono_bdd_4.setText("")
        self.lbl_icono_bdd_4.setPixmap(QtGui.QPixmap("icons/document.svg"))
        self.lbl_icono_bdd_4.setScaledContents(True)
        self.lbl_icono_bdd_4.setObjectName("lbl_icono_bdd_4")
        self.frame_bdd_info = QtWidgets.QFrame(parent=self.frame_bdd)
        self.frame_bdd_info.setGeometry(QtCore.QRect(100, 100, 181, 181))
        self.frame_bdd_info.setStyleSheet("background-color: white;\n"
                                          "border-radius: 10px;\n"
                                          "border: 1px solid rgba(0,0,0, 0.1)")
        self.frame_bdd_info.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_bdd_info.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_bdd_info.setLineWidth(3)
        self.frame_bdd_info.setObjectName("frame_bdd_info")
        self.label_contador_bdd = QtWidgets.QLabel(parent=self.frame_bdd_info)
        self.label_contador_bdd.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.label_contador_bdd.setStyleSheet("font-size: 16pt;\n"
                                              "font-weight: 550;\n"
                                              "border: none;")
        self.label_contador_bdd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_contador_bdd.setObjectName("label_contador_bdd")
        self.lbl_bdd_s = QtWidgets.QLabel(parent=self.frame_bdd_info)
        self.lbl_bdd_s.setGeometry(QtCore.QRect(26, 128, 131, 20))
        self.lbl_bdd_s.setStyleSheet("font-size: 10pt;\n"
                                     "color: rgba(0,0, 0, 0.7);\n"
                                     "border: none;")
        self.lbl_bdd_s.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_bdd_s.setObjectName("lbl_bdd_s")
        self.lbl_icono_bdd = QtWidgets.QLabel(parent=self.frame_bdd_info)
        self.lbl_icono_bdd.setGeometry(QtCore.QRect(60, 40, 61, 51))
        self.lbl_icono_bdd.setStyleSheet("border: none;")
        self.lbl_icono_bdd.setText("")
        self.lbl_icono_bdd.setPixmap(QtGui.QPixmap("images/table_img.png"))
        self.lbl_icono_bdd.setScaledContents(True)
        self.lbl_icono_bdd.setObjectName("lbl_icono_bdd")
        self.tabla_bdd = QtWidgets.QTableWidget(parent=self.frame_bdd)
        self.tabla_bdd.setGeometry(QtCore.QRect(60, 330, 1131, 331))
        self.tabla_bdd.setStyleSheet("QTableWidget {\n"
                                     "    background-color: #FFFFFF;\n"
                                     "    alternate-background-color: #F0F0F0;\n"
                                     "    color: #212121;\n"
                                     "    gridline-color: #DCDCDC;\n"
                                     "    selection-color-background: #FF4081;\n"
                                     "    selection-color: #ffffff;\n"
                                     "    border-radius: 10px\n"
                                     "}\n"
                                     "\n"
                                     "QTableWidget::item {\n"
                                     "    padding: 4px;\n"
                                     "}\n"
                                     "\n"
                                     "QHeaderView::section {\n"
                                     "    background-color: rgb(27, 38, 59);\n"
                                     "    color: #FFFFFF;\n"
                                     "    padding: 12px;\n"
                                     "    font-weight: bold;\n"
                                     "    font-size: 9pt;\n"
                                     "    border: none;\n"
                                     "    border-bottom: 1px solid gray;\n"
                                     "}\n"
                                     "\n"
                                     "QHeaderView::section:first {\n"
                                     "     border-radius: 4px;\n"
                                     "}\n"
                                     "\n"
                                     "QHeaderView::section:last {\n"
                                     "     border-radius: 4px;\n"
                                     "}")
        self.tabla_bdd.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tabla_bdd.setAlternatingRowColors(True)
        self.tabla_bdd.setShowGrid(False)
        self.tabla_bdd.setObjectName("tabla_bdd")
        self.tabla_bdd.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_bdd.setHorizontalHeaderItem(4, item)
        self.tabla_bdd.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_bdd.horizontalHeader().setDefaultSectionSize(195)
        self.tabla_bdd.horizontalHeader().setMinimumSectionSize(36)
        self.tabla_bdd.horizontalHeader().setSortIndicatorShown(False)
        self.tabla_bdd.horizontalHeader().setStretchLastSection(True)
        self.tabla_bdd.verticalHeader().setVisible(False)
        self.tabla_bdd.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_bdd.verticalHeader().setDefaultSectionSize(36)
        self.tabla_bdd.verticalHeader().setMinimumSectionSize(25)
        self.tabla_bdd.verticalHeader().setSortIndicatorShown(True)
        self.tabla_bdd.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_25.addWidget(self.frame_bdd)
        self.content.addWidget(self.Export)
        self.Import = QtWidgets.QWidget()
        self.Import.setObjectName("Import")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.Import)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_reportes = QtWidgets.QFrame(parent=self.Import)
        self.frame_reportes.setStyleSheet("QFrame {\n"
                                          "    font: 11pt \"Roboto\";\n"
                                          "}")
        self.frame_reportes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_reportes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_reportes.setObjectName("frame_reportes")
        self.frame_14 = QtWidgets.QFrame(parent=self.frame_reportes)
        self.frame_14.setGeometry(QtCore.QRect(0, 0, 1241, 61))
        self.frame_14.setStyleSheet("QFrame {\n"
                                    "    background-color: white;\n"
                                    "    border: 1px solid rgba(0,0,0, 0.3);\n"
                                    "    border-bottom:2px solid rgba(0,0,0, 0.3);\n"
                                    "}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_14)
        self.label_6.setGeometry(QtCore.QRect(80, 20, 171, 21))
        self.label_6.setStyleSheet("font-weight: 650;\n"
                                   "font-size: 13.5pt;\n"
                                   "color: rgba(0,0,0, 0.7);\n"
                                   "border: none;")
        self.label_6.setObjectName("label_6")
        self.btn_reportes_generar = QtWidgets.QPushButton(parent=self.frame_14)
        self.btn_reportes_generar.setGeometry(QtCore.QRect(870, 10, 151, 41))
        self.btn_reportes_generar.setStyleSheet("QPushButton {\n"
                                                "    color:     white;\n"
                                                "    font-weight: 550;\n"
                                                "    background-color: rgb(27, 38, 59);\n"
                                                "    border-radius: 5px;\n"
                                                "    font-size: 9.5pt;\n"
                                                "}\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgb(0, 0, 61);\n"
                                          "}")
        self.btn_reportes_generar.setObjectName("btn_reportes_generar")
        self.btn_reportes_vp = QtWidgets.QPushButton(parent=self.frame_14)
        self.btn_reportes_vp.setGeometry(QtCore.QRect(1040, 10, 131, 41))
        self.btn_reportes_vp.setStyleSheet("QPushButton {\n"
                                           "    color:     black;\n"
                                           "    font-weight: 550;\n"
                                           "    background-color: white;\n"
                                           "    border-radius: 5px;\n"
                                           "    font-size: 9.5pt;\n"
                                           "    border: 1px solid red;\n"
                                           "}\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgb(0, 0, 61);\n"
                                          "}")
        self.btn_reportes_vp.setObjectName("btn_reportes_vp")
        self.ico_reportes_principal = QtWidgets.QLabel(parent=self.frame_14)
        self.ico_reportes_principal.setGeometry(QtCore.QRect(30, 12, 36, 36))
        self.ico_reportes_principal.setStyleSheet("border: 1px solid rgba(0, 91, 186, 0.4);\n"
                                                  "background-color: rgba(0, 91, 186, 0.9);\n"
                                                  "border-radius: 15px;")
        self.ico_reportes_principal.setText("")
        self.ico_reportes_principal.setPixmap(QtGui.QPixmap("icons/import.png"))
        self.ico_reportes_principal.setScaledContents(True)
        self.ico_reportes_principal.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ico_reportes_principal.setMargin(5)
        self.ico_reportes_principal.setIndent(-9)
        self.ico_reportes_principal.setObjectName("ico_reportes_principal")
        self.frame_reportes_info_4 = QtWidgets.QFrame(parent=self.frame_reportes)
        self.frame_reportes_info_4.setGeometry(QtCore.QRect(380, 100, 181, 181))
        self.frame_reportes_info_4.setStyleSheet("background-color: white;\n"
                                                 "border-radius: 10px;\n"
                                                 "border: 1px solid rgba(0,0,0, 0.1)")
        self.frame_reportes_info_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_reportes_info_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_reportes_info_4.setLineWidth(3)
        self.frame_reportes_info_4.setObjectName("frame_reportes_info_4")
        self.label_contador_pacientes_totales = QtWidgets.QLabel(parent=self.frame_reportes_info_4)
        self.label_contador_pacientes_totales.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.label_contador_pacientes_totales.setStyleSheet("font-size: 16pt;\n"
                                                            "font-weight: 550;\n"
                                                            "border: none;")
        self.label_contador_pacientes_totales.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_contador_pacientes_totales.setObjectName("label_contador_pacientes_totales")
        self.lbl_pacientes_s_5 = QtWidgets.QLabel(parent=self.frame_reportes_info_4)
        self.lbl_pacientes_s_5.setGeometry(QtCore.QRect(30, 133, 131, 20))
        self.lbl_pacientes_s_5.setStyleSheet("font-size: 10pt;\n"
                                             "color: rgba(0,0, 0, 0.7);\n"
                                             "border: none;")
        self.lbl_pacientes_s_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_pacientes_s_5.setObjectName("lbl_pacientes_s_5")
        self.lbl_icono_reportes_5 = QtWidgets.QLabel(parent=self.frame_reportes_info_4)
        self.lbl_icono_reportes_5.setGeometry(QtCore.QRect(55, 20, 71, 81))
        self.lbl_icono_reportes_5.setStyleSheet("border: none;")
        self.lbl_icono_reportes_5.setText("")
        self.lbl_icono_reportes_5.setPixmap(QtGui.QPixmap("icons/pacientes_morado.png"))
        self.lbl_icono_reportes_5.setScaledContents(True)
        self.lbl_icono_reportes_5.setObjectName("lbl_icono_reportes_5")
        self.frame_reportes_info_6 = QtWidgets.QFrame(parent=self.frame_reportes)
        self.frame_reportes_info_6.setGeometry(QtCore.QRect(670, 100, 181, 181))
        self.frame_reportes_info_6.setStyleSheet("background-color: white;\n"
                                                 "border-radius: 10px;\n"
                                                 "border: 1px solid rgba(0,0,0, 0.1)")
        self.frame_reportes_info_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_reportes_info_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_reportes_info_6.setLineWidth(3)
        self.frame_reportes_info_6.setObjectName("frame_reportes_info_6")
        self.label_contador_pacientes_adultos = QtWidgets.QLabel(parent=self.frame_reportes_info_6)
        self.label_contador_pacientes_adultos.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.label_contador_pacientes_adultos.setStyleSheet("font-size: 16pt;\n"
                                                            "font-weight: 550;\n"
                                                            "border: none;")
        self.label_contador_pacientes_adultos.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_contador_pacientes_adultos.setObjectName("label_contador_pacientes_adultos")
        self.lbl_pacientes_s_7 = QtWidgets.QLabel(parent=self.frame_reportes_info_6)
        self.lbl_pacientes_s_7.setGeometry(QtCore.QRect(20, 128, 141, 21))
        self.lbl_pacientes_s_7.setStyleSheet("font-size: 10pt;\n"
                                             "color: rgba(0,0, 0, 0.7);\n"
                                             "border: none;")
        self.lbl_pacientes_s_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_pacientes_s_7.setObjectName("lbl_pacientes_s_7")
        self.lbl_icono_reportes_7 = QtWidgets.QLabel(parent=self.frame_reportes_info_6)
        self.lbl_icono_reportes_7.setGeometry(QtCore.QRect(55, 24, 71, 71))
        self.lbl_icono_reportes_7.setStyleSheet("border: none;")
        self.lbl_icono_reportes_7.setText("")
        self.lbl_icono_reportes_7.setPixmap(QtGui.QPixmap("images/person_img.png"))
        self.lbl_icono_reportes_7.setScaledContents(True)
        self.lbl_icono_reportes_7.setObjectName("lbl_icono_reportes_7")
        self.frame_reportes_info_8 = QtWidgets.QFrame(parent=self.frame_reportes)
        self.frame_reportes_info_8.setGeometry(QtCore.QRect(940, 100, 181, 181))
        self.frame_reportes_info_8.setStyleSheet("background-color: white;\n"
                                                 "border-radius: 10px;\n"
                                                 "border: 1px solid rgba(0,0,0, 0.1)")
        self.frame_reportes_info_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_reportes_info_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_reportes_info_8.setLineWidth(3)
        self.frame_reportes_info_8.setObjectName("frame_reportes_info_8")
        self.label_contador_pacientes_atletas = QtWidgets.QLabel(parent=self.frame_reportes_info_8)
        self.label_contador_pacientes_atletas.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.label_contador_pacientes_atletas.setStyleSheet("font-size: 16pt;\n"
                                                            "font-weight: 550;\n"
                                                            "border: none;")
        self.label_contador_pacientes_atletas.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_contador_pacientes_atletas.setObjectName("label_contador_pacientes_atletas")
        self.lbl_pacientes_s_9 = QtWidgets.QLabel(parent=self.frame_reportes_info_8)
        self.lbl_pacientes_s_9.setGeometry(QtCore.QRect(20, 130, 141, 20))
        self.lbl_pacientes_s_9.setStyleSheet("font-size: 10pt;\n"
                                             "color: rgba(0,0, 0, 0.7);\n"
                                             "border: none;")
        self.lbl_pacientes_s_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_pacientes_s_9.setObjectName("lbl_pacientes_s_9")
        self.lbl_icono_reportes_9 = QtWidgets.QLabel(parent=self.frame_reportes_info_8)
        self.lbl_icono_reportes_9.setGeometry(QtCore.QRect(59, 36, 61, 51))
        self.lbl_icono_reportes_9.setStyleSheet("border: none;")
        self.lbl_icono_reportes_9.setText("")
        self.lbl_icono_reportes_9.setPixmap(QtGui.QPixmap("icons/pesas_verde_fullimg.png"))
        self.lbl_icono_reportes_9.setScaledContents(True)
        self.lbl_icono_reportes_9.setObjectName("lbl_icono_reportes_9")
        self.frame_reportes_info_3 = QtWidgets.QFrame(parent=self.frame_reportes)
        self.frame_reportes_info_3.setGeometry(QtCore.QRect(100, 100, 181, 181))
        self.frame_reportes_info_3.setStyleSheet("background-color: white;\n"
                                                 "border-radius: 10px;\n"
                                                 "border: 1px solid rgba(0,0,0, 0.1)")
        self.frame_reportes_info_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_reportes_info_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_reportes_info_3.setLineWidth(3)
        self.frame_reportes_info_3.setObjectName("frame_reportes_info_3")
        self.label_contador_pacientes_3 = QtWidgets.QLabel(parent=self.frame_reportes_info_3)
        self.label_contador_pacientes_3.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.label_contador_pacientes_3.setStyleSheet("font-size: 16pt;\n"
                                                      "font-weight: 550;\n"
                                                      "border: none;")
        self.label_contador_pacientes_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_contador_pacientes_3.setObjectName("label_contador_pacientes_3")
        self.lbl_pacientes_s_3 = QtWidgets.QLabel(parent=self.frame_reportes_info_3)
        self.lbl_pacientes_s_3.setGeometry(QtCore.QRect(26, 133, 131, 20))
        self.lbl_pacientes_s_3.setStyleSheet("font-size: 10pt;\n"
                                             "color: rgba(0,0, 0, 0.7);\n"
                                             "border: none;")
        self.lbl_pacientes_s_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_pacientes_s_3.setObjectName("lbl_pacientes_s_3")
        self.lbl_icono_reportes_3 = QtWidgets.QLabel(parent=self.frame_reportes_info_3)
        self.lbl_icono_reportes_3.setGeometry(QtCore.QRect(60, 40, 61, 51))
        self.lbl_icono_reportes_3.setStyleSheet("border: none;")
        self.lbl_icono_reportes_3.setText("")
        self.lbl_icono_reportes_3.setPixmap(QtGui.QPixmap("icons/reportes_azul.png"))
        self.lbl_icono_reportes_3.setScaledContents(True)
        self.lbl_icono_reportes_3.setObjectName("lbl_icono_reportes_3")
        self.tabla_reportes = QtWidgets.QTableWidget(parent=self.frame_reportes)
        self.tabla_reportes.setGeometry(QtCore.QRect(60, 370, 1131, 291))
        self.tabla_reportes.setStyleSheet("QTableWidget {\n"
                                          "    background-color: #FFFFFF;\n"
                                          "    alternate-background-color: #F0F0F0;\n"
                                          "    color: #212121;\n"
                                          "    gridline-color: #DCDCDC;\n"
                                          "    selection-color-background: #FF4081;\n"
                                          "    selection-color: #ffffff;\n"
                                          "    border-radius: 10px\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item {\n"
                                          "    padding: 4px;\n"
                                          "}\n"
                                          "\n"
                                          "QHeaderView::section {\n"
                                          "    background-color: rgb(27, 38, 59);\n"
                                          "    color: #FFFFFF;\n"
                                          "    padding: 12px;\n"
                                          "    font-weight: bold;\n"
                                          "    font-size: 9pt;\n"
                                          "    border: none;\n"
                                          "    border-bottom: 1px solid gray;\n"
                                          "}\n"
                                          "\n"
                                          "QHeaderView::section:first {\n"
                                          "     border-radius: 4px;\n"
                                          "}\n"
                                          "\n"
                                          "QHeaderView::section:last {\n"
                                          "     border-radius: 4px;\n"
                                          "}")
        self.tabla_reportes.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tabla_reportes.setAlternatingRowColors(True)
        self.tabla_reportes.setShowGrid(False)
        self.tabla_reportes.setObjectName("tabla_reportes")
        self.tabla_reportes.setColumnCount(5)
        self.tabla_reportes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_reportes.setHorizontalHeaderItem(4, item)
        self.tabla_reportes.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_reportes.horizontalHeader().setDefaultSectionSize(195)
        self.tabla_reportes.horizontalHeader().setMinimumSectionSize(36)
        self.tabla_reportes.horizontalHeader().setSortIndicatorShown(False)
        self.tabla_reportes.horizontalHeader().setStretchLastSection(True)
        self.tabla_reportes.verticalHeader().setVisible(False)
        self.tabla_reportes.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_reportes.verticalHeader().setDefaultSectionSize(36)
        self.tabla_reportes.verticalHeader().setMinimumSectionSize(25)
        self.tabla_reportes.verticalHeader().setSortIndicatorShown(True)
        self.tabla_reportes.verticalHeader().setStretchLastSection(False)
        self.frame_13 = QtWidgets.QFrame(parent=self.frame_reportes)
        self.frame_13.setGeometry(QtCore.QRect(60, 309, 1131, 61))
        self.frame_13.setStyleSheet("background-color: white;\n"
                                    "border-radius: 5px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setLineWidth(3)
        self.frame_13.setMidLineWidth(3)
        self.frame_13.setObjectName("frame_13")
        self.filtro_pac = QtWidgets.QComboBox(parent=self.frame_13)
        self.filtro_pac.setGeometry(QtCore.QRect(840, 18, 241, 31))
        self.filtro_pac.setStyleSheet("QComboBox {\n"
                                      "    color: black;\n"
                                      "    font: 550 9.5pt \"Roboto\";\n"
                                      "    border-bottom: 1px solid gray;\n"
                                      "    border-radius: 0;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::drop-down {\n"
                                      "    border:0px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::down-arrow {\n"
                                      "    image: url(icons/keyboard_arrow_down_FILL0_wght400_GRAD0_opsz24.svg);\n"
                                      "    width: 64px;\n"
                                      "    height: 18px;\n"
                                      "    color: black;\n"
                                      "}")
        self.filtro_pac.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.filtro_pac.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.filtro_pac.setIconSize(QtCore.QSize(64, 64))
        self.filtro_pac.setFrame(True)
        self.filtro_pac.setObjectName("filtro_pac")
        self.filtro_pac.addItem("")
        self.filtro_pac.addItem("")
        self.verticalLayout_24.addWidget(self.frame_reportes)
        self.content.addWidget(self.Import)
        self.Creditos = QtWidgets.QWidget()
        self.Creditos.setObjectName("Creditos")
        self.content.addWidget(self.Creditos)
        self.horizontalLayout.addWidget(self.content)
        self.verticalLayout.addWidget(self.mainwindow)
        self.row_update_cita = 0
        self.endo = ""
        self.meso = ""
        self.ecto = ""
        self.sex_selected = ""
        MainWindow.setCentralWidget(self.centralwidget)
        self.visor_3d = None
        self.p = None
        self.retranslateUi(MainWindow, paises)
        self.content.setCurrentIndex(1)
        self.content_patient.setCurrentIndex(0)
        self.ingresar_patient.setCurrentIndex(0)
        self.pag_connection()
        self.strech_table()
        self.script_path = './scripts/script_blender.py'
        self.blender_path = 'c:/Program Files/Blender Foundation/Blender 3.4/blender.exe'
        self.model_path = './test/exported_model.obj'
        self.json_path = './scripts/datos_modelo.json'

    def retranslateUi(self, MainWindow, paises):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project RVR"))
        self.lbl_name_program.setText(_translate("MainWindow", "Project RVR"))
        self.btn_menu.setText(_translate("MainWindow", "  Menú"))
        self.btn_paciente.setText(_translate("MainWindow", "  Paciente"))
        self.btn_estadistica_patient.setText(_translate("MainWindow", "  Estadísticas del Paciente"))
        self.btn_report.setText(_translate("MainWindow", "  Reporte"))
        self.btn_db.setText(_translate("MainWindow", "  Base de Datos"))
        self.btn_settings.setText(_translate("MainWindow", "   Configuración"))
        self.lbl_inicio.setText(_translate("MainWindow", ""))
        self.lbl_tablep.setText(_translate("MainWindow", "Lista de Pacientes"))
        item = self.table_patient.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre Completo"))
        item = self.table_patient.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Documento"))
        item = self.table_patient.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo de Paciente"))
        item = self.table_patient.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sexo"))
        item = self.table_patient.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "País"))
        item = self.table_patient.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Opción"))
        __sortingEnabled = self.table_patient.isSortingEnabled()
        self.table_patient.setSortingEnabled(False)
        item = self.table_patient.item(0, 0)
        item.setText(_translate("MainWindow", "Nombre Completo"))
        item = self.table_patient.item(0, 1)
        item.setText(_translate("MainWindow", "Documento"))
        item = self.table_patient.item(0, 2)
        item.setText(_translate("MainWindow", "Tipo de Paciente"))
        item = self.table_patient.item(0, 3)
        item.setText(_translate("MainWindow", "Sexo"))
        item = self.table_patient.item(0, 4)
        item.setText(_translate("MainWindow", "País"))
        item = self.table_patient.item(0, 5)
        item.setText(_translate("MainWindow", "Opción"))
        self.content_table_patient()
        self.table_patient.setSortingEnabled(__sortingEnabled)
        self.btn_add.setText(_translate("MainWindow", " Agregar paciente"))
        self.label_4_i.setText(_translate("MainWindow", "Información General para el Registro:"))
        self.name.setPlaceholderText(_translate("MainWindow", "  Nombre"))
        self.apellido.setPlaceholderText(_translate("MainWindow", "  Apellido"))
        self.tipo_pac.setPlaceholderText(_translate("MainWindow", "Tipo de Paciente"))
        self.tipo_pac.setItemText(0, _translate("MainWindow", "Seleccione"))
        self.tipo_pac.setItemText(1, _translate("MainWindow", "Adulto"))
        self.tipo_pac.setItemText(2, _translate("MainWindow", "Atleta"))
        self.sexo.setPlaceholderText(_translate("MainWindow", "Género"))
        self.sexo.setItemText(0, _translate("MainWindow", "Masculino"))
        self.sexo.setItemText(1, _translate("MainWindow", "Femenino"))
        self.fnacimiento.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.act_deporte.setPlaceholderText(_translate("MainWindow", "  Deportes y Actividades Fisicas"))
        self.btn_subir_foto.setText(_translate("MainWindow", "Subir Foto"))
        self.label_5_i.setText(_translate("MainWindow", "Detalles de Contacto"))
        self.country.setPlaceholderText(_translate("MainWindow", "País"))
        for i, data in enumerate(paises):
            self.country.setItemText(i, _translate("MainWindow", data))
        self.documento.setPlaceholderText(_translate("MainWindow", "Documento"))
        self.tipo_doc.setPlaceholderText(_translate("MainWindow", "---"))
        self.tipo_doc.setItemText(0, _translate("MainWindow", "CI"))
        self.correo.setPlaceholderText(_translate("MainWindow", "Correo"))
        self.direccion.setPlaceholderText(_translate("MainWindow", "Dirección"))
        self.btn_sigR1.setText(_translate("MainWindow", "REGISTRAR"))
        self.code_country.setPlaceholderText(_translate("MainWindow", "---"))
        self.code_country.setItemText(0, _translate("MainWindow", "+58"))
        self.telf.setPlaceholderText(_translate("MainWindow", "Télefono"))
        __sortingEnabled = self.table_medidas.isSortingEnabled()
        self.table_medidas.setSortingEnabled(False)
        item = self.table_medidas.item(0, 0)
        item.setText(_translate("MainWindow", "TOMAS "))
        item = self.table_medidas.item(0, 1)
        item.setText(_translate("MainWindow", "TOMA 1"))
        item = self.table_medidas.item(0, 2)
        item.setText(_translate("MainWindow", "TOMA 2"))
        item = self.table_medidas.item(0, 3)
        item.setText(_translate("MainWindow", "TOMA 3"))
        item = self.table_medidas.item(0, 4)
        item.setText(_translate("MainWindow", "RESULTADO"))
        item = self.table_medidas.item(1, 0)
        item.setText(_translate("MainWindow", "Estatura (Metros)"))
        item = self.table_medidas.item(2, 0)
        item.setText(_translate("MainWindow", "Peso (Kg)"))
        item = self.table_medidas.item(3, 0)
        item.setText(_translate("MainWindow", "Profundidad Abdominal (cm)"))
        self.table_medidas.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.table_pliegues_cut.isSortingEnabled()
        self.table_pliegues_cut.setSortingEnabled(False)
        item = self.table_pliegues_cut.item(0, 0)
        item.setText(_translate("MainWindow", "TOMAS"))
        item = self.table_pliegues_cut.item(0, 1)
        item.setText(_translate("MainWindow", "TOMA 1"))
        item = self.table_pliegues_cut.item(0, 2)
        item.setText(_translate("MainWindow", "TOMA 2"))
        item = self.table_pliegues_cut.item(0, 3)
        item.setText(_translate("MainWindow", "TOMA 3"))
        item = self.table_pliegues_cut.item(0, 4)
        item.setText(_translate("MainWindow", "RESULTADO"))
        item = self.table_pliegues_cut.item(1, 0)
        item.setText(_translate("MainWindow", "Triceps (mm)"))
        item = self.table_pliegues_cut.item(2, 0)
        item.setText(_translate("MainWindow", "Subescapular (mm)"))
        item = self.table_pliegues_cut.item(3, 0)
        item.setText(_translate("MainWindow", "Biceps (mm)"))
        item = self.table_pliegues_cut.item(4, 0)
        item.setText(_translate("MainWindow", "Cresta Iliaca (mm)"))
        self.table_pliegues_cut.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.table_perife_circun.isSortingEnabled()
        self.table_perife_circun.setSortingEnabled(False)
        item = self.table_perife_circun.item(0, 0)
        item.setText(_translate("MainWindow", "TOMAS"))
        item = self.table_perife_circun.item(0, 1)
        item.setText(_translate("MainWindow", "TOMA 1"))
        item = self.table_perife_circun.item(0, 2)
        item.setText(_translate("MainWindow", "TOMA 2"))
        item = self.table_perife_circun.item(0, 3)
        item.setText(_translate("MainWindow", "TOMA 3"))
        item = self.table_perife_circun.item(0, 4)
        item.setText(_translate("MainWindow", "RESULTADO"))
        item = self.table_perife_circun.item(1, 0)
        item.setText(_translate("MainWindow", "Brazo Relajado (cm)"))
        item = self.table_perife_circun.item(2, 0)
        item.setText(_translate("MainWindow", "Brazo Flexionado Contraido (cm)"))
        item = self.table_perife_circun.item(3, 0)
        item.setText(_translate("MainWindow", "Muñeca (cm)"))
        item = self.table_perife_circun.item(4, 0)
        item.setText(_translate("MainWindow", "Minimo Cintura (cm)"))
        item = self.table_perife_circun.item(5, 0)
        item.setText(_translate("MainWindow", "Abdominal (cm)"))
        item = self.table_perife_circun.item(6, 0)
        item.setText(_translate("MainWindow", "Caderas (cm)"))
        self.table_perife_circun.setSortingEnabled(__sortingEnabled)
        self.label_medidas.setText(_translate("MainWindow", "MEDIDAS BÁSICAS"))
        self.label_pliegues.setText(_translate("MainWindow", "PLIEGUES CUTANEOS"))
        self.label_perimetros.setText(_translate("MainWindow", "CIRCUNFERENCIAS"))
        self.btn_guardar_medidas.setText(_translate("MainWindow", "TERMINAR CITA"))
        self.nombrec_s_3.setText(_translate("MainWindow", "GUSTAVO RODRÍGUEZ"))
        self.documento_s_3.setText(_translate("MainWindow", "TIPO DE ACTIVIDAD FÍSICA:"))
        self.sexo_s_3.setText(_translate("MainWindow", "GÉNERO:"))
        self.telf_s_3.setText(_translate("MainWindow", "DEPORTES:"))
        self.fnacimiento_s_3.setText(_translate("MainWindow", "EDAD:"))
        __sortingEnabled = self.table_medidas_atleta.isSortingEnabled()
        self.table_medidas_atleta.setSortingEnabled(False)
        item = self.table_medidas_atleta.item(0, 0)
        item.setText(_translate("MainWindow", "TOMAS "))
        item = self.table_medidas_atleta.item(0, 1)
        item.setText(_translate("MainWindow", "TOMA 1"))
        item = self.table_medidas_atleta.item(0, 2)
        item.setText(_translate("MainWindow", "TOMA 2"))
        item = self.table_medidas_atleta.item(0, 3)
        item.setText(_translate("MainWindow", "TOMA 3"))
        item = self.table_medidas_atleta.item(0, 4)
        item.setText(_translate("MainWindow", "RESULTADO"))
        item = self.table_medidas_atleta.item(1, 0)
        item.setText(_translate("MainWindow", "Estatura (Metros)"))
        item = self.table_medidas_atleta.item(2, 0)
        item.setText(_translate("MainWindow", "Peso (Kg)"))
        item = self.table_medidas_atleta.item(3, 0)
        item.setText(_translate("MainWindow", "Profundidad Abdominal (cm)"))
        item = self.table_medidas_atleta.item(4, 0)
        item.setText(_translate("MainWindow", "Envergadura"))
        item = self.table_medidas_atleta.item(5, 0)
        item.setText(_translate("MainWindow", "Estatura Sentado"))
        item = self.table_medidas_atleta.item(6, 0)
        item.setText(_translate("MainWindow", "Longitud Acromio-Dedal"))
        self.table_medidas_atleta.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.table_pliegues_cut_atleta.isSortingEnabled()
        self.table_pliegues_cut_atleta.setSortingEnabled(False)
        item = self.table_pliegues_cut_atleta.item(0, 0)
        item.setText(_translate("MainWindow", "TOMAS"))
        item = self.table_pliegues_cut_atleta.item(0, 1)
        item.setText(_translate("MainWindow", "TOMA 1"))
        item = self.table_pliegues_cut_atleta.item(0, 2)
        item.setText(_translate("MainWindow", "TOMA 2"))
        item = self.table_pliegues_cut_atleta.item(0, 3)
        item.setText(_translate("MainWindow", "TOMA 3"))
        item = self.table_pliegues_cut_atleta.item(0, 4)
        item.setText(_translate("MainWindow", "RESULTADO"))
        item = self.table_pliegues_cut_atleta.item(1, 0)
        item.setText(_translate("MainWindow", "Triceps (mm)"))
        item = self.table_pliegues_cut_atleta.item(2, 0)
        item.setText(_translate("MainWindow", "Subescapular (mm)"))
        item = self.table_pliegues_cut_atleta.item(3, 0)
        item.setText(_translate("MainWindow", "Biceps (mm)"))
        item = self.table_pliegues_cut_atleta.item(4, 0)
        item.setText(_translate("MainWindow", "Cresta Iliaca (mm)"))
        item = self.table_pliegues_cut_atleta.item(5, 0)
        item.setText(_translate("MainWindow", "Supraespinal"))
        item = self.table_pliegues_cut_atleta.item(6, 0)
        item.setText(_translate("MainWindow", "Abdominal"))
        item = self.table_pliegues_cut_atleta.item(7, 0)
        item.setText(_translate("MainWindow", "Muslo Frontal"))
        item = self.table_pliegues_cut_atleta.item(8, 0)
        item.setText(_translate("MainWindow", "Pantorrila"))
        self.table_pliegues_cut_atleta.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.table_perife_circun_atleta.isSortingEnabled()
        self.table_perife_circun_atleta.setSortingEnabled(False)
        item = self.table_perife_circun_atleta.item(0, 0)
        item.setText(_translate("MainWindow", "TOMAS"))
        item = self.table_perife_circun_atleta.item(0, 1)
        item.setText(_translate("MainWindow", "TOMA 1"))
        item = self.table_perife_circun_atleta.item(0, 2)
        item.setText(_translate("MainWindow", "TOMA 2"))
        item = self.table_perife_circun_atleta.item(0, 3)
        item.setText(_translate("MainWindow", "TOMA 3"))
        item = self.table_perife_circun_atleta.item(0, 4)
        item.setText(_translate("MainWindow", "RESULTADO"))
        item = self.table_perife_circun_atleta.item(1, 0)
        item.setText(_translate("MainWindow", "P. Brazo Relajado (cm)"))
        item = self.table_perife_circun_atleta.item(2, 0)
        item.setText(_translate("MainWindow", "P. Brazo Flexionado Contraido (cm)"))
        item = self.table_perife_circun_atleta.item(3, 0)
        item.setText(_translate("MainWindow", "P. Muñeca (cm)"))
        item = self.table_perife_circun_atleta.item(4, 0)
        item.setText(_translate("MainWindow", "P. Minimo Cintura (cm)"))
        item = self.table_perife_circun_atleta.item(5, 0)
        item.setText(_translate("MainWindow", "P. Abdominal (cm)"))
        item = self.table_perife_circun_atleta.item(6, 0)
        item.setText(_translate("MainWindow", "P. Caderas (cm)"))
        item = self.table_perife_circun_atleta.item(7, 0)
        item.setText(_translate("MainWindow", "P. Cefalico"))
        item = self.table_perife_circun_atleta.item(8, 0)
        item.setText(_translate("MainWindow", "P. Torax"))
        item = self.table_perife_circun_atleta.item(9, 0)
        item.setText(_translate("MainWindow", "P. Cuello"))
        item = self.table_perife_circun_atleta.item(10, 0)
        item.setText(_translate("MainWindow", "P. Maximo Antebrazo Derecha"))
        item = self.table_perife_circun_atleta.item(11, 0)
        item.setText(_translate("MainWindow", "P. Maximo Antebrazo Izquierdo M."))
        item = self.table_perife_circun_atleta.item(12, 0)
        item.setText(_translate("MainWindow", "P. Muslo Derecho. 1cm del Pliegue del Musculo"))
        item = self.table_perife_circun_atleta.item(13, 0)
        item.setText(_translate("MainWindow", "P. Muslo Izquierdo. 1cm del Pliegue del Musculo"))
        item = self.table_perife_circun_atleta.item(14, 0)
        item.setText(_translate("MainWindow", "P. Muslo Medio"))
        item = self.table_perife_circun_atleta.item(15, 0)
        item.setText(_translate("MainWindow", "P. Pantorrila"))
        item = self.table_perife_circun_atleta.item(16, 0)
        item.setText(_translate("MainWindow", "P. Minimo del Tobillo"))
        self.table_perife_circun_atleta.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.table_longitud_alt_atleta.isSortingEnabled()
        self.table_longitud_alt_atleta.setSortingEnabled(False)
        item = self.table_longitud_alt_atleta.item(0, 0)
        item.setText(_translate("MainWindow", "TOMAS"))
        item = self.table_longitud_alt_atleta.item(0, 1)
        item.setText(_translate("MainWindow", "TOMA 1"))
        item = self.table_longitud_alt_atleta.item(0, 2)
        item.setText(_translate("MainWindow", "TOMA 2"))
        item = self.table_longitud_alt_atleta.item(0, 3)
        item.setText(_translate("MainWindow", "TOMA 3"))
        item = self.table_longitud_alt_atleta.item(0, 4)
        item.setText(_translate("MainWindow", "RESULTADO"))
        item = self.table_longitud_alt_atleta.item(1, 0)
        item.setText(_translate("MainWindow", "Acromiale-Radiale"))
        item = self.table_longitud_alt_atleta.item(2, 0)
        item.setText(_translate("MainWindow", "Radiale-Stylion"))
        item = self.table_longitud_alt_atleta.item(3, 0)
        item.setText(_translate("MainWindow", "Midstylion-Dactylion"))
        item = self.table_longitud_alt_atleta.item(4, 0)
        item.setText(_translate("MainWindow", "Altura Iliospinale"))
        item = self.table_longitud_alt_atleta.item(5, 0)
        item.setText(_translate("MainWindow", "Altura Trochanterion"))
        item = self.table_longitud_alt_atleta.item(6, 0)
        item.setText(_translate("MainWindow", "Trochanterion-Tibiale Laterale"))
        item = self.table_longitud_alt_atleta.item(7, 0)
        item.setText(_translate("MainWindow", "Altura Tibiale-Laterale"))
        item = self.table_longitud_alt_atleta.item(8, 0)
        item.setText(_translate("MainWindow", "Tibiale Laterale-Sphyrion Tibiale"))
        self.table_longitud_alt_atleta.setSortingEnabled(__sortingEnabled)
        self.label_longitudes_atleta.setText(_translate("MainWindow", "LONGITUDES/ALTURAS"))
        self.label_longitudes_atleta_2.setText(_translate("MainWindow", "DIÁMETROS"))
        __sortingEnabled = self.table_diametros_atleta.isSortingEnabled()
        self.table_diametros_atleta.setSortingEnabled(False)
        item = self.table_diametros_atleta.item(0, 0)
        item.setText(_translate("MainWindow", "TOMAS"))
        item = self.table_diametros_atleta.item(0, 1)
        item.setText(_translate("MainWindow", "TOMA 1"))
        item = self.table_diametros_atleta.item(0, 2)
        item.setText(_translate("MainWindow", "TOMA 2"))
        item = self.table_diametros_atleta.item(0, 3)
        item.setText(_translate("MainWindow", "TOMA 3"))
        item = self.table_diametros_atleta.item(0, 4)
        item.setText(_translate("MainWindow", "RESULTADO"))
        item = self.table_diametros_atleta.item(1, 0)
        item.setText(_translate("MainWindow", "Diámetro Biacromial"))
        item = self.table_diametros_atleta.item(2, 0)
        item.setText(_translate("MainWindow", "Diámetro Biiliocristal"))
        item = self.table_diametros_atleta.item(3, 0)
        item.setText(_translate("MainWindow", "Largo del Pie"))
        item = self.table_diametros_atleta.item(4, 0)
        item.setText(_translate("MainWindow", "Anchura del Tórax Transverso"))
        item = self.table_diametros_atleta.item(5, 0)
        item.setText(_translate("MainWindow", "Profundidad del Tórax Anterior-Posterior"))
        item = self.table_diametros_atleta.item(6, 0)
        item.setText(_translate("MainWindow", "Diámetro Biepicondilar del Húmero"))
        item = self.table_diametros_atleta.item(7, 0)
        item.setText(_translate("MainWindow", "Diámetro Biepicondilar del Fémur"))
        self.table_diametros_atleta.setSortingEnabled(__sortingEnabled)
        self.label_medidas_atleta.setText(_translate("MainWindow", "MEDIDAS BÁSICAS"))
        self.label_pliegues_atleta.setText(_translate("MainWindow", "PLIEGUES CUTANEOS"))
        self.label_perimetros_atleta.setText(_translate("MainWindow", "CIRCUNFERENCIAS"))
        self.btn_guardar_medidas_atleta.setText(_translate("MainWindow", "TERMINAR CITA"))
        self.nombrec_s_atleta_2.setText(_translate("MainWindow", "GUSTAVO RODRÍGUEZ"))
        self.documento_s_atleta.setText(_translate("MainWindow", "TIPO DE ACTIVIDAD FÍSICA:"))
        self.sexo_s_atleta.setText(_translate("MainWindow", "GÉNERO:"))
        self.telf_s_atleta.setText(_translate("MainWindow", "DEPORTES:"))
        self.fnacimiento_s_atleta.setText(_translate("MainWindow", "EDAD:"))
        self.hora_s.setText(_translate("MainWindow", "Hora:"))
        self.nombrec_s.setText(_translate("MainWindow", "Gustavo Rodriguez"))
        self.documento_s.setText(_translate("MainWindow", "Documento:"))
        self.tipo_patient_s.setText(_translate("MainWindow", "Tipo de Paciente:"))
        self.sexo_s.setText(_translate("MainWindow", "Sexo:"))
        self.nombrec_s_5.setText(_translate("MainWindow", "Pais:"))
        self.telf_s.setText(_translate("MainWindow", "Teléfono:"))
        self.Act_fisica_s.setText(_translate("MainWindow", "Actividad:"))
        self.fnacimiento_s.setText(_translate("MainWindow", "Fecha de nacimiento:"))
        self.edad_s.setText(_translate("MainWindow", "Edad:"))
        self.fecha_s.setText(_translate("MainWindow", "Fecha: "))
        self.lbl_title_cal_s.setText(_translate("MainWindow", "Cálculos"))
        self.lbl_imc.setText(_translate("MainWindow", "I.M.C:"))
        self.lbl_icc.setText(_translate("MainWindow", "I.C.C:"))
        self.lbl_ice.setText(_translate("MainWindow", "I.C.E:"))
        self.lbl_porcent_grasa.setText(_translate("MainWindow", "% de Grasa:"))
        self.lbl_p_degrasa.setText(_translate("MainWindow", "P. de Grasa:"))
        self.lbl_p_degrasa_percentil.setText(_translate("MainWindow", "% de Grasa en Percentiles:"))
        self.lbl_indice_mlg.setText(_translate("MainWindow", "Indice M.L.G:"))
        self.lbl_camb.setText(_translate("MainWindow", "C.A.M.B:"))
        self.lbl_iamb.setText(_translate("MainWindow", "I.A.M.B:"))
        self.lbl_complex.setText(_translate("MainWindow", "Complexión:"))
        self.lbl_peso_ideal.setText(_translate("MainWindow", "Peso Ideal:"))
        self.btn_patient_s.setText(_translate("MainWindow", "Volver a Pacientes"))
        self.btn_inform_s.setText(_translate("MainWindow", "Ver Informe"))
        self.btn_model3D_s.setText(_translate("MainWindow", "Ver Modelo 3D"))
        self.lbl_name_c.setText(_translate("MainWindow", "Nombre"))
        self.lbl_edad_c.setText(_translate("MainWindow", "Edad"))
        self.lbl_tpatient_c.setText(_translate("MainWindow", "Tipo de Paciente"))
        self.lbl_sexo_c.setText(_translate("MainWindow", "Sexo"))
        self.lbl_pais_c.setText(_translate("MainWindow", "País"))
        self.lbl_fecha_hora.setText(
            _translate("MainWindow", "La última vez que se agregó una cita fue el XX/XX/XXX a las XX:XX:XXXX"))
        __sortingEnabled = self.table_citas.isSortingEnabled()
        self.table_citas.setSortingEnabled(False)
        item = self.table_citas.item(0, 0)
        item.setText(_translate("MainWindow", "Nro de la Cita"))
        item = self.table_citas.item(0, 1)
        item.setText(_translate("MainWindow", "Nombre "))
        item = self.table_citas.item(0, 2)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.table_citas.item(0, 3)
        item.setText(_translate("MainWindow", "Hora"))
        self.table_citas.setSortingEnabled(__sortingEnabled)
        self.btn_volver_patient_cita.setText(_translate("MainWindow", "Volver a pacientes"))
        self.btn_agregar_cita.setText(_translate("MainWindow", "Agregar cita"))
        self.btn_verinfo_cita.setText(_translate("MainWindow", "Ver cita"))

        self.label_cant_hombres_titulo.setText(_translate("MainWindow", "   Cantidad de Hombres"))
        self.lbl_cant_hombres.setText(_translate("MainWindow", "0"))
        self.label_edadprom_titulo.setText(_translate("MainWindow", "   Edad Promedio"))
        self.lbl_edad_promedio.setText(_translate("MainWindow", "0"))
        self.label_cant_mujeres_titulo.setText(_translate("MainWindow", "   Cantidad de Mujeres"))
        self.lbl_cant_mujeres.setText(_translate("MainWindow", "0"))
        self.lbl_patient_adulto.setText(_translate("MainWindow", "      Adulto:"))
        self.label_pacientetotal_titulo.setText(_translate("MainWindow", "   Pacientes Totales"))
        self.lbl_patient_atleta.setText(_translate("MainWindow", "      Atleta:"))
        self.lbl_patient_adulto_count.setText(_translate("MainWindow", "0"))
        self.lbl_patient_atleta_count.setText(_translate("MainWindow", "0"))
        self.lbl_patient_total.setText(_translate("MainWindow", "0"))
        self.label_citatota_titulo.setText(_translate("MainWindow", "   Citas Totales"))
        self.lbl_cita_total.setText(_translate("MainWindow", "0"))
        self.label_estadp_titulo.setText(_translate("MainWindow", "Estadisticas del Paciente"))
        self.label_paciente.setText(_translate("MainWindow", "Paciente"))
        self.label_cita1.setText(_translate("MainWindow", "Cita 1"))
        self.label_cita2.setText(_translate("MainWindow", "Cita 2"))
        self.comboBox__paciente1.setItemText(0, _translate("MainWindow", "---"))
        self.label_dato.setText(_translate("MainWindow", "Dato"))
        self.btn_comparar.setText(_translate("MainWindow", "Ver comparacion"))
        self.label_dato1.setText(_translate("MainWindow", "% De Grasa Cita 1"))
        self.label_dato2.setText(_translate("MainWindow", "% De Grasa Cita 2"))
        self.label_comparacion_dif1.setText(_translate("MainWindow", "Cita 1: 52%"))
        self.label_comparacion_dif2.setText(_translate("MainWindow", "Cita 2: 48%"))
        self.label_comparacion_diftotal.setText(_translate("MainWindow", "Diferencia: -4%"))

        self.label_7.setText(_translate("MainWindow", "Base de Datos"))
        self.btn_bdd_backup.setText(_translate("MainWindow", "Generar Backup"))
        self.btn_bdd_restaurar.setText(_translate("MainWindow", "Restaurar"))
        self.label_fecha_bdd.setText(_translate("MainWindow", "0"))
        self.lbl_pacientes_s_6.setText(_translate("MainWindow", "Fecha del último backup"))
        self.label_pacientes_totales.setText(_translate("MainWindow", "0"))
        self.lbl_pacientes_s_8.setText(_translate("MainWindow", "Pacientes Totales"))
        self.label_contador_bdd_2.setText(_translate("MainWindow", "0"))
        self.lbl_pacientes_s_10.setText(_translate("MainWindow", "Restauraciones realizadas"))
        self.label_contador_bdd.setText(_translate("MainWindow", "0"))
        self.lbl_bdd_s.setText(_translate("MainWindow", "Backups Realizadas"))
        item = self.tabla_bdd.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.tabla_bdd.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Backup No."))
        item = self.tabla_bdd.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Hora Realizada"))
        item = self.tabla_bdd.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fecha Realizada"))
        item = self.tabla_bdd.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Acceder"))
        self.label_6.setText(_translate("MainWindow", "Sección de Reportes"))
        self.btn_reportes_generar.setText(_translate("MainWindow", "Generar Reporte"))
        self.btn_reportes_vp.setText(_translate("MainWindow", "Volver a Pacientes"))
        self.label_contador_pacientes_totales.setText(_translate("MainWindow", "0"))
        self.lbl_pacientes_s_5.setText(_translate("MainWindow", "Pacientes Totales"))
        self.label_contador_pacientes_adultos.setText(_translate("MainWindow", "0"))
        self.lbl_pacientes_s_7.setText(_translate("MainWindow", "Pacientes Adultos"))
        self.label_contador_pacientes_atletas.setText(_translate("MainWindow", "0"))
        self.lbl_pacientes_s_9.setText(_translate("MainWindow", "Pacientes Atletas"))
        self.label_contador_pacientes_3.setText(_translate("MainWindow", "0"))
        self.lbl_pacientes_s_3.setText(_translate("MainWindow", "Reportes Realizados"))
        item = self.tabla_reportes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.tabla_reportes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo de Reporte"))
        item = self.tabla_reportes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Hora Realizada"))
        item = self.tabla_reportes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fecha Realizada"))
        item = self.tabla_reportes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Descargar"))
        self.filtro_pac.setPlaceholderText(_translate("MainWindow", "Tipo de Paciente"))
        self.filtro_pac.setItemText(0, _translate("MainWindow", "Adulto"))
        self.filtro_pac.setItemText(1, _translate("MainWindow", "Atleta"))
        self.btn_agregar_cita.setText(_translate("MainWindow", "Agregar cita"))
        self.btn_verinfo_cita.setText(_translate("MainWindow", "Ver cita"))
        self.btn_crear_modelo_cita.setText(_translate("MainWindow", "Crear Modelo"))
        self.lbl_nombre.setText(_translate("MainWindow", "Walter J. Raleigh"))
        self.btn_tipo_paciente.setText(_translate("MainWindow", "Adulto"))
        self.lbl_info.setText(_translate("MainWindow", "Información General"))
        self.lbl_desc1.setText(_translate("MainWindow", "Fecha de la Cita:"))
        self.lbl_fecha.setText(_translate("MainWindow", "24 de Noviembre del 2023"))
        self.lbl_desc2.setText(_translate("MainWindow", "Documento:"))
        self.lbl_documento.setText(_translate("MainWindow", "C.I. 24.734.053"))
        self.lbl_desc3.setText(_translate("MainWindow", "Edad de la Persona:"))
        self.lbl_edad.setText(_translate("MainWindow", "26 años"))
        self.lbl_desc4.setText(_translate("MainWindow", "Peso Actual:"))
        self.lbl_peso.setText(_translate("MainWindow", "1,80kgs"))
        self.lbl_desc5.setText(_translate("MainWindow", "Estatura Actual:"))
        self.lbl_estatura.setText(_translate("MainWindow", "1,64cm"))
        self.lbl_desc6.setText(_translate("MainWindow", "Teléfono:"))
        self.lbl_telefono.setText(_translate("MainWindow", "+584246765152"))
        self.label_26.setText(_translate("MainWindow", "Fecha de la Cita:"))
        self.label_27.setText(_translate("MainWindow", "24 de Noviembre del 2023"))
        self.lbl_desc7.setText(_translate("MainWindow", "Actividad Física"))
        self.lbl_actividad_fisica.setText(_translate("MainWindow", "Dormir"))

    # Conexiones de las ventanas

    def pag_connection(self):
        self.btn_menu.clicked.connect(self.side_menu)
        self.btn_paciente.clicked.connect(self.patient)
        self.btn_paciente.clicked.connect(self.side_menu_op)
        self.btn_add.clicked.connect(self.ingresar_datap)
        self.btn_sigR1.clicked.connect(lambda: self.txt_exists(-1))
        self.btn_guardar_medidas.clicked.connect(self.comprobar)
        self.btn_guardar_medidas_atleta.clicked.connect(self.comprobar)
        self.btn_inform_s.clicked.connect(lambda: self.data_pdf(self.row_update_cita, 0))
        self.btn_agregar_cita.clicked.connect(self.new_cita)
        self.btn_volver_patient_cita.clicked.connect(self.patient)
        self.btn_verinfo_cita.clicked.connect(self.ver_informe_cita)
        self.btn_estadistica_patient.clicked.connect(self.estadisticas)
        self.btn_estadistica_patient.clicked.connect(self.estadisticas_sistem)
        self.btn_estadistica_patient.clicked.connect(self.side_menu_op)
        self.btn_report.clicked.connect(self.reportes)
        self.btn_report.clicked.connect(self.side_menu_op)
        self.btn_crear_modelo_cita.clicked.connect(self.cambiar_ventana3d)
        self.btn_db.clicked.connect(self.cambiar_ventanabdd)
        self.btn_reportes_generar.clicked.connect(self.realizar_reporte)
        self.btn_bdd_backup.clicked.connect(self.generar_backup_bdd)
    # Base de Datos
    def cambiar_ventanabdd(self):
        self.content.setCurrentIndex(4)

    def generar_backup_bdd(self):
        data = []
        with open(f'pacientes.txt', 'rb') as file_new_d:
            while True:
                try:
                    info = pickle.load(file_new_d)
                    data.append(info)
                except EOFError:
                    break

        # for paciente in data:
        #     for p in vars(paciente):
        #         print(p, ':', vars(paciente)[p])
        #     print('------------------------')

        DB_HOST = 'localhost'
        DB_USER = 'root'
        DB_USER_PASSWORD = 'admin123'
        DB_NAME = 'tesis_antropometria'
        BACKUP_PATH = './backup/dbbackup'
        OS_BACK_PATH = os.path.abspath(BACKUP_PATH)

        connection = m.connect(host=DB_HOST, user=DB_USER,
                               password=DB_USER_PASSWORD, database=DB_NAME)
        cursor = connection.cursor()
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

        try:
            connection.start_transaction()
            cursor.execute('SHOW TABLES;')
            table_names = []
            # Eliminar todas los datos de todas las tablas

            cursor.fetchall()
            cursor.execute('DELETE FROM ' + "informe_atleta" + ';')
            connection.commit()

            cursor.fetchall()
            cursor.execute('DELETE FROM ' + "informe_adulto" + ';')
            connection.commit()

            cursor.fetchall()
            cursor.execute('DELETE FROM ' + "citas" + ';')
            connection.commit()

            cursor.fetchall()
            cursor.execute('DELETE FROM ' + "tipo_paciente" + ';')
            connection.commit()

            cursor.fetchall()
            cursor.execute('DELETE FROM ' + "paciente" + ';')
            connection.commit()

            query_adulto = "INSERT INTO tipo_paciente(idTipo, nombre_tipo) VALUES (%s, %s)"
            values_adulto = (1, "Adulto")
            cursor.execute(query_adulto, values_adulto)

            query_atleta = "INSERT INTO tipo_paciente(idTipo, nombre_tipo) VALUES (%s, %s)"
            values_atleta = (2, "Atleta")
            cursor.execute(query_atleta, values_atleta)

            for paciente in data:
                #     for
                # Consulta 1: INSERT INTO paciente
                # ENUM: Masculino:, Femenino:
                genero = 1 if paciente.get_sex() == 'Masculino' else 2
                f_nacimiento = datetime.strptime(paciente.get_fnacimiento(), "%m/%d/%Y").date()
                query1 = "INSERT INTO paciente(nombre, documento, genero, pais, fnacimiento, act_deporte, correo, direccion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                values1 = (paciente.get_name(), paciente.get_doc(), genero, paciente.get_country(), f_nacimiento,
                           paciente.get_actdeporte(), paciente.correo, paciente.direccion)
                cursor.execute(query1, values1)
                id_paciente = cursor.lastrowid

                # Consulta 2: INSERT INTO citas
                # Adulto id=1, Atleta id=2
                tipo = 1 if paciente.get_t_pac() == 'Adulto' else 2
                print(id_paciente)
                print(tipo)
                query3 = "INSERT INTO citas(Paciente_idPaciente, tipo_idTipo, fecha) VALUES (%s, %s, %s)"
                values3 = (id_paciente, tipo, datetime.now())
                cursor.execute(query3, values3)
                id_cita = cursor.lastrowid

                if tipo == 1:
                    for i in range(0, len(paciente.get_medidas())):
                        medidas_adulto = paciente.get_medidas()[i]
                        print(medidas_adulto)
                        # Consulta 3: INSERT INTO informe_adulto
                        query4 = "INSERT INTO informe_adulto(estatura, peso, profundidad_abdominal, triceps, subescapular, biceps, cresta, brazo_relajado, bfr, muneca, minimo_cintura, abdominal, caderas, Citas_Paciente_idPaciente, Citas_tipo_idTipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        values4 = (
                        medidas_adulto[0], medidas_adulto[1], medidas_adulto[2], medidas_adulto[3], medidas_adulto[4],
                        medidas_adulto[5], medidas_adulto[6], medidas_adulto[7], medidas_adulto[8], medidas_adulto[9],
                        medidas_adulto[10], medidas_adulto[11], medidas_adulto[12], id_paciente, tipo)
                        cursor.execute(query4, values4)

                # Consulta 4: INSERT INTO informe_atleta
                if tipo == 2:
                    for i in range(0, len(paciente.get_medidas())):
                        medidas_atleta = paciente.get_medidas()[i]
                        print(len(medidas_atleta))
                        query5 = "INSERT INTO informe_atleta(estatura, peso, profundidad_abdominal, envergadura, estatura_sentado, longitud_ad, triceps, subescapular, biceps, cresta, supraespinal, abdominal_atleta, muslo_frontal, pantorrilla, brazo_relajado, bfc, muneca_atleta, minimo_cintura_atleta, abdominal, caderas, cefalico, torax, cuello, mad, mai, md_1, mi_1, muslo_medio, p_pantorrilla, p_mdt, acromiale_radiale, radiale_stylion, midstylion_dactylion, altura_iliospinale, altura_trochanterion, trochanterion_tl, altura_tl, tibiale_ls_t, diametro_biacromial, diametro_biliocristal, largo_pie, torax_t, torax_ap, diametro_biepicondilar_h, diametro_biepicondilar_f, Citas_Paciente_idPaciente, Citas_tipo_idTipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        values5 = (
                        medidas_atleta[0], medidas_atleta[1], medidas_atleta[2], medidas_atleta[3], medidas_atleta[4],
                        medidas_atleta[5], medidas_atleta[6], medidas_atleta[7], medidas_atleta[8], medidas_atleta[9],
                        medidas_atleta[10], medidas_atleta[11], medidas_atleta[12], medidas_atleta[13],
                        medidas_atleta[14], medidas_atleta[15], medidas_atleta[16], medidas_atleta[17],
                        medidas_atleta[18], medidas_atleta[19], medidas_atleta[20], medidas_atleta[21],
                        medidas_atleta[22], medidas_atleta[23], medidas_atleta[24], medidas_atleta[25],
                        medidas_atleta[26], medidas_atleta[27], medidas_atleta[28], medidas_atleta[29],
                        medidas_atleta[30], medidas_atleta[31], medidas_atleta[32], medidas_atleta[33],
                        medidas_atleta[34], medidas_atleta[35], medidas_atleta[36], medidas_atleta[37],
                        medidas_atleta[38], medidas_atleta[39], medidas_atleta[40], medidas_atleta[41],
                        medidas_atleta[42], medidas_atleta[43], medidas_atleta[44], id_paciente, tipo)
                        cursor.execute(query5, values5)

                # Confirmar la transacción
                connection.commit()

        except m.Error as Error:
            connection.rollback()
            print(
                "que hiciste vergacion nojoda dios mio porque no se hizo esta vergaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            print("PORQUE: ", Error)

        cursor.close()
        connection.close()

        DATETIME = time.strftime('%Y%m%d-%H%M%S')
        TODAYBACKUPPATH = BACKUP_PATH

        # Checking if backup folder already exists or not. If not exists will create it.
        # try:
        #     os.stat(TODAYBACKUPPATH)
        # except:
        #     os.mkdir(TODAYBACKUPPATH)

        # Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
        # print ("checking for databases names file.")
        # if os.path.exists(DB_NAME):
        #     file1 = open(DB_NAME)
        #     multi = 1
        #     print ("Databases file found...")
        #     print ("Starting backup of all dbs listed in file " + DB_NAME)
        # else:
        #     print ("Databases file not found...")
        #     print ("Starting backup of database " + DB_NAME)
        #     multi = 0

        # Starting actual database backup process.

        # if multi:
        #    in_file = open(DB_NAME,"r")
        #    flength = len(in_file.readlines())
        #    in_file.close()
        #    p = 1
        #    dbfile = open(DB_NAME,"r")

        #    while p <= flength:
        #        db = dbfile.readline()   # reading database name from file
        #        db = db[:-1]         # deletes extra line
        #        dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
        #        os.system(dumpcmd)
        #        gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
        #        os.system(gzipcmd)
        #        p = p + 1
        #    dbfile.close()
        # else:
        db = DB_NAME
        dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(
            TODAYBACKUPPATH) + "/" + db + DATETIME + ".sql"
        os.system(dumpcmd)
        # gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
        # os.system(gzipcmd)
        QMessageBox.information(None, "Información", "El backup se generó correctamente", QMessageBox.StandardButton.Ok)
        self.agregar_row_bdd('icons/Database-mysql.svg', f'Backup No. {self.tabla_bdd.rowCount() + 1}', datetime.now().strftime("%H:%M:%S"), datetime.now().strftime("%d/%m/%Y"), f'{OS_BACK_PATH}/{db}{DATETIME}.sql')

    #copia y pega desesperao kill me
    def agregar_row_bdd(self, img_path, nombre_reporte, hora, fecha, ruta_archivo):
        row = self.tabla_bdd.rowCount()
        self.tabla_bdd.setRowCount(row + 1)
        imagen_pdf = self.obtenerImagen(img_path)

        self.tabla_bdd.setCellWidget(row, 0, imagen_pdf)

        self.tabla_bdd.setItem(row, 1, QTableWidgetItem(nombre_reporte))
        self.tabla_bdd.setItem(row, 2, QTableWidgetItem(hora))
        self.tabla_bdd.setItem(row, 3, QTableWidgetItem(fecha))

        font = QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(750)
        alignment = QtCore.Qt.AlignmentFlag.AlignCenter

        for column in range(1, 4):
            item = self.tabla_bdd.item(row, column)
            item.setFont(font)
            item.setTextAlignment(alignment)

        btn_widget = QWidget()
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(60, 0, 60, 0)
        btn = QtWidgets.QPushButton()
        btn.setGeometry(QtCore.QRect(240, 10, 131, 41))
        btn.setStyleSheet("QPushButton {\n"
                          "    color:     black;\n"
                          "    font-weight: 750;\n"
                          "    background-color: white;\n"
                          "    border-radius: 5px;\n"
                          "    font: 8.5pt;\n"
                          "    min-width: 50px;\n"
                          "height: 40px;\n"
                          "text-align: center;\n"
                          "border: 1px solid rgb(27, 38, 59);"
                          "}\n"
                          "QPushButton:hover {\n"
                          "background-color: rgb(27, 38, 59);\n"
                          "color: white;\n"
                          "}")
        btn.setFont(font)
        btn.setText("RESTAURAR")
        button_layout.addWidget(btn)
        btn_widget.setLayout(button_layout)
        if row % 2 == 0:
            btn_widget.setStyleSheet("background-color: white;")
        else:
            btn_widget.setStyleSheet("background-color: #F0F0F0;")
        # btn.clicked.connect(lambda _, path=ruta_archivo: self.abrir_reporte(path))
        self.tabla_bdd.setCellWidget(row, 4, btn_widget)
        self.tabla_bdd.setRowHeight(row, 55)
        self.tabla_bdd.setColumnWidth(0, 50)
        self.tabla_bdd.setColumnWidth(1, 300)
        self.tabla_bdd.setColumnWidth(2, 375)

    # Reportes

    def obtenerImagen(self, imagen):
        lbl_imagen = QLabel()
        lbl_imagen.setText("")
        lbl_imagen.setGeometry(0, 0, 20, 100)
        lbl_imagen.setScaledContents(True)
        pixmap = QPixmap(imagen)
        lbl_imagen.setPixmap(pixmap)
        lbl_imagen.setMargin(100)
        return lbl_imagen

    def agregar_row_reporte(self, img_path, nombre_reporte, hora, fecha, ruta_archivo):
        row = self.tabla_reportes.rowCount()
        self.tabla_reportes.setRowCount(row + 1)
        imagen_pdf = self.obtenerImagen(img_path)

        self.tabla_reportes.setCellWidget(row, 0, imagen_pdf)

        self.tabla_reportes.setItem(row,1, QTableWidgetItem(nombre_reporte))
        self.tabla_reportes.setItem(row,2, QTableWidgetItem(hora))
        self.tabla_reportes.setItem(row,3, QTableWidgetItem(fecha))
        
        font = QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(750)
        alignment = QtCore.Qt.AlignmentFlag.AlignCenter
        
        for column in range(1, 4):
            item = self.tabla_reportes.item(row, column)
            item.setFont(font)
            item.setTextAlignment(alignment)
        
        btn_widget = QWidget()
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(60, 0, 60, 0)
        btn = QtWidgets.QPushButton()
        btn.setGeometry(QtCore.QRect(240, 10, 131, 41))
        btn.setStyleSheet("QPushButton {\n"
                                           "    color:     black;\n"
                                           "    font-weight: 550;\n"
                                           "    background-color: white;\n"
                                           "    border-radius: 5px;\n"
                                           "    font-size: 8.5pt;\n"
                                           "    min-width: 50px;\n"
                                            "height: 40px;\n"
                                            "text-align: center;\n"
                                            "border: 1px solid #ED0800;"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background-color: #ED0800;\n"
                                            "color: white;\n"
                                           "}")
        btn.setText("ABRIR")
        button_layout.addWidget(btn)
        btn_widget.setLayout(button_layout)
        if row % 2 == 0:
            btn_widget.setStyleSheet("background-color: white;")
        else:
            btn_widget.setStyleSheet("background-color: #F0F0F0;")
        btn.clicked.connect(lambda _, path=ruta_archivo: self.abrir_reporte(path))
        self.tabla_reportes.setCellWidget(row, 4, btn_widget)
        self.tabla_reportes.setRowHeight(row, 55)
        self.tabla_reportes.setColumnWidth(0, 50)
        self.tabla_reportes.setColumnWidth(1, 300)
        self.tabla_reportes.setColumnWidth(2, 375)

    def abrir_reporte(self, file_path):
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

    def realizar_reporte(self):
        # Create PDF object
        pdf = PDF()

        # Set the document properties
        pdf.set_title('Reporte de Pacientes')
        pdf.set_author('Walter')

        # Add a page
        pdf.add_page()

        # Set font for the main content
        pdf.set_font('Helvetica', '', 9)

        # Add table header
        pdf.table_header()

        # Add data rows
        data_row = []

        with open(f'pacientes.txt', 'rb') as file_new_d:
            while True:
                try:
                    info = pickle.load(file_new_d)
                    data_row.append(info)
                except EOFError:
                    break

        pdf.add_data_row(data_row)
        current_date = time.strftime('%d-%m-%Y')
        row = self.tabla_reportes.rowCount()
        # Output the PDF file
        try:
            nombre_archivo = './reportes/reporte-' + str(current_date) + str(row) + '.pdf'
            ruta_archivo = os.path.abspath(nombre_archivo)
            pdf.output(nombre_archivo)
        except Exception as e:
            error_message = f"Se produjo un error al generar o abrir el archivo PDF"
            QMessageBox.critical(None, "Error", error_message, QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.information(None, "Información", "El reporte se generó correctamente", QMessageBox.StandardButton.Ok)
            self.agregar_row_reporte('images/PDF_file_icon.svg', 'Reporte General', str(datetime.now().time())[:8], str(current_date), ruta_archivo)
            os.startfile(ruta_archivo)

    def obtenerImagen(self, imagen):
        lbl_imagen = QLabel()
        lbl_imagen.setText("")
        lbl_imagen.setGeometry(0, 0, 20, 100)
        lbl_imagen.setScaledContents(True)
        pixmap = QPixmap(imagen)
        lbl_imagen.setPixmap(pixmap)
        lbl_imagen.setMargin(8)
        lbl_imagen.setStyleSheet("background-color: transparent;")
        return lbl_imagen


    #Modelado 3D
    def cambiar_ventana3d(self):
        if self.visor_3d is None:
            self.visor_3d = QVTKRenderWindowInteractor(parent=self.frame_visor3d)
            self.visor_3d.setObjectName("visor_3d")
            self.verticalLayout_frame3d.addWidget(self.visor_3d)
            self.verticalLayout_frame3d.setContentsMargins(0, 0, 0, 0)

        if self.table_citas.currentRow() > 0:
            cita_row = self.table_citas.currentRow()
            self.actualizar_json(self.row_update_cita, cita_row, self.json_path)
            self.correr_subproceso(self.blender_path, self.script_path)
            #self.cargarModelo(self.model_path)
        else:
            msg = QMessageBox()
            QMessageBox.critical(msg, "Error", "No se ha seleccionado ninguna cita del paciente.")

    def cargarModelo(self, ruta):
        self.content.setCurrentIndex(3)
        model = load(ruta)
        scals = model.points()[:, 0] + 100  # pick x coordinates of vertices
        model.cmap("gray", scals)
        vp = Plotter(qt_widget=self.visor_3d, pos=(0, 1))
        vp.add(model)
        vp.show(title='Modelo 3D', mode=1)

    def correr_subproceso(self, blender, script):
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


    def actualizar_json(self, row_paciente, row_cita, ruta_json):
        data = []
        with open(f'pacientes.txt', 'rb') as file_new_d:
            while True:
                try:
                    info = pickle.load(file_new_d)
                    data.append(info)
                except EOFError:
                    break

        multi_medidas = []
        all_data = []
        for position, datos in enumerate(data):
            str((datos.__dict__).get('name'))
            str((datos.__dict__).get('fnacimiento'))
            str((datos.__dict__).get('medidas'))
            str((datos.__dict__).get('doc'))
            str((datos.__dict__).get('t_pac'))
            str((datos.__dict__).get('act_deporte'))
            str((datos.__dict__).get('sex')),


            row_data = [str((datos.__dict__).get('t_pac')),
                        str((datos.__dict__).get('name')),
                        str((datos.__dict__).get('doc')),
                        str((datos.__dict__).get('fnacimiento')),
                        str((datos.__dict__).get('act_deporte')),
                        datos.__dict__.get('medidas'),
                        str((datos.__dict__).get('sex'))
                        ]
            all_data.append(row_data)

        nombre_sin_div = str(all_data[row_paciente - 1][1])
        edad = self.calcular_edad(str(all_data[row_paciente - 1][3]))
        self.lbl_nombre.setText(" ".join(nombre_sin_div.split()))
        self.lbl_documento.setText(str(all_data[row_paciente - 1][2]))
        self.lbl_actividad_fisica.setText(str(all_data[row_paciente - 1][4]))
        self.lbl_edad.setText(str(edad) + " años")
        self.lbl_peso.setText(str(all_data[row_paciente - 1][5][row_cita - 1][1]) + "kgs")
        self.lbl_estatura.setText(str(all_data[row_paciente - 1][5][row_cita - 1][0]) + "mts")
        datos_finales = all_data[row_paciente - 1][5][row_cita - 1]
        datos_finales = datos_finales[:len(datos_finales) - 2]
        datos_finales = [float(d) for d in datos_finales]

        edad_modelo = self.transformar_valor(0.0, 80.0, -1.0, 1.0, edad)

        # Preparando datos para Paciente Adulto
        if all_data[row_paciente - 1][0] == 'Adulto':
            self.tipo_pac.setCurrentIndex(1)
            datos_finales_cita = self.salida_final(datos_finales)
            datos_finales_cita = [float(d) for d in datos_finales_cita]
            print(datos_finales_cita)

            altura_modelo = self.transformar_valor(0.0, 180.0, -1.0, 1.0, datos_finales[0])
            # peso va con IMC
            profundidad_abdominal_modelo = self.transformar_valor(0.0, 45.0, -1.0, 1.0, datos_finales[2])
            triceps_modelo = self.transformar_valor(0.0, 15.0, -1.0, 1.0, datos_finales[3])
            subescapular_modelo = self.transformar_valor(0.0, 20.0, -1.0, 1.0, datos_finales[4])
            biceps_modelo = self.transformar_valor(0.0, 10.0, -1.0, 1.0, datos_finales[5])
            cresta_iliaca_modelo = self.transformar_valor(0.0, 30.0, -1.0, 1.0, datos_finales[6])
            pbr_modelo = self.transformar_valor(0.0, 45.0, -1.0, 1.0, datos_finales[7])
            pbf_modelo = self.transformar_valor(0.0, 45.0, -1.0, 1.0, datos_finales[8])
            pm_modelo = self.transformar_valor(0.0, 20.0, -1.0, 1.0, datos_finales[9])
            minimo_cintura_modelo = self.transformar_valor(0.0, 100.0, -1.0, 1.0, datos_finales[10])
            pa_modelo = self.transformar_valor(0.0, 120.0, -1.0, 1.0, datos_finales[11])
            pc_modelo = self.transformar_valor(0.0, 120.0, -1.0, 1.0, datos_finales[12])

            imc_modelo = self.transformar_valor(0.0, 60.0, -1.0, 1.0, datos_finales_cita[0])
            musculatura_modelo = self.transformar_valor(15.0, 40.0, -1.0, 1.0, datos_finales[7])
            print(imc_modelo)
            print(musculatura_modelo)
            brazo_musculatura_modelo = self.transformar_valor(0.0, 95.0, -1.0, 1.0, datos_finales[7])

        # Preparando datos para Paciente Atleta
        elif all_data[row_paciente - 1][0] == 'Atleta':
            self.tipo_pac.setCurrentIndex(1)
            datos_finales_cita = self.salida_final(datos_finales)
            datos_finales_cita = [float(d) for d in datos_finales_cita]
            print(datos_finales_cita)

            altura_modelo = self.transformar_valor(0.0, 180.0, -1.0, 1.0, datos_finales[0])
            # peso va con IMC
            profundidad_abdominal_modelo = self.transformar_valor(0.0, 45.0, -1.0, 1.0, datos_finales[2])
            envergadura_modelo = self.transformar_valor(165.0, 200.0, -1.0, 1.0, datos_finales[3])
            lad_modelo = self.transformar_valor(70.0, 80.0, -1.0, 1.0, datos_finales[5])
            triceps_modelo = self.transformar_valor(0.0, 15.0, -1.0, 1.0, datos_finales[6])
            subescapular_modelo = self.transformar_valor(0.0, 20.0, -1.0, 1.0, datos_finales[7])
            biceps_modelo = self.transformar_valor(0.0, 10.0, -1.0, 1.0, datos_finales[8])
            cresta_iliaca_modelo = self.transformar_valor(0.0, 30.0, -1.0, 1.0, datos_finales[9])
            supraespinal_modelo = self.transformar_valor(0.0, 35.0, -1.0, 1.0, datos_finales[10])
            # abdominal_modelo = self.transformar_valor(0.0, 35.0, -1.0, 1.0, datos_finales[11])
            muslo_frontal_modelo = self.transformar_valor(20.0, 40.0, -1.0, 1.0, datos_finales[12])
            pantorrilla_modelo = self.transformar_valor(10.0, 100.0, -1.0, 1.0, datos_finales[13])

            pbr_modelo = self.transformar_valor(0.0, 45.0, -1.0, 1.0, datos_finales[14])
            pbf_modelo = self.transformar_valor(0.0, 45.0, -1.0, 1.0, datos_finales[15])
            p_muneca = self.transformar_valor(0.0, 20.0, -1.0, 1.0, datos_finales[16])
            minimo_cintura_modelo = self.transformar_valor(0.0, 70.0, -1.0, 1.0, datos_finales[17])
            pcefalico_modelo = self.transformar_valor(55.0, 60.0, -1.0, 1.0, datos_finales[20])
            ptorax_modelo = self.transformar_valor(80.0, 100.0, -1.0, 1.0, datos_finales[21])
            pcuello_modelo = self.transformar_valor(20.0, 45.0, -1.0, 1.0, datos_finales[22])
            pmuslomedio_modelo = self.transformar_valor(45.0, 65.0, -1.0, 1.0, datos_finales[27])
            ppantorrilla_modelo = self.transformar_valor(30.0, 40.0, -1.0, 1.0, datos_finales[28])
            pmtobillo_modelo = self.transformar_valor(18.0, 26.0, -1.0, 1.0, datos_finales[29])

            acromialeradiale_modelo = self.transformar_valor(35.0, 90.0, -1.0, 1.0, datos_finales[30])
            radiale_stylion_modelo = self.transformar_valor(20.0, 50.0, -1.0, 1.0, datos_finales[31])
            midstylion_dactylion_modelo = self.transformar_valor(20.0, 30.0, -1.0, 1.0, datos_finales[32])
            altura_iliospinale_modelo = self.transformar_valor(90.0, 110.0, -1.0, 1.0, datos_finales[33])
            altura_tronchanterion_modelo = self.transformar_valor(20.0, 200.0, -1.0, 1.0, datos_finales[34])
            trochanterion_tl_modelo = self.transformar_valor(40.0, 55.0, -1.0, 1.0, datos_finales[35])
            altura_tl_modelo = self.transformar_valor(40.0, 55.0, -1.0, 1.0, datos_finales[36])
            tl_sl_modelo = self.transformar_valor(36.0, 42.0, -1.0, 1.0, datos_finales[37])

            diametro_biacromial_modelo = self.transformar_valor(40.0, 49.0, -1.0, 1.0, datos_finales[37])
            diametro_biliocristal_modelo = self.transformar_valor(15.0, 40.0, -1.0, 1.0, datos_finales[38])
            largo_pie_modelo = self.transformar_valor(24.0, 28.0, -1.0, 1.0, datos_finales[40])
            anchura_torax = self.transformar_valor(15.0, 35.0, -1.0, 1.0, datos_finales[41])
            profundidad_toraxt = self.transformar_valor(18.0, 23.0, -1.0, 1.0, datos_finales[42])
            diametro_bch = self.transformar_valor(5.0, 20.0, -1.0, 1.0, datos_finales[43])
            diametro_bcf = self.transformar_valor(9.0, 12.0, -1.0, 1.0, datos_finales[44])

            imc_modelo = self.transformar_valor(0.0, 60.0, -1.0, 1.0, datos_finales_cita[0])
            musculatura_modelo = self.transformar_valor(15.0, 24.0, -1.0, 1.0, 22)
            brazo_musculatura_modelo = self.transformar_valor(12.0, 60.0, -1.0, 1.0, datos_finales_cita[2])


        with open(ruta_json, 'r', encoding='utf-8') as json_file:
            datos = json.load(json_file)

        if all_data[row_paciente - 1][6] == 'Masculino':
            datos['preset'] = 'm_la01'
        elif all_data[row_paciente - 1][6] == 'Femenino':
            datos['preset'] = 'f_la01'

        if all_data[row_paciente - 1][0] == 'Adulto':
            datos['tpac'] = 'Adulto'
            datos['altura'] = altura_modelo
            datos['edad'] = edad_modelo
            datos['grasa'] = imc_modelo
            datos['musculatura'] = musculatura_modelo
            datos['profundidad-abdominal'] = profundidad_abdominal_modelo
            datos['triceps'] = triceps_modelo
            datos['subescapular'] = subescapular_modelo
            datos['biceps'] = biceps_modelo
            datos['cresta'] = cresta_iliaca_modelo
            datos['pbr'] = pbr_modelo
            datos['pbf'] = pbf_modelo
            datos['pm'] = pm_modelo
            datos['minimo-cintura'] = minimo_cintura_modelo
            datos['pa'] = pa_modelo
            datos['pc'] = pc_modelo
            datos['brazo-musculatura'] = brazo_musculatura_modelo
        elif all_data[row_paciente - 1][0] == 'Atleta':
            datos['tpac'] = 'Atleta'
            datos['altura'] = altura_modelo
            datos['edad'] = edad
            datos['profundidad-abdominal'] = profundidad_abdominal_modelo
            datos['envergadura'] = envergadura_modelo
            datos['lad'] = lad_modelo
            datos['triceps'] = triceps_modelo
            datos['subescapular'] = subescapular_modelo
            datos['biceps'] = biceps_modelo
            datos['cresta'] = cresta_iliaca_modelo
            datos['supraespinal'] = supraespinal_modelo
            datos['muslo-frontal'] = muslo_frontal_modelo
            datos['pantorrilla'] = pantorrilla_modelo
            datos['pbr'] = pbr_modelo
            datos['pbf'] = pbf_modelo
            datos['pm'] = p_muneca
            datos['pcefalico'] = pcefalico_modelo
            datos['ptorax'] = ptorax_modelo
            datos['pcuello'] = pcuello_modelo
            datos['pmuslomedio'] = pmuslomedio_modelo
            datos['ppantorrilla'] = ppantorrilla_modelo
            datos['pmtobillo'] = pmtobillo_modelo
            datos['acromialeradiale'] = acromialeradiale_modelo
            datos['radiale_stylion'] = radiale_stylion_modelo
            datos['midstylion_dactylion'] = midstylion_dactylion_modelo
            datos['altura_iliospinale'] = altura_iliospinale_modelo
            datos['altura-tronchanterion'] = altura_tronchanterion_modelo
            datos['tronchanterion_tl'] = trochanterion_tl_modelo
            datos['altura_tl'] = altura_tl_modelo
            datos['tl_sl'] = tl_sl_modelo
            datos['diametro_biacromial'] = diametro_biacromial_modelo
            datos['diametro_biliocristal'] = diametro_biliocristal_modelo
            datos['largo_pie'] = largo_pie_modelo
            datos['anchura_torax'] = anchura_torax
            datos['profundidad_toraxt'] = profundidad_toraxt
            datos['diametro_bch'] = diametro_bch
            datos['diametro_bcf'] = diametro_bcf
            datos['grasa'] = imc_modelo
            datos['musculatura'] = musculatura_modelo
            datos['brazo-musculatura'] = brazo_musculatura_modelo

        with open(ruta_json, 'w', encoding='utf-8') as json_file:
            json.dump(datos, json_file)


    def calcular_edad(self, fecha_edad):
        fecha_nacimiento = datetime.strptime(fecha_edad, "%d/%m/%Y").date()
        hoy = date.today()
        edad = hoy.year - fecha_nacimiento.year

        if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1

        return edad

    def transformar_valor(self, min_val, max_val, new_min, new_max, val):
        valor_normalizado = (val - min_val) / (max_val - min_val)
        valor_transformado = (valor_normalizado * (new_max - new_min)) + new_min

        return round(valor_transformado, 3)

    def patient(self):
        self.selected_op(self.btn_paciente)
        self.deselected_op(self.btn_db)
        self.deselected_op(self.btn_estadistica_patient)
        self.deselected_op(self.btn_report)

        self.row_update_cita = 0

        self.lbl_imc.setText("I.M.C:")
        self.lbl_icc.setText("I.C.C:")
        self.lbl_ice.setText("I.C.E:")
        self.lbl_porcent_grasa.setText("% de Grasa:")
        self.lbl_p_degrasa.setText("P. de Grasa:")
        self.lbl_p_degrasa_percentil.setText("% de Grasa en Percentiles:")
        self.lbl_indice_mlg.setText("Indice M.L.G:")
        self.lbl_camb.setText("C.A.M.B:")
        self.lbl_iamb.setText("I.A.M.B:")
        self.lbl_complex.setText("Complexión:")
        self.lbl_peso_ideal.setText("Peso Ideal:")

        self.name.clear()
        self.apellido.clear()
        self.documento.clear()
        self.tipo_doc.setCurrentIndex(0)
        self.telf.clear()
        self.act_deporte.clear()
        self.code_country.setCurrentIndex(0)
        self.country.setCurrentIndex(0)
        self.sexo.setCurrentIndex(0)
        self.tipo_pac.setCurrentIndex(0)

        # for i in range(3):
        #     i += 1
        #     for j in range(4):
        #         j += 1
        #         self.table_medidas.item(i, j).setText("")
        # for i in range(4):
        #     i += 1
        #     for j in range(4):
        #         j += 1
        #         self.table_pliegues_cut.item(i, j).setText("")
        # for i in range(6):
        #     i += 1
        #     for j in range(4):
        #         j += 1
        #         self.table_perife_circun.item(i, j).setText("")
        # for i in range(6):
        #     i += 1
        #     for j in range(4):
        #         j += 1
        #         self.table_medidas_atleta.item(i, j).setText("")
        # for i in range(8):
        #     i += 1
        #     for j in range(4):
        #         j += 1
        #         self.table_pliegues_cut_atleta.item(i, j).setText("")
        # for i in range(16):
        #     i += 1
        #     for j in range(4):
        #         j += 1
        #         self.table_perife_circun_atleta.item(i, j).setText("")
        # for i in range(8):
        #     i += 1
        #     for j in range(4):
        #         j += 1
        #         self.table_longitud_alt_atleta.item(i, j).setText("")
        # for i in range(7):
        #     i += 1
        #     for j in range(4):
        #         j += 1
        #         self.table_diametros_atleta.item(i, j).setText("")
        #
        # self.name.setText("a")
        # self.apellido.setText("a")
        # self.direccion.setText("a")
        # self.correo.setText("a")
        # self.act_deporte.setText("a")
        # self.tipo_pac.setCurrentIndex(1)
        # self.documento.setText("1")
        # self.telf.setText("1")
        #
        # table1 = self.table_medidas
        # table2 = self.table_pliegues_cut
        # table3 = self.table_perife_circun
        # table4 = self.table_medidas_atleta
        # table5 = self.table_pliegues_cut_atleta
        # table6 = self.table_perife_circun_atleta
        # table7 = self.table_longitud_alt_atleta
        # table8 = self.table_diametros_atleta
        #
        # table1.item(1, 4).setText("1")
        # table1.item(2, 4).setText("2")
        # table1.item(3, 4).setText("3")
        # table2.item(1, 4).setText("4")
        # table2.item(2, 4).setText("5")
        # table2.item(3, 4).setText("6")
        # table2.item(4, 4).setText("7")
        # table3.item(1, 4).setText("8")
        # table3.item(2, 4).setText("9")
        # table3.item(3, 4).setText("10")
        # table3.item(4, 4).setText("11")
        # table3.item(5, 4).setText("12")
        # table3.item(6, 4).setText("13")
        #
        # table4.item(1, 4).setText("1")
        # table4.item(2, 4).setText("2")
        # table4.item(3, 4).setText("3")
        # table4.item(4, 4).setText("4")
        # table4.item(5, 4).setText("5")
        # table4.item(6, 4).setText("6")
        # table5.item(1, 4).setText("7")
        # table5.item(2, 4).setText("8")
        # table5.item(3, 4).setText("9")
        # table5.item(4, 4).setText("10")
        # table5.item(5, 4).setText("11")
        # table5.item(6, 4).setText("12")
        # table5.item(7, 4).setText("13")
        # table5.item(8, 4).setText("14")
        # table6.item(1, 4).setText("15")
        # table6.item(2, 4).setText("16")
        # table6.item(3, 4).setText("17")
        # table6.item(4, 4).setText("18")
        # table6.item(5, 4).setText("19")
        # table6.item(6, 4).setText("20")
        # table6.item(7, 4).setText("21")
        # table6.item(8, 4).setText("22")
        # table6.item(9, 4).setText("23")
        # table6.item(10, 4).setText("24")
        # table6.item(11, 4).setText("25")
        # table6.item(12, 4).setText("26")
        # table6.item(13, 4).setText("27")
        # table6.item(14, 4).setText("28")
        # table6.item(15, 4).setText("29")
        # table6.item(16, 4).setText("30")
        # table7.item(1, 4).setText("31")
        # table7.item(2, 4).setText("32")
        # table7.item(3, 4).setText("33")
        # table7.item(4, 4).setText("34")
        # table7.item(5, 4).setText("35")
        # table7.item(6, 4).setText("36")
        # table7.item(7, 4).setText("37")
        # table7.item(8, 4).setText("38")
        # table8.item(1, 4).setText("39")
        # table8.item(2, 4).setText("40")
        # table8.item(3, 4).setText("41")
        # table8.item(4, 4).setText("42")
        # table8.item(5, 4).setText("43")
        # table8.item(6, 4).setText("44")
        # table8.item(7, 4).setText("45")

        self.btn_sigR1.setEnabled(True)
        self.btn_guardar_medidas.setChecked(False)
        self.btn_agregar_cita.setChecked(False)

        self.content.setCurrentWidget(self.Paciente)
        self.content_patient.setCurrentWidget(self.Pacientes)

    # Tabla con la lista de pacientes

    def rows(self):
        if os.path.exists('pacientes.txt'):
            if os.stat('pacientes.txt').st_size == 0:
                row = 1
                return row
            else:
                data = []
                with open(f'pacientes.txt', 'rb') as file_row:
                    while True:
                        try:
                            info = pickle.load(file_row)
                            data.append(info)
                        except EOFError:
                            break
                row = len(data) + 1
                file_row.close()
                return row
        else:
            open('pacientes.txt', 'ab').close()
            row = 1
            return row

    def items(self):
        items = []
        filas = 0
        with open(f'pacientes.txt', 'rb') as file_new_i:
            while True:
                try:
                    info = pickle.load(file_new_i)
                    items.append(info)
                    filas += 1
                except EOFError:
                    break
        for row in range(filas):
            it = row + 1
            for i in range(6):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                font = QtGui.QFont()
                font.setFamily("Circular Std")
                font.setPointSize(11)
                item.setFont(font)
                item.setFlags(
                    QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                self.table_patient.setItem(it, i, item)

    def content_table_patient(self):
        data_table = []
        row_data = 0
        with open(f'pacientes.txt', 'rb') as file_new_d:
            while True:
                try:
                    info = pickle.load(file_new_d)
                    data_table.append(info)
                    row_data += 1
                except EOFError:
                    break

        for position, datos in enumerate(data_table):
            item = self.table_patient.item(position + 1, 0)
            item.setText(str(datos.__dict__.get('name')))
            item = self.table_patient.item(position + 1, 1)
            item.setText(str(datos.__dict__.get('doc')))
            item = self.table_patient.item(position + 1, 2)
            item.setText(str(datos.__dict__.get('t_pac')))
            item = self.table_patient.item(position + 1, 3)
            item.setText(str(datos.__dict__.get('sex')))
            item = self.table_patient.item(position + 1, 4)
            item.setText(str(datos.__dict__.get('country')))

            self.btn_informe = QtWidgets.QPushButton()
            self.btn_informe.setMinimumSize(QtCore.QSize(20, 20))
            self.btn_informe.setMaximumSize(QtCore.QSize(20, 20))
            font = QtGui.QFont()
            font.setFamily("Circular Std")
            font.setPointSize(11)
            self.btn_informe.setFont(font)
            self.btn_informe.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.btn_informe.setStyleSheet("QPushButton {\n"
                                           "border: 0px solid;\n"
                                           "border-radius: 5px;\n"
                                           "color: black;\n"
                                           "margin: 0px;\n"
                                           "padding: 0px;\n"
                                           "background-color: rgb(0, 0, 30);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background-color: rgb(0, 0, 61);\n"
                                           "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/informe.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.btn_informe.setIcon(icon)
            self.btn_informe.setIconSize(QtCore.QSize(20, 20))
            self.btn_informe.setObjectName("btn_citas")

            self.btn_vinforme = QtWidgets.QPushButton()
            self.btn_vinforme.setMinimumSize(QtCore.QSize(20, 20))
            self.btn_vinforme.setMaximumSize(QtCore.QSize(20, 20))
            font = QtGui.QFont()
            font.setFamily("Circular Std")
            font.setPointSize(11)
            self.btn_vinforme.setFont(font)
            self.btn_vinforme.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.btn_vinforme.setStyleSheet("QPushButton {\n"
                                            "border: 0px solid;\n"
                                            "border-radius: 5px;\n"
                                            "color: black;\n"
                                            "margin: 0px;\n"
                                            "padding: 0px;\n"
                                            "background-color: rgb(0, 0, 30);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "background-color: rgb(0, 0, 61);\n"
                                            "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/edit.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.btn_vinforme.setIcon(icon)
            self.btn_vinforme.setIconSize(QtCore.QSize(20, 20))
            self.btn_vinforme.setObjectName("btn_vinforme")

            self.btn_delete = QtWidgets.QPushButton()
            self.btn_delete.setMinimumSize(QtCore.QSize(20, 20))
            self.btn_delete.setMaximumSize(QtCore.QSize(20, 20))
            font = QtGui.QFont()
            font.setFamily("Circular Std")
            font.setPointSize(11)
            self.btn_delete.setFont(font)
            self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.btn_delete.setStyleSheet("QPushButton {\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 5px;\n"
                                          "color: black;\n"
                                          "margin: 0px;\n"
                                          "padding: 0px;\n"
                                          "background-color: rgb(0, 0, 30);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgb(0, 0, 61);\n"
                                          "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.btn_delete.setIcon(icon)
            self.btn_delete.setIconSize(QtCore.QSize(20, 20))
            self.btn_delete.setObjectName("btn_delete")

            self.btn_informe.clicked.connect(partial(self.ver_cita, item))
            self.btn_vinforme.clicked.connect(partial(self.editar_paciente, item))
            self.btn_delete.clicked.connect(partial(self.eliminar_paciente, item))

            self.fr_button = QtWidgets.QFrame()
            self.fr_button.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.fr_button.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.fr_button.setObjectName("fr_button")
            button_layout = QtWidgets.QHBoxLayout(self.fr_button)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_layout.setSpacing(0)
            button_layout.setObjectName("button_layout")
            button_layout.addWidget(self.btn_informe)
            button_layout.addWidget(self.btn_vinforme)
            button_layout.addWidget(self.btn_delete)
            buttons_widget = QtWidgets.QWidget()
            buttons_widget.setLayout(button_layout)
            self.table_patient.setCellWidget(position + 1, 5, buttons_widget)

    def update_table(self):

        # Update rows
        rows = []
        row = 1
        with open(f'pacientes.txt', 'rb') as file_new_r:
            while True:
                try:
                    info = pickle.load(file_new_r)
                    rows.append(info)
                except EOFError:
                    break
        row = len(rows) + 1
        self.table_patient.setRowCount(row)

        # Update items
        items = []
        filas = 0
        with open(f'pacientes.txt', 'rb') as file_new_i:
            while True:
                try:
                    info = pickle.load(file_new_i)
                    items.append(info)
                    filas += 1
                except EOFError:
                    break
        if filas == 0:
            filas = 1
        for i in range(7):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            font = QtGui.QFont()
            font.setFamily("Circular Std")
            font.setPointSize(11)
            item.setFont(font)
            item.setFlags(
                QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.table_patient.setItem(filas, i, item)

        # Update data
        data_table = []
        new_position = 0
        with open(f'pacientes.txt', 'rb') as file_new_d:
            while True:
                try:
                    info = pickle.load(file_new_d)
                    data_table.append(info)
                    new_position += 1
                except EOFError:
                    break
        for position, datos in enumerate(data_table):
            item = self.table_patient.item(position + 1, 0)
            item.setText(str(datos.__dict__.get('name')))
            item = self.table_patient.item(position + 1, 1)
            item.setText(str(datos.__dict__.get('doc')))
            item = self.table_patient.item(position + 1, 2)
            item.setText(str(datos.__dict__.get('t_pac')))
            item = self.table_patient.item(position + 1, 3)
            item.setText(str(datos.__dict__.get('sex')))
            item = self.table_patient.item(position + 1, 4)
            item.setText(str(datos.__dict__.get('country')))

            self.btn_informe = QtWidgets.QPushButton()
            self.btn_informe.setMinimumSize(QtCore.QSize(20, 20))
            self.btn_informe.setMaximumSize(QtCore.QSize(20, 20))
            font = QtGui.QFont()
            font.setFamily("Circular Std")
            font.setPointSize(11)
            self.btn_informe.setFont(font)
            self.btn_informe.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.btn_informe.setStyleSheet("QPushButton {\n"
                                           "border: 0px solid;\n"
                                           "border-radius: 5px;\n"
                                           "color: black;\n"
                                           "margin: 0px;\n"
                                           "padding: 0px;\n"
                                           "background-color: rgb(0, 0, 30);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background-color: rgb(0, 0, 61);\n"
                                           "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/informe.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.btn_informe.setIcon(icon)
            self.btn_informe.setIconSize(QtCore.QSize(20, 20))
            self.btn_informe.setObjectName("btn_citas")

            self.btn_vinforme = QtWidgets.QPushButton()
            self.btn_vinforme.setMinimumSize(QtCore.QSize(20, 20))
            self.btn_vinforme.setMaximumSize(QtCore.QSize(20, 20))
            font = QtGui.QFont()
            font.setFamily("Circular Std")
            font.setPointSize(11)
            self.btn_vinforme.setFont(font)
            self.btn_vinforme.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.btn_vinforme.setStyleSheet("QPushButton {\n"
                                            "border: 0px solid;\n"
                                            "border-radius: 5px;\n"
                                            "color: black;\n"
                                            "margin: 0px;\n"
                                            "padding: 0px;\n"
                                            "background-color: rgb(0, 0, 30);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "background-color: rgb(0, 0, 61);\n"
                                            "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/edit.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.btn_vinforme.setIcon(icon)
            self.btn_vinforme.setIconSize(QtCore.QSize(20, 20))
            self.btn_vinforme.setObjectName("btn_vinforme")

            self.btn_delete = QtWidgets.QPushButton()
            self.btn_delete.setMinimumSize(QtCore.QSize(20, 20))
            self.btn_delete.setMaximumSize(QtCore.QSize(20, 20))
            font = QtGui.QFont()
            font.setFamily("Circular Std")
            font.setPointSize(11)
            self.btn_delete.setFont(font)
            self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.btn_delete.setStyleSheet("QPushButton {\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 5px;\n"
                                          "color: black;\n"
                                          "margin: 0px;\n"
                                          "padding: 0px;\n"
                                          "background-color: rgb(0, 0, 30);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgb(0, 0, 61);\n"
                                          "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.btn_delete.setIcon(icon)
            self.btn_delete.setIconSize(QtCore.QSize(20, 20))
            self.btn_delete.setObjectName("btn_delete")

            self.btn_informe.clicked.connect(partial(self.ver_cita, item))
            self.btn_vinforme.clicked.connect(partial(self.editar_paciente, item))
            self.btn_delete.clicked.connect(partial(self.eliminar_paciente, item))

            self.fr_button = QtWidgets.QFrame()
            self.fr_button.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.fr_button.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.fr_button.setObjectName("fr_button")
            button_layout = QtWidgets.QHBoxLayout(self.fr_button)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_layout.setSpacing(0)
            button_layout.setObjectName("button_layout")
            button_layout.addWidget(self.btn_informe)
            button_layout.addWidget(self.btn_vinforme)
            button_layout.addWidget(self.btn_delete)
            buttons_widget = QtWidgets.QWidget()
            buttons_widget.setLayout(button_layout)
            self.table_patient.setCellWidget(position + 1, 5, buttons_widget)

    def ingresar_datap(self):
        self.content.setCurrentWidget(self.Paciente)
        self.content_patient.setCurrentWidget(self.data_patient)
        self.ingresar_patient.setCurrentWidget(self.data_personal)

    def txt_exists(self, row):
        if row == -1:
            verify = self.verification()
            if verify == 0:
                if self.tipo_pac.currentIndex() != 0:
                    self.nombrec = self.name.text() + " " + self.apellido.text()
                    self.nombrec_s_3.setText(self.nombrec)
                    self.sex_selected = self.sexo.currentText()
                    self.btn_sigR1.setEnabled(True)
                    if self.tipo_pac.currentText() == "Adulto":
                        self.table_medidas.itemChanged.connect(self.row_table)
                        self.table_pliegues_cut.itemChanged.connect(self.row_table)
                        self.table_perife_circun.itemChanged.connect(self.row_table)
                        self.ingresar_patient.setCurrentWidget(self.Mediciones_adulto)
                    elif self.tipo_pac.currentText() == "Atleta":
                        self.table_medidas_atleta.itemChanged.connect(self.row_table_atleta)
                        self.table_pliegues_cut_atleta.itemChanged.connect(self.row_table_atleta)
                        self.table_perife_circun_atleta.itemChanged.connect(self.row_table_atleta)
                        self.table_longitud_alt_atleta.itemChanged.connect(self.row_table_atleta)
                        self.table_diametros_atleta.itemChanged.connect(self.row_table_atleta)
                        self.ingresar_patient.setCurrentWidget(self.Mediciones_atleta)
                else:
                    msg = QMessageBox()
                    QMessageBox.critical(msg, "Falta un tipo de paciente",
                                         "Por favor, seleccione un tipo de paciente.")
        else:
            self.guardar_edit(row)
            self.patient()
            msg = QMessageBox()
            resp = QMessageBox.question(msg, "Edicion completada",
                                        "¡El paciente ha sido editado con exito!")
            self.update_table()

    def verification(self):
        name = self.name.text()
        apellido = self.apellido.text()
        documento = self.documento.text()
        telf = self.telf.text()
        deporte = self.act_deporte.text()
        correo = self.correo.text()
        direccion = self.direccion

        if name != "":
            if apellido != "":
                if documento != "":
                    if telf != "":
                        if deporte != "":
                            if correo != "":
                                if direccion != "":
                                    return 0
                                elif direccion == "":
                                    msg = QMessageBox()
                                    QMessageBox.warning(msg, "Alerta",
                                                        "El campo de Deporte y Actividades Físicas no puede estar vacio.")
                            elif correo == "":
                                msg = QMessageBox()
                                QMessageBox.warning(msg, "Alerta",
                                                    "El campo de Deporte y Actividades Físicas no puede estar vacio.")
                        elif deporte == "":
                            msg = QMessageBox()
                            QMessageBox.warning(msg, "Alerta",
                                                "El campo de Deporte y Actividades Físicas no puede estar vacio.")
                    elif telf == "":
                        msg = QMessageBox()
                        QMessageBox.warning(msg, "Alerta", "El campo de teléfono no puede estar vacio.")
                elif documento == "":
                    msg = QMessageBox()
                    QMessageBox.warning(msg, "Alerta", "El campo de documento no puede estar vacio.")
            elif apellido == "":
                msg = QMessageBox()
                QMessageBox.warning(msg, "Alerta", "El campo de apellido no puede estar vacio.")
        elif name == "":
            msg = QMessageBox()
            QMessageBox.warning(msg, "Alerta", "El campo de nombre no puede estar vacio.")

    def row_table(self, item):
        table1 = self.table_medidas
        table2 = self.table_pliegues_cut
        table3 = self.table_perife_circun

        try:
            test = float(item.text())
            if (table1.item(1, 4).text() == "" or table1.item(2, 4).text() == "" or table1.item(3,
                                                                                                4).text() == "") and item.row() <= 3:
                medidas = [1, 2]
                table1 = self.table_medidas
                self.item_content(table1, item.row(), medidas)
            if (table2.item(1, 4).text() == "" or table2.item(2, 4).text() == "" or table2.item(3,
                                                                                                4).text() == "" or table2.item(
                4, 4).text() == "") and item.row() <= 4:
                medidas = [0]
                table2 = self.table_pliegues_cut
                self.item_content(table2, item.row(), medidas)
            if (table3.item(1, 4).text() == "" or table3.item(2, 4).text() == "" or table3.item(3,
                                                                                                4).text() == "" or table3.item(
                4, 4).text() == "" or table3.item(5, 4).text() == "" or table3.item(6,
                                                                                    4).text() == "") and item.row() <= 6:
                medidas = [1, 2, 3, 4, 6]
                table3 = self.table_perife_circun
                self.item_content(table3, item.row(), medidas)
        except ValueError:
            if "," in item.text():
                cadena = item.text().replace(",", ".")
                item.setText(cadena)
            elif item.text() == "":
                print("¡Ninguna de las tomas pueden estar vacias!")
            else:
                item.setText("")
                msg = QMessageBox()
                QMessageBox.critical(msg, "Error en la tabla",
                                     "¡Las tomas solo pueden ser valores numericos!")

    def row_table_atleta(self, item):
        table1 = self.table_medidas_atleta
        table2 = self.table_pliegues_cut_atleta
        table3 = self.table_perife_circun_atleta
        table4 = self.table_longitud_alt_atleta
        table5 = self.table_diametros_atleta

        try:
            test = float(item.text())
            if (table1.item(1, 4).text() == "" or table1.item(2, 4).text() == "" or table1.item(3, 4).text() == ""
                or table1.item(4, 4).text() == "" or table1.item(5, 4).text() == "" or table1.item(6, 4).text() == "") and item.row() <= 6:
                medidas = [1, 2, 3, 4, 6]
                self.item_content(table1, item.row(), medidas)
            if (table2.item(1, 4).text() == "" or table2.item(2, 4).text() == "" or table2.item(3, 4).text() == ""
                or table2.item(4, 4).text() == "" or table2.item(5, 4).text() == "" or table2.item(6, 4).text() == ""
                or table2.item(7, 4).text() == "" or table2.item(8, 4).text() == "") and item.row() <= 8:
                medidas = [0]
                table2 = self.table_pliegues_cut_atleta
                self.item_content(table2, item.row(), medidas)
            if (table3.item(1, 4).text() == "" or table3.item(2, 4).text() == "" or table3.item(3, 4).text() == ""
                or table3.item(4, 4).text() == "" or table3.item(5, 4).text() == "" or table3.item(6, 4).text() == ""
                or table3.item(7, 4).text() == "" or table3.item(8, 4).text() == "" or table3.item(9, 4).text() == ""
                or table3.item(10, 4).text() == "" or table3.item(11, 4).text() == "" or table3.item(12, 4).text() == ""
                or table3.item(13, 4).text() == "" or table3.item(14, 4).text() == "" or table3.item(15, 4).text() == ""
                or table3.item(16, 4).text() == "") and item.row() <= 16:
                medidas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
                table3 = self.table_perife_circun_atleta
                self.item_content(table3, item.row(), medidas)
            if (table4.item(1, 4).text() == "" or table4.item(2, 4).text() == "" or table4.item(3, 4).text() == ""
                or table4.item(4, 4).text() == "" or table4.item(5, 4).text() == "" or table4.item(6, 4).text() == ""
                or table4.item(7, 4).text() == "" or table4.item(8, 4).text() == "") and item.row() <= 8:
                medidas = [1, 2, 3, 4, 5, 6, 7, 8]
                table4 = self.table_longitud_alt_atleta
                self.item_content(table4, item.row(), medidas)
            if (table5.item(1, 4).text() == "" or table5.item(2, 4).text() == "" or table5.item(3, 4).text() == ""
                or table5.item(4, 4).text() == "" or table5.item(5, 4).text() == "" or table5.item(6, 4).text() == ""
                or table5.item(7, 4).text() == "") and item.row() <= 7:
                medidas = [1, 2, 3, 4, 5, 6, 7]
                table5 = self.table_diametros_atleta
                self.item_content(table5, item.row(), medidas)
        except ValueError:
            if "," in item.text():
                cadena = item.text().replace(",", ".")
                item.setText(cadena)
            elif item.text() == "":
                print("¡Ninguna de las tomas pueden estar vacias!")
            else:
                item.setText("")
                msg = QMessageBox()
                QMessageBox.critical(msg, "Error en la tabla", "¡Las tomas solo pueden ser valores numericos!")

    def item_content(self, table, row, tipo_m):
        lim = self.check_medidas(row, tipo_m, table)
        if lim != 0:
            if table.item(row, 1).text() != "" or table.item(row, 2).text() != "":
                prueba = self.comparativa(row, lim, table)
                if prueba:
                    table.blockSignals(True)
                    if table.signalsBlocked():
                        if table.item(row, 3).text() == "":
                            msg = QMessageBox()
                            QMessageBox.information(msg, "Aviso",
                                                    "Se requiere que ingrese una 3ra medida")
                            table.item(row, 3).setFlags(
                                QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                            brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
                            table.item(row, 3).setBackground(brush)
                            table.item(row, 4).setText("")
                        self.calculos(row, table)
                        table.blockSignals(False)
                elif not prueba:
                    table.blockSignals(True)
                    if table.signalsBlocked():
                        table.item(row, 3).setFlags(
                            QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                        table.item(row, 3).setText("")
                        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
                        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
                        table.item(row, 3).setBackground(brush)
                        table.item(row, 4).setText("")
                        self.calculos2medidas(row, table)
                        table.blockSignals(False)
            else:
                print("Faltan medidas.")
        else:
            print("Error en las medidas agregadas.")

    def check_medidas(self, i, m, table):

        if table.item(i, 1).text() == "" or table.item(i, 2).text() == "":
            return 0
        else:
            if i in m:
                return 1
            else:
                return 5

    def calculos(self, i, table):

        if table.item(i, 3).text() == "":

            print("La medicion 3 no puede estar vacia.")

        elif table.item(i, 3).text() != "":

            dato1 = float(table.item(i, 1).text())
            dato2 = float(table.item(i, 2).text())
            dato3 = float(table.item(i, 3).text())

            if dato1 <= dato2 <= dato3 or dato3 <= dato2 <= dato1:
                table.item(i, 4).setText(str(dato2))
            elif dato2 <= dato1 <= dato3 or dato3 <= dato1 <= dato2:
                table.item(i, 4).setText(str(dato1))
            else:
                table.item(i, 4).setText(str(dato3))

        else:
            print("Error en el ingreso de datos.")

    def calculos2medidas(self, i, table):

        dato1 = float(table.item(i, 1).text())
        dato2 = float(table.item(i, 2).text())

        datof = (dato1 + dato2) / 2
        table.item(i, 4).setText(str(datof))

    def comparativa(self, i, lim, table):
        dato1 = float(table.item(i, 1).text())
        dato2 = float(table.item(i, 2).text())

        if dato1 != dato2:
            datofp = (abs(dato1 - dato2) / dato1) * 100
            return datofp > lim
        return False

    def comprobar(self):

        if self.btn_sigR1.isEnabled():

            verify = False

            table1 = self.table_medidas
            table2 = self.table_pliegues_cut
            table3 = self.table_perife_circun
            cont1 = 1
            cont2 = 1
            cont3 = 1

            if self.tipo_pac.currentText() == "Adulto":

                for i in range(3):
                    if table1.item(cont1, 4).text() != "":
                        if cont1 == 3:
                            for i in range(4):
                                if table2.item(cont2, 4).text() != "":
                                    if cont2 == 3:
                                        for i in range(6):
                                            if table3.item(cont3, 4).text() != "":
                                                if cont3 == 6:
                                                    verify = True
                                            else:
                                                msg = QMessageBox()
                                                QMessageBox.critical(msg,
                                                                     "Error en la tabla Perifericos/Circunferencias",
                                                                     "Faltan valores por completar en la tabla.")
                                                verify = False
                                                print("Hola")
                                                break
                                            cont3 += 1
                                else:
                                    msg = QMessageBox()
                                    QMessageBox.critical(msg, "Error en la tabla Pliegues Cutaneos",
                                                         "Faltan valores por completar en la tabla.")
                                    verify = False
                                    break
                                cont2 += 1
                    else:
                        msg = QMessageBox()
                        QMessageBox.critical(msg, "Error en la tabla Medidas Simples",
                                             "Faltan valores por completar en la tabla.")
                        verify = False
                        break
                    cont1 += 1

            elif self.tipo_pac.currentText() == "Atleta":

                table1 = self.table_medidas_atleta
                table2 = self.table_pliegues_cut_atleta
                table3 = self.table_perife_circun_atleta
                table4 = self.table_longitud_alt_atleta
                table5 = self.table_diametros_atleta
                cont1 = 1
                cont2 = 1
                cont3 = 1
                cont4 = 1
                cont5 = 1

                for i in range(6):
                    if table1.item(cont1, 4).text() != "":
                        if cont1 == 6:
                            for i in range(8):
                                if table2.item(cont2, 4).text() != "":
                                    if cont2 == 8:
                                        for i in range(16):
                                            if table3.item(cont3, 4).text() != "":
                                                if cont3 == 16:
                                                    for i in range(8):
                                                        if table4.item(cont4, 4).text() != "":
                                                            if cont4 == 8:
                                                                for i in range(7):
                                                                    if table5.item(cont5, 4).text() != "":
                                                                        if cont5 == 7:
                                                                            verify = True
                                                                    else:
                                                                        msg = QMessageBox()
                                                                        QMessageBox.critical(msg,
                                                                                             "Error en la tabla Diametros",
                                                                                             "Faltan valores por completar en la tabla.")
                                                                        verify = False
                                                                        break
                                                                    cont5 += 1
                                                        else:
                                                            msg = QMessageBox()
                                                            QMessageBox.critical(msg,
                                                                                 "Error en la tabla Longitudes",
                                                                                 "Faltan valores por completar en la tabla.")
                                                            verify = False
                                                            break
                                                        cont4 += 1
                                            else:
                                                msg = QMessageBox()
                                                QMessageBox.critical(msg,
                                                                     "Error en la tabla Circunferencias",
                                                                     "Faltan valores por completar en la tabla.")
                                                verify = False
                                                break
                                            cont3 += 1
                                else:
                                    msg = QMessageBox()
                                    QMessageBox.critical(msg, "Error en la tabla Pliegues Cutaneos",
                                                         "Faltan valores por completar en la tabla.")
                                    verify = False
                                    break
                                cont2 += 1
                    else:
                        msg = QMessageBox()
                        QMessageBox.critical(msg, "Error en la tabla Medidas Simples",
                                             "Faltan valores por completar en la tabla.")
                        verify = False
                        break
                    cont1 += 1

            if verify is True:

                self.nombrec = self.name.text() + " " + self.apellido.text()
                self.date = datetime.now().date()
                self.hora = datetime.now().time()
                h = str(self.hora.hour)
                min = str(self.hora.minute)
                seg = str(self.hora.second)
                hora_completa = h + ":" + min + ":" + seg

                self.nombrec_s.setText("Paciente: " + self.nombrec)
                self.fecha_s.setText("Fecha: " + str(self.date))
                self.hora_s.setText("Hora: " + hora_completa)

                self.btn_patient_s.setText("Volver a Pacientes")
                self.btn_patient_s.clicked.connect(self.patient)
                self.ingresar_patient.setCurrentWidget(self.Salida)

                self.guardar_data(self.nombrec, self.date, hora_completa)
            else:
                print("Faltan valores por completar en alguna de las tablas.")
                # msg = QMessageBox()
                # QMessageBox.critical(msg, "Error", "Faltan valores por completar.")

        elif self.btn_agregar_cita.isEnabled():

            verify = False

            data = []
            with open(f'pacientes.txt', 'rb') as file_new_d:
                while True:
                    try:
                        info = pickle.load(file_new_d)
                        data.append(info)
                    except EOFError:
                        break

            multi_medidas = []
            all_data = []
            for position, datos in enumerate(data):
                str(datos.__dict__.get('t_pac'))

                row_data = [datos.__dict__.get('t_pac')]
                all_data.append(row_data)

            if all_data[self.row_update_cita - 1][0] == "Adulto":

                table1 = self.table_medidas
                table2 = self.table_pliegues_cut
                table3 = self.table_perife_circun
                cont1 = 1
                cont2 = 1
                cont3 = 1

                for i in range(3):
                    if table1.item(cont1, 4).text() != "":
                        if cont1 == 3:
                            for i in range(4):
                                if table2.item(cont2, 4).text() != "":
                                    if cont2 == 3:
                                        for i in range(6):
                                            if table3.item(cont3, 4).text() != "":
                                                if cont3 == 6:
                                                    verify = True
                                            else:
                                                msg = QMessageBox()
                                                QMessageBox.critical(msg,
                                                                     "Error en la tabla Perifericos/Circunferencias",
                                                                     "Faltan valores por completar en la tabla.")
                                                verify = False
                                                print("Hola")
                                                break
                                            cont3 += 1
                                else:
                                    msg = QMessageBox()
                                    QMessageBox.critical(msg, "Error en la tabla Pliegues Cutaneos",
                                                         "Faltan valores por completar en la tabla.")
                                    verify = False
                                    break
                                cont2 += 1
                    else:
                        msg = QMessageBox()
                        QMessageBox.critical(msg, "Error en la tabla Medidas Simples",
                                             "Faltan valores por completar en la tabla.")
                        verify = False
                        break
                    cont1 += 1

            elif all_data[self.row_update_cita - 1][0] == "Atleta":

                table1 = self.table_medidas_atleta
                table2 = self.table_pliegues_cut_atleta
                table3 = self.table_perife_circun_atleta
                table4 = self.table_longitud_alt_atleta
                table5 = self.table_diametros_atleta
                cont1 = 1
                cont2 = 1
                cont3 = 1
                cont4 = 1
                cont5 = 1

                for i in range(6):
                    if table1.item(cont1, 4).text() != "":
                        if cont1 == 6:
                            for i in range(8):
                                if table2.item(cont2, 4).text() != "":
                                    if cont2 == 8:
                                        for i in range(16):
                                            if table3.item(cont3, 4).text() != "":
                                                if cont3 == 16:
                                                    for i in range(8):
                                                        if table4.item(cont4, 4).text() != "":
                                                            if cont4 == 8:
                                                                for i in range(7):
                                                                    if table5.item(cont5, 4).text() != "":
                                                                        if cont5 == 7:
                                                                            verify = True
                                                                    else:
                                                                        msg = QMessageBox()
                                                                        QMessageBox.critical(msg,
                                                                                             "Error en la tabla Diametros",
                                                                                             "Faltan valores por completar en la tabla.")
                                                                        verify = False
                                                                        break
                                                                    cont5 += 1
                                                        else:
                                                            msg = QMessageBox()
                                                            QMessageBox.critical(msg,
                                                                                 "Error en la tabla Longitudes",
                                                                                 "Faltan valores por completar en la tabla.")
                                                            verify = False
                                                            break
                                                        cont4 += 1
                                            else:
                                                msg = QMessageBox()
                                                QMessageBox.critical(msg,
                                                                     "Error en la tabla Circunferencias",
                                                                     "Faltan valores por completar en la tabla.")
                                                verify = False
                                                break
                                            cont3 += 1
                                else:
                                    msg = QMessageBox()
                                    QMessageBox.critical(msg, "Error en la tabla Pliegues Cutaneos",
                                                         "Faltan valores por completar en la tabla.")
                                    verify = False
                                    break
                                cont2 += 1
                    else:
                        msg = QMessageBox()
                        QMessageBox.critical(msg, "Error en la tabla Medidas Simples",
                                             "Faltan valores por completar en la tabla.")
                        verify = False
                        break
                    cont1 += 1

            if verify is True:

                data = []
                with open(f'pacientes.txt', 'rb') as file_new_d:
                    while True:
                        try:
                            info = pickle.load(file_new_d)
                            data.append(info)
                        except EOFError:
                            break

                row_data = []
                all_data = []
                medidas = []
                for position, datos in enumerate(data):
                    str(datos.__dict__.get('id'))
                    str(datos.__dict__.get('name'))
                    str(datos.__dict__.get('doc'))
                    str(datos.__dict__.get('t_pac'))
                    str(datos.__dict__.get('sex'))
                    str(datos.__dict__.get('country'))
                    str(datos.__dict__.get('fnacimiento'))
                    str(datos.__dict__.get('medidas'))
                    str(datos.__dict__.get('act_deporte'))
                    str(datos.__dict__.get('correo'))
                    str(datos.__dict__.get('direccion'))

                    row_data = [datos.__dict__.get('id'), datos.__dict__.get('name'), datos.__dict__.get('doc'),
                                datos.__dict__.get('t_pac'), datos.__dict__.get('sex'), datos.__dict__.get('country'),
                                datos.__dict__.get('fnacimiento'), datos.__dict__.get('medidas'),
                                datos.__dict__.get('act_deporte'), datos.__dict__.get('correo'),
                                datos.__dict__.get('direccion')]

                    all_data.append(row_data)

                if all_data[self.row_update_cita-1][3] == "Adulto":

                    self.tipo_pac.setCurrentIndex(1)

                    table1 = self.table_medidas
                    table2 = self.table_pliegues_cut
                    table3 = self.table_perife_circun
                    cont1 = 1
                    cont2 = 1
                    cont3 = 1

                    for i in range(3):
                        medidas.append(table1.item(cont1, 4).text())
                        if cont1 == 3:
                            for i in range(4):
                                medidas.append(table2.item(cont2, 4).text())
                                if cont2 == 3:
                                    for i in range(6):
                                        medidas.append(table3.item(cont2, 4).text())
                                        cont3 += 1
                                cont2 += 1

                        cont1 += 1

                    self.lbl_imc.setText("I.M.C:")
                    self.lbl_icc.setText("I.C.C:")
                    self.lbl_ice.setText("I.C.E:")
                    self.lbl_porcent_grasa.setText("% de Grasa:")
                    self.lbl_p_degrasa.setText("P. de Grasa:")
                    self.lbl_p_degrasa_percentil.setText("% de Grasa en Percentiles:")
                    self.lbl_indice_mlg.setText("Indice M.L.G:")
                    self.lbl_camb.setText("C.A.M.B:")
                    self.lbl_iamb.setText("I.A.M.B:")
                    self.lbl_complex.setText("Complexión:")
                    self.lbl_peso_ideal.setText("Peso Ideal:")

                    lbl_adulto_h = [self.lbl_imc, self.lbl_icc, self.lbl_ice, self.lbl_porcent_grasa
                        , self.lbl_p_degrasa, self.lbl_p_degrasa_percentil, self.lbl_indice_mlg
                        , self.lbl_camb, self.lbl_iamb, self.lbl_complex, self.lbl_peso_ideal]
                    salida_f = self.salida_final(medidas)
                    salida_f = [float(medida) for medida in salida_f]
                    for label, salida in zip(lbl_adulto_h, salida_f):
                        label.setText(f"{label.text()} {salida:.2f}")

                elif all_data[self.row_update_cita-1][3] == "Atleta":

                    self.tipo_pac.setCurrentIndex(2)

                    table1 = self.table_medidas_atleta
                    table2 = self.table_pliegues_cut_atleta
                    table3 = self.table_perife_circun_atleta
                    table4 = self.table_longitud_alt_atleta
                    table5 = self.table_diametros_atleta
                    cont1 = 1
                    cont2 = 1
                    cont3 = 1
                    cont4 = 1
                    cont5 = 1

                    for i in range(6):
                        medidas.append(table1.item(cont1, 4).text())
                        if cont1 == 6:
                            for i in range(8):
                                medidas.append(table2.item(cont2, 4).text())
                                if cont2 == 8:
                                    for i in range(16):
                                        medidas.append(table3.item(cont3, 4).text())
                                        if cont3 == 16:
                                            for i in range(8):
                                                medidas.append(table4.item(cont4, 4).text())
                                                if cont4 == 8:
                                                    for i in range(7):
                                                        medidas.append(table5.item(cont5, 4).text())
                                                cont4 += 1
                                        cont3 += 1
                                cont2 += 1
                        cont1 += 1

                    self.lbl_imc.setText("I.M.C:")
                    self.lbl_icc.setText("% de Grasa:")
                    self.lbl_ice.setText("Indice M.L.G:")
                    self.lbl_porcent_grasa.setText("C.A.M.B:")
                    self.lbl_p_degrasa.setText("I.A.M.B:")
                    self.lbl_p_degrasa_percentil.setText("Complexión:")
                    self.lbl_camb.setText("Indice Cormico:")
                    self.lbl_iamb.setText("Longitud Relativa Superior de la Extremidad:")
                    self.lbl_complex.setText("Indice Esqueletico:")
                    self.lbl_peso_ideal.setText("Envergadura Relativa:")

                    lbl_atleta_h = [self.lbl_imc, self.lbl_icc, self.lbl_ice, self.lbl_porcent_grasa,
                                    self.lbl_p_degrasa, self.lbl_p_degrasa_percentil, self.lbl_camb,
                                    self.lbl_iamb, self.lbl_complex, self.lbl_peso_ideal]

                    salida_f = self.salida_final(medidas)
                    salida_f = [medida for medida in salida_f]

                    self.lbl_indice_mlg.setText("Somatotipo: " + "Endo: " + self.endo +
                                                ", Meso: " + self.meso + ", Ecto: " + self.ecto)

                    for label, salida in zip(lbl_atleta_h, salida_f):
                        label.setText(f"{label.text()} {salida:.2f}")

                self.date = datetime.now().date()
                self.hora = datetime.now().time()
                h = str(self.hora.hour)
                min = str(self.hora.minute)
                seg = str(self.hora.second)
                hora_completa = h + ":" + min + ":" + seg

                medidas.append(str(self.date))
                medidas.append(str(hora_completa))

                all_data[self.row_update_cita-1][7].append(medidas)
                self.nombrec = all_data[self.row_update_cita-1][1]

                self.nombrec_s.setText("Paciente: " + self.nombrec)
                self.fecha_s.setText("Fecha: " + str(self.date))
                self.hora_s.setText("Hora: " + hora_completa)

                for x, data in enumerate(all_data):
                    self.guardar_cita(all_data[x][0], all_data[x][1], all_data[x][2], all_data[x][3],
                                      all_data[x][4],
                                      all_data[x][5], all_data[x][6], all_data[x][7], all_data[x][8],
                                      all_data[x][9], all_data[x][10], x)

                msg = QMessageBox()
                QMessageBox.information(msg, "Registro de cita completado",
                                        "¡La cita fue registrada con exito!")

                self.btn_sigR1.setChecked(False)
                self.btn_guardar_medidas.setChecked(False)
                self.btn_agregar_cita.setChecked(False)

                self.btn_patient_s.setText("Volver a Citas")
                self.btn_patient_s.clicked.connect(lambda: self.volver_cita(self.row_update_cita))
                self.ingresar_patient.setCurrentWidget(self.Salida)

            else:
                print("Faltan valores por completar en alguna de las tablas.")

    def guardar_data(self, nombrec, fecha, hora):

        medidas = []
        multi_medidas = []

        if self.tipo_pac.currentText() == "Adulto":

            table1 = self.table_medidas
            table2 = self.table_pliegues_cut
            table3 = self.table_perife_circun
            cont1 = 1
            cont2 = 1
            cont3 = 1

            for i in range(3):
                medidas.append(table1.item(cont1, 4).text())
                if cont1 == 3:
                    for i in range(4):
                        medidas.append(table2.item(cont2, 4).text())
                        if cont2 == 4:
                            for i in range(6):
                                medidas.append(table3.item(cont3, 4).text())
                                cont3 += 1
                        cont2 += 1

                cont1 += 1

            self.lbl_imc.setText("I.M.C:")
            self.lbl_icc.setText("I.C.C:")
            self.lbl_ice.setText("I.C.E:")
            self.lbl_porcent_grasa.setText("% de Grasa:")
            self.lbl_p_degrasa.setText("P. de Grasa:")
            self.lbl_p_degrasa_percentil.setText("% de Grasa en Percentiles:")
            self.lbl_indice_mlg.setText("Indice M.L.G:")
            self.lbl_camb.setText("C.A.M.B:")
            self.lbl_iamb.setText("I.A.M.B:")
            self.lbl_complex.setText("Complexión:")
            self.lbl_peso_ideal.setText("Peso Ideal:")

            lbl_adulto_h = [self.lbl_imc, self.lbl_icc, self.lbl_ice, self.lbl_porcent_grasa
                , self.lbl_p_degrasa, self.lbl_p_degrasa_percentil, self.lbl_indice_mlg
                , self.lbl_camb, self.lbl_iamb, self.lbl_complex, self.lbl_peso_ideal]

            salida_f = self.salida_final(medidas)
            salida_f = [float(medida) for medida in salida_f]

            for label, salida in zip(lbl_adulto_h, salida_f):
                label.setText(f"{label.text()} {salida:.2f}")

        elif self.tipo_pac.currentText() == "Atleta":

            table1 = self.table_medidas_atleta
            table2 = self.table_pliegues_cut_atleta
            table3 = self.table_perife_circun_atleta
            table4 = self.table_longitud_alt_atleta
            table5 = self.table_diametros_atleta
            cont1 = 1
            cont2 = 1
            cont3 = 1
            cont4 = 1
            cont5 = 1

            for i in range(6):
                medidas.append(table1.item(cont1, 4).text())
                if cont1 == 6:
                    for i in range(8):
                        medidas.append(table2.item(cont2, 4).text())
                        if cont2 == 8:
                            for i in range(16):
                                medidas.append(table3.item(cont3, 4).text())
                                if cont3 == 16:
                                    for i in range(8):
                                        medidas.append(table4.item(cont4, 4).text())
                                        if cont4 == 8:
                                            for i in range(7):
                                                medidas.append(table5.item(cont5, 4).text())
                                                cont5 += 1
                                        cont4 += 1
                                cont3 += 1
                        cont2 += 1
                cont1 += 1

            self.lbl_imc.setText("I.M.C:")
            self.lbl_icc.setText("% de Grasa:")
            self.lbl_ice.setText("Indice M.L.G:")
            self.lbl_porcent_grasa.setText("C.A.M.B:")
            self.lbl_p_degrasa.setText("I.A.M.B:")
            self.lbl_p_degrasa_percentil.setText("Complexión:")
            self.lbl_camb.setText("Indice Cormico:")
            self.lbl_iamb.setText("Longitud Relativa Superior de la Extremidad:")
            self.lbl_complex.setText("Indice Esqueletico:")
            self.lbl_peso_ideal.setText("Envergadura Relativa:")

            lbl_atleta_h = [self.lbl_imc, self.lbl_icc, self.lbl_ice, self.lbl_porcent_grasa,
                            self.lbl_p_degrasa, self.lbl_p_degrasa_percentil, self.lbl_camb,
                            self.lbl_iamb, self.lbl_complex, self.lbl_peso_ideal]

            salida_f = self.salida_final(medidas)
            salida_f = [medida for medida in salida_f]

            self.lbl_indice_mlg.setText("Somatotipo: " + "Endo: " + self.endo +
                                        ", Meso: " + self.meso + ", Ecto: " + self.ecto)

            for label, salida in zip(lbl_atleta_h, salida_f):
                label.setText(f"{label.text()} {salida:.2f}")

        medidas.append(str(fecha))
        medidas.append(str(hora))
        multi_medidas.append(medidas)

        datas = []
        self.doc_complete = self.tipo_doc.currentText() + "-" + self.documento.text()
        self.fecha_nac = str(self.fnacimiento.text())
        if os.stat('pacientes.txt').st_size == 0:
            new_patient = Patient(1, nombrec, self.doc_complete, self.tipo_pac.currentText(),
                                  self.sexo.currentText(), self.country.currentText(), self.fecha_nac, multi_medidas,
                                  self.act_deporte.text(), self.correo.text(), self.direccion.text())
            with open(f'pacientes.txt', 'ab') as file:
                pickle.dump(new_patient, file)
            file.close()
            self.btn_sigR1.setChecked(False)
            self.btn_guardar_medidas.setChecked(False)
            self.btn_agregar_cita.setChecked(False)
            self.confirm_patient()
        else:
            with open(f'pacientes.txt', 'rb') as file2:
                while True:
                    try:
                        data = pickle.load(file2)
                        datas.append(data)
                    except EOFError:
                        break
                file2.close()
            for indice, data in enumerate(datas, start=1):
                if self.documento.text() in data.__dict__.values():
                    self.problem_patient()
                    break
                elif self.documento.text() not in data.__dict__.values() and indice in data.__dict__.values():
                    self.doc_complete = self.tipo_doc.currentText() + "-" + self.documento.text()
                    id = indice + len(datas)
                    new_patient = Patient(str(id), nombrec, self.doc_complete, self.tipo_pac.currentText(),
                                          self.sexo.currentText(), self.country.currentText(), self.fecha_nac,
                                          multi_medidas, self.act_deporte.text(), self.correo.text(),
                                          self.direccion.text())
                    with open(f'pacientes.txt', 'ab') as file:
                        pickle.dump(new_patient, file)
                    file.close()
                    self.btn_sigR1.setChecked(False)
                    self.btn_guardar_medidas.setChecked(False)
                    self.btn_agregar_cita.setChecked(False)
                    self.confirm_patient()
                    break

    def salida_final(self, medidas):

        if self.tipo_pac.currentText() == "Adulto":
            fecha_nac = datetime.strptime(str(self.fnacimiento.text()), "%d/%m/%Y")
            now = datetime.now()
            date = now.strftime("%d/%m/%Y")
            fecha_me = datetime.strptime(str(date), "%d/%m/%Y")
            edad = relativedelta(fecha_me, fecha_nac).years

            estatura = float(medidas[0]) / 100
            peso = float(medidas[1])
            prof_abdominal = float(medidas[2])
            triceps = float(medidas[3])
            subescapular = float(medidas[4])
            biceps = float(medidas[5])
            cresta_iliaca = float(medidas[6])
            p_brazo_rela = float(medidas[7])
            p_brazo_flex_contraido = float(medidas[8])
            p_muñeca = float(medidas[9])
            p_min_cintura = float(medidas[10])
            p_abdo = float(medidas[11])
            p_caderas = float(medidas[12])

            imc = peso / (estatura ** 2)

            icc = p_min_cintura / p_caderas

            ice = p_min_cintura / estatura

            porcent_grasa = triceps + subescapular + biceps + cresta_iliaca
            porcent_grasa_con_log = log10(porcent_grasa)
            dato6 = 0
            if self.sex_selected == "Masculino":
                dato6 = 1.1610 - (0.0632 * porcent_grasa_con_log)
            else:
                dato6 = 1.1581 - (0.0720 * porcent_grasa_con_log)
            dato7 = ((4.95 / dato6) - 4.50) * 100
            porcent_grasa_f = dato7

            peso_d_grasa = peso * (porcent_grasa_f / 100)

            porcent_grasa_percentil = 0
            if self.sex_selected == "Masculino":
                porcent_grasa_percentil = self.porcent_grasa_percentil_h(porcent_grasa_f, edad)
            else:
                porcent_grasa_percentil = self.porcent_grasa_percentil_m(porcent_grasa_f, edad)

            indice_mlg = 0
            if self.sex_selected == "Masculino":
                (peso * (((100 - porcent_grasa_f) / 100) + 6.1 * (1.8 * estatura))) / estatura ** 2
            else:
                indice_mlg = (peso * ((100 - porcent_grasa_f) / 100)) / estatura ** 2
            dato_extra = 0.31416 * (triceps / 10)

            camb = 0
            if self.sex_selected == "Masculino":
                camb = (((p_brazo_rela - dato_extra) ** 2) / (4 * 3.1416)) - 10.0
            else:
                camb = (((p_brazo_rela - dato_extra) ** 2) / (4 * 3.1416)) - 6.5

            iamb = 0
            if self.sex_selected == "Masculino":
                iamb = self.iamb(porcent_grasa_f, edad)
            else:
                iamb = self.iamb_m(porcent_grasa_f, edad)

            complex = estatura / p_muñeca

            peso_ideal = 0
            if self.sex_selected == "Masculino":
                peso_ideal = estatura - 100 - (((estatura - 150) / 4) + ((edad - 20) / 20))
            else:
                peso_ideal = estatura - 100 - (((estatura - 150) / 2.5) + ((edad - 20) / 20))

            salida = [imc, icc, ice, porcent_grasa_f, peso_d_grasa, porcent_grasa_percentil, indice_mlg, camb, iamb,
                      complex, peso_ideal]
            return salida

        elif self.tipo_pac.currentText() == "Atleta":
            fecha_nac = datetime.strptime(str(self.fnacimiento.text()), "%m/%d/%Y")
            now = datetime.now()
            date = now.strftime("%m/%d/%Y")
            fecha_me = datetime.strptime(str(date), "%m/%d/%Y")
            edad = relativedelta(fecha_me, fecha_nac).years

            #table1
            estatura = float(medidas[0]) / 100
            peso = float(medidas[1])
            estatura_sentado = float(medidas[2])
            envergadura = float(medidas[3])
            profundidad_abdo = float(medidas[4])
            longitud_acromio_dedal = float(medidas[5])

            #table2
            triceps = float(medidas[6])
            subescapular = float(medidas[7])
            biceps = float(medidas[8])
            cresta_ili = float(medidas[9])
            supraespinal = float(medidas[10])
            abdominal = float(medidas[11])
            muslo_frontal = float(medidas[12])
            pantorrilla = float(medidas[13])

            #table3
            per_cefalico = float(medidas[14])
            per_cuello = float(medidas[15])
            per_brazo_rela = float(medidas[16])
            per_brazo_flex_cont = float(medidas[17])
            per_maximo_antebr_der = float(medidas[18])
            per_maximo_antebr_izq = float(medidas[19])
            per_muneca = float(medidas[20])
            per_torax = float(medidas[21])
            per_min_cintura = float(medidas[22])
            per_abdo = float(medidas[23])
            per_caderas = float(medidas[24])
            per_muslo_der = float(medidas[25])
            per_muslo_izq = float(medidas[26])
            per_muslo_medio = float(medidas[27])
            per_pantorrilla = float(medidas[28])
            per_min_tobillo = float(medidas[29])

            #table4
            acromiale_radiale = float(medidas[30])
            radiale_stylion = float(medidas[31])
            midstylion_dactylion = float(medidas[32])
            altura_iliospinale = float(medidas[33])
            altura_trochanterion = float(medidas[34])
            trochanterion_tibiale_laterale = float(medidas[35])
            altura_tibiale_laterale = float(medidas[36])
            tibiale_laterale_sphyrion_tibiale = float(medidas[37])

            #table5
            diam_biacromial = float(medidas[38])
            diam_biiliocristal = float(medidas[39])
            largo_pie = float(medidas[40])
            anchura_torax_transverso = float(medidas[41])
            prof_torax_ante_poste = float(medidas[42])
            diam_biepicondilar_humero = float(medidas[43])
            diam_biepicondilar_femur = float(medidas[44])
            imc = self.logica_imc_atl(estatura, peso)
            porcent_grasa = self.logica_porcentaje_grasa_atl(self.sexo.currentText(), triceps, subescapular, cresta_ili, abdominal, muslo_frontal,
                                                             pantorrilla)
            indice_mlg = self.logica_mlg_atl(peso, porcent_grasa, estatura)
            result_camb_iamb = self.logica_camb__iamb_atl(self.sexo.currentText(), per_brazo_rela, triceps)
            camb = result_camb_iamb[0]
            iamb = result_camb_iamb[1]
            complexion = self.complexion_atl(estatura, per_muneca)
            somatotipo = self.somatotipo_atl(estatura, triceps, subescapular, supraespinal, diam_biepicondilar_humero,
                                            diam_biepicondilar_femur, per_brazo_rela, per_pantorrilla, pantorrilla, peso)
            self.endo = str(somatotipo[0])
            self.meso = str(somatotipo[1])
            self.ecto = str(somatotipo[2])
            """fracc_corporal = self.fraccionamiento_corporal_atl(self.sexo.currentText(), peso, estatura, per_cefalico,
                                                              diam_biacromial, diam_biiliocristal, diam_biepicondilar_humero,
                                                              diam_biepicondilar_femur, triceps, subescapular, supraespinal,
                                                              abdominal, muslo_frontal, pantorrilla, per_brazo_rela, per_maximo_antebr_der,
                                                              per_muslo_medio, per_pantorrilla, per_torax, prof_torax_ante_poste,
                                                              anchura_torax_transverso, per_min_cintura, estatura_sentado)"""
            indice_cormico = self.indice_cormico_atl(estatura, estatura_sentado)
            longitud_relativa_extremidad_super = self.longitud_relativa_extremidad_superior_atl(longitud_acromio_dedal, estatura)
            ind_esqueletico = self.indice_esqueletico_atl(estatura, estatura_sentado)
            envergadura_relativa = self.envergadura_relativa_atl(envergadura, estatura)

            salida = [imc, porcent_grasa, indice_mlg, camb, iamb, complexion, indice_cormico,
                      longitud_relativa_extremidad_super, ind_esqueletico, envergadura_relativa]

            return salida

    def logica_imc_atl(self, altura, peso):
        dato1 = float(altura)
        dato2 = float(peso)
        IMC_atl = dato2 / dato1 ** 2
        return IMC_atl

    ##manuargpop: problema, existen mas de 6 pliegues, preguntar al profesor manuel
    def logica_porcentaje_grasa_atl(self, sexo, triceps, subescapular, cresta_ili, abdominal, muslo_anterior, pantorrilla_medial):
        dato1 = float(triceps)
        dato2 = float(subescapular)
        dato3 = float(cresta_ili)
        dato4 = float(abdominal)
        dato5 = float(muslo_anterior)
        dato6 = float(pantorrilla_medial)
        if sexo == "Masculino":
            porcentaje_grasa_atl = ((dato1 + dato2 + dato3 + dato4 + dato5 + dato6) * 0.1051) + 2.585
            return porcentaje_grasa_atl
        elif sexo == "Femenino":
            porcentaje_grasa_atl = ((dato1 + dato2 + dato3 + dato4 + dato5 + dato6) * 0.1548) + 3.580
            return porcentaje_grasa_atl
        else:
            print("error en sexo")

    def logica_mlg_atl(self, peso, porcentaje_grasa_atl, altura):
        dato1 = float(peso)
        dato2 = float(porcentaje_grasa_atl)
        dato3 = float(altura)
        MLG_atl = (peso * (((100 - porcentaje_grasa_atl) / 100) + 6.1 * (1.8 * dato3))) / dato3 ** 2
        return MLG_atl

    def logica_camb__iamb_atl(self, sexo, circunferencia_brazo_rela, pliegue_triceps):

        if sexo == "Masculino":
            dato1 = float(circunferencia_brazo_rela)
            dato2 = float(pliegue_triceps)
            dato3 = 0.31416 * (dato2 / 10)
            camb = (((dato1 - dato3) ** 2) / (4 * 3.1416)) - 10.0

            fecha_de_nacimiento = datetime.strptime(str(self.fnacimiento.text()), "%m/%d/%Y")
            now = datetime.now()
            date = now.strftime("%m/%d/%Y")
            fecha_de_medicion = datetime.strptime(str(date), "%m/%d/%Y")

            porcentaje_g = camb
            edad_u = float(relativedelta(fecha_de_medicion, fecha_de_nacimiento).years)

            edad_min = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
            edad_max = [24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74]
            tabla = [34.2, 37.3, 39.6, 42.7, 49.4, 57.1, 61.8, 65.0, 72.0], [36.6, 39.9, 42.4, 46.0, 53.0, 61.4,
                                                                             66.1, 68.9, 74.5], [37.9, 40.9, 43.4,
                                                                                                 47.3, 54.4, 63.2,
                                                                                                 67.6, 70.8,
                                                                                                 76.1], [38.5, 42.6,
                                                                                                         44.6, 47.9,
                                                                                                         55.3, 64.0,
                                                                                                         69.1, 72.7,
                                                                                                         77.6], [
                38.4, 42.1, 45.1, 48.7, 56.0, 64.0, 68.5, 71.6, 77.0], [37.7, 41.3, 43.7, 47.9, 55.2, 63.3, 68.4,
                                                                        72.2, 76.2], [36.0, 40.0, 42.7, 46.6, 54.0,
                                                                                      62.7, 67.0, 70.4, 77.4], [
                36.5, 40.8, 42.7, 46.7, 54.3, 61.9, 66.4, 69.6, 75.1], [34.5, 38.7, 41.2, 44.9, 52.1, 60.0, 64.8,
                                                                        67.5, 71.6], [31.4, 35.8, 38.4, 42.3, 49.1,
                                                                                      57.3, 61.2, 64.3, 69.4], [
                29.7, 33.8, 36.1, 40.2, 47.0, 54.6, 59.1, 62.1, 67.3]
            percentil = [5, 10, 15, 25, 50, 75, 85, 90, 95]

            for edad in zip(edad_min, edad_max):

                if edad_u >= edad[0] and edad_u <= edad[1]:

                    posicion_edad = edad_min.index(edad[0])
                    percentage = tabla[posicion_edad]

                    for valor in percentage:
                        closest_body_fat = min(percentage, key=lambda x: abs(x - porcentaje_g))
                        if closest_body_fat == valor:
                            ubicacion = percentage.index(valor)
                            iamb_atl = (percentil[ubicacion])
                            resultado = [camb, iamb_atl]
                            return resultado

        elif sexo == "Femenino":
            dato1 = float(circunferencia_brazo_rela)
            dato2 = float(pliegue_triceps)
            dato3 = 0.31416 * (dato2 / 10)
            camb = (((dato1 - dato3) ** 2) / (4 * 3.1416)) - 6.5

            fecha_de_nacimiento = datetime.strptime(str(self.fnacimiento.text()), "%m/%d/%Y")
            now = datetime.now()
            date = now.strftime("%m/%d/%Y")
            fecha_de_medicion = datetime.strptime(str(date), "%m/%d/%Y")

            porcentaje_g = camb
            edad_u = float(relativedelta(fecha_de_medicion, fecha_de_nacimiento).years)

            edad_min = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
            edad_max = [24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74]
            tabla = [19.5, 21.5, 22.8, 23.5, 28.3, 33.1, 36.4, 39.0, 44.2], [20.5, 21.9, 23.1, 25.2, 29.4, 34.9,
                                                                             38.5, 41.9, 47.8], [21.1, 23.0, 24.2,
                                                                                                 26.3, 30.9, 36.8,
                                                                                                 41.2, 44.7,
                                                                                                 51.3], [21.1, 23.4,
                                                                                                         24.7, 27.3,
                                                                                                         31.8, 38.7,
                                                                                                         43.1, 46.1,
                                                                                                         54.2], [
                21.3, 23.4, 25.5, 27.5, 32.3, 39.8, 45.8, 49.5, 55.8], [21.6, 23.1, 24.8, 27.4, 32.5, 39.5, 44.7,
                                                                        48.4, 56.1], [22.2, 24.6, 25.7, 28.3, 33.4,
                                                                                      40.4, 46.1, 49.6, 55.6], [
                22.8, 24.7, 26.5, 28.7, 33.7, 42.3, 47.3, 52.1, 58.8], [22.4, 24.5, 26.3, 29.2, 34.5, 41.1, 45.6,
                                                                        49.1, 55.1], [21.9, 24.5, 26.2, 28.9, 34.6,
                                                                                      41.6, 46.3, 49.6, 56.5], [
                22.2, 24.4, 26.0, 28.8, 34.3, 41.8, 46.4, 49.2, 54.6]
            percentil = [5, 10, 15, 25, 50, 75, 85, 90, 95]

            for edad in zip(edad_min, edad_max):

                if edad_u >= edad[0] and edad_u <= edad[1]:

                    posicion_edad = edad_min.index(edad[0])
                    percentage = tabla[posicion_edad]

                    for valor in percentage:
                        closest_body_fat = min(percentage, key=lambda x: abs(x - porcentaje_g))
                        if closest_body_fat == valor:
                            ubicacion = percentage.index(valor)
                            iamb_atl = (percentil[ubicacion])
                            resultado = [camb, iamb_atl]
                            return resultado

    def complexion_atl(self, altura, circunferencia_muñeca):
        dato1 = float(altura)
        dato2 = float(circunferencia_muñeca)
        complexion_atl = dato1 / dato2
        return complexion_atl

    def somatotipo_atl(self, altura, pliegue_triceps, pliegue_subescapular, pliegue_supraespinal, diametro_humero,
                       diametro_femur, perimetro_circunferencia_brazo_relajado, perimetro_circunferencia_pantorrilla,
                       pliegue_pantorilla, peso):
        ##manuargpop: inicia el de endomorfo
        dato1 = float(altura)
        dato2 = float(pliegue_triceps)
        dato3 = float(pliegue_subescapular)
        dato4 = float(pliegue_supraespinal)
        dato5 = dato1 + dato2 + dato3
        dato6 = dato5 * (170.18 / dato1)
        endomorfia = (0.1451 * dato6) - (0.00068 * (dato6 ** 2)) + (0.0000014 * (dato6 ** 3)) - 0.7182
        ##manuargpop: un resultado tipico seria 2.6 o 2.61

        ##manuargpop: inicia el de mesomorfo
        dato7 = float(diametro_humero)
        dato8 = float(diametro_femur)

        dato9 = float(perimetro_circunferencia_brazo_relajado)
        dato10 = float(dato9 - (dato2 / 10))

        dato11 = float(perimetro_circunferencia_pantorrilla)
        dato12 = float(pliegue_pantorilla)
        dato13 = float(dato11 - (dato12 / 10))
        mesomorfia = (0.858 * dato7) + (0.601 * dato8) + (0.188 * dato10) + (0.161 * dato13) - (0.131 * dato1) + 4.50

        ##manuargpop: inicia ectomorfia
        def getectomorfia(dato12):
            if dato12 > 40.75:
                ectomorfiar = (dato12 * 0.732) - 28.58
                return ectomorfiar
            elif 40.75 >= dato12 >= 38.25:
                ectomorfiar = (dato12 * 0.463) - 17.63
                return ectomorfiar
            elif dato12 < 38.25:
                ectomorfiar = 0.1
                return ectomorfiar
            else:
                print("error ectomorfia")

        dato11 = float(peso)
        dato12 = dato1 / (dato11 ** (1 / 3))
        ectomorfia = getectomorfia(dato12)

        ##inicia x y y en el plano delsomatotipo
        datox = ectomorfia - endomorfia
        datoy = 2 * mesomorfia - (endomorfia + ectomorfia)
        ##esto se usara para una futura grafica de somatotipo
        somatotipo_f = [endomorfia, mesomorfia, ectomorfia, datox, datoy]
        return somatotipo_f

    def fraccionamiento_corporal_atl(self, sexo, peso, altura, perimetro_cefalico, diametro_biacromial,
                                     diametro_biiliocristal, diametro_humero, diametro_femur,
                                     pliegue_cutaneo_triceps, pliegue_cutaneo_subescapular, pliegue_cutaneo_supraespinal,
                                     pliegue_cutaneo_abdominal, pliegue_cutaneo_muslo_frontal, pliegue_cutaneo_pantorrilla_medial,
                                     circunferencia_brazo_relajado, circunferencia_antebrazo, circunferencia_muslo,
                                     circunferencia_pantorrilla, circunferencia_torax, profundidad_anteroposterior_tórax,
                                     diametro_transversal_torax, circunferencia_cintura, estatura_sentado):

        def getcas(sexo):
            if sexo == "Masculino":
                return 68.308
            elif sexo == "Femenino":
                return 73.074
            else:
                print("Error en el sexo")

        def gettsk(sexo):
            if sexo == "Masculino":
                return 2.07
            elif sexo == "Femenino":
                return 1.96
            else:
                print("Error en el sexo")

        ##inicio masa de la piel

        cas = getcas(sexo)
        dato1 = float(peso)
        dato2 = float(altura)  ##(en_centimetros)

        sa = cas * (dato1 ** 0.425) * (dato2 ** 0.725) / 10000
        tsk = gettsk(sexo)

        masa_piel = sa * tsk * 1.05

        ##inicio prediccion de la masa osea

        dato3 = float(perimetro_cefalico)
        z_osea_cabeza = (dato3 - 57) / 1.44
        m_osea_cabeza = (z_osea_cabeza * 0.18) + 1.20

        dato4 = float(diametro_biacromial)
        dato5 = float(diametro_biiliocristal)
        dato6 = float(diametro_humero)
        dato7 = float(diametro_femur)

        scorporal = (dato4 + dato5 + dato6 + dato7)

        zcorporal = ((scorporal * (170.18 / dato2)) - 98.88) / 5.33

        mcorporal = ((zcorporal * 1.34) + 6.70) / (170.18 / dato2) ** 3

        total_masa_osea = m_osea_cabeza + mcorporal

        ##inicio prediccion dle tegido adiposo

        dato8 = float(pliegue_cutaneo_triceps)
        dato9 = float(pliegue_cutaneo_subescapular)
        dato10 = float(pliegue_cutaneo_supraespinal)
        dato11 = float(pliegue_cutaneo_abdominal)
        dato12 = float(pliegue_cutaneo_muslo_frontal)
        dato13 = float(pliegue_cutaneo_pantorrilla_medial)

        sadiposa = dato8 + dato9 + dato10 + dato11 + dato12 + dato13

        zadiposa = ((sadiposa * (170.18 / dato2)) - 116.41) / 34.79

        madiposa = ((zadiposa * 5.85) + 25.4) / (170.18 / dato2) ** 3

        ##inicio prediccion de la masa muscular

        cbrc = float(circunferencia_brazo_relajado) - (3.14 * (dato8 / 10))
        ca = float(circunferencia_antebrazo)
        cmfc = float(circunferencia_muslo) - (3.14 * (dato12 / 10))
        cpmc = float(circunferencia_pantorrilla) - (3.14 * (dato13 / 10))
        ctc = float(circunferencia_torax) - (3.14 * (dato9 / 10))

        smus = cbrc + ca + cmfc + cpmc + ctc

        zmus = (smus * (170.18 / dato2) - 207.21) / 13.74

        mmusculae = ((zmus * 5.4) + 24.5) / (170.18 / dato2) ** 3

        ##inicia prediccion de masa residual
        dato14 = float(profundidad_anteroposterior_tórax)  ##esta en diametros
        dato15 = float(diametro_transversal_torax)
        dato16 = float(circunferencia_cintura) - (3.14 * dato11)
        sres = (dato14 + dato15 + dato16)
        hs = float(estatura_sentado)
        zres = ((sres * (89.92 / hs)) - 109.35) / 7.08

        mres = ((zres * 1.24) + 1.60) / (89.92 / hs) ** 3

        ##inicio masa total
        masa_total = masa_piel + madiposa + mmusculae + total_masa_osea + mres

        fracc_corp_f = [masa_piel, total_masa_osea, madiposa, mmusculae, mres, masa_total]
        return fracc_corp_f

    ##inicio indice cormico
    def indice_cormico_atl(self, estatura, estatura_sentado):
        dato1 = float(estatura)
        dato2 = float(estatura_sentado)
        icor = (dato2 / dato1) * 100
        return icor

    ##inicio longitud relativa de la extremidad superior

    def longitud_relativa_extremidad_superior_atl(self, longitud_acromio_dedal, estatura):
        dato1 = float(longitud_acromio_dedal)  ##en cm
        dato2 = float(estatura)
        lres = (dato1 / dato2) * 100

        ##esto es para medica
        if lres <= 44.9:
            print("usted califica en braquibraquial, osea, tiene extremidades superiores cortas")
        elif 45 < lres < 46.9:
            print("usted califica en mesobraquial, osea, tiene extremidades superiores intermedias")
        elif lres >= 47:
            print("usted califica en macrobraquial, osea, tiene extremidades superiores largas")

        return lres

    ##inicio indice esqueletico
    def indice_esqueletico_atl(self, estatura, estatura_sentado):
        dato1 = float(estatura)
        dato2 = float(estatura_sentado)
        ie = ((dato1 - dato2) / dato2) * 100
        return ie

    ##inicio envergadura relativa
    def envergadura_relativa_atl(self, envergadura, estatura):
        dato1 = float(envergadura)
        dato2 = float(estatura)
        er = (dato1 / dato2) * 100
        return er

    #Editar paciente

    def editar_paciente(self, item):

        confirm = self.confirm_edit()

        if confirm == "y":

            row = item.row()

            data = []
            with open(f'pacientes.txt', 'rb') as file_new_d:
                while True:
                    try:
                        info = pickle.load(file_new_d)
                        data.append(info)
                    except EOFError:
                        break

            row_data = []
            all_data = []
            for position, datos in enumerate(data):
                str(datos.__dict__.get('id'))
                str(datos.__dict__.get('name'))
                str(datos.__dict__.get('doc'))
                str(datos.__dict__.get('t_pac'))
                str(datos.__dict__.get('sex'))
                str(datos.__dict__.get('country'))
                str(datos.__dict__.get('fnacimiento'))
                str(datos.__dict__.get('medidas'))
                str(datos.__dict__.get('act_deporte'))
                str(datos.__dict__.get('correo'))
                str(datos.__dict__.get('direccion'))

                row_data = [datos.__dict__.get('id'), datos.__dict__.get('name'), datos.__dict__.get('doc'),
                            datos.__dict__.get('t_pac'), datos.__dict__.get('sex'), datos.__dict__.get('country'),
                            datos.__dict__.get('fnacimiento'), datos.__dict__.get('medidas'),
                            datos.__dict__.get('act_deporte'), datos.__dict__.get('correo'),
                            str(datos.__dict__.get('direccion'))]

                all_data.append(row_data)

            nombre_sin_div = str(all_data[row - 1][1])
            nombre_apellido = nombre_sin_div.split()
            self.name.setText(nombre_apellido[0])
            self.apellido.setText(nombre_apellido[1])
            self.documento.setText(str(all_data[row - 1][2]))
            for x in range(2):
                self.tipo_pac.setCurrentIndex(x)
                if self.tipo_pac.currentText() == str(all_data[row - 1][3]):
                    self.tipo_pac.setCurrentIndex(x)
                    break
            for x in range(2):
                self.sexo.setCurrentIndex(x)
                if self.sexo.currentText() == str(all_data[row - 1][4]):
                    self.sexo.setCurrentIndex(x)
                    break
            for x in range(195):
                self.country.setCurrentIndex(x)
                if self.country.currentText() == str(all_data[row - 1][5]):
                    self.country.setCurrentIndex(x)
                    break
            self.act_deporte.setText(str(all_data[row - 1][8]))
            self.correo.setText(str(all_data[row - 1][9]))
            self.direccion.setText(str(all_data[row - 1][10]))

            self.content.setCurrentWidget(self.Paciente)
            self.content_patient.setCurrentWidget(self.data_patient)
            self.ingresar_patient.setCurrentWidget(self.data_personal)

            self.btn_sigR1.clicked.connect(lambda: self.txt_exists(row - 1))

        else:
            print("No se ha confirmado el proceso de edicion.")

    def guardar_edit(self, row):
        data = []
        with open(f'pacientes.txt', 'rb') as file_new_d:
            while True:
                try:
                    info = pickle.load(file_new_d)
                    data.append(info)
                except EOFError:
                    break

        row_data = []
        all_data = []
        for position, datos in enumerate(data):
            str(datos.__dict__.get('id'))
            str(datos.__dict__.get('name'))
            str(datos.__dict__.get('doc'))
            str(datos.__dict__.get('t_pac'))
            str(datos.__dict__.get('sex'))
            str(datos.__dict__.get('country'))
            str(datos.__dict__.get('fnacimiento'))
            str(datos.__dict__.get('medidas'))
            str(datos.__dict__.get('act_deporte'))
            str(datos.__dict__.get('correo'))
            str(datos.__dict__.get('direccion'))

            row_data = [datos.__dict__.get('id'), datos.__dict__.get('name'), datos.__dict__.get('doc'),
                        datos.__dict__.get('t_pac'), datos.__dict__.get('sex'), datos.__dict__.get('country'),
                        datos.__dict__.get('fnacimiento'), datos.__dict__.get('medidas'),
                        datos.__dict__.get('act_deporte'), datos.__dict__.get('correo'),
                        str(datos.__dict__.get('direccion'))]

            all_data.append(row_data)

        all_data[int(row)][1] = self.name.text() + " " + self.apellido.text()
        all_data[int(row)][2] = self.documento.text()
        all_data[int(row)][3] = self.tipo_pac.currentText()
        all_data[int(row)][4] = self.sexo.currentText()
        all_data[int(row)][5] = self.country.currentText()
        all_data[int(row)][6] = str(self.fnacimiento.text())
        all_data[int(row)][8] = self.act_deporte.text()
        all_data[int(row)][9] = self.correo.text()
        all_data[int(row)][10] = self.direccion.text()

        for x, data in enumerate(all_data):
            if x == 0:
                new_patient = Patient(data[0], data[1], data[2],
                                      data[3], data[4],
                                      data[5], data[6], data[7], data[8], data[9], data[10])
                with open(f'pacientes.txt', 'wb') as file:
                    pickle.dump(new_patient, file)
            else:
                new_patient = Patient(data[0], data[1], data[2],
                                      data[3], data[4],
                                      data[5], data[6], data[7], data[8], data[9], data[10])
                with open(f'pacientes.txt', 'ab') as file:
                    pickle.dump(new_patient, file)
        file.close()

    def confirm_edit(self):
        msg = QMessageBox()
        resp = QMessageBox.question(msg, "Confirmación",
                             "¿Está seguro que desea editar a este paciente?", QMessageBox.StandardButton.Yes |
                               QMessageBox.StandardButton.No)
        if resp == QMessageBox.StandardButton.Yes:
            return "y"
        else:
            return "n"

    #Eliminar paciente

    def eliminar_paciente(self, item):

        confirm = self.confirm_delete()

        if confirm == "y":

            row = item.row()

            data = []
            with open(f'pacientes.txt', 'rb') as file_new_d:
                while True:
                    try:
                        info = pickle.load(file_new_d)
                        data.append(info)
                    except EOFError:
                        break

            row_data = []
            all_data = []
            for position, datos in enumerate(data):
                str(datos.__dict__.get('id'))
                str(datos.__dict__.get('name'))
                str(datos.__dict__.get('doc'))
                str(datos.__dict__.get('t_pac'))
                str(datos.__dict__.get('sex'))
                str(datos.__dict__.get('country'))
                str(datos.__dict__.get('fnacimiento'))
                str(datos.__dict__.get('medidas'))
                str(datos.__dict__.get('act_deporte'))
                str(datos.__dict__.get('correo'))
                str(datos.__dict__.get('direccion'))

                row_data = [datos.__dict__.get('id'), datos.__dict__.get('name'), datos.__dict__.get('doc'),
                            datos.__dict__.get('t_pac'), datos.__dict__.get('sex'), datos.__dict__.get('country'),
                            datos.__dict__.get('fnacimiento'), datos.__dict__.get('medidas'),
                            datos.__dict__.get('act_deporte'), datos.__dict__.get('correo'),
                            datos.__dict__.get('direccion')]

                all_data.append(row_data)

            del all_data[row - 1]

            if len(all_data) == 0:
                with open(f'pacientes.txt', 'wb') as file:
                    print("Archivo vaciado completamente.")
            else:
                with open(f'pacientes.txt', 'wb') as file:
                    for data in all_data:
                        new_patient = Patient(data[0], data[1], data[2],
                                              data[3], data[4],
                                              data[5], data[6], data[7], data[8], data[9], data[10])
                        pickle.dump(new_patient, file)
                file.close()

            msg = QMessageBox()
            resp = QMessageBox.information(msg, "Eliminacion completada",
                                        "¡El paciente ha sido eliminado con exito!")
            self.update_table()
        else:
            print("No se ha confirmado el proceso de eliminación.")

    def confirm_delete(self):
        msg = QMessageBox()
        resp = QMessageBox.question(msg, "Confirmación",
                             "¿Está seguro que desea eliminar al paciente del sistema?", QMessageBox.StandardButton.Yes |
                               QMessageBox.StandardButton.No)
        if resp == QMessageBox.StandardButton.Yes:
            return "y"
        else:
            return "n"

    #Informe de la cita

    def data_pdf(self, row, c_row):

        if row == 0:

            row = 0

            fecha_nac = datetime.strptime(str(self.fnacimiento.text()), "%m/%d/%Y")
            now = datetime.now()
            date = now.strftime("%m/%d/%Y")
            fecha_me = datetime.strptime(str(date), "%m/%d/%Y")
            edad = relativedelta(fecha_me, fecha_nac).years

            all_data = [edad, self.apellido.text(), self.name.text(), self.sexo.currentText(),
                        self.tipo_doc.currentText(),
                        self.documento.text(), self.country.currentText(), self.act_deporte.text(),
                        self.tipo_pac.currentText(),
                        fecha_nac, fecha_me]

            if all_data[8] == "Adulto":

                medidas = []
                multi_medidas = []

                table1 = self.table_medidas
                table2 = self.table_pliegues_cut
                table3 = self.table_perife_circun
                cont1 = 1
                cont2 = 1
                cont3 = 1

                for i in range(3):
                    medidas.append(table1.item(cont1, 4).text())
                    if cont1 == 3:
                        for i in range(4):
                            medidas.append(table2.item(cont2, 4).text())
                            if cont2 == 3:
                                for i in range(6):
                                    medidas.append(table3.item(cont3, 4).text())
                                    cont3 += 1
                            cont2 += 1

                    cont1 += 1

                multi_medidas.append(medidas)
                self.create_pdf(all_data, multi_medidas)

            elif all_data[8] == "Atleta":

                medidas = []
                multi_medidas = []

                table1 = self.table_medidas_atleta
                table2 = self.table_pliegues_cut_atleta
                table3 = self.table_perife_circun_atleta
                table4 = self.table_longitud_alt_atleta
                table5 = self.table_diametros_atleta
                cont1 = 1
                cont2 = 1
                cont3 = 1
                cont4 = 1
                cont5 = 1

                for i in range(6):
                    medidas.append(table1.item(cont1, 4).text())
                    if cont1 == 6:
                        for i in range(8):
                            medidas.append(table2.item(cont2, 4).text())
                            if cont2 == 8:
                                for i in range(16):
                                    medidas.append(table3.item(cont3, 4).text())
                                    if cont3 == 16:
                                        for i in range(8):
                                            medidas.append(table4.item(cont4, 4).text())
                                            if cont4 == 8:
                                                for i in range(7):
                                                    medidas.append(table5.item(cont5, 4).text())
                                                    cont5 += 1
                                            cont4 += 1
                                    cont3 += 1
                            cont2 += 1
                    cont1 += 1

                multi_medidas.append(medidas)
                self.create_pdf_atleta(all_data, multi_medidas)

        elif row > 0:

            data = []
            with open(f'pacientes.txt', 'rb') as file_new_d:
                while True:
                    try:
                        info = pickle.load(file_new_d)
                        data.append(info)
                    except EOFError:
                        break

            multi_medidas = []
            all_data = []
            for position, datos in enumerate(data):
                str(datos.__dict__.get('name'))
                str(datos.__dict__.get('doc'))
                str(datos.__dict__.get('t_pac'))
                str(datos.__dict__.get('sex'))
                str(datos.__dict__.get('country'))
                str(datos.__dict__.get('fnacimiento'))
                str(datos.__dict__.get('fecha'))
                str(datos.__dict__.get('hora'))
                str(datos.__dict__.get('medidas'))
                str(datos.__dict__.get('act_deporte'))

                row_data = [datos.__dict__.get('name'), datos.__dict__.get('doc'),
                            datos.__dict__.get('t_pac'), datos.__dict__.get('sex'), datos.__dict__.get('country'),
                            datos.__dict__.get('fnacimiento'), datos.__dict__.get('fecha'), datos.__dict__.get('hora'),
                            datos.__dict__.get('medidas'), str(datos.__dict__.get('act_deporte'))]
                all_data.append(row_data)

            fecha_nac = datetime.strptime(str(all_data[row-1][5]), "%m/%d/%Y")
            now = datetime.now()
            date = now.strftime("%m/%d/%Y")
            fecha_me = datetime.strptime(str(date), "%m/%d/%Y")
            edad = relativedelta(fecha_me, fecha_nac).years

            nombre_sin_div = str(all_data[row - 1][0])
            nombre_apellido = nombre_sin_div.split()

            doc_sin_div = str(all_data[row - 1][1])
            tipo_y_doc = doc_sin_div.split("-")

            multi_medidas.append(all_data[row - 1][8][c_row - 1])

            all_data_f = [edad, nombre_apellido[1], nombre_apellido[0], all_data[row - 1][3], tipo_y_doc[0],
                          tipo_y_doc[1],
                          all_data[row - 1][3], all_data[row - 1][9], all_data[row - 1][2], all_data[row - 1][5],
                          all_data[row - 1][8][c_row - 1][13]]
            if all_data[row - 1][2] == "Adulto":
                self.create_pdf(all_data_f, multi_medidas)
            elif all_data[row - 1][2] == "Atleta":
                self.create_pdf_atleta(all_data_f, multi_medidas)

    def create_pdf(self, data, med):

        edad = data[0]
        apellidos = data[1]
        nombres = data[2]
        sexo = data[3]
        tipo_doc = data[4]
        id_doc = data[5]
        lugar_nac = data[6]
        deporte = data[7]
        tipo_pa = data[8]
        fecha_nac = data[9]
        fecha_me = data[10]

        estatura = float(med[0][0])
        peso = float(med[0][1])
        triceps = float(med[0][3])
        subescapular = float(med[0][4])
        biceps = float(med[0][5])
        cresta_iliaca = float(med[0][6])
        p_brazo_rela = float(med[0][7])
        p_muñeca = float(med[0][9])
        p_min_cintura = float(med[0][10])
        p_caderas = float(med[0][12])

        imc = round(peso / estatura ** 2, 2)
        icc = round(p_min_cintura / p_caderas, 2)
        ice = round(p_min_cintura / estatura, 2)
        porcent_grasa = triceps + subescapular + biceps + cresta_iliaca
        porcent_grasa_con_log = log10(porcent_grasa)
        dato1 = 1.1610 - (0.0632 * porcent_grasa_con_log)
        por_grasa = ((4.95 / dato1) - 4.50) * 100
        pe_grasa = round(peso * (por_grasa / 100), 2)
        result_por_grasa_p = self.porcent_grasa_percentil_m(por_grasa, edad)
        por_grasa_p = round(float(result_por_grasa_p), 2)
        mlg = round((peso * (((100 - por_grasa) / 100) + 6.1 * (1.8 * estatura))) / estatura ** 2, 2)
        dato_extra = 0.31416 * (triceps / 10)
        camb = round((((p_brazo_rela - dato_extra) ** 2) / (4 * 3.1416)) - 10.0, 2)
        result_iamb = self.iamb(por_grasa, edad)
        iamb = round(float(result_iamb), 2)
        complexion = round(estatura / p_muñeca, 2)
        peso_ideal = round(estatura - 100 - (((estatura - 150) / 4) + ((edad - 20) / 20)), 2)

        imc = str(imc)
        icc = str(icc)
        ice = str(ice)
        pe_grasa = str(pe_grasa)
        por_grasa_p = str(por_grasa_p)
        mlg = str(mlg)
        camb = str(camb)
        iamb = str(iamb)
        complexion = str(complexion)
        peso_ideal = str(peso_ideal)

        ##fuente: Helvetica

        pdf = FPDF('P', 'pt', (2067, 2756))
        pdf.add_page()
        pdf.set_font("Helvetica", "", 45)
        pdf.image("images/formato_adulto_1.jpg", 0, 0)
        top = pdf.y
        offset = pdf.x + 40
        pdf.multi_cell(0, 10, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{apellidos}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{nombres}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{sexo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{tipo_doc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{id_doc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{lugar_nac}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{deporte}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{tipo_pa}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{fecha_me}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{fecha_nac}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{estatura}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{peso}")

        pdf.y = top
        pdf.x = offset

        pdf.multi_cell(0, 10, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {imc}"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {icc}"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {ice}"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {por_grasa}"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {pe_grasa}"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {por_grasa_p}"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {mlg}"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {camb}"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {iamb}"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {complexion}"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                            "
                              f"                         {peso_ideal}")

        pdf.add_page()
        pdf.set_font("Helvetica", "", 45)
        pdf.image("images/formato_adulto_2.jpg", 0, 0)
        pdf.y = top
        pdf.x = offset

        def imc_medic(imc):
            fimc = float(imc)
            if fimc < 18.5:
                print("peso bajo")
                return "peso bajo"
            elif 18.5 < fimc < 24.9:
                print("Peso saludable")
                return "peso saludable"
            elif 18.5 < fimc < 24.9:
                print("Sobre peso")
                return "sobre peso"
            elif 18.5 < fimc < 24.9:
                print("Obesidad, grado 1")
                return "obesidad, grado 1"
            elif 18.5 < fimc < 24.9:
                print("Obesidad, grado 2")
                return "obesidad, grado 2"
            elif 18.5 < fimc < 24.9:
                print("Obesidad, grado 3, obesidad morbida")
                return "obesidad, grado 3, obesidad morbida"
            else:
                print("error final1bonus1")
                return "error imc"

        def icc_medic(icc, sexo):
            ficc = float(icc)
            if sexo == "Masculino":
                if ficc >= 1.0:
                    print("androide")
                    return "androide"
                elif ficc < 1.0:
                    print("ginecoide")
                    return "ginecoide"
                else:
                    print("error final2bonus1")
                    return "error icc"
            elif sexo == "Femenino":
                if ficc >= 0.8:
                    print("androide")
                    return "androide"
                elif ficc < 0.8:
                    print("ginecoide")
                    return "ginecoide"
                else:
                    print("error final2bonus1")
                    return "error icc"
            else:
                print("error sexo")
                return "error sexo"

        def icc_texto(icc):
            if icc == "androide":
                return f"usted tiene mayor riesgo para el desarrollo de \n\n\n       " \
                        f"enfermedades crónico-degenerativas debido a la \n\n\n       " \
                        f"acumulación de grasa visceral"
            elif icc == "ginecoide":
                return f"usted tiene mayor riesgo problemas de retorno venoso \n\n\n       "

        def mlg_medic(mlg, sexo):
            fmlg = float(mlg)
            if sexo == "Masculino":
                mlgh = [18, 20, 22, 25]
                dato2 = min(mlgh, key=lambda x: abs(x - fmlg))
                if dato2 == 18:
                    print("Complexión ligera con poca musculatura")
                    return "con complexion ligera con poca musculatura"
                if dato2 == 20:
                    print("Musculatura promedio")
                    return "con musculatura promedio"
                if dato2 == 22:
                    print("Marcadamente musculoso ")
                    return "marcadamente musculoso"
                if dato2 == 25:
                    print(
                        "No se logra normalmente sin levantar pesas / Límite superior de la musculatura obtenida sin uso de "
                        "agentes fármaco-lógicos, por lo que el MLG podría llegar a 40")
                    return f"en un rango que no se logra normalmente sin \n\n\n       " \
                            f"levantar pesas / límite superior de la \n\n\n       " \
                            f"musculatura obtenida sin uso de agentes \n\n\n       " \
                            f"fármaco-lógicos, por loque el MLG podría  \n\n\n       " \
                            f"llegar a 40"
                else:
                    print("error final2bonus1")
                    return "error mlg"
            elif sexo == "Femenino":
                mlgm = [13, 15, 17, 22]
                dato2 = min(mlgm, key=lambda x: abs(x - fmlg))
                if dato2 == 13:
                    print("Complexión ligera con poca musculatura")
                    return "con complexion ligera con poca musculatura"
                if dato2 == 15:
                    print("Musculatura promedio")
                    return "con musculatura promedio"
                if dato2 == 17:
                    print("Marcadamente musculoso ")
                    return "marcadamente musculosa"
                if dato2 == 22:
                    print(
                        "No se logra normalmente sin levantar pesas / Límite superior de la musculatura obtenida sin uso "
                        "de agentes fármaco-lógicos, por lo que el MLG podría llegar a 40")
                    return "con medidas que no se logran normalmente \n\n\n      " \
                            "sin levantar pesas / límite superior de \n\n\n      " \
                            "la musculatura obtenida sin uso de \n\n\n      " \
                            "agentes fármaco-lógicos, por lo que el \n\n\n      " \
                            "MLG podría llegar a 40"
                else:
                    print("error final2bonus1")

        def iamb_medic(iamb):
            fiamb = float(iamb)
            if fiamb < 5:
                print("Bajo nivel de musculatura o disminución")
                return "un bajo nivel de musculatura o disminucion"
            elif fiamb in range(5, 15):
                print("Masa muscular debajo del promedio")
                return "una masa muscular debajo del promedio"
            elif fiamb in range(16, 85):
                print("Masa muscular promedio")
                return "una masa muscular promedio"
            elif fiamb in range(86, 95):
                print("Masa muscular arriba del promedio o hipertrofia muscular")
                return "una masa muscular arriba del promedio o \n\n\n      " \
                        "hièrtrofia muscular"
            elif fiamb > 95:
                print("Masa muscular alta - hipertrofia muscular")
                return "una masa muscular alta - hipertrofia \n\n\n      " \
                        "muscular"
            else:
                print("error iamb")
                return "error iamb"

        def complexion_medic(complexion, sexo):
            fcomplexion = float(complexion)
            if sexo == "Masculino":
                if fcomplexion > 10.4:
                    print("complexion pequeña")
                    return "complexion pequeña"
                elif 9.6 < fcomplexion < 10.3:
                    print("complexion mediana")
                    return "complexion mediana"
                elif fcomplexion < 9.5:
                    print("complexion grande")
                    return "complexion grande"
            elif sexo == "Femenino":
                if fcomplexion > 10.9:
                    print("complexion pequeña")
                    return "complexion pequeña"
                elif 9.9 < fcomplexion < 10.8:
                    print("complexion mediana")
                    return "complexion mediana"
                elif fcomplexion < 9.8:
                    print("complexion grande")
                    return "complexion grande"

        def peso_ideal_medic(peso, peso_ideal):
            fpeso = float(peso)
            fpeso_ideal = float(peso_ideal)
            print(fpeso_ideal)
            ## abajo esta % de peso ideal, falta este dato de salida
            dato3 = int((fpeso * 100) / fpeso_ideal)
            print(dato3)
            if dato3 < 60:
                print("Malnutrición severa")
                return "malnutricion severa"
            elif 60 <= dato3 <= 89:
                print("Malnutrición moderada")
                return "malnutricion moderada"
            elif 90 <= dato3 <= 109:
                print("Normalidad")
                return "nutricion promedio"
            elif 110 <= dato3 <= 120:
                print("Sobrepeso")
                return "sobrepeso"
            elif dato3 > 120:
                print("Obesidad")
            else:
                print("error")

        imc_info = imc_medic(imc)
        icc_info = icc_medic(icc, sexo)
        icc_text = icc_texto(icc_info)
        mlg_info = mlg_medic(mlg, sexo)
        iamb_info = iamb_medic(iamb)
        complexion_info = complexion_medic(complexion, sexo)
        peso_ideal_info = peso_ideal_medic(peso, peso_ideal)

        pdf.multi_cell(0, 20, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                     "
                              f"Con un Indicé de Masa Corporal de "
                              f"{imc} usted califica que posee\n\n\n                     {imc_info}."
                              f"\n\n\n\n\n\n                     "
                              f"Con un Indicé Cintura Cadera de {icc} usted califica como "
                              f"{icc_info} y \n\n\n                     {icc_text}.\n\n\n\n                     "
                              f"Con un Indicé de Masa Libre de Grasa de {mlg} usted esta \n\n\n                     "
                              f"{mlg_info}.\n\n\n\n\n\n\n                     "
                              f"Con un Indicé del Área Muscular del brazo de {iamb} "
                              f"en Percentiles se \n\n\n                     puede afirmar que usted posee "
                              f"{iamb_info}.\n\n\n\n\n\n\n                     "
                              f"Con un Indicé de Complexión de {complexion} usted posee una "
                              f"{complexion_info}.\n\n\n\n\n\n\n                     "
                              f"Con un Porcentaje de Peso Ideal del {peso_ideal}% usted posee \n\n\n                     "
                              f"{peso_ideal_info}.")

        msg = QMessageBox()
        QMessageBox.information(msg, "Informe",
                                "El informe fue realizado con exito.")
        ruta_paciente = f'informes/informe-{nombres}-{fecha_me}.pdf'
        pdf.output(ruta_paciente, "F")

    def create_pdf_atleta(self, data, medidas):

        apellidos = data[1]
        nombres = data[2]
        sexo = data[3]
        tipo_doc = data[4]
        id_doc = data[5]
        lugar_nac = data[6]
        deporte = data[7]
        tipo_pa = data[8]
        fecha_me = data[10]
        fecha_nac = data[9]

        estatura = float(medidas[0][0])
        peso = float(medidas[0][1])
        triceps = float(medidas[0][6])
        subescapular = float(medidas[0][7])
        cresta_ili = float(medidas[0][9])
        supraespinal = float(medidas[0][10])
        abdominal = float(medidas[0][11])
        muslo_frontal = float(medidas[0][12])
        pantorrilla = float(medidas[0][13])
        per_cefalico = float(medidas[0][14])
        per_brazo_rela = float(medidas[0][16])
        per_muneca = float(medidas[0][20])
        estatura_sentado = float(medidas[0][2])
        longitud_acromio_dedal = float(medidas[0][5])
        envergadura = float(medidas[0][3])
        per_torax = float(medidas[0][21])
        per_muslo_medio = float(medidas[0][27])
        per_maximo_antebr_der = float(medidas[0][18])
        per_pantorrilla = float(medidas[0][28])
        diam_biacromial = float(medidas[0][38])
        diam_biiliocristal = float(medidas[0][39])
        per_min_cintura = float(medidas[0][22])
        anchura_torax_transverso = float(medidas[0][41])
        prof_torax_ante_poste = float(medidas[0][42])
        diam_biepicondilar_humero = float(medidas[0][43])
        diam_biepicondilar_femur = float(medidas[0][44])

        imc = self.logica_imc_atl(estatura, peso)
        por_grasa = self.logica_porcentaje_grasa_atl(sexo, triceps, subescapular, cresta_ili,
                                                         abdominal, muslo_frontal,
                                                         pantorrilla)
        mlg = self.logica_mlg_atl(peso, por_grasa, estatura)
        result_camb_iamb = self.logica_camb__iamb_atl(sexo, per_brazo_rela, triceps)
        camb = result_camb_iamb[0]
        iamb = result_camb_iamb[1]
        complexion = self.complexion_atl(estatura, per_muneca)
        somatotipo = self.somatotipo_atl(estatura, triceps, subescapular, supraespinal, diam_biepicondilar_humero,
                                            diam_biepicondilar_femur, per_brazo_rela, per_pantorrilla, pantorrilla, peso)
        endomorfo = somatotipo[0]
        mesomorfo = somatotipo[1]
        ectomorfo = somatotipo[2]

        valorx = ectomorfo - endomorfo
        if valorx > 11:
            valorx = 11
        if valorx < -12:
            valorx = -12
        valory = 2 * mesomorfo - (endomorfo + ectomorfo)
        if valory > 12:
            valory = 12
        if valory < -12:
            valory = -12

        pdf = FPDF('P', 'pt', (2067, 2756))
        pdf.add_page()
        pdf.set_font("Helvetica", "", 45)
        pdf.image("images/formato_atleta_1.jpg", 0, 0)
        top = pdf.y
        offset = pdf.x + 40
        pdf.multi_cell(0, 10, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{apellidos}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{nombres}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{sexo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{tipo_doc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{id_doc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{lugar_nac}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{deporte}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{tipo_pa}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{fecha_me}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{fecha_nac}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{estatura}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             "
                              f"{peso}")

        pdf.y = top
        pdf.x = offset

        pdf.multi_cell(0, 9, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                                                     "
                              f"{imc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n"
                              f"                                                                                     "
                              f"{por_grasa}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n\n\n"
                              f"                                                                                     "
                              f"{mlg}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                                                     "
                              f"{camb}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n"
                              f"                                                                                     "
                              f"{iamb}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n"
                              f"                                                                                     "
                              f"{complexion}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n\n\n\n\n\n                   "
                              f"                                                                                     "
                              f"{endomorfo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                   "
                              f"                                                                                     "
                              f"{mesomorfo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                   "
                              f"                                                                                     "
                              f"{ectomorfo}")

        fracc_corporal = self.fraccionamiento_corporal_atl(sexo, peso, estatura, per_cefalico,
                                                           diam_biacromial, diam_biiliocristal,
                                                           diam_biepicondilar_humero,
                                                           diam_biepicondilar_femur, triceps, subescapular,
                                                           supraespinal,
                                                           abdominal, muslo_frontal, pantorrilla, per_brazo_rela,
                                                           per_maximo_antebr_der,
                                                           per_muslo_medio, per_pantorrilla, per_torax,
                                                           prof_torax_ante_poste,
                                                           anchura_torax_transverso, per_min_cintura, estatura_sentado)
        masa_piel = fracc_corporal[0]
        masa_osea = fracc_corporal[1]
        tegido_adiposo = fracc_corporal[2]
        masa_muscular = fracc_corporal[3]
        masa_residual = fracc_corporal[4]
        masa_total = fracc_corporal[5]

        indice_cormico = self.indice_cormico_atl(estatura, estatura_sentado)
        longitud_relativa = self.longitud_relativa_extremidad_superior_atl(longitud_acromio_dedal,
                                                                                            estatura)
        ##longitud relativa de la extremidad superior
        indice_esqueletico = self.indice_esqueletico_atl(estatura, estatura_sentado)
        envergadura_relativa = self.envergadura_relativa_atl(envergadura, estatura)

        pdf.add_page()
        pdf.set_font("Helvetica", "", 45)
        pdf.image("images/formato_atleta_2.jpg", 0, 0)
        pdf.y = top
        pdf.x = offset

        pdf.multi_cell(0, 9, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                  "
                              f"{masa_piel}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                             "
                              f"{masa_osea}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                  "
                              f"{tegido_adiposo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                  "
                              f"{masa_muscular}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                "
                              f"{masa_residual}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                            "
                              f"{masa_total}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                              "
                              f"{indice_cormico}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                              "
                              f"{longitud_relativa}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                              "
                              f"{indice_esqueletico}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                              "
                              f"{envergadura_relativa}")

        pdf.add_page()
        pdf.set_font("Helvetica", "", 45)
        pdf.image("images/formato_atleta_3.jpg", 0, 0)
        pdf.y = top
        pdf.x = offset

        def imc_medic(imc):
            fimc = float(imc)
            if fimc < 18.5:
                print("peso bajo")
                return "peso bajo"
            elif 18.5 < fimc < 24.9:
                print("Peso saludable")
                return "peso saludable"
            elif 18.5 < fimc < 24.9:
                print("Sobre peso")
                return "sobre peso"
            elif 18.5 < fimc < 24.9:
                print("Obesidad, grado 1")
                return "obesidad, grado 1"
            elif 18.5 < fimc < 24.9:
                print("Obesidad, grado 2")
                return "obesidad, grado 2"
            elif 18.5 < fimc < 24.9:
                print("Obesidad, grado 3, obesidad morbida")
                return "obesidad, grado 3, obesidad morbida"
            else:
                print("error final1bonus1")
                return "error imc"

        def mlg_medic(mlg, sexo):
            fmlg = float(mlg)
            if sexo == "Masculino":
                mlgh = [18, 20, 22, 25]
                dato2 = min(mlgh, key=lambda x: abs(x - fmlg))
                if dato2 == 18:
                    print("Complexión ligera con poca musculatura")
                    return "con complexion ligera con poca musculatura"
                if dato2 == 20:
                    print("Musculatura promedio")
                    return "con musculatura promedio"
                if dato2 == 22:
                    print("Marcadamente musculoso ")
                    return "marcadamente musculoso"
                if dato2 == 25:
                    print("No se logra normalmente sin levantar pesas / Límite superior de la musculatura obtenida sin "
                          "uso de agentes fármaco-lógicos, por lo que el MLG podría llegar a 40")
                    return f"en un rango que no se logra normalmente sin \n\n\n       " \
                           f"levantar pesas / límite superior de la \n\n\n       " \
                           f"musculatura obtenida sin uso de agentes \n\n\n       " \
                           f"fármaco-lógicos, por loque el MLG podría  \n\n\n       " \
                           f"llegar a 40"
                else:
                    print("error final2bonus1")
                    return "error mlg"
            elif sexo == "Femenino":
                mlgm = [13, 15, 17, 22]
                dato2 = min(mlgm, key=lambda x: abs(x - fmlg))
                if dato2 == 13:
                    print("Complexión ligera con poca musculatura")
                    return "con complexion ligera con poca musculatura"
                if dato2 == 15:
                    print("Musculatura promedio")
                    return "con musculatura promedio"
                if dato2 == 17:
                    print("Marcadamente musculoso ")
                    return "marcadamente musculosa"
                if dato2 == 22:
                    print(
                        "No se logra normalmente sin levantar pesas / Límite superior de la musculatura obtenida sin uso "
                        "de agentes fármaco-lógicos, por lo que el MLG podría llegar a 40")
                    return "con medidas que no se logran normalmente \n\n\n      " \
                           "sin levantar pesas / límite superior de \n\n\n      " \
                           "la musculatura obtenida sin uso de \n\n\n      " \
                           "agentes fármaco-lógicos, por lo que el \n\n\n      " \
                           "MLG podría llegar a 40"
                else:
                    print("error final2bonus1")

        def iamb_medic(iamb):
            fiamb = float(iamb)
            if fiamb < 5:
                print("Bajo nivel de musculatura o disminución")
                return "un bajo nivel de musculatura o disminucion"
            elif fiamb in range(5, 15):
                print("Masa muscular debajo del promedio")
                return "una masa muscular debajo del promedio"
            elif fiamb in range(16, 85):
                print("Masa muscular promedio")
                return "una masa muscular promedio"
            elif fiamb in range(86, 95):
                print("Masa muscular arriba del promedio o hipertrofia muscular")
                return "una masa muscular arriba del promedio o \n\n\n      " \
                       "hièrtrofia muscular"
            elif fiamb > 95:
                print("Masa muscular alta - hipertrofia muscular")
                return "una masa muscular alta - hipertrofia \n\n\n      " \
                       "muscular"
            else:
                print("error iamb")
                return "error iamb"

        def complexion_medic(complexion, sexo):
            fcomplexion = float(complexion)
            if sexo == "Masculino":
                if fcomplexion > 10.4:
                    print("complexion pequeña")
                    return "complexion pequeña"
                elif 9.6 < fcomplexion < 10.3:
                    print("complexion mediana")
                    return "complexion mediana"
                elif fcomplexion < 9.5:
                    print("complexion grande")
                    return "complexion grande"
            elif sexo == "Femenino":
                if fcomplexion > 10.9:
                    print("complexion pequeña")
                    return "complexion pequeña"
                elif 9.9 < fcomplexion < 10.8:
                    print("complexion mediana")
                    return "complexion mediana"
                elif fcomplexion < 9.8:
                    print("complexion grande")
                    return "complexion grande"

        def indice_cormico_medic(sexo, indice_c):
            if sexo == "Masculino":
                if indice_c <= 51:
                    return "Braquicórmico (Tronco corto)"
                elif 51.1 < indice_c < 53:
                    return "Metricórmico (Tronco medio)"
                elif indice_c >= 53.1:
                    return "Macrocórmico (Tronco largo)"
            elif sexo == "Femenino":
                if indice_c <= 52:
                    return "Braquicórmico (Tronco corto)"
                elif 52.1 < indice_c < 54:
                    return "Metricórmico (Tronco medio)"
                elif indice_c >= 54.1:
                    return "Macrocórmico (Tronco largo)"

        def longitud_relativa_medic(longitud_relativa):
            if longitud_relativa <= 44.9:
                return "Braquibraquial \n\n\n\n\n\n\n\n                   (extremidad superior corta)"
            elif 45 < indice_cormico < 46.9:
                return "Mesobraquial \n\n\n\n\n\n\n\n                   (extremidad superior intermedia)"
            elif indice_cormico >= 47:
                return "Macrobraquial \n\n\n\n\n\n\n\n                   (extremidad superior larga)"

        def indice_esqueletico_medic(indice_esqueletico):
            if indice_esqueletico <= 84.9:
                return "Braquiesquélico \n\n\n\n\n\n\n\n                   (extremidad inferior corta)"
            elif 85 < indice_esqueletico < 89.9:
                return "Mesoesquélico \n\n\n\n\n\n\n\n                   (extremidad inferior mediana)"
            elif indice_esqueletico >= 90:
                return "Macroesquélico \n\n\n\n\n\n\n\n                   (extremidad inferior larga)"

        imc_info = imc_medic(imc)
        mlg_info = mlg_medic(mlg, sexo)
        iamb_info = iamb_medic(iamb)
        complexion_info = complexion_medic(complexion, sexo)
        cormico_info = indice_cormico_medic(sexo, indice_cormico)
        long_info = longitud_relativa_medic(longitud_relativa)
        icor_info = indice_esqueletico_medic(indice_esqueletico)

        pdf.multi_cell(0, 10, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                   "
                              f"Con un Indicé de masa corporal de "
                              f"{imc} usted califica que posee \n\n\n\n\n\n\n\n                   {imc_info}."
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n                   "
                              f"Con un Indicé de masa libre de grasa de {mlg} usted esta \n\n\n\n\n\n\n\n                   "
                              f"{mlg_info}.\n\n\n\n\n\n\n\n\n\n\n\n\n                   "
                              f"Con un Indicé del área muscular del brazo de {iamb} "
                              f"en percentiles se puede \n\n\n\n\n\n\n\n                   afirmar que usted posee "
                              f"{iamb_info}.\n\n\n\n\n\n\n\n\n\n\n\n\n                   "
                              f"Con un Indicé de complexión de {complexion} usted posee una"
                              f"\n\n\n\n\n\n\n                   "
                              f"{complexion_info}.\n\n\n\n\n\n\n\n\n\n\n\n\n                   "
                              f"Con un Indicé cormico de {indice_cormico} usted califica como"
                              f"\n\n\n\n\n\n\n                   "
                              f"{cormico_info}.\n\n\n\n\n\n\n\n\n\n\n\n\n                   "
                              f"Con una longitud relativa de {longitud_relativa} usted califica "
                              f"\n\n\n\n\n\n\n                   como "
                              f"{long_info}.\n\n\n\n\n\n\n\n\n\n\n\n\n                   "
                              f"Con un Indicé esquelético de {indice_esqueletico} usted califica"
                              f"\n\n\n\n\n\n\n                   como "
                              f"{icor_info}.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                                                          "
                              f"Valor en X: {valorx}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"                                                                                          "
                              f"Valor en Y: {valory}")

        ix = 300
        iy = 2130
        pdf.image("images/big_good.png", ix, iy)
        img_endo_x = 100
        img_endo_y = 2500
        img_meso_x = 520
        img_meso_y = 1920
        img_ecto_x = 900
        img_ecto_y = 2500
        pdf.image("images/endomorfo.png", img_endo_x, img_endo_y)
        pdf.image("images/mesomorfo.png", img_meso_x, img_meso_y)
        pdf.image("images/ectomorfo.png", img_ecto_x, img_ecto_y)

        ##el 3 y el -2 son valores que coloque de ejemplo y deben remplazarse por los valores que da logica de atleta para
        ##saber el posicionamiento en la grafica del somatotipo

        x = valorx * 25
        y = (valory * 30) * -1
        imgx = x + (ix + 290 - 12.5)
        imgy = y + (iy + 320 - 12.5)

        pdf.image("images/dot.png", imgx, imgy)

        ruta_paciente = f'informes/informe-{nombres}-{fecha_me}.pdf'
        pdf.output(ruta_paciente, "F")

        msg = QMessageBox()
        QMessageBox.information(msg, "Informe",
                                "El informe fue realizado con exito.")

    def porcent_grasa_percentil_h(self, porcentaje_g, edad_u):
        edad_min = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        edad_max = [24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74]
        tabla = [8, 9, 10, 12, 16, 20, 23, 25, 28], [9, 10, 11, 13, 18, 23, 25, 26, 29], [16, 17, 18, 20, 23, 26, 27,
                                                                                          28, 30], [15, 17, 18, 20, 23,
                                                                                                    25, 27, 27, 29], [
            14, 16, 18, 21,
            26,
            30,
            32,
            34,
            36], [15, 17, 19, 21, 26, 30, 32, 34, 36], [15, 17, 19, 22, 27, 31, 30, 35, 37], [15, 18, 20, 22, 27, 31,
                                                                                              30, 35, 37], [16, 18,
                                                                                                            20, 22,
                                                                                                            27, 31,
                                                                                                            33, 35,
                                                                                                            37], [13,
                                                                                                                  16,
                                                                                                                  18,
                                                                                                                  21,
                                                                                                                  26,
                                                                                                                  30,
                                                                                                                  33,
                                                                                                                  35,
                                                                                                                  37], [
            13, 16, 18, 21, 26, 30, 33, 34, 36]
        percentil = [5, 10, 15, 25, 50, 75, 85, 90, 95]

        for edad in zip(edad_min, edad_max):

            if edad_u >= edad[0] and edad_u <= edad[1]:

                posicion_edad = edad_min.index(edad[0])
                percentage = tabla[posicion_edad]

                for valor in percentage:
                    closest_body_fat = min(percentage, key=lambda x: abs(x - porcentaje_g))
                    if closest_body_fat == valor:
                        ubicacion = percentage.index(valor)
                        return str(percentil[ubicacion])

    def porcent_grasa_percentil_m(self, porcentaje_g, edad_u):
        edad_min = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        edad_max = [24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74]
        tabla = [17, 19, 21, 23, 27, 33, 35, 37, 40], [18, 20, 21, 24, 29, 34, 37, 39, 41], [21, 23, 25, 27, 31, 36, 38, 40, 42], [22, 24, 25, 28, 32, 37, 39, 40, 42], [25, 28, 29, 31, 35, 39, 41, 42, 43], [26, 28, 29, 32, 36, 39, 41, 42, 44], [27, 30, 32, 35, 39, 43, 46, 47, 48], [27, 30, 32, 35, 39, 44, 45, 47, 49], [28, 31, 32, 35, 40, 43, 45, 46, 48], [27, 30, 32, 34, 38, 42, 44, 46, 47], [26, 29, 31, 34, 38, 42, 44, 45, 47]
        percentil = [5, 10, 15, 25, 50, 75, 85, 90, 95]

        for edad in zip(edad_min, edad_max):

            if edad_u >= edad[0] and edad_u <= edad[1]:

                posicion_edad = edad_min.index(edad[0])
                percentage = tabla[posicion_edad]

                for valor in percentage:
                    closest_body_fat = min(percentage, key=lambda x: abs(x - porcentaje_g))
                    if closest_body_fat == valor:
                        ubicacion = percentage.index(valor)
                        return str(percentil[ubicacion])

    def iamb(self, porcentaje_g, edad_u):
        edad_min = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        edad_max = [24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74]
        tabla = [34.2, 37.3, 39.6, 42.7, 49.4, 57.1, 61.8, 65.0, 72.0], [36.6, 39.9, 42.4, 46.0, 53.0, 61.4, 66.1,
                                                                         68.9, 74.5], [37.9, 40.9, 43.4, 47.3, 54.4,
                                                                                       63.2, 67.6, 70.8, 76.1], [
            38.5, 42.6, 44.6, 47.9, 55.3, 64.0, 69.1, 72.7, 77.6], [38.4, 42.1, 45.1, 48.7, 56.0, 64.0, 68.5,
                                                                    71.6, 77.0], [37.7, 41.3, 43.7, 47.9, 55.2,
                                                                                  63.3, 68.4, 72.2, 76.2], [
            36.0, 40.0, 42.7, 46.6, 54.0, 62.7, 67.0, 70.4, 77.4], [36.5, 40.8, 42.7, 46.7, 54.3, 61.9, 66.4,
                                                                    69.6, 75.1], [34.5, 38.7, 41.2, 44.9, 52.1,
                                                                                  60.0, 64.8, 67.5, 71.6], [
            31.4, 35.8, 38.4, 42.3, 49.1, 57.3, 61.2, 64.3, 69.4], [29.7, 33.8, 36.1, 40.2, 47.0, 54.6, 59.1,
                                                                    62.1, 67.3]
        percentil = [5, 10, 15, 25, 50, 75, 85, 90, 95]

        for edad in zip(edad_min, edad_max):

            if edad_u >= edad[0] and edad_u <= edad[1]:

                posicion_edad = edad_min.index(edad[0])
                percentage = tabla[posicion_edad]

                for valor in percentage:
                    closest_body_fat = min(percentage, key=lambda x: abs(x - porcentaje_g))
                    if closest_body_fat == valor:
                        ubicacion = percentage.index(valor)
                        return str(percentil[ubicacion])

    def iamb_m(self, porcentaje_g, edad_u):
        edad_min = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        edad_max = [24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74]
        tabla = [19.5, 21.5, 22.8, 23.5, 28.3, 33.1, 36.4, 39.0, 44.2], [20.5, 21.9, 23.1, 25.2, 29.4, 34.9, 38.5, 41.9, 47.8], [21.1, 23.0, 24.2, 26.3, 30.9, 36.8, 41.2, 44.7, 51.3], [21.1, 23.4, 24.7, 27.3, 31.8, 38.7, 43.1, 46.1, 54.2], [21.3, 23.4, 25.5, 27.5, 32.3, 39.8, 45.8, 49.5, 55.8], [21.6, 23.1, 24.8, 27.4, 32.5, 39.5, 44.7, 48.4, 56.1], [22.2, 24.6, 25.7, 28.3, 33.4, 40.4, 46.1, 49.6, 55.6], [22.8, 24.7, 26.5, 28.7, 33.7, 42.3, 47.3, 52.1, 58.8], [22.4, 24.5, 26.3, 29.2, 34.5, 41.1, 45.6, 49.1, 55.1], [21.9, 24.5, 26.2, 28.9, 34.6, 41.6, 46.3, 49.6, 56.5], [22.2, 24.4, 26.0, 28.8, 34.3, 41.8, 46.4, 49.2, 54.6]
        percentil = [5, 10, 15, 25, 50, 75, 85, 90, 95]

        for edad in zip(edad_min, edad_max):

            if edad_u >= edad[0] and edad_u <= edad[1]:

                posicion_edad = edad_min.index(edad[0])
                percentage = tabla[posicion_edad]

                for valor in percentage:
                    closest_body_fat = min(percentage, key=lambda x: abs(x - porcentaje_g))
                    if closest_body_fat == valor:
                        ubicacion = percentage.index(valor)
                        return str(percentil[ubicacion])

    def problem_patient(self):
        msg = QMessageBox()
        QMessageBox.critical(msg, "Error al registrar al paciente",
                             "Este paciente ya se encuentra en el sistema.")
        self.content.setCurrentWidget(self.Paciente)
        self.content_patient.setCurrentWidget(self.Pacientes)

    def confirm_patient(self):
        msg = QMessageBox()
        QMessageBox.information(msg, "Registro completado",
                                "¡El paciente " + self.name.text() + " " + self.apellido.text() + " fue registrado con exito!")
        self.update_table()

    #Citas

    def ver_cita(self, item):
        self.row_update_cita = item.row()
        self.items_c(item.row())
        self.content_table_c(item.row())
        self.content_patient.setCurrentWidget(self.data_patient)
        self.ingresar_patient.setCurrentWidget(self.citas)
        self.table_citas.selectRow(0)

    def volver_cita(self, i):
        self.row_update_cita = i
        self.items_c(self.row_update_cita)
        self.content_table_c(self.row_update_cita)
        self.content_patient.setCurrentWidget(self.data_patient)
        self.ingresar_patient.setCurrentWidget(self.citas)
        self.table_citas.selectRow(0)

    def new_cita(self):
        self.btn_sigR1.setEnabled(False)
        self.btn_agregar_cita.setEnabled(True)

        data = []
        with open(f'pacientes.txt', 'rb') as file_new_d:
            while True:
                try:
                    info = pickle.load(file_new_d)
                    data.append(info)
                except EOFError:
                    break

        multi_medidas = []
        all_data = []
        for position, datos in enumerate(data):
            str(datos.__dict__.get('t_pac'))

            row_data = [datos.__dict__.get('t_pac')]
            all_data.append(row_data)

        if all_data[self.row_update_cita - 1][0] == "Adulto":
            self.table_medidas.itemChanged.connect(self.row_table)
            self.table_pliegues_cut.itemChanged.connect(self.row_table)
            self.table_perife_circun.itemChanged.connect(self.row_table)
            self.ingresar_patient.setCurrentWidget(self.Mediciones_adulto)
        elif all_data[self.row_update_cita - 1][0] == "Atleta":
            self.table_medidas_atleta.itemChanged.connect(self.row_table_atleta)
            self.table_pliegues_cut_atleta.itemChanged.connect(self.row_table_atleta)
            self.table_perife_circun_atleta.itemChanged.connect(self.row_table_atleta)
            self.table_longitud_alt_atleta.itemChanged.connect(self.row_table_atleta)
            self.table_diametros_atleta.itemChanged.connect(self.row_table_atleta)
            self.ingresar_patient.setCurrentWidget(self.Mediciones_atleta)

    def ver_informe_cita(self):
        if self.table_citas.currentRow() > 0:
            cita_row = self.table_citas.currentRow()
            self.data_pdf(self.row_update_cita, cita_row)
        else:
            msg = QMessageBox()
            QMessageBox.critical(msg, "Selección de la cita",
                                 "No se ha seleccionado ninguna cita del paciente.")

    def items_c(self, i):
        data = []
        with open(f'pacientes.txt', 'rb') as file_new_d:
            while True:
                try:
                    info = pickle.load(file_new_d)
                    data.append(info)
                except EOFError:
                    break

        row_data = []
        all_data = []
        med = []
        for datos in data:
            str(datos.__dict__.get('medidas'))
            row_data = [datos.__dict__.get('medidas')]
            all_data.append(row_data)

        med = all_data[i - 1][0]

        contador = 1

        for x in med:
            contador += 1

        self.table_citas.setRowCount(contador)

        for row in range(contador):
            it = row + 1
            for i in range(4):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                font = QtGui.QFont()
                font.setFamily("Circular Std")
                font.setPointSize(11)
                item.setFont(font)
                item.setFlags(
                    QtCore.Qt.ItemFlag.ItemIsDragEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsDropEnabled | QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                self.table_citas.setItem(it, i, item)

    def content_table_c(self, i):

        data = []
        with open(f'pacientes.txt', 'rb') as file_new_d:
            while True:
                try:
                    info = pickle.load(file_new_d)
                    data.append(info)
                except EOFError:
                    break

        row_data = []
        all_data = []
        med = []
        contador = 0
        for position, datos in enumerate(data):
            str(datos.__dict__.get('medidas'))
            str(datos.__dict__.get('name'))
            str(datos.__dict__.get('fnacimiento'))
            str(datos.__dict__.get('t_pac'))
            str(datos.__dict__.get('sex'))
            str(datos.__dict__.get('country'))

            row_data = [datos.__dict__.get('medidas'), str(datos.__dict__.get('name')),
                        str(datos.__dict__.get('fnacimiento')), str(datos.__dict__.get('t_pac')),
                        str(datos.__dict__.get('sex')), str(datos.__dict__.get('country'))]
            all_data.append(row_data)
            contador += 1

        med = all_data[i - 1][0]

        fecha_nac = datetime.strptime(all_data[i-1][2], "%d/%m/%Y")
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        fecha_me = datetime.strptime(str(date), "%d/%m/%Y")
        edad = relativedelta(fecha_me, fecha_nac).years

        self.name_cita.setText(all_data[i - 1][1])
        self.edad_cita.setText(str(edad))
        self.tpaciente_cita.setText(all_data[i - 1][3])
        self.sexo_cita.setText(all_data[i - 1][4])
        self.pais_cita.setText(all_data[i - 1][5])

        for x, medida in enumerate(med):
            if all_data[i - 1][3] == "Adulto":
                self.lbl_fecha_hora.setText(
                    "La última vez que se agregó una cita fue el " + all_data[i - 1][0][x][13] + " a las " +
                    all_data[i - 1][0][x][14])

                item = self.table_citas.item(x + 1, 0)
                item.setText(str(x + 1))
                item = self.table_citas.item(x + 1, 1)
                item.setText(str("Informe #") + str(x + 1))
                item = self.table_citas.item(x + 1, 2)
                item.setText(str(all_data[i - 1][0][x][13]))
                item = self.table_citas.item(x + 1, 3)
                item.setText(str(all_data[i - 1][0][x][14]))
            elif all_data[i - 1][3] == "Atleta":
                self.lbl_fecha_hora.setText(
                    "La última vez que se agregó una cita fue el " + all_data[i - 1][0][x][13] + " a las " +
                    all_data[i - 1][0][x][14])

                item = self.table_citas.item(x + 1, 0)
                item.setText(str(x + 1))
                item = self.table_citas.item(x + 1, 1)
                item.setText(str("Informe #") + str(x + 1))
                item = self.table_citas.item(x + 1, 2)
                item.setText(str(all_data[i - 1][0][x][45]))
                item = self.table_citas.item(x + 1, 3)
                item.setText(str(all_data[i - 1][0][x][46]))

    def guardar_cita(self, id, name, doc, t_pac, sex, country, fnacimiento, medidas, act_deporte, correo, direccion,
                     overwrite):
        if overwrite == 0:
            new_patient = Patient(id, name, doc,
                                  t_pac, sex,
                                  country, fnacimiento, medidas, act_deporte, correo, direccion)
            with open(f'pacientes.txt', 'wb') as file:
                pickle.dump(new_patient, file)
            file.close()
        else:
            new_patient = Patient(id, name, doc,
                                  t_pac, sex,
                                  country, fnacimiento, medidas, act_deporte, correo, direccion)
            with open(f'pacientes.txt', 'ab') as file:
                pickle.dump(new_patient, file)
            file.close()

    #Estadisticas
    def estadisticas(self):
        self.deselected_op(self.btn_paciente)
        self.deselected_op(self.btn_db)
        self.selected_op(self.btn_estadistica_patient)
        self.deselected_op(self.btn_report)
        self.content.setCurrentWidget(self.Estadisticas)

    #Reportes

    def reportes(self):
        self.deselected_op(self.btn_paciente)
        self.deselected_op(self.btn_db)
        self.deselected_op(self.btn_estadistica_patient)
        self.selected_op(self.btn_report)
        self.content.setCurrentWidget(self.Import)

    # Stretch para la tabla

    def strech_table(self):

        # Horizontal

        horizontal_table_p = self.table_patient.horizontalHeader()
        for i in range(5):
            horizontal_table_p.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        horizontal_medidas_simples = self.table_medidas.horizontalHeader()
        for i in range(4):
            horizontal_medidas_simples.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        horizontal_tabla_pliegues = self.table_pliegues_cut.horizontalHeader()
        for i in range(4):
            horizontal_tabla_pliegues.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        horizontal_tabla_citas = self.table_citas.horizontalHeader()
        for i in range(4):
            horizontal_tabla_citas.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        # Vertical

        verticalHeader = self.table_medidas.verticalHeader()
        for i in range(4):
            verticalHeader.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        verticalHeader = self.table_pliegues_cut.verticalHeader()
        for i in range(5):
            verticalHeader.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeMode.Stretch)

    # Animaciones para el side menu y sus opciones

    def side_menu(self):
        width = self.menu.width()

        Ui_MainWindow.animation(self, width, "left")

    def side_menu_op(self):
        width = self.menu.width()

        Ui_MainWindow.animation_op(self, width, "left")

    def animation(self, left_box_width, direction):
        right_width = 0
        left_width = 0

        if left_box_width == 50 and direction == "left":
            left_width = 240
            tg_menu = QtGui.QIcon()
            tg_menu.addPixmap(QtGui.QPixmap("icons/left.png"), QtGui.QIcon.Mode.Normal,
                              QtGui.QIcon.State.Off)
            self.selected_op(self.btn_menu)
            self.btn_menu.setIcon(tg_menu)
        else:
            tg_menu = QtGui.QIcon()
            tg_menu.addPixmap(QtGui.QPixmap("icons/menu-lockw.png"), QtGui.QIcon.Mode.Normal,
                              QtGui.QIcon.State.Off)
            self.deselected_op(self.btn_menu)
            self.btn_menu.setIcon(tg_menu)
            left_width = 50

        self.left_box = QPropertyAnimation(self.menu, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.Type.InOutQuart)

        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.start()

    def animation_op(self, left_box_width, direction):
        right_width = 0
        left_width = 0

        if left_box_width == 240 and direction == "left":
            tg_menu = QtGui.QIcon()
            tg_menu.addPixmap(QtGui.QPixmap("icons/menu-lockw.png"), QtGui.QIcon.Mode.Normal,
                              QtGui.QIcon.State.Off)
            self.deselected_op(self.btn_menu)
            self.btn_menu.setIcon(tg_menu)
            left_width = 50

            self.left_box = QPropertyAnimation(self.menu, b"minimumWidth")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(left_box_width)
            self.left_box.setEndValue(left_width)
            self.left_box.setEasingCurve(QEasingCurve.Type.InOutQuart)

            self.op = QParallelAnimationGroup()
            self.op.addAnimation(self.left_box)
            self.op.start()

    def selected_op(self, btn):
        btn.setStyleSheet("QPushButton {\n"
                          "background-color: rgb(0, 0, 30);\n"
                          "color: white;\n"
                          "border-left: 3px solid;\n"
                          "border-color: rgb(255, 255, 255);\n"
                          "}")

    def deselected_op(self, btn):
        btn.setStyleSheet("QPushButton {\n"
                          "border: 0px solid;\n"
                          "color: white;\n"
                          "text-align: left;\n"
                          "padding-left: 9px;\n"
                          "}\n"
                          "\n"
                          "QPushButton:hover {\n"
                          "background-color: rgb(0, 0, 30);\n"
                          "color: white;\n"
                          "border-left: 3px solid;\n"
                          "border-color: rgb(255, 255, 255);\n"
                          "}")

    def estadisticas_sistem(self):
        self.comboBox__paciente1.clear()
        self.comboBox__paciente1.addItem("---")
        # funcion para llenar la lista de cita 1 y 2 y la lista de datos a comparar
        def cambio_paciente(max):
            if self.comboBox__paciente1.currentText() != "---":
                contenido_raw = self.comboBox__paciente1.currentText()
                # print("contenido raw: ", contenido_raw)
                contenido_split = contenido_raw.split()
                # print("contenido_split[2]: ", str(contenido_split[2]))
                contenido = contenido_split[2]  # cedula
                tipo = contenido_split[3]  # tipo paciente
                datos_adulto = ("0 ESTATURA", "1 PESO", "2 PROFUNDIDAD ABDOMINAL", "3 PLIEGUES TRICEPS",
                                "4 PLIEGUES SUBESCAPULAR", "5 PLIEGUES BICEPS", "6 PLIEGUES CRESTA ILIACA",
                                "7 PERIMETRO BRAZO RELAJADO", "8 PERIMETRO BRAZO FLEXIONADO CONTRAIDO",
                                "9 PERIMETRO MUÑECA",
                                "10 PERIMETRO MINIMO CINTURA", "11 PERIMETRO ABDOMINAL", "12 PERIMETRO CADERAS")

                datos_atleta = ("0 ESTATURA", "1 PESO", "2 PROFUNDIDAD ABDOMINAL",
                                "3 PLIEGUES TRICEPS", "4 PLIEGUES CRESTA ILIACA", "5 PERIMETRO CINTURA MINIMA",
                                "6 PLIEGUES ABDOMINAL", "7 PERIMETRO BRAZO FLEXIONADO CONTRAIDO",
                                "8 PERIMETRO ABDOMINAL", "9 PERIMETRO MUSLO MEDIO")

                if tipo == "Adulto":
                    contador_tipoa = 0
                    self.combobox_dato.clear()
                    while contador_tipoa < 13:
                        self.combobox_dato.addItem(datos_adulto[contador_tipoa])
                        contador_tipoa += 1
                    # print("done")

                if tipo == "Atleta":
                    contador_tipot = 0
                    self.combobox_dato.clear()
                    while contador_tipot < 10:
                        self.combobox_dato.addItem(datos_atleta[contador_tipot])
                        contador_tipot += 1
                    # print("done")

                contador_p = 0
                contador_c = 0
                self.combobox_cita1.clear()
                self.combobox_cita2.clear()
                while contador_p < max:
                    if contenido == all_data[contador_p][3]:
                        # print("good paciente")
                        while contador_c < len(all_data[contador_p][1]):
                            if tipo == "Adulto":
                                combo_cita1 = str(contador_c) + " " + str(
                                    all_data[contador_p][1][contador_c][13]) + " " + str(
                                    all_data[contador_p][1][contador_c][14])
                                self.combobox_cita1.addItem(combo_cita1)
                                combo_cita2 = str(contador_c) + " " + str(
                                    all_data[contador_p][1][contador_c][13]) + " " + str(
                                    all_data[contador_p][1][contador_c][14])
                                self.combobox_cita2.addItem(combo_cita2)
                                contador_c += 1
                            else:
                                combo_cita1 = str(contador_c) + " " + str(
                                    all_data[contador_p][1][contador_c][45]) + " " + str(
                                    all_data[contador_p][1][contador_c][46])
                                self.combobox_cita1.addItem(combo_cita1)
                                combo_cita2 = str(contador_c) + " " + str(
                                    all_data[contador_p][1][contador_c][45]) + " " + str(
                                    all_data[contador_p][1][contador_c][46])
                                self.combobox_cita2.addItem(combo_cita2)
                                contador_c += 1
                        else:
                            contador_p += 1
                    else:
                        contador_p += 1
                        # print("no es el paciente")

        def comparar():
            self.label_dato1.setText("")
            self.label_dato2.setText("")
            fix_atl = [0, 1, 2, 6, 9, 11, 15, 17, 18, 27]
            paciente = self.comboBox__paciente1.currentIndex() - 1
            cita1 = self.combobox_cita1.currentIndex()
            cita2 = self.combobox_cita2.currentIndex()
            dato = self.combobox_dato.currentIndex()
            tipo = str(all_data[paciente][2])
            if tipo == "Atleta":
                dato = fix_atl[dato]
                # print("es atleta")
            dato1 = all_data[paciente][1][cita1][dato]
            # print(all_data[paciente][1][cita1][dato])
            dato2 = all_data[paciente][1][cita2][dato]
            # print(all_data[paciente][1][cita2][dato])
            self.label_dato1.setText(str(dato1))
            self.label_dato2.setText(str(dato2))

            mixdato1 = float(dato1)
            mixdato2 = float(dato2)

            final1 = int(mixdato1)
            final2 = int(mixdato2)
            y1 = [final1, 0]
            y2 = [0, final2]
            xlab = ['CITA 1', 'CITA 2']
            xval = list(range(1, len(xlab) + 1))
            ticks = []
            for i, item in enumerate(xlab):
                ticks.append((xval[i], item))
            ticks = [ticks]

            self.gridLayout_30.removeWidget(self.plot)
            self.plot = pg.plot()
            self.plot.setBackground("w")
            self.gridLayout_30.addWidget(self.plot, 0, 2, 1, 1)

            bargraph = pg.BarGraphItem(x=xval, height=y1, width=0.5, brush='#1f78b4')
            self.plot.addItem(bargraph)
            bargraph2 = pg.BarGraphItem(x=xval, height=y2, width=0.5, brush="#fe7f0e")
            self.plot.addItem(bargraph2)
            self.plot.setBackground("w")
            ax = self.plot.getAxis('bottom')
            ax.setTicks(ticks)

        data = []
        # el contador contiene = pacientes adultos, pacientes atletas, pacientes totales, hombres, mujeres
        contadores = [0, 0, 0, 0, 0, 0]
        edad_total = 0
        edad_prom = 0
        # esto lee los pacientes del txt y los saca
        with open(f'pacientes.txt', 'rb') as file_new_d:
            while True:
                try:
                    info = pickle.load(file_new_d)
                    data.append(info)
                except EOFError:
                    break
        row_data = []
        all_data = []
        contador = 0
        for position, datos in enumerate(data):
            str(datos.__dict__.get('name'))
            str(datos.__dict__.get('medidas'))
            str(datos.__dict__.get('t_pac'))
            str(datos.__dict__.get('fecha'))
            str(datos.__dict__.get('doc'))
            str(datos.__dict__.get('fnacimiento'))

            row_data = [datos.__dict__.get('name'), datos.__dict__.get('medidas'), datos.__dict__.get('t_pac'),
                        datos.__dict__.get('doc'), datos.__dict__.get('fecha'), datos.__dict__.get('hora'),
                        datos.__dict__.get('fnacimiento')]
            all_data.append(row_data)
            contador += 1

        # primero paciente (de momento hay 2, primo jose y segundo joestar)
        # segundo es dato del row_data (0 nombre completo, 1 todas las medidas de entrada, 2 tipo de paciente,
        # 3 documento, 4 fecha de cita (no sirve), 5 hora(no sirve), 6 nacimiento)
        # tercero depende del anterior:
        # si es 0 es una letra del nombre completo,
        # si es 1 son todos los datos de una cita,
        # si es 2 son las letras de tipo de paciente
        # el cuarto dato es solo para medidas de citas, te da una medida e particular de la cita seleccionada
        # anteriormente
        # nota: no tienes que usar los 4, solo usa los nesezarios
        # por ejemplo arriba llamame a primo josue, dame todas sus medidas, solo las de la cita 1, solo su peso
        # print(all_data[1][1])

        # esto llama a los pacientes y los cuenta el total ademas de contar por tipos de paciente y los asigna en sus
        # label (done)

        for position, datos in enumerate(data):
            if str(datos.__dict__.get('t_pac')) == "Adulto":
                contadores[0] += 1
                contadores[2] += 1
            elif str(datos.__dict__.get('t_pac')) == "Atleta":
                contadores[1] += 1
                contadores[2] += 1
            else:
                print("error")
        self.lbl_patient_adulto_count.setText(str(contadores[0]))
        self.lbl_patient_atleta_count.setText(str(contadores[1]))
        self.lbl_patient_total.setText(str(contadores[2]))

        # calcula la cantidad total de citas y la escribe en su label (done)

        for position, datos in enumerate(data):
            if str(datos.__dict__.get('t_pac')) == "Adulto":
                contadores[5] += len(datos.get_medidas())
            elif str(datos.__dict__.get('t_pac')) == "Atleta":
                contadores[5] += len(datos.get_medidas())
            else:
                print("error")
        self.lbl_cita_total.setText(str(contadores[5]))

        # esto calcula cuantos pacientes hombres y mujeres hay en el sistema y los coloca en sus labels (done)
        for position, datos in enumerate(data):
            if str(datos.__dict__.get('sex')) == "Masculino":
                contadores[3] += 1
            elif str(datos.__dict__.get('sex')) == "Femenino":
                contadores[4] += 1
            else:
                print(str(datos.__dict__.get('sex')))
        self.lbl_cant_hombres.setText(str(contadores[3]))
        self.lbl_cant_mujeres.setText(str(contadores[4]))

        # esto llena la combobox de paciente con los pacientes (done)

        for position, datos in enumerate(data):
            paciente_combo = str(datos.__dict__.get('name')) + " " + str(datos.__dict__.get('doc')) + " " + str(
                datos.__dict__.get('t_pac'))
            self.comboBox__paciente1.addItem(paciente_combo)

        # al seleccionar un paciente empieza a cargar las citas de este y que datos puede comparar (done)
        max = contadores[2]
        self.comboBox__paciente1.currentTextChanged.connect(lambda: cambio_paciente(max))

        # esto calcula la edad promedio de los pacientes (no esta listo) y lo asigna en su label (done)

        contador_edadp = 0
        while contador_edadp < max:
            nacimiento = datetime.strptime(all_data[contador_edadp][6], "%d/%m/%Y")
            now = datetime.now()
            date = now.strftime("%d/%m/%Y")
            fecha_me = datetime.strptime(str(date), "%d/%m/%Y")
            edad = (relativedelta(fecha_me, nacimiento).years)
            contador_edadp += 1
            edad_total += int(edad)
        else:
            edad_prom = int(edad_total / max)
            self.lbl_edad_promedio.setText(str(edad_prom))

        # boton que se usa para comparar los datos introducidos (done)

        self.btn_comparar.clicked.connect(lambda: comparar())

class Patient:
    def __init__(self, id, name, doc, t_pac, sex, country, fnacimiento, medidas, act_deporte, correo, direccion):
        self.id = id
        self.name = name
        self.doc = doc
        self.t_pac = t_pac
        self.sex = sex
        self.country = country
        self.fnacimiento = fnacimiento
        self.medidas = medidas
        self.act_deporte = act_deporte
        self.correo = correo
        self.direccion = direccion

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

    def get_medidas(self):
        return self.medidas

    def get_actdeporte(self):
        return self.act_deporte

    def get_correo(self):
        return self.correo

    def get_direccion(self):
        return self.direccion

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
        return datetime.now().strftime("%d/%m/%Y")

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



class NumericDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)
        if isinstance(editor, QtWidgets.QLineEdit):
            validator = QRegularExpressionValidator(QRegularExpression('^[1-9](?:\d+|\d*\.\d+)?$'))
            editor.setValidator(validator)
        return editor

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
