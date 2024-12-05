import maya.cmds as cmds


def mirror_along_specific_plane(crv_to_mirror, apply_mirror_to_obj, negate_axis=None):
    if negate_axis is None:
        negate_axis = ["x", "y", "z"]

    cvs = get_curve_shape_info(apply_mirror_to_obj)  # type:int
    coords = get_curve_shape_coords(crv_to_mirror)  # type:[[float]]

    # For Mirrored/Non-Mirrored Transforms SET The Negation To what Fit Axis right
    for index in range(cvs):
        x = coords[index][0] if negate_axis[0] == "x" else -coords[index][0]  # type:float
        y = coords[index][1] if negate_axis[1] == "y" else -coords[index][1]  # type:float
        z = coords[index][2] if negate_axis[2] == "z" else -coords[index][2]  # type:float

        cmds.xform("{}.cv[{}]".format(apply_mirror_to_obj, index), t=[x, y, z])


def get_direction_x():
    radio_button_value = cmds.radioButtonGrp("X_Direction", query=True, sl=1, la2=1)
    x_axis_direction = "x" if radio_button_value == 1 else "-x"
    return x_axis_direction


def get_direction_y():
    radio_button_value = cmds.radioButtonGrp("Y_Direction", query=True, sl=1, la2=1)
    y_axis_direction = "y" if radio_button_value == 1 else "-y"
    return y_axis_direction


def get_direction_z():
    radio_button_value = cmds.radioButtonGrp("Z_Direction", query=True, sl=1, la2=1)
    z_axis_direction = "z" if radio_button_value == 1 else "-z"
    return z_axis_direction


def mirror_selected_curves():
    selected_curves = cmds.ls(sl=1)  # type:[str]
    search_for = cmds.textField("search_text", query=True, text=True)
    replace_with = cmds.textField("replace_text", query=True, text=True)
    # ------------------------------------------------------------------------------------------------
    for crv in selected_curves:
        target_crv = crv.replace(search_for, replace_with) if \
            (search_for in crv) else crv.replace(replace_with, search_for)  # type:str

        x = get_direction_x()
        y = get_direction_y()
        z = get_direction_z()
        # ---------------------------------------------------
        mirror_along_specific_plane(crv_to_mirror=crv,
                                    apply_mirror_to_obj=target_crv,
                                    negate_axis=[x, y, z])
        # ---------------------------------------------------


"""
------------------------------------------------------------------------------------------------
Section End for Ctrl Mirror Direction 
------------------------------------------------------------------------------------------------
"""


def curve_options_gui():
    ctrls_window = "curve_multi_options_gui"

    if cmds.window(ctrls_window, exists=True):
        cmds.deleteUI(ctrls_window, window=True)

    ctrl_window = cmds.window(ctrls_window, title="RigTopia:Curve Multiple Options", width=200, tlb=1, s=1)
    cmds.showWindow(ctrl_window)
    # ------------------------------------------------------------------------------------------------
    cmds.columnLayout(adj=1)
    cmds.text(l="Curve Mirror Options", h=15, w=200, bgc=gui_colors["black"])
    cmds.setParent("..")
    cmds.separator(st="shelf", h=3)
    cmds.setParent("..")

    cmds.rowColumnLayout(nc=2)
    cmds.text(l="Search", h=25, w=50, bgc=gui_colors["orange"])
    cmds.textField("search_text", placeholderText="Search For", text="_Rt_", h=25, w=150)
    cmds.setParent("..")
    cmds.separator(st="shelf", h=2)
    cmds.setParent("..")
    cmds.rowColumnLayout(nc=2)
    cmds.text(l="Replace", h=25, w=50, bgc=gui_colors["orange"])
    cmds.textField("replace_text", placeholderText="Replace With", text="_Lt_", h=25, w=150)

    cmds.setParent("..")
    cmds.separator(st="shelf", h=2)
    cmds.setParent("..")

    cmds.columnLayout()
    cmds.text(l="X Direction", h=20, w=200, bgc=gui_colors["red"])
    cmds.radioButtonGrp("X_Direction", nrb=2, sl=1, labelArray2=["+X", "-X"])
    cmds.setParent("..")
    cmds.separator(st="shelf", h=2)
    cmds.setParent("..")

    cmds.columnLayout()
    cmds.text(l="Y Direction", h=20, w=200, bgc=gui_colors["green"])
    cmds.radioButtonGrp("Y_Direction", nrb=2, sl=1, labelArray2=["+Y", "-Y"])
    cmds.setParent("..")
    cmds.separator(st="shelf", h=2)
    cmds.setParent("..")

    cmds.columnLayout()
    cmds.text(l="Z Direction", h=20, w=200, bgc=gui_colors["white_blue"])
    cmds.radioButtonGrp("Z_Direction", nrb=2, sl=1, labelArray2=["+Z", "-Z"])
    cmds.setParent("..")
    cmds.separator(st="shelf", h=2)
    cmds.setParent("..")

    cmds.columnLayout(adj=1)
    cmds.button(l="Mirror Shape", c=lambda x: mirror_selected_curves(), h=30, w=200, bgc=gui_colors["orange"])
    # ------------------------------------------------------------------------------------------------
    cmds.setParent("..")
    cmds.separator(st="shelf", h=10)
    cmds.setParent("..")


if __name__ == '__main__':
    curve_options_gui()
