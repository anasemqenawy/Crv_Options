import importlib
import maya.OpenMayaUI as OMUI

try:
    from shiboken2 import wrapInstance
    from PySide2 import QtCore, QtWidgets, QtGui
except ModuleNotFoundError:
    from shiboken6 import wrapInstance
    from PySide6 import QtCore, QtWidgets, QtGui

import crv_options.style as style
import crv_options.crv_shapes as crv_shapes
import crv_options.widgets as widgets

importlib.reload(style)
importlib.reload(widgets)
importlib.reload(crv_shapes)


def get_maya_main_window():
    main_window_ptr = OMUI.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


class CurveOptionsGUI(QtWidgets.QDialog):
    def __init__(self, parent=get_maya_main_window()):
        super().__init__(parent)
        self.setWindowTitle(":: RigTopia ::")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowMinimizeButtonHint)
        self.main_width = 300
        self.setMaximumWidth(self.main_width)
        self.setMaximumHeight(300)

        self.setStyleSheet(
            style.custom_style_sheet["dialog"].format(
                background_color=style.color_palette["darkest_gray"].name(),
                border_color=style.color_palette["darkest_gray"].name()
            )
        )

        self.create_widgets_with_layout()
        # self.create_connections()

    def create_widgets_with_layout(self):
        # -----------------------------------------------------
        # ------------------ Main Layout ----------------------
        # -----------------------------------------------------
        main_layout = widgets.add_layout(parent=self,
                                         layout_type="V",
                                         widget_list=None)

        # -----------------------------------------------------
        # ------------------ Tool Name Layout -----------------
        # -----------------------------------------------------
        self.tool_label = widgets.add_label(text=":: Curve Options v.0.1 ::",
                                            width=self.main_width,
                                            background_color=style.color_palette["darkest_gray"].name(),
                                            color=style.color_palette["lightest_gray"].name(),
                                            center=True)

        main_layout.addWidget(widgets.add_separator())
        main_layout.addWidget(self.tool_label)

        # -----------------------------------------------------
        # ------------------ Curve Shape Layout ---------------
        # -----------------------------------------------------
        self.crv_shape_label = widgets.add_label(text=":: Curve Shape ::", width=60,
                                                 background_color=style.color_palette["darkest_gray"].name(),
                                                 color=style.color_palette["lightest_gray"].name(),
                                                 center=False)

        self.crv_shape_dropdwn = widgets.add_combo_box(width=180,
                                                       background_color=style.color_palette["gray"].name(),
                                                       color=style.color_palette["lightest_gray"].name(),
                                                       hover_color=style.color_palette["light_gray"].name(),
                                                       items_list=list(crv_shapes.shapes_data.keys())
                                                       )
        self.crv_shape_dropdwn.setMaxVisibleItems(25)

        crv_change_pick_layout = widgets.add_layout(parent=None,
                                                    layout_type="H",
                                                    widget_list=[self.crv_shape_label, self.crv_shape_dropdwn])

        main_layout.addWidget(widgets.add_separator())
        main_layout.addLayout(crv_change_pick_layout)

        # -----------------------------------------------------
        # ------------------ Curve Commands Layout ------------
        # -----------------------------------------------------
        self.create_crv_button = widgets.add_button(text=":: Create New ::")

        self.replace_crv_button = widgets.add_button(text=":: Replace Existing ::")

        crv_commands_layout = widgets.add_layout(parent=None, layout_type="V", widget_list=[self.create_crv_button,
                                                                                            self.replace_crv_button])

        main_layout.addWidget(widgets.add_separator())
        main_layout.addLayout(crv_commands_layout)

        # -----------------------------------------------------
        # ------------------ Curve Scale Layout ---------------
        # -----------------------------------------------------
        self.scale_button = widgets.add_button(text=":: Curve Scale ::", width=100, height=35)

        self.scale_field = QtWidgets.QDoubleSpinBox()
        self.scale_field.setMinimumWidth(100)
        self.scale_field.setMinimumHeight(30)
        self.scale_field.setRange(0.1, 10)
        self.scale_field.setValue(0.1)
        self.scale_field.setSingleStep(0.1)
        self.scale_field.setStyleSheet(style.custom_style_sheet["spin_box"])

        scale_up_layout = widgets.add_layout(parent=None,
                                             layout_type="H",
                                             widget_list=[self.scale_button, self.scale_field])

        main_layout.addWidget(widgets.add_separator())
        main_layout.addLayout(scale_up_layout)

        # -----------------------------------------------------
        # ------------------ Curve Color Layout ---------------
        # -----------------------------------------------------
        self.pick_color_label = widgets.add_label(text=":: Pick Color ::",
                                                  background_color=style.color_palette["darkest_gray"].name(),
                                                  color=style.color_palette["lightest_gray"].name(),
                                                  center=True)

        self.colored_button = QtWidgets.QPushButton()
        self.colored_button.setStyleSheet(style.custom_style_sheet["colored_button"])

        colors_label_layout = widgets.add_layout(parent=None,
                                                 layout_type="V",
                                                 widget_list=[self.pick_color_label])

        colors_picker_layout = widgets.add_layout(parent=None,
                                                  layout_type="V",
                                                  widget_list=[self.colored_button])

        main_layout.addWidget(widgets.add_separator())
        main_layout.addLayout(colors_label_layout)
        main_layout.addWidget(widgets.add_separator())
        main_layout.addLayout(colors_picker_layout)

        # -----------------------------------------------------
        # ------------------ Label Mirror Layout --------------
        # -----------------------------------------------------
        self.mirror_label = widgets.add_label(text=":: Mirror Options ::",
                                              background_color=style.color_palette["darkest_gray"].name(),
                                              color=style.color_palette["lightest_gray"].name(),
                                              center=True)

        main_layout.addWidget(widgets.add_separator())
        main_layout.addWidget(self.mirror_label)

        # -----------------------------------------------------
        # ---------------- Search Replace Layout --------------
        # -----------------------------------------------------
        self.search_for_label = widgets.add_label(text=":: Search For ::", width=100, center=False)
        self.search_for_field = widgets.add_line_edit(text="_Rt_", width=150)

        self.replace_with_label = widgets.add_label(text=":: Replace With ::", width=100, center=False)
        self.replace_with_field = widgets.add_line_edit(text="_Lt_", width=150)

        search_for_layout = widgets.add_layout(parent=None, layout_type="H",
                                               widget_list=[self.search_for_label, self.search_for_field])

        replace_with_layout = widgets.add_layout(parent=None, layout_type="H",
                                                 widget_list=[self.replace_with_label, self.replace_with_field])

        main_layout.addWidget(widgets.add_separator())
        main_layout.addLayout(search_for_layout)
        main_layout.addWidget(widgets.add_separator())
        main_layout.addLayout(replace_with_layout)

        # -----------------------------------------------------
        # ---------------- Directions Layout ------------------
        # -----------------------------------------------------
        self.x_label, self.y_label, self.z_label = [widgets.add_label(text=label,
                                                                      background_color=style.color_palette[
                                                                          color].name(),
                                                                      color=style.color_palette["darkest_gray"].name())
                                                    for label, color in
                                                    zip([":: X Axis ::", ":: Y Axis ::", ":: Z Axis ::"],
                                                        ["soft_red", "soft_green", "soft_blue"])
                                                    ]

        self.x_axis_group, self.x_axis_radio_buttons = widgets.add_radio_button_grp(
            radio_button_name_list=["+X", "-X"])
        x_axis_layout = widgets.add_layout(parent=None,
                                           layout_type="H",
                                           widget_list=self.x_axis_radio_buttons)

        self.y_axis_group, self.y_axis_radio_buttons = widgets.add_radio_button_grp(
            radio_button_name_list=["+Y", "-Y"])
        y_axis_layout = widgets.add_layout(parent=None,
                                           layout_type="H",
                                           widget_list=self.y_axis_radio_buttons)

        self.z_axis_group, self.z_axis_radio_buttons = widgets.add_radio_button_grp(
            radio_button_name_list=["+Z", "-Z"])
        z_axis_layout = widgets.add_layout(parent=None,
                                           layout_type="H",
                                           widget_list=self.z_axis_radio_buttons)

        main_layout.addWidget(widgets.add_separator())
        main_layout.addWidget(self.x_label)
        main_layout.addLayout(x_axis_layout)

        main_layout.addWidget(widgets.add_separator())
        main_layout.addWidget(self.y_label)
        main_layout.addLayout(y_axis_layout)

        main_layout.addWidget(widgets.add_separator())
        main_layout.addWidget(self.z_label)
        main_layout.addLayout(z_axis_layout)

        # -----------------------------------------------------
        # ---------------- Build Mirror Layout ----------------
        # -----------------------------------------------------
        self.mirror_button = widgets.add_button(text=":: Mirror ::",
                                                height=40,
                                                width=self.main_width,
                                                background_color=style.color_palette["gray"].name(),
                                                color=style.color_palette["lightest_gray"].name(),
                                                hover_color=style.color_palette["light_gray"].name(),
                                                pressed_color=style.color_palette["dark_gray"].name()
                                                )
        main_layout.addWidget(widgets.add_separator())
        main_layout.addWidget(self.mirror_button)
        main_layout.addWidget(widgets.add_separator())


if __name__ == "__main__":
    try:
        global _main
        _main.close()
        _main.deleteLater()

    except:
        pass
    _main = CurveOptionsGUI()
    _main.show()
