import maya.OpenMayaUI as OMUI

try:
    from shiboken2 import wrapInstance
    from PySide2 import QtCore, QtWidgets, QtGui
except ModuleNotFoundError:
    from shiboken6 import wrapInstance
    from PySide6 import QtCore, QtWidgets, QtGui


def get_maya_main_window():
    main_window_ptr = OMUI.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


gui_colors = {
    "background": QtGui.QColor(45, 45, 45),
    "text": QtGui.QColor(220, 220, 220),
    "button": QtGui.QColor(70, 70, 70),
    "blue": QtGui.QColor(93, 173, 226),
    "green": QtGui.QColor(88, 214, 141),
    "cyan": QtGui.QColor(115, 198, 182),
    "red": QtGui.QColor(236, 112, 99),
    "yellow": QtGui.QColor(244, 208, 63),
    "pink": QtGui.QColor(217, 136, 128),
    "orange": QtGui.QColor(245, 176, 65),
}


class CurveOptionsGUI(QtWidgets.QDialog):
    def __init__(self, parent=get_maya_main_window()):
        super().__init__(parent)
        self.setWindowTitle("RigTopia: Curve Multiple Options")
        self.setFixedSize(300, 600)
        self.setStyleSheet(
            f"background-color: {gui_colors['background'].name()}; color: {gui_colors['text'].name()};"
        )
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.ctrl_shape_label = self.create_label("::Ctrl Shape::", max_width=80)
        self.ctrl_shape_dropdown = self.create_dropdown(
            ["Box", "Square", "Smooth Square", "Shine Circle", "Diamond", "Sphere", "Sphere Rough",
             "Four Arrows", "Plus", "Rotated Plus", "Lollipop", "Pyramid", "Hexagon", "Arrow", "Star",
             "Pelvis", "Cylinder", "Locator", "Hoop", "Gear"]
        )
        self.create_button = self.create_button_widget("Create New Curve")
        self.replace_button = self.create_button_widget("Replace Existing Curve")
        self.scale_up_button = self.create_button_widget("Scale +")
        self.scale_down_button = self.create_button_widget("Scale -")
        self.search_field = QtWidgets.QLineEdit()
        self.replace_field = QtWidgets.QLineEdit()
        self.mirror_button = self.create_button_widget("Mirror Shape")

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        self.create_label("Curve Change Options", main_layout)
        main_layout.addWidget(self.create_separator())

        ctrl_shape_layout = QtWidgets.QHBoxLayout()
        ctrl_shape_layout.addWidget(self.ctrl_shape_label)
        ctrl_shape_layout.addWidget(self.ctrl_shape_dropdown)
        main_layout.addLayout(ctrl_shape_layout)
        main_layout.addWidget(self.create_separator())

        main_layout.addWidget(self.create_button)
        main_layout.addWidget(self.replace_button)
        main_layout.addWidget(self.create_separator())

        scale_layout = QtWidgets.QHBoxLayout()
        scale_layout.addWidget(self.scale_up_button)
        scale_layout.addWidget(self.scale_down_button)
        main_layout.addLayout(scale_layout)
        main_layout.addWidget(self.create_separator())

        self.create_label("Curve Color Options", main_layout)
        main_layout.addWidget(self.create_separator())

        color_layout = QtWidgets.QGridLayout()
        colors = ["blue", "green", "cyan", "red", "yellow", "pink", "orange"]
        for i, color in enumerate(colors):
            color_button = self.create_color_button(gui_colors[color])
            color_button.clicked.connect(lambda _, c=color: self.change_color(c))
            color_layout.addWidget(color_button, i // 4, i % 4)
        main_layout.addLayout(color_layout)

        main_layout.addWidget(self.create_separator())

        self.create_label("Curve Mirror Options", main_layout)
        main_layout.addWidget(self.create_separator())

        search_replace_layout = QtWidgets.QGridLayout()
        self.create_label("Search")
        search_replace_layout.addWidget(self.search_field, 0, 1)
        self.create_label("Replace")
        search_replace_layout.addWidget(self.replace_field, 1, 1)
        main_layout.addLayout(search_replace_layout)

        direction_layout = QtWidgets.QVBoxLayout()
        self.add_radio_group("X Direction", direction_layout, ["+X", "-X"], "red")
        direction_layout.addWidget(self.create_separator())
        self.add_radio_group("Y Direction", direction_layout, ["+Y", "-Y"], "green")
        direction_layout.addWidget(self.create_separator())
        self.add_radio_group("Z Direction", direction_layout, ["+Z", "-Z"], "blue")
        direction_layout.addWidget(self.create_separator())

        main_layout.addLayout(direction_layout)
        main_layout.addWidget(self.mirror_button)

        self.setLayout(main_layout)

    def create_connections(self):
        self.create_button.clicked.connect(self.create_curve)
        self.replace_button.clicked.connect(self.replace_curve)
        self.scale_up_button.clicked.connect(self.scale_up)
        self.scale_down_button.clicked.connect(self.scale_down)
        self.mirror_button.clicked.connect(self.mirror_shape)

    def create_label(self, text, max_width=None):
        label = QtWidgets.QLabel(text)
        label.setStyleSheet(f"color: {gui_colors['text'].name()}; padding: 4px;")
        label.setAlignment(QtCore.Qt.AlignCenter)
        # if max_width:
        #     label.setMaximumWidth(max_width)
        return label

    def create_button_widget(self, text):
        button = QtWidgets.QPushButton(text)
        button.setStyleSheet(
            f"background-color: {gui_colors['button'].name()}; color: {gui_colors['text'].name()};"
        )
        button.setFixedHeight(35)
        return button

    def create_dropdown(self, items):
        dropdown = QtWidgets.QComboBox()
        dropdown.setStyleSheet(
            f"background-color: {gui_colors['button'].name()}; color: {gui_colors['text'].name()};"
        )
        dropdown.addItems(items)
        return dropdown

    def create_color_button(self, color):
        button = QtWidgets.QPushButton()
        button.setFixedSize(30, 30)
        button.setStyleSheet(f"background-color: {color.name()};")
        return button

    def add_radio_group(self, label_text, layout, options, color):
        label = self.create_label(label_text)
        label.setStyleSheet(f"background-color: {gui_colors[color].name()};")
        layout.addWidget(label)

        for option in options:
            radio_button = QtWidgets.QRadioButton(option)
            radio_button.setStyleSheet(f"color: {gui_colors['text'].name()};")
            layout.addWidget(radio_button)

    def create_separator(self):
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        separator.setStyleSheet("background-color: #505050;")
        separator.setLineWidth(2)
        return separator

    def create_curve(self):
        print("Create Curve clicked!")

    def replace_curve(self):
        print("Replace Curve clicked!")

    def scale_up(self):
        print("Scale Up clicked!")

    def scale_down(self):
        print("Scale Down clicked!")

    def change_color(self, color):
        print(f"Color {color} selected!")

    def mirror_shape(self):
        print("Mirror Shape clicked!")


if __name__ == "__main__":
    gui_x = CurveOptionsGUI()
    gui_x.show()
