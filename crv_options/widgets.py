import importlib

try:
    from PySide2 import QtWidgets, QtGui, QtCore
except ModuleNotFoundError:
    from PySide6 import QtWidgets, QtGui, QtCore

import crv_options.style as style

importlib.reload(style)


def add_button(text: str,
               background_color=style.color_palette["gray"].name(),
               color=style.color_palette["lightest_gray"].name(),
               hover_color=style.color_palette["light_gray"].name(),
               pressed_color=style.color_palette["dark_gray"].name(),
               width: float = 280,
               height: float = 30,
               ):
    #

    button = QtWidgets.QPushButton(text)
    button.setMinimumHeight(height)
    button.setMinimumWidth(width)

    button.setStyleSheet(
        style.custom_style_sheet["button"].format(
            background_color=background_color,
            color=color,
            hover_color=hover_color,
            pressed_color=pressed_color
        )
    )

    return button


def add_slider(handle_color: QtGui.QColor,
               handle_pressed: QtGui.QColor,
               range):
    #

    slider = QtWidgets.QSlider(orientation=QtCore.Qt.Horizontal)

    slider.setSingleStep(1)
    slider.setRange(1, range)
    slider.setValue(range / 2)
    slider.setStyleSheet(
        style.custom_style_sheet["slider"].format(
            handle_color=handle_color,
            handle_pressed=handle_pressed
        )
    )

    return slider


def add_label(text: str,
              background_color=style.color_palette["darkest_gray"].name(),
              color=style.color_palette["lightest_gray"].name(),
              center: bool = True,
              width: float = 80,
              height: float = 30,
              ):
    #
    label = QtWidgets.QLabel(text)
    label.setStyleSheet(
        style.custom_style_sheet["label"].format(
            background_color=background_color,
            color=color)
    )
    label.setMinimumHeight(height)
    label.setMinimumWidth(width)

    if center:
        label.setAlignment(QtCore.Qt.AlignCenter)

    return label


def add_line_edit(
        background_color=style.color_palette["gray"].name(),
        color=style.color_palette["lightest_gray"].name(),
        text: str = "",
        width: float = 10,
        height=30):
    #
    line_edit = QtWidgets.QLineEdit(text)
    line_edit.setStyleSheet(
        style.custom_style_sheet["line_edit"].format(
            background_color=background_color,
            color=color,
            width=width,
            height=height)
    )

    return line_edit


def add_combo_box(background_color: QtGui.QColor,
                  color: QtGui.QColor,
                  hover_color: QtGui.QColor,
                  items_list: [str],
                  height: float = 30,
                  width: float = 80,
                  ):
    #
    combo_box = QtWidgets.QComboBox()
    combo_box.setStyleSheet(
        style.custom_style_sheet["combo_box"].format(
            background_color=background_color,
            color=color,
            hover_color=hover_color)
    )
    combo_box.setMinimumWidth(width)
    combo_box.setMinimumHeight(height)

    combo_box.addItems(item for item in items_list)

    return combo_box


def add_layout(parent: QtWidgets.QWidget = None,
               layout_type: str = "V",
               widget_list: [str] = None):
    #
    if widget_list is None:
        widget_list = []
    layout = QtWidgets.QVBoxLayout(parent) if layout_type == "V" else QtWidgets.QHBoxLayout(parent)
    for widget in widget_list:
        layout.addWidget(widget)

    return layout


def add_separator():
    separator = QtWidgets.QFrame()
    separator.setFrameShape(QtWidgets.QFrame.HLine)
    separator.setFrameShadow(QtWidgets.QFrame.Sunken)
    separator.setStyleSheet("background-color: #404040;")
    separator.setLineWidth(2)
    return separator


def add_radio_button_grp(radio_button_name_list):
    # Attribute Type Widgets
    radio_button_grp = QtWidgets.QButtonGroup()
    radio_buttons = []
    for button_name in radio_button_name_list:
        radio_button = QtWidgets.QRadioButton(button_name)
        radio_button.setStyleSheet(style.custom_style_sheet["radio_button"])
        radio_button_grp.addButton(radio_button)
        radio_buttons.append(radio_button)

    radio_buttons[0].setChecked(True)

    return radio_button_grp, radio_buttons


def connect_slider_to_field(slider, line_edit, divided_by):
    slider_value = float(slider.value())
    line_edit.setText(str(slider_value / float(divided_by)))


def get_axis_direction(radio_button_grp):
    for button in radio_button_grp.buttons():
        if button.isChecked():
            return str(button.text())
