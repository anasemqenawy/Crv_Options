import importlib
from maya import cmds

try:
    from shiboken2 import wrapInstance
    from PySide2 import QtCore, QtWidgets, QtGui
except ModuleNotFoundError:
    from shiboken6 import wrapInstance
    from PySide6 import QtCore, QtWidgets, QtGui

import crv_options.ui as ui
import crv_options.core as core
import crv_options.widgets as widgets
import crv_options.crv_shapes as crv_shapes

importlib.reload(ui)
importlib.reload(core)
importlib.reload(widgets)
importlib.reload(crv_shapes)

from crv_options.core import *
from crv_options.ui import CurveOptionsGUI


class CurveOptionsMain(CurveOptionsGUI):
    def __init__(self):
        super().__init__()

        self.create_connections()

    def create_connections(self):
        self.create_crv_button.clicked.connect(
            lambda x: crv_shapes.create_replace_shape(ctrl_shape=self.crv_shape_dropdwn.currentText(),
                                                      replace=False,
                                                      create=True))
        self.replace_crv_button.clicked.connect(
            lambda x: crv_shapes.create_replace_shape(ctrl_shape=self.crv_shape_dropdwn.currentText(),
                                                      replace=True,
                                                      create=False))
        self.scale_button.clicked.connect(lambda x: core.scale_shape(scale_value=self.scale_field.value()))

        self.colored_button.clicked.connect(self.change_curve_color)

        self.mirror_button.clicked.connect(self.mirror_selected_curves)

    @core.enable_undo
    def change_curve_color(self):
        curve_color = QtWidgets.QColorDialog.getColor(parent=self)
        if curve_color:
            color_tuple = (curve_color.redF(),
                           curve_color.greenF(),
                           curve_color.blueF())

            [core.colorize(item=item, color_type="rgb", color_rgb=color_tuple) for item in
             cmds.ls(sl=1)]

    def get_attrs_direction(self, button_grp):
        for button in button_grp.buttons():
            if button.isChecked():
                return str(button.text())

    @core.enable_undo
    def mirror_selected_curves(self):
        selected_curves: [str] = cmds.ls(sl=1)
        search_for: str = self.search_for_field.text()
        replace_with: str = self.replace_with_field.text()
        # ------------------------------------------------------------------------------------------------
        for crv in selected_curves:
            replaced_crv: str = crv.replace(search_for, replace_with) \
                if search_for in crv else crv.replace(replace_with, search_for)

            target_crv = replaced_crv if cmds.objExists(replaced_crv) else crv

            x_value: str = self.get_attrs_direction(self.x_axis_group)
            y_value: str = self.get_attrs_direction(self.y_axis_group)
            z_value: str = self.get_attrs_direction(self.z_axis_group)

            # ---------------------------------------------------
            crv_shapes.mirror_along_specific_plane(crv_to_mirror=crv,
                                                   output_mirror_to=target_crv,
                                                   negate_axis=[x_value, y_value, z_value])


if __name__ == "__main__":
    try:
        global _main_
        _main_.close()
        _main_.deleteLater()

    except:
        pass
    _main_ = CurveOptionsMain()
    _main_.show()
