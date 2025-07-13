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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1348, 687)
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

        self.control_mcu_groupbox = QGroupBox(self.ecu_menu_tab)
        self.control_mcu_groupbox.setObjectName(u"control_mcu_groupbox")
        self.control_mcu_groupbox.setMinimumSize(QSize(450, 0))
        self.control_mcu_groupbox.setMaximumSize(QSize(650, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.control_mcu_groupbox.setFont(font2)
        self.gridLayout_7 = QGridLayout(self.control_mcu_groupbox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.control_mcu_status_led = QLabel(self.control_mcu_groupbox)
        self.control_mcu_status_led.setObjectName(u"control_mcu_status_led")
        self.control_mcu_status_led.setMaximumSize(QSize(40, 40))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(9)
        font3.setWeight(QFont.Black)
        font3.setKerning(True)
        self.control_mcu_status_led.setFont(font3)
        self.control_mcu_status_led.setPixmap(QPixmap(u"images/red-led.png"))
        self.control_mcu_status_led.setScaledContents(True)

        self.gridLayout_7.addWidget(self.control_mcu_status_led, 1, 3, 1, 1)

        self.control_mcu_status_label = QLabel(self.control_mcu_groupbox)
        self.control_mcu_status_label.setObjectName(u"control_mcu_status_label")

        self.gridLayout_7.addWidget(self.control_mcu_status_label, 1, 2, 1, 1)

        self.control_stop_mcu_button = QPushButton(self.control_mcu_groupbox)
        self.control_stop_mcu_button.setObjectName(u"control_stop_mcu_button")

        self.gridLayout_7.addWidget(self.control_stop_mcu_button, 1, 5, 1, 1)

        self.control_reset_mcu_button = QPushButton(self.control_mcu_groupbox)
        self.control_reset_mcu_button.setObjectName(u"control_reset_mcu_button")

        self.gridLayout_7.addWidget(self.control_reset_mcu_button, 1, 4, 1, 1)

        self.control_mcu_id_label = QLabel(self.control_mcu_groupbox)
        self.control_mcu_id_label.setObjectName(u"control_mcu_id_label")

        self.gridLayout_7.addWidget(self.control_mcu_id_label, 0, 2, 1, 1)

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
        __qtablewidgetitem = QTableWidgetItem()
        self.control_binfiles_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.control_binfiles_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.control_binfiles_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
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

        self.control_reset_mcu_id_button = QPushButton(self.control_mcu_groupbox)
        self.control_reset_mcu_id_button.setObjectName(u"control_reset_mcu_id_button")
        self.control_reset_mcu_id_button.setMaximumSize(QSize(45, 16777215))
        self.control_reset_mcu_id_button.setFont(font2)

        self.gridLayout_7.addWidget(self.control_reset_mcu_id_button, 0, 3, 1, 1)

        self.control_mcu_id_lineEdit = QLineEdit(self.control_mcu_groupbox)
        self.control_mcu_id_lineEdit.setObjectName(u"control_mcu_id_lineEdit")

        self.gridLayout_7.addWidget(self.control_mcu_id_lineEdit, 0, 4, 1, 2)


        self.gridLayout_5.addWidget(self.control_mcu_groupbox, 1, 0, 3, 1)

        self.groupBox = QGroupBox(self.ecu_menu_tab)
        self.groupBox.setObjectName(u"groupBox")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setBold(True)
        self.groupBox.setFont(font4)
        self.gridLayout_12 = QGridLayout(self.groupBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.temperature_label = QLabel(self.groupBox)
        self.temperature_label.setObjectName(u"temperature_label")

        self.gridLayout_12.addWidget(self.temperature_label, 0, 3, 1, 1)

        self.temperature_value_label = QLabel(self.groupBox)
        self.temperature_value_label.setObjectName(u"temperature_value_label")
        self.temperature_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.temperature_value_label, 0, 4, 1, 1)

        self.poweroff_pi = QPushButton(self.groupBox)
        self.poweroff_pi.setObjectName(u"poweroff_pi")
        self.poweroff_pi.setMaximumSize(QSize(80, 16777215))
        self.poweroff_pi.setFont(font2)

        self.gridLayout_12.addWidget(self.poweroff_pi, 0, 2, 1, 1)

        self.reboot_pi = QPushButton(self.groupBox)
        self.reboot_pi.setObjectName(u"reboot_pi")
        self.reboot_pi.setFont(font2)

        self.gridLayout_12.addWidget(self.reboot_pi, 0, 0, 1, 2)

        self.datalogging_timestamp = QLabel(self.groupBox)
        self.datalogging_timestamp.setObjectName(u"datalogging_timestamp")

        self.gridLayout_12.addWidget(self.datalogging_timestamp, 2, 0, 1, 3)

        self.datalogging_timestamp_value = QLabel(self.groupBox)
        self.datalogging_timestamp_value.setObjectName(u"datalogging_timestamp_value")
        self.datalogging_timestamp_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.datalogging_timestamp_value, 2, 3, 1, 2)

        self.streaming_hz = QLabel(self.groupBox)
        self.streaming_hz.setObjectName(u"streaming_hz")

        self.gridLayout_12.addWidget(self.streaming_hz, 4, 0, 1, 3)

        self.streaming_hz_value = QLabel(self.groupBox)
        self.streaming_hz_value.setObjectName(u"streaming_hz_value")
        self.streaming_hz_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.streaming_hz_value, 4, 3, 1, 2)

        self.restart_supervisor = QPushButton(self.groupBox)
        self.restart_supervisor.setObjectName(u"restart_supervisor")
        self.restart_supervisor.setFont(font2)

        self.gridLayout_12.addWidget(self.restart_supervisor, 5, 0, 1, 2)

        self.stop_supervisor = QPushButton(self.groupBox)
        self.stop_supervisor.setObjectName(u"stop_supervisor")

        self.gridLayout_12.addWidget(self.stop_supervisor, 5, 3, 1, 2)

        self.start_supervisor = QPushButton(self.groupBox)
        self.start_supervisor.setObjectName(u"start_supervisor")
        self.start_supervisor.setFont(font2)

        self.gridLayout_12.addWidget(self.start_supervisor, 5, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 1, 1, 1)

        self.datafile_management_groupBox = QGroupBox(self.ecu_menu_tab)
        self.datafile_management_groupBox.setObjectName(u"datafile_management_groupBox")
        self.datafile_management_groupBox.setFont(font4)
        self.gridLayout_9 = QGridLayout(self.datafile_management_groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.delete_datafiles_pushButton = QPushButton(self.datafile_management_groupBox)
        self.delete_datafiles_pushButton.setObjectName(u"delete_datafiles_pushButton")

        self.gridLayout_9.addWidget(self.delete_datafiles_pushButton, 3, 1, 1, 1)

        self.target_folder_label = QLabel(self.datafile_management_groupBox)
        self.target_folder_label.setObjectName(u"target_folder_label")

        self.gridLayout_9.addWidget(self.target_folder_label, 0, 0, 1, 1)

        self.datafiles_tableWidget = QTableWidget(self.datafile_management_groupBox)
        if (self.datafiles_tableWidget.columnCount() < 3):
            self.datafiles_tableWidget.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.datafiles_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.datafiles_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.datafiles_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
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

        self.target_folder_lineEdit = QLineEdit(self.datafile_management_groupBox)
        self.target_folder_lineEdit.setObjectName(u"target_folder_lineEdit")

        self.gridLayout_9.addWidget(self.target_folder_lineEdit, 0, 1, 1, 4)

        self.datafile_download_status_label = QLabel(self.datafile_management_groupBox)
        self.datafile_download_status_label.setObjectName(u"datafile_download_status_label")
        self.datafile_download_status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.datafile_download_status_label, 4, 0, 1, 5)

        self.refresh_datafiles_pushButton = QPushButton(self.datafile_management_groupBox)
        self.refresh_datafiles_pushButton.setObjectName(u"refresh_datafiles_pushButton")

        self.gridLayout_9.addWidget(self.refresh_datafiles_pushButton, 3, 0, 1, 1)

        self.convert_merge_groupBox = QGroupBox(self.datafile_management_groupBox)
        self.convert_merge_groupBox.setObjectName(u"convert_merge_groupBox")
        self.gridLayout_10 = QGridLayout(self.convert_merge_groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.convert_pushButton = QPushButton(self.convert_merge_groupBox)
        self.convert_pushButton.setObjectName(u"convert_pushButton")

        self.gridLayout_10.addWidget(self.convert_pushButton, 0, 0, 1, 2)

        self.convert_merge__status_label = QLabel(self.convert_merge_groupBox)
        self.convert_merge__status_label.setObjectName(u"convert_merge__status_label")
        self.convert_merge__status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.convert_merge__status_label, 1, 0, 1, 2)


        self.gridLayout_9.addWidget(self.convert_merge_groupBox, 5, 0, 1, 5)

        self.download_datafiles_pushButton = QPushButton(self.datafile_management_groupBox)
        self.download_datafiles_pushButton.setObjectName(u"download_datafiles_pushButton")

        self.gridLayout_9.addWidget(self.download_datafiles_pushButton, 3, 2, 1, 3)


        self.gridLayout_5.addWidget(self.datafile_management_groupBox, 0, 4, 4, 1)

        self.general_mcu_groupbox = QGroupBox(self.ecu_menu_tab)
        self.general_mcu_groupbox.setObjectName(u"general_mcu_groupbox")
        self.general_mcu_groupbox.setMinimumSize(QSize(450, 0))
        self.general_mcu_groupbox.setMaximumSize(QSize(650, 16777215))
        self.general_mcu_groupbox.setFont(font2)
        self.gridLayout = QGridLayout(self.general_mcu_groupbox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.general_mcu_status_led = QLabel(self.general_mcu_groupbox)
        self.general_mcu_status_led.setObjectName(u"general_mcu_status_led")
        self.general_mcu_status_led.setMaximumSize(QSize(40, 40))
        self.general_mcu_status_led.setFont(font3)
        self.general_mcu_status_led.setPixmap(QPixmap(u"images/red-led.png"))
        self.general_mcu_status_led.setScaledContents(True)

        self.gridLayout.addWidget(self.general_mcu_status_led, 1, 3, 1, 1)

        self.general_reset_mcu_button = QPushButton(self.general_mcu_groupbox)
        self.general_reset_mcu_button.setObjectName(u"general_reset_mcu_button")

        self.gridLayout.addWidget(self.general_reset_mcu_button, 1, 4, 1, 1)

        self.general_mcu_status_label = QLabel(self.general_mcu_groupbox)
        self.general_mcu_status_label.setObjectName(u"general_mcu_status_label")

        self.gridLayout.addWidget(self.general_mcu_status_label, 1, 2, 1, 1)

        self.general_stop_mcu_button = QPushButton(self.general_mcu_groupbox)
        self.general_stop_mcu_button.setObjectName(u"general_stop_mcu_button")

        self.gridLayout.addWidget(self.general_stop_mcu_button, 1, 5, 1, 1)

        self.general_mcu_id_label = QLabel(self.general_mcu_groupbox)
        self.general_mcu_id_label.setObjectName(u"general_mcu_id_label")
        self.general_mcu_id_label.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.general_mcu_id_label, 0, 2, 1, 1)

        self.general_firmware_managemen_groupBox = QGroupBox(self.general_mcu_groupbox)
        self.general_firmware_managemen_groupBox.setObjectName(u"general_firmware_managemen_groupBox")
        self.gridLayout_2 = QGridLayout(self.general_firmware_managemen_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.general_refresh_files_button = QPushButton(self.general_firmware_managemen_groupBox)
        self.general_refresh_files_button.setObjectName(u"general_refresh_files_button")

        self.gridLayout_2.addWidget(self.general_refresh_files_button, 3, 0, 1, 1)

        self.general_delete_file_button = QPushButton(self.general_firmware_managemen_groupBox)
        self.general_delete_file_button.setObjectName(u"general_delete_file_button")

        self.gridLayout_2.addWidget(self.general_delete_file_button, 3, 1, 1, 1)

        self.general_destination_path_lineEdit = QLineEdit(self.general_firmware_managemen_groupBox)
        self.general_destination_path_lineEdit.setObjectName(u"general_destination_path_lineEdit")

        self.gridLayout_2.addWidget(self.general_destination_path_lineEdit, 1, 1, 1, 2)

        self.general_firmware_status_label = QLabel(self.general_firmware_managemen_groupBox)
        self.general_firmware_status_label.setObjectName(u"general_firmware_status_label")
        self.general_firmware_status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.general_firmware_status_label, 4, 0, 1, 3)

        self.general_choose_local_file_button = QPushButton(self.general_firmware_managemen_groupBox)
        self.general_choose_local_file_button.setObjectName(u"general_choose_local_file_button")

        self.gridLayout_2.addWidget(self.general_choose_local_file_button, 0, 0, 1, 1)

        self.general_transfer_file_button = QPushButton(self.general_firmware_managemen_groupBox)
        self.general_transfer_file_button.setObjectName(u"general_transfer_file_button")
        self.general_transfer_file_button.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.general_transfer_file_button, 1, 3, 1, 1)

        self.general_binfiles_tableWidget = QTableWidget(self.general_firmware_managemen_groupBox)
        if (self.general_binfiles_tableWidget.columnCount() < 3):
            self.general_binfiles_tableWidget.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.general_binfiles_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.general_binfiles_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.general_binfiles_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.general_binfiles_tableWidget.setObjectName(u"general_binfiles_tableWidget")
        self.general_binfiles_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.general_binfiles_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.general_binfiles_tableWidget.setDragDropOverwriteMode(False)
        self.general_binfiles_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.general_binfiles_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.general_binfiles_tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.general_binfiles_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.general_binfiles_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.general_binfiles_tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.general_binfiles_tableWidget, 2, 0, 1, 4)

        self.general_load_code_button = QPushButton(self.general_firmware_managemen_groupBox)
        self.general_load_code_button.setObjectName(u"general_load_code_button")

        self.gridLayout_2.addWidget(self.general_load_code_button, 3, 2, 1, 2)

        self.general_local_path_lineEdit = QLineEdit(self.general_firmware_managemen_groupBox)
        self.general_local_path_lineEdit.setObjectName(u"general_local_path_lineEdit")

        self.gridLayout_2.addWidget(self.general_local_path_lineEdit, 0, 1, 1, 3)

        self.general_destination_path_label = QLabel(self.general_firmware_managemen_groupBox)
        self.general_destination_path_label.setObjectName(u"general_destination_path_label")
        self.general_destination_path_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.general_destination_path_label, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.general_firmware_managemen_groupBox, 2, 2, 1, 4)

        self.general_mcu_id_lineEdit = QLineEdit(self.general_mcu_groupbox)
        self.general_mcu_id_lineEdit.setObjectName(u"general_mcu_id_lineEdit")

        self.gridLayout.addWidget(self.general_mcu_id_lineEdit, 0, 4, 1, 2)

        self.general_reset_mcu_id_button = QPushButton(self.general_mcu_groupbox)
        self.general_reset_mcu_id_button.setObjectName(u"general_reset_mcu_id_button")
        self.general_reset_mcu_id_button.setMaximumSize(QSize(45, 16777215))
        self.general_reset_mcu_id_button.setFont(font2)

        self.gridLayout.addWidget(self.general_reset_mcu_id_button, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.general_mcu_groupbox, 1, 1, 3, 1)

        self.tabWidget.addTab(self.ecu_menu_tab, "")
        self.all_variables_tab = QWidget()
        self.all_variables_tab.setObjectName(u"all_variables_tab")
        self.gridLayout_6 = QGridLayout(self.all_variables_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.control_tune_groupBox = QGroupBox(self.all_variables_tab)
        self.control_tune_groupBox.setObjectName(u"control_tune_groupBox")
        self.gridLayout_14 = QGridLayout(self.control_tune_groupBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.control_tuning_value_lineEdit = QLineEdit(self.control_tune_groupBox)
        self.control_tuning_value_lineEdit.setObjectName(u"control_tuning_value_lineEdit")

        self.gridLayout_14.addWidget(self.control_tuning_value_lineEdit, 1, 0, 1, 1)

        self.control_tuning_vars_comboBox = QComboBox(self.control_tune_groupBox)
        self.control_tuning_vars_comboBox.addItem("")
        self.control_tuning_vars_comboBox.setObjectName(u"control_tuning_vars_comboBox")

        self.gridLayout_14.addWidget(self.control_tuning_vars_comboBox, 0, 0, 1, 1)

        self.control_tune_refresh_pushButton = QPushButton(self.control_tune_groupBox)
        self.control_tune_refresh_pushButton.setObjectName(u"control_tune_refresh_pushButton")

        self.gridLayout_14.addWidget(self.control_tune_refresh_pushButton, 0, 1, 1, 1)

        self.control_tune_pushButton = QPushButton(self.control_tune_groupBox)
        self.control_tune_pushButton.setObjectName(u"control_tune_pushButton")

        self.gridLayout_14.addWidget(self.control_tune_pushButton, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.control_tune_groupBox, 0, 1, 1, 1)

        self.general_tune_groupBox = QGroupBox(self.all_variables_tab)
        self.general_tune_groupBox.setObjectName(u"general_tune_groupBox")
        self.gridLayout_15 = QGridLayout(self.general_tune_groupBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.general_tuning_value_lineEdit = QLineEdit(self.general_tune_groupBox)
        self.general_tuning_value_lineEdit.setObjectName(u"general_tuning_value_lineEdit")

        self.gridLayout_15.addWidget(self.general_tuning_value_lineEdit, 1, 0, 1, 1)

        self.general_tune_pushButton = QPushButton(self.general_tune_groupBox)
        self.general_tune_pushButton.setObjectName(u"general_tune_pushButton")

        self.gridLayout_15.addWidget(self.general_tune_pushButton, 1, 1, 1, 1)

        self.general_tuning_vars_comboBox = QComboBox(self.general_tune_groupBox)
        self.general_tuning_vars_comboBox.addItem("")
        self.general_tuning_vars_comboBox.setObjectName(u"general_tuning_vars_comboBox")

        self.gridLayout_15.addWidget(self.general_tuning_vars_comboBox, 0, 0, 1, 1)

        self.general_tune_refresh_pushButton = QPushButton(self.general_tune_groupBox)
        self.general_tune_refresh_pushButton.setObjectName(u"general_tune_refresh_pushButton")

        self.gridLayout_15.addWidget(self.general_tune_refresh_pushButton, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.general_tune_groupBox, 0, 2, 1, 1)

        self.main_variables_groupBox = QGroupBox(self.all_variables_tab)
        self.main_variables_groupBox.setObjectName(u"main_variables_groupBox")
        self.main_variables_groupBox.setFont(font4)
        self.horizontalLayout_2 = QHBoxLayout(self.main_variables_groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.main_tableWidget_1 = QTableWidget(self.main_variables_groupBox)
        if (self.main_tableWidget_1.columnCount() < 2):
            self.main_tableWidget_1.setColumnCount(2)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.main_tableWidget_1.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.main_tableWidget_1.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        self.main_tableWidget_1.setObjectName(u"main_tableWidget_1")
        self.main_tableWidget_1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.main_tableWidget_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.main_tableWidget_1.horizontalHeader().setMinimumSectionSize(500)
        self.main_tableWidget_1.horizontalHeader().setStretchLastSection(True)
        self.main_tableWidget_1.verticalHeader().setVisible(True)
        self.main_tableWidget_1.verticalHeader().setHighlightSections(True)

        self.horizontalLayout_2.addWidget(self.main_tableWidget_1)


        self.gridLayout_6.addWidget(self.main_variables_groupBox, 1, 0, 2, 3)

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
        self.control_mcu_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Control MCU", None))
        self.control_mcu_status_led.setText("")
        self.control_mcu_status_label.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.control_stop_mcu_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.control_reset_mcu_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.control_mcu_id_label.setText(QCoreApplication.translate("MainWindow", u"MCU ID:", None))
        self.control_firmware_managemen_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Firmware Management", None))
        self.control_choose_local_file_button.setText(QCoreApplication.translate("MainWindow", u"Select local file", None))
        self.control_refresh_files_button.setText(QCoreApplication.translate("MainWindow", u"Refresh folder", None))
        self.control_delete_file_button.setText(QCoreApplication.translate("MainWindow", u"Delete file", None))
        self.control_firmware_status_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.control_transfer_file_button.setText(QCoreApplication.translate("MainWindow", u"Transmit", None))
        ___qtablewidgetitem = self.control_binfiles_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.control_binfiles_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"kB", None));
        ___qtablewidgetitem2 = self.control_binfiles_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.control_load_code_button.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.control_destination_path_label.setText(QCoreApplication.translate("MainWindow", u"Destination_path:", None))
        self.control_reset_mcu_id_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Supervisor", None))
        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"CPU Temp:", None))
        self.temperature_value_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.poweroff_pi.setText(QCoreApplication.translate("MainWindow", u"Poweroff", None))
        self.reboot_pi.setText(QCoreApplication.translate("MainWindow", u"Reboot", None))
        self.datalogging_timestamp.setText(QCoreApplication.translate("MainWindow", u"DL Timespamp:", None))
        self.datalogging_timestamp_value.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.streaming_hz.setText(QCoreApplication.translate("MainWindow", u"Streaming (Hz):", None))
        self.streaming_hz_value.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.restart_supervisor.setText(QCoreApplication.translate("MainWindow", u"Restart Supervisor", None))
        self.stop_supervisor.setText(QCoreApplication.translate("MainWindow", u"Stop Supervisor", None))
        self.start_supervisor.setText(QCoreApplication.translate("MainWindow", u"Start Supervisor", None))
        self.datafile_management_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Data Files Managment", None))
        self.delete_datafiles_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete files", None))
        self.target_folder_label.setText(QCoreApplication.translate("MainWindow", u"Target ECU Folder", None))
        ___qtablewidgetitem3 = self.datafiles_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem4 = self.datafiles_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"kB", None));
        ___qtablewidgetitem5 = self.datafiles_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.datafile_download_status_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.refresh_datafiles_pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh contents", None))
        self.convert_merge_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Convert/Merge Files", None))
        self.convert_pushButton.setText(QCoreApplication.translate("MainWindow", u"Convert files", None))
        self.convert_merge__status_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.download_datafiles_pushButton.setText(QCoreApplication.translate("MainWindow", u"Download files", None))
        self.general_mcu_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"General MCU", None))
        self.general_mcu_status_led.setText("")
        self.general_reset_mcu_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.general_mcu_status_label.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.general_stop_mcu_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.general_mcu_id_label.setText(QCoreApplication.translate("MainWindow", u"MCU ID:", None))
        self.general_firmware_managemen_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Firmware Management", None))
        self.general_refresh_files_button.setText(QCoreApplication.translate("MainWindow", u"Refresh folder", None))
        self.general_delete_file_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.general_firmware_status_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.general_choose_local_file_button.setText(QCoreApplication.translate("MainWindow", u"Select local file", None))
        self.general_transfer_file_button.setText(QCoreApplication.translate("MainWindow", u"Transmit", None))
        ___qtablewidgetitem6 = self.general_binfiles_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem7 = self.general_binfiles_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"kB", None));
        ___qtablewidgetitem8 = self.general_binfiles_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.general_load_code_button.setText(QCoreApplication.translate("MainWindow", u"Load chosen file", None))
        self.general_destination_path_label.setText(QCoreApplication.translate("MainWindow", u"Destination path:", None))
        self.general_reset_mcu_id_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ecu_menu_tab), QCoreApplication.translate("MainWindow", u"VCU Menu", None))
        self.control_tune_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Control Tunning", None))
        self.control_tuning_vars_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.control_tune_refresh_pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.control_tune_pushButton.setText(QCoreApplication.translate("MainWindow", u"Tune", None))
        self.general_tune_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"General Tunning", None))
        self.general_tune_pushButton.setText(QCoreApplication.translate("MainWindow", u"Tune", None))
        self.general_tuning_vars_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.general_tune_refresh_pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.main_variables_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Logged Variables", None))
        ___qtablewidgetitem9 = self.main_tableWidget_1.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem10 = self.main_tableWidget_1.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.all_variables_tab), QCoreApplication.translate("MainWindow", u"Variables && Tune", None))
    # retranslateUi

