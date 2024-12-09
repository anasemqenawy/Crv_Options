from maya import cmds


def enable_undo(function, _name=None):
    """
    returns Decorator That Make The Process Undoable in one undo step
    """

    def undo_func(*args, **kwargs):
        # Open Chunk
        cmds.undoInfo(openChunk=True, chunkName=_name)

        result = function(*args, **kwargs)

        # Close Chunk
        cmds.undoInfo(closeChunk=True)

        return result

    return undo_func


def colorize(item: str,
             color_index: int = 0,
             color_type: str = "index",
             color_rgb: tuple = (0, 0, 0)):
    #
    shapes = cmds.listRelatives(item, shapes=1)

    if color_type == "index":
        cmds.setAttr(f"{item}.overrideEnabled", 1)
        [cmds.setAttr(f"{shape}.overrideEnabled", 1) for shape in shapes]
        cmds.setAttr(f"{item}.overrideColor", color_index)
        [cmds.setAttr(f"{shape}.overrideColor", color_index) for shape in shapes]

    else:
        cmds.setAttr(f"{item}.overrideEnabled", 1)
        [cmds.setAttr(f"{shape}.overrideEnabled", 1) for shape in shapes]
        cmds.setAttr(f"{item}.overrideRGBColors", 1)
        [cmds.setAttr(f"{shape}.overrideRGBColors", 1) for shape in shapes]
        cmds.setAttr(f"{item}.overrideColorRGB",
                     color_rgb[0],
                     color_rgb[1],
                     color_rgb[2])
        [cmds.setAttr(f"{shape}.overrideColorRGB",
                      color_rgb[0],
                      color_rgb[1],
                      color_rgb[2]) for shape in shapes]

    cmds.select(d=1)


@enable_undo
def scale_shape(scale_value):
    # Get the selected objects
    sel = cmds.ls(sl=True)

    for item in sel:
        # List shapes under the selected item
        shapes = cmds.listRelatives(item, shapes=True)

        if shapes:
            for shape in shapes:
                # Select CVs of the shape and apply scale
                cmds.select(f"{shape}.cv[*]", r=True)
                cmds.scale(scale_value, scale_value, scale_value, r=True)

    # Reselect the original selection
    cmds.select(sel)


def get_curve_shape_info(curve):
    spans: int = cmds.getAttr("{}.spans".format(curve))
    degrees: int = cmds.getAttr("{}.degree".format(curve))
    cvs: int = spans + degrees

    return cvs


def get_curve_points_cords(curve):
    points_positions: [[float]] = []
    cvs: int = get_curve_shape_info(curve)

    for index in range(cvs):
        cv_position: [float] = cmds.xform(f"{curve}.cv[{index}]",
                                          q=1, t=1, worldSpaceDistance=1, a=1)
        points_positions.append(cv_position)

    return points_positions
