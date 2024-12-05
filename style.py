try:
    from PySide2 import QtGui
except ModuleNotFoundError:
    from PySide6 import QtGui

color_palette = {
    # Base Colors
    "black": QtGui.QColor(0, 0, 0),
    "white": QtGui.QColor(255, 255, 255),
    "gray": QtGui.QColor(70, 70, 70),
    "light_gray": QtGui.QColor(90, 90, 90),
    "dark_gray": QtGui.QColor(45, 45, 45),

    # Primary Colors
    "red": QtGui.QColor(255, 0, 0),
    "green": QtGui.QColor(0, 255, 0),
    "blue": QtGui.QColor(0, 0, 255),

    # Secondary Colors
    "yellow": QtGui.QColor(255, 255, 0),
    "cyan": QtGui.QColor(0, 255, 255),
    "magenta": QtGui.QColor(255, 0, 255),

    "dark_red": QtGui.QColor(139, 0, 0),
    "dark_green": QtGui.QColor(0, 100, 0),
    "dark_blue": QtGui.QColor(0, 0, 139),

    "light_blue": QtGui.QColor(173, 216, 230),
    "light_green": QtGui.QColor(144, 238, 144),
    "light_red": QtGui.QColor(255, 102, 102),

    "balanced_red": QtGui.QColor(200, 70, 70),
    "balanced_green": QtGui.QColor(70, 200, 70),
    "balanced_blue": QtGui.QColor(70, 70, 200),

    "muted_red": QtGui.QColor(220, 110, 110),
    "muted_green": QtGui.QColor(110, 220, 110),
    "muted_blue": QtGui.QColor(110, 110, 220),

    "medium_red": QtGui.QColor(220, 50, 50),
    "medium_green": QtGui.QColor(50, 220, 50),
    "medium_blue": QtGui.QColor(50, 50, 220),

    "soft_red": QtGui.QColor(178, 76, 102),
    "soft_green": QtGui.QColor(128, 255, 128),
    "soft_blue": QtGui.QColor(51, 178, 229),

    # Other Colors
    "orange": QtGui.QColor(255, 165, 0),
    "purple": QtGui.QColor(128, 0, 128),
    "brown": QtGui.QColor(165, 42, 42),
    "pink": QtGui.QColor(255, 192, 203),
    "teal": QtGui.QColor(0, 128, 128),
    "olive": QtGui.QColor(128, 128, 0),

    # Custom Colors
    "custom_blue": QtGui.QColor(23, 153, 231),
    "custom_green": QtGui.QColor(37, 211, 102),
    "custom_red": QtGui.QColor(255, 58, 58),
    "darkest_gray": QtGui.QColor(30, 30, 30),
    "lightest_gray": QtGui.QColor(220, 220, 220),
}

custom_style_sheet = {
    "dialog":
        """
        QDialog
        {{
            background-color: {background_color};
            border-width: 4px;
            border-color: {border_color};
            border-radius: 10px;
            padding: 10px;
        }}
    """,

    "line_edit":
        """
        QLineEdit 
        {{ 
            height:{height};
            width: {width};
            background-color: {background_color};
            border-width: 3px; 
            border-radius: 4px;
            font: bold 14px;
        }}
        QLineEdit:placeholder 
        {{
            color: black;
            font: bold 10px;
        }}
    """,

    "button":
        """
        QPushButton
        {{
            background-color: {background_color}; 
            border-width: 2px;
            border-radius: 4px;
            color: {color};
            padding: 4px;
            font:bold 12px;
        }}
        QPushButton:hover 
        {{
            background-color: {hover_color}; 
        }}
        QPushButton:pressed 
        {{
            background-color: {pressed_color};
            color: lightgray; 
        }}
    """,
    "colored_button":
        """
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #FF7070, stop: 0.16 #FFC870, stop: 0.33 #FFFF70,
                    stop: 0.5 #70FF70, stop: 0.66 #70B0FF, stop: 0.83 #B070FF, stop: 1 #FF70B0
                );
                border: 2px solid #555;
                border-radius: 8px;
                color: white;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #FF7070, stop: 0.16 #FFC870, stop: 0.33 #FFFF70,
                    stop: 0.5 #70FF70, stop: 0.66 #70B0FF, stop: 0.83 #B070FF, stop: 1 #FF70B0
                );
                border: 2px solid #fff;
            }
        """,

    "label":
        """
        QLabel
        {{   
            background-color: {background_color};
            padding: 4px;
            border-width: 3px;
            border-radius: 4px;
            color: {color}; 
            font:bold 12px;
        }}
    """,

    "combo_box":
        """
        QComboBox 
        {{
            background-color: {background_color};
            color: {color};
            font: 14px;
        }}
        QComboBox:hover 
        {{
            background-color: {hover_color}; 
        }}
    """,
    "spin_box":
        """
        QDoubleSpinBox 
        {
            background-color: (70, 70, 70);
            color: (90, 90, 90);
            border-width: 2px; 
            border-radius: 5px;
            font: bold 12px;
        }
    """,

    "group_box":
        """
        QGroupBox 
        {{
            font: bold 13px;
            border-style: outset;
            border-width: 2px;
            border-radius: 6px;
            border-color: {border_color}; /* Replace with desired border color */
            padding: 10px;
        }}
    """,

    "radio_button":
        """
        QRadioButton 
        {
            font: bold 12px;
        }
        QRadioButton::indicator
        {
        width:15;
        height:15;
        radius: 9;
        }
        """
    ,
    "checkbox":
        """
        QCheckBox::indicator 
        {
            width: 30px;
            height: 30px;
            border: 2px solid black; /* Thicker border for larger size */
            background-color: white;
        }

        QCheckBox::indicator:checked 
        {
            background-color: blue;
            border-color: darkblue;
        }
    """,

    "slider":
        """
        QSlider
        {{
            border-style: solid;
            border-color: rgb(37, 211, 102);
        }}
        QSlider::handle
        {{
            background-color: {handle_color};
            width: 12px;
            height: 12px;
            border-radius: 2px;
        }}
        QSlider::handle:pressed 
        {{
            background-color: {handle_pressed};
        }}
    """
}
