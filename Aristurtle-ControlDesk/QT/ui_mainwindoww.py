# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1348, 673)
        self.actionEdit_Defaults = QAction(MainWindow)
        self.actionEdit_Defaults.setObjectName(u"actionEdit_Defaults")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.centralwidjet_layout = QGridLayout()
        self.centralwidjet_layout.setObjectName(u"centralwidjet_layout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setMovable(False)
        self.ecu_menu_tab = QWidget()
        self.ecu_menu_tab.setObjectName(u"ecu_menu_tab")
        self.gridLayout_5 = QGridLayout(self.ecu_menu_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mqtt_connection_groupbox = QGroupBox(self.ecu_menu_tab)
        self.mqtt_connection_groupbox.setObjectName(u"mqtt_connection_groupbox")
        self.mqtt_connection_groupbox.setMaximumSize(QSize(650, 16777215))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setBold(True)
        font.setKerning(True)
        self.mqtt_connection_groupbox.setFont(font)
        self.gridLayout_3 = QGridLayout(self.mqtt_connection_groupbox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ip_label = QLabel(self.mqtt_connection_groupbox)
        self.ip_label.setObjectName(u"ip_label")

        self.gridLayout_3.addWidget(self.ip_label, 0, 0, 1, 1)

        self.connect_pushButton = QPushButton(self.mqtt_connection_groupbox)
        self.connect_pushButton.setObjectName(u"connect_pushButton")

        self.gridLayout_3.addWidget(self.connect_pushButton, 3, 0, 1, 4)

        self.client_name_label = QLabel(self.mqtt_connection_groupbox)
        self.client_name_label.setObjectName(u"client_name_label")

        self.gridLayout_3.addWidget(self.client_name_label, 2, 0, 1, 1)

        self.connection_status_label = QLabel(self.mqtt_connection_groupbox)
        self.connection_status_label.setObjectName(u"connection_status_label")
        self.connection_status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.connection_status_label, 4, 1, 1, 2)

        self.connection_label = QLabel(self.mqtt_connection_groupbox)
        self.connection_label.setObjectName(u"connection_label")

        self.gridLayout_3.addWidget(self.connection_label, 4, 0, 1, 1)

        self.ip_lineEdit = QLineEdit(self.mqtt_connection_groupbox)
        self.ip_lineEdit.setObjectName(u"ip_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ip_lineEdit.sizePolicy().hasHeightForWidth())
        self.ip_lineEdit.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.ip_lineEdit, 0, 1, 1, 1)

        self.ping_pushButton = QPushButton(self.mqtt_connection_groupbox)
        self.ping_pushButton.setObjectName(u"ping_pushButton")

        self.gridLayout_3.addWidget(self.ping_pushButton, 0, 2, 1, 1)

        self.ping_output_label = QLabel(self.mqtt_connection_groupbox)
        self.ping_output_label.setObjectName(u"ping_output_label")
        self.ping_output_label.setMinimumSize(QSize(80, 0))
        self.ping_output_label.setMaximumSize(QSize(80, 16777215))
        self.ping_output_label.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ping_output_label.setTextFormat(Qt.AutoText)
        self.ping_output_label.setScaledContents(False)
        self.ping_output_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.ping_output_label, 0, 3, 1, 1)

        self.client_name_lineEdit = QLineEdit(self.mqtt_connection_groupbox)
        self.client_name_lineEdit.setObjectName(u"client_name_lineEdit")

        self.gridLayout_3.addWidget(self.client_name_lineEdit, 2, 1, 1, 3)

        self.connection_status_led = QLabel(self.mqtt_connection_groupbox)
        self.connection_status_led.setObjectName(u"connection_status_led")
        self.connection_status_led.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setWeight(QFont.Black)
        font1.setKerning(True)
        self.connection_status_led.setFont(font1)
        self.connection_status_led.setPixmap(QPixmap(u"images/red-led.png"))
        self.connection_status_led.setScaledContents(True)

        self.gridLayout_3.addWidget(self.connection_status_led, 4, 3, 1, 1)


        self.gridLayout_5.addWidget(self.mqtt_connection_groupbox, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.ecu_menu_tab)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setBold(True)
        self.groupBox.setFont(font2)

        self.gridLayout_5.addWidget(self.groupBox, 0, 1, 1, 1)

        self.temperature_cooling_groupBox = QGroupBox(self.ecu_menu_tab)
        self.temperature_cooling_groupBox.setObjectName(u"temperature_cooling_groupBox")
        self.temperature_cooling_groupBox.setFont(font2)
        self.gridLayout_11 = QGridLayout(self.temperature_cooling_groupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.temperature_value_label = QLabel(self.temperature_cooling_groupBox)
        self.temperature_value_label.setObjectName(u"temperature_value_label")
        self.temperature_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.temperature_value_label, 0, 1, 1, 1)

        self.cooling_power_spinBox = QSpinBox(self.temperature_cooling_groupBox)
        self.cooling_power_spinBox.setObjectName(u"cooling_power_spinBox")
        self.cooling_power_spinBox.setEnabled(False)
        self.cooling_power_spinBox.setMaximum(100)
        self.cooling_power_spinBox.setValue(100)

        self.gridLayout_11.addWidget(self.cooling_power_spinBox, 1, 1, 1, 1)

        self.cooling_power_label = QLabel(self.temperature_cooling_groupBox)
        self.cooling_power_label.setObjectName(u"cooling_power_label")

        self.gridLayout_11.addWidget(self.cooling_power_label, 1, 0, 1, 1)

        self.temperature_label = QLabel(self.temperature_cooling_groupBox)
        self.temperature_label.setObjectName(u"temperature_label")

        self.gridLayout_11.addWidget(self.temperature_label, 0, 0, 1, 1)

        self.autocooling_checkBox = QCheckBox(self.temperature_cooling_groupBox)
        self.autocooling_checkBox.setObjectName(u"autocooling_checkBox")
        self.autocooling_checkBox.setChecked(True)

        self.gridLayout_11.addWidget(self.autocooling_checkBox, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.temperature_cooling_groupBox, 3, 4, 1, 1)

        self.datafile_management_groupBox = QGroupBox(self.ecu_menu_tab)
        self.datafile_management_groupBox.setObjectName(u"datafile_management_groupBox")
        self.datafile_management_groupBox.setFont(font2)
        self.gridLayout_9 = QGridLayout(self.datafile_management_groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.target_folder_label = QLabel(self.datafile_management_groupBox)
        self.target_folder_label.setObjectName(u"target_folder_label")

        self.gridLayout_9.addWidget(self.target_folder_label, 0, 0, 1, 1)

        self.refresh_datafiles_pushButton = QPushButton(self.datafile_management_groupBox)
        self.refresh_datafiles_pushButton.setObjectName(u"refresh_datafiles_pushButton")

        self.gridLayout_9.addWidget(self.refresh_datafiles_pushButton, 3, 0, 1, 1)

        self.download_datafiles_pushButton = QPushButton(self.datafile_management_groupBox)
        self.download_datafiles_pushButton.setObjectName(u"download_datafiles_pushButton")

        self.gridLayout_9.addWidget(self.download_datafiles_pushButton, 3, 2, 1, 3)

        self.delete_datafiles_pushButton = QPushButton(self.datafile_management_groupBox)
        self.delete_datafiles_pushButton.setObjectName(u"delete_datafiles_pushButton")

        self.gridLayout_9.addWidget(self.delete_datafiles_pushButton, 3, 1, 1, 1)

        self.datafiles_tableWidget = QTableWidget(self.datafile_management_groupBox)
        if (self.datafiles_tableWidget.columnCount() < 3):
            self.datafiles_tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.datafiles_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.datafiles_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.datafiles_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.datafiles_tableWidget.setObjectName(u"datafiles_tableWidget")
        self.datafiles_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.datafiles_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.datafiles_tableWidget.setDragDropOverwriteMode(False)
        self.datafiles_tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.datafiles_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.datafiles_tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.datafiles_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.datafiles_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.datafiles_tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_9.addWidget(self.datafiles_tableWidget, 2, 0, 1, 5)

        self.convert_merge_groupBox = QGroupBox(self.datafile_management_groupBox)
        self.convert_merge_groupBox.setObjectName(u"convert_merge_groupBox")
        self.gridLayout_10 = QGridLayout(self.convert_merge_groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.autoMerge_checkBox = QCheckBox(self.convert_merge_groupBox)
        self.autoMerge_checkBox.setObjectName(u"autoMerge_checkBox")
        self.autoMerge_checkBox.setMaximumSize(QSize(20, 16777215))
        self.autoMerge_checkBox.setLayoutDirection(Qt.LeftToRight)
        self.autoMerge_checkBox.setAutoFillBackground(False)
        self.autoMerge_checkBox.setChecked(True)
        self.autoMerge_checkBox.setTristate(False)

        self.gridLayout_10.addWidget(self.autoMerge_checkBox, 1, 1, 1, 1)

        self.convert_merge__status_label = QLabel(self.convert_merge_groupBox)
        self.convert_merge__status_label.setObjectName(u"convert_merge__status_label")
        self.convert_merge__status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.convert_merge__status_label, 3, 0, 1, 2)

        self.convert_pushButton = QPushButton(self.convert_merge_groupBox)
        self.convert_pushButton.setObjectName(u"convert_pushButton")

        self.gridLayout_10.addWidget(self.convert_pushButton, 0, 0, 1, 2)

        self.autoMerge_label = QLabel(self.convert_merge_groupBox)
        self.autoMerge_label.setObjectName(u"autoMerge_label")

        self.gridLayout_10.addWidget(self.autoMerge_label, 1, 0, 1, 1)

        self.merge_pushButton = QPushButton(self.convert_merge_groupBox)
        self.merge_pushButton.setObjectName(u"merge_pushButton")

        self.gridLayout_10.addWidget(self.merge_pushButton, 2, 0, 1, 2)


        self.gridLayout_9.addWidget(self.convert_merge_groupBox, 5, 0, 1, 5)

        self.datafile_download_status_label = QLabel(self.datafile_management_groupBox)
        self.datafile_download_status_label.setObjectName(u"datafile_download_status_label")
        self.datafile_download_status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.datafile_download_status_label, 4, 0, 1, 5)

        self.target_folder_lineEdit = QLineEdit(self.datafile_management_groupBox)
        self.target_folder_lineEdit.setObjectName(u"target_folder_lineEdit")

        self.gridLayout_9.addWidget(self.target_folder_lineEdit, 0, 1, 1, 4)


        self.gridLayout_5.addWidget(self.datafile_management_groupBox, 0, 4, 3, 1)

        self.control_mcu_groupbox = QGroupBox(self.ecu_menu_tab)
        self.control_mcu_groupbox.setObjectName(u"control_mcu_groupbox")
        self.control_mcu_groupbox.setMinimumSize(QSize(450, 0))
        self.control_mcu_groupbox.setMaximumSize(QSize(650, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.control_mcu_groupbox.setFont(font3)
        self.gridLayout_7 = QGridLayout(self.control_mcu_groupbox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.control_reset_mcu_button = QPushButton(self.control_mcu_groupbox)
        self.control_reset_mcu_button.setObjectName(u"control_reset_mcu_button")

        self.gridLayout_7.addWidget(self.control_reset_mcu_button, 1, 4, 1, 1)

        self.control_firmware_managemen_groupBox = QGroupBox(self.control_mcu_groupbox)
        self.control_firmware_managemen_groupBox.setObjectName(u"control_firmware_managemen_groupBox")
        self.gridLayout_8 = QGridLayout(self.control_firmware_managemen_groupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.control_choose_local_file_button = QPushButton(self.control_firmware_managemen_groupBox)
        self.control_choose_local_file_button.setObjectName(u"control_choose_local_file_button")

        self.gridLayout_8.addWidget(self.control_choose_local_file_button, 0, 0, 1, 1)

        self.control_refresh_files_button = QPushButton(self.control_firmware_managemen_groupBox)
        self.control_refresh_files_button.setObjectName(u"control_refresh_files_button")

        self.gridLayout_8.addWidget(self.control_refresh_files_button, 3, 0, 1, 1)

        self.control_destination_path_lineEdit = QLineEdit(self.control_firmware_managemen_groupBox)
        self.control_destination_path_lineEdit.setObjectName(u"control_destination_path_lineEdit")

        self.gridLayout_8.addWidget(self.control_destination_path_lineEdit, 1, 1, 1, 2)

        self.control_delete_file_button = QPushButton(self.control_firmware_managemen_groupBox)
        self.control_delete_file_button.setObjectName(u"control_delete_file_button")

        self.gridLayout_8.addWidget(self.control_delete_file_button, 3, 1, 1, 1)

        self.control_firmware_status_label = QLabel(self.control_firmware_managemen_groupBox)
        self.control_firmware_status_label.setObjectName(u"control_firmware_status_label")
        self.control_firmware_status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.control_firmware_status_label, 4, 0, 1, 3)

        self.control_transfer_file_button = QPushButton(self.control_firmware_managemen_groupBox)
        self.control_transfer_file_button.setObjectName(u"control_transfer_file_button")
        self.control_transfer_file_button.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_8.addWidget(self.control_transfer_file_button, 1, 3, 1, 1)

        self.control_binfiles_tableWidget = QTableWidget(self.control_firmware_managemen_groupBox)
        if (self.control_binfiles_tableWidget.columnCount() < 3):
            self.control_binfiles_tableWidget.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.control_binfiles_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.control_binfiles_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.control_binfiles_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.control_binfiles_tableWidget.setObjectName(u"control_binfiles_tableWidget")
        self.control_binfiles_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.control_binfiles_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.control_binfiles_tableWidget.setDragDropOverwriteMode(False)
        self.control_binfiles_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.control_binfiles_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.control_binfiles_tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.control_binfiles_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.control_binfiles_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.control_binfiles_tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_8.addWidget(self.control_binfiles_tableWidget, 2, 0, 1, 4)

        self.control_local_path_lineEdit = QLineEdit(self.control_firmware_managemen_groupBox)
        self.control_local_path_lineEdit.setObjectName(u"control_local_path_lineEdit")

        self.gridLayout_8.addWidget(self.control_local_path_lineEdit, 0, 1, 1, 3)

        self.control_load_code_button = QPushButton(self.control_firmware_managemen_groupBox)
        self.control_load_code_button.setObjectName(u"control_load_code_button")

        self.gridLayout_8.addWidget(self.control_load_code_button, 3, 2, 1, 2)

        self.control_destination_path_label = QLabel(self.control_firmware_managemen_groupBox)
        self.control_destination_path_label.setObjectName(u"control_destination_path_label")

        self.gridLayout_8.addWidget(self.control_destination_path_label, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.control_firmware_managemen_groupBox, 2, 2, 1, 4)

        self.control_mcu_id_lineEdit = QLineEdit(self.control_mcu_groupbox)
        self.control_mcu_id_lineEdit.setObjectName(u"control_mcu_id_lineEdit")

        self.gridLayout_7.addWidget(self.control_mcu_id_lineEdit, 0, 4, 1, 2)

        self.control_mcu_id_label = QLabel(self.control_mcu_groupbox)
        self.control_mcu_id_label.setObjectName(u"control_mcu_id_label")

        self.gridLayout_7.addWidget(self.control_mcu_id_label, 0, 2, 1, 1)

        self.control_reset_mcu_id_button = QPushButton(self.control_mcu_groupbox)
        self.control_reset_mcu_id_button.setObjectName(u"control_reset_mcu_id_button")
        self.control_reset_mcu_id_button.setMaximumSize(QSize(45, 16777215))
        self.control_reset_mcu_id_button.setFont(font3)

        self.gridLayout_7.addWidget(self.control_reset_mcu_id_button, 0, 3, 1, 1)

        self.control_mcu_status_led = QLabel(self.control_mcu_groupbox)
        self.control_mcu_status_led.setObjectName(u"control_mcu_status_led")
        self.control_mcu_status_led.setMaximumSize(QSize(40, 40))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(9)
        font4.setWeight(QFont.Black)
        font4.setKerning(True)
        self.control_mcu_status_led.setFont(font4)
        self.control_mcu_status_led.setPixmap(QPixmap(u"images/red-led.png"))
        self.control_mcu_status_led.setScaledContents(True)

        self.gridLayout_7.addWidget(self.control_mcu_status_led, 1, 3, 1, 1)

        self.control_mcu_status_label = QLabel(self.control_mcu_groupbox)
        self.control_mcu_status_label.setObjectName(u"control_mcu_status_label")

        self.gridLayout_7.addWidget(self.control_mcu_status_label, 1, 2, 1, 1)

        self.control_stop_mcu_button = QPushButton(self.control_mcu_groupbox)
        self.control_stop_mcu_button.setObjectName(u"control_stop_mcu_button")

        self.gridLayout_7.addWidget(self.control_stop_mcu_button, 1, 5, 1, 1)


        self.gridLayout_5.addWidget(self.control_mcu_groupbox, 1, 0, 3, 1)

        self.safety_mcu_groupbox = QGroupBox(self.ecu_menu_tab)
        self.safety_mcu_groupbox.setObjectName(u"safety_mcu_groupbox")
        self.safety_mcu_groupbox.setMinimumSize(QSize(450, 0))
        self.safety_mcu_groupbox.setMaximumSize(QSize(650, 16777215))
        self.safety_mcu_groupbox.setFont(font3)
        self.gridLayout = QGridLayout(self.safety_mcu_groupbox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.safety_mcu_status_led = QLabel(self.safety_mcu_groupbox)
        self.safety_mcu_status_led.setObjectName(u"safety_mcu_status_led")
        self.safety_mcu_status_led.setMaximumSize(QSize(40, 40))
        self.safety_mcu_status_led.setFont(font4)
        self.safety_mcu_status_led.setPixmap(QPixmap(u"images/red-led.png"))
        self.safety_mcu_status_led.setScaledContents(True)

        self.gridLayout.addWidget(self.safety_mcu_status_led, 1, 3, 1, 1)

        self.safety_reset_mcu_button = QPushButton(self.safety_mcu_groupbox)
        self.safety_reset_mcu_button.setObjectName(u"safety_reset_mcu_button")

        self.gridLayout.addWidget(self.safety_reset_mcu_button, 1, 4, 1, 1)

        self.safety_mcu_status_label = QLabel(self.safety_mcu_groupbox)
        self.safety_mcu_status_label.setObjectName(u"safety_mcu_status_label")

        self.gridLayout.addWidget(self.safety_mcu_status_label, 1, 2, 1, 1)

        self.stop_mcu_button = QPushButton(self.safety_mcu_groupbox)
        self.stop_mcu_button.setObjectName(u"stop_mcu_button")

        self.gridLayout.addWidget(self.stop_mcu_button, 1, 5, 1, 1)

        self.safety_mcu_id_label = QLabel(self.safety_mcu_groupbox)
        self.safety_mcu_id_label.setObjectName(u"safety_mcu_id_label")
        self.safety_mcu_id_label.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.safety_mcu_id_label, 0, 2, 1, 1)

        self.safety_firmware_managemen_groupBox = QGroupBox(self.safety_mcu_groupbox)
        self.safety_firmware_managemen_groupBox.setObjectName(u"safety_firmware_managemen_groupBox")
        self.gridLayout_2 = QGridLayout(self.safety_firmware_managemen_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.safety_refresh_files_button = QPushButton(self.safety_firmware_managemen_groupBox)
        self.safety_refresh_files_button.setObjectName(u"safety_refresh_files_button")

        self.gridLayout_2.addWidget(self.safety_refresh_files_button, 3, 0, 1, 1)

        self.safety_delete_file_button = QPushButton(self.safety_firmware_managemen_groupBox)
        self.safety_delete_file_button.setObjectName(u"safety_delete_file_button")

        self.gridLayout_2.addWidget(self.safety_delete_file_button, 3, 1, 1, 1)

        self.safety_destination_path_lineEdit = QLineEdit(self.safety_firmware_managemen_groupBox)
        self.safety_destination_path_lineEdit.setObjectName(u"safety_destination_path_lineEdit")

        self.gridLayout_2.addWidget(self.safety_destination_path_lineEdit, 1, 1, 1, 2)

        self.safety_firmware_status_label = QLabel(self.safety_firmware_managemen_groupBox)
        self.safety_firmware_status_label.setObjectName(u"safety_firmware_status_label")
        self.safety_firmware_status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.safety_firmware_status_label, 4, 0, 1, 3)

        self.safety_safety_choose_local_file_button = QPushButton(self.safety_firmware_managemen_groupBox)
        self.safety_safety_choose_local_file_button.setObjectName(u"safety_safety_choose_local_file_button")

        self.gridLayout_2.addWidget(self.safety_safety_choose_local_file_button, 0, 0, 1, 1)

        self.safety_transfer_file_button = QPushButton(self.safety_firmware_managemen_groupBox)
        self.safety_transfer_file_button.setObjectName(u"safety_transfer_file_button")
        self.safety_transfer_file_button.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.safety_transfer_file_button, 1, 3, 1, 1)

        self.safety_binfiles_tableWidget = QTableWidget(self.safety_firmware_managemen_groupBox)
        if (self.safety_binfiles_tableWidget.columnCount() < 3):
            self.safety_binfiles_tableWidget.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.safety_binfiles_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.safety_binfiles_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.safety_binfiles_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.safety_binfiles_tableWidget.setObjectName(u"safety_binfiles_tableWidget")
        self.safety_binfiles_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.safety_binfiles_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.safety_binfiles_tableWidget.setDragDropOverwriteMode(False)
        self.safety_binfiles_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.safety_binfiles_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.safety_binfiles_tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.safety_binfiles_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.safety_binfiles_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.safety_binfiles_tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.safety_binfiles_tableWidget, 2, 0, 1, 4)

        self.safety_load_code_button = QPushButton(self.safety_firmware_managemen_groupBox)
        self.safety_load_code_button.setObjectName(u"safety_load_code_button")

        self.gridLayout_2.addWidget(self.safety_load_code_button, 3, 2, 1, 2)

        self.safety_local_path_lineEdit = QLineEdit(self.safety_firmware_managemen_groupBox)
        self.safety_local_path_lineEdit.setObjectName(u"safety_local_path_lineEdit")

        self.gridLayout_2.addWidget(self.safety_local_path_lineEdit, 0, 1, 1, 3)

        self.safety_destination_path_label = QLabel(self.safety_firmware_managemen_groupBox)
        self.safety_destination_path_label.setObjectName(u"safety_destination_path_label")
        self.safety_destination_path_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.safety_destination_path_label, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.safety_firmware_managemen_groupBox, 2, 2, 1, 4)

        self.safety_mcu_id_lineEdit = QLineEdit(self.safety_mcu_groupbox)
        self.safety_mcu_id_lineEdit.setObjectName(u"safety_mcu_id_lineEdit")

        self.gridLayout.addWidget(self.safety_mcu_id_lineEdit, 0, 4, 1, 2)

        self.safety_reset_mcu_id_button = QPushButton(self.safety_mcu_groupbox)
        self.safety_reset_mcu_id_button.setObjectName(u"safety_reset_mcu_id_button")
        self.safety_reset_mcu_id_button.setMaximumSize(QSize(45, 16777215))
        self.safety_reset_mcu_id_button.setFont(font3)

        self.gridLayout.addWidget(self.safety_reset_mcu_id_button, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.safety_mcu_groupbox, 1, 1, 3, 1)

        self.tabWidget.addTab(self.ecu_menu_tab, "")
        self.all_variables_tab = QWidget()
        self.all_variables_tab.setObjectName(u"all_variables_tab")
        self.gridLayout_6 = QGridLayout(self.all_variables_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.arcode_variables_groupBox = QGroupBox(self.all_variables_tab)
        self.arcode_variables_groupBox.setObjectName(u"arcode_variables_groupBox")
        self.arcode_variables_groupBox.setFont(font2)
        self.horizontalLayout = QHBoxLayout(self.arcode_variables_groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.arcode_tableWidget_1 = QTableWidget(self.arcode_variables_groupBox)
        if (self.arcode_tableWidget_1.columnCount() < 2):
            self.arcode_tableWidget_1.setColumnCount(2)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.arcode_tableWidget_1.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.arcode_tableWidget_1.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        self.arcode_tableWidget_1.setObjectName(u"arcode_tableWidget_1")
        self.arcode_tableWidget_1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.arcode_tableWidget_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.arcode_tableWidget_1.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.arcode_tableWidget_1)

        self.arcode_tableWidget_2 = QTableWidget(self.arcode_variables_groupBox)
        if (self.arcode_tableWidget_2.columnCount() < 2):
            self.arcode_tableWidget_2.setColumnCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.arcode_tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.arcode_tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        self.arcode_tableWidget_2.setObjectName(u"arcode_tableWidget_2")
        self.arcode_tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.arcode_tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.arcode_tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.arcode_tableWidget_2)


        self.gridLayout_6.addWidget(self.arcode_variables_groupBox, 0, 2, 1, 1)

        self.main_variables_groupBox = QGroupBox(self.all_variables_tab)
        self.main_variables_groupBox.setObjectName(u"main_variables_groupBox")
        self.main_variables_groupBox.setFont(font2)
        self.horizontalLayout_2 = QHBoxLayout(self.main_variables_groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.main_tableWidget_1 = QTableWidget(self.main_variables_groupBox)
        if (self.main_tableWidget_1.columnCount() < 2):
            self.main_tableWidget_1.setColumnCount(2)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.main_tableWidget_1.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.main_tableWidget_1.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        self.main_tableWidget_1.setObjectName(u"main_tableWidget_1")
        self.main_tableWidget_1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.main_tableWidget_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.main_tableWidget_1.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_2.addWidget(self.main_tableWidget_1)

        self.main_tableWidget_2 = QTableWidget(self.main_variables_groupBox)
        if (self.main_tableWidget_2.columnCount() < 2):
            self.main_tableWidget_2.setColumnCount(2)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.main_tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.main_tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        self.main_tableWidget_2.setObjectName(u"main_tableWidget_2")
        self.main_tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.main_tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.main_tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_2.addWidget(self.main_tableWidget_2)


        self.gridLayout_6.addWidget(self.main_variables_groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.all_variables_tab, "")

        self.centralwidjet_layout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.centralwidjet_layout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionEdit_Defaults.setText(QCoreApplication.translate("MainWindow", u"Edit Defaults", None))
        self.mqtt_connection_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"MQTT Connection", None))
        self.ip_label.setText(QCoreApplication.translate("MainWindow", u"Target IP address:", None))
        self.connect_pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.client_name_label.setText(QCoreApplication.translate("MainWindow", u"My Client Name:", None))
        self.connection_status_label.setText(QCoreApplication.translate("MainWindow", u"Not Connected", None))
        self.connection_label.setText(QCoreApplication.translate("MainWindow", u"Connection Status:", None))
        self.ip_lineEdit.setText("")
        self.ping_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ping IP", None))
        self.ping_output_label.setText("")
        self.connection_status_led.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Supervisor", None))
        self.temperature_cooling_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Temperature and Cooling", None))
        self.temperature_value_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.cooling_power_label.setText(QCoreApplication.translate("MainWindow", u"Cooling Power", None))
        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.autocooling_checkBox.setText(QCoreApplication.translate("MainWindow", u"Automatic Cooling", None))
        self.datafile_management_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Data Files Managment", None))
        self.target_folder_label.setText(QCoreApplication.translate("MainWindow", u"Target ECU Folder", None))
        self.refresh_datafiles_pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh contents", None))
        self.download_datafiles_pushButton.setText(QCoreApplication.translate("MainWindow", u"Download files", None))
        self.delete_datafiles_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete files", None))
        ___qtablewidgetitem = self.datafiles_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.datafiles_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"kB", None));
        ___qtablewidgetitem2 = self.datafiles_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.convert_merge_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Convert/Merge Files", None))
        self.autoMerge_checkBox.setText("")
        self.convert_merge__status_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.convert_pushButton.setText(QCoreApplication.translate("MainWindow", u"Convert files", None))
        self.autoMerge_label.setText(QCoreApplication.translate("MainWindow", u"Auto-Merge multiple files", None))
        self.merge_pushButton.setText(QCoreApplication.translate("MainWindow", u"Merge mat files", None))
        self.datafile_download_status_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.control_mcu_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Control MCU", None))
        self.control_reset_mcu_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.control_firmware_managemen_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Firmware Management", None))
        self.control_choose_local_file_button.setText(QCoreApplication.translate("MainWindow", u"Select local file", None))
        self.control_refresh_files_button.setText(QCoreApplication.translate("MainWindow", u"Refresh folder", None))
        self.control_delete_file_button.setText(QCoreApplication.translate("MainWindow", u"Delete file", None))
        self.control_firmware_status_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.control_transfer_file_button.setText(QCoreApplication.translate("MainWindow", u"Transmit", None))
        ___qtablewidgetitem3 = self.control_binfiles_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem4 = self.control_binfiles_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"kB", None));
        ___qtablewidgetitem5 = self.control_binfiles_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.control_load_code_button.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.control_destination_path_label.setText(QCoreApplication.translate("MainWindow", u"Destination_path:", None))
        self.control_mcu_id_label.setText(QCoreApplication.translate("MainWindow", u"MCU ID:", None))
        self.control_reset_mcu_id_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.control_mcu_status_led.setText("")
        self.control_mcu_status_label.setText(QCoreApplication.translate("MainWindow", u"Not responding", None))
        self.control_stop_mcu_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.safety_mcu_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Safety MCU", None))
        self.safety_mcu_status_led.setText("")
        self.safety_reset_mcu_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.safety_mcu_status_label.setText(QCoreApplication.translate("MainWindow", u"Not responding", None))
        self.stop_mcu_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.safety_mcu_id_label.setText(QCoreApplication.translate("MainWindow", u"MCU ID:", None))
        self.safety_firmware_managemen_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Firmware Management", None))
        self.safety_refresh_files_button.setText(QCoreApplication.translate("MainWindow", u"Refresh folder", None))
        self.safety_delete_file_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.safety_firmware_status_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.safety_safety_choose_local_file_button.setText(QCoreApplication.translate("MainWindow", u"Select local file", None))
        self.safety_transfer_file_button.setText(QCoreApplication.translate("MainWindow", u"Transmit", None))
        ___qtablewidgetitem6 = self.safety_binfiles_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem7 = self.safety_binfiles_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"kB", None));
        ___qtablewidgetitem8 = self.safety_binfiles_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.safety_load_code_button.setText(QCoreApplication.translate("MainWindow", u"Load chosen file", None))
        self.safety_destination_path_label.setText(QCoreApplication.translate("MainWindow", u"Destination path:", None))
        self.safety_reset_mcu_id_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ecu_menu_tab), QCoreApplication.translate("MainWindow", u"ECU Menu", None))
        self.arcode_variables_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Monitor only Variables", None))
        ___qtablewidgetitem9 = self.arcode_tableWidget_1.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem10 = self.arcode_tableWidget_1.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem11 = self.arcode_tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem12 = self.arcode_tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.main_variables_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Logged Variables", None))
        ___qtablewidgetitem13 = self.main_tableWidget_1.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem14 = self.main_tableWidget_1.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem15 = self.main_tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem16 = self.main_tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.all_variables_tab), QCoreApplication.translate("MainWindow", u"All Variables", None))
    # retranslateUi

