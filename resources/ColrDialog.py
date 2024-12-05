class ColorPicker(QColorDialog):
    def __init__(self, *args):
        super(ColorPicker, self).__init__(*args)
        self.setOptions(QColorDialog.NoButtons | QColorDialog.DontUseNativeDialog)

        widgets = self.findChildren(QWidget)

        mainLayout = self.layout()
        hboxLayout = nullLayout(QHBoxLayout, None, 0)
        mainLayout.insertLayout(0, hboxLayout)
        vboxLayout = nullLayout(QVBoxLayout, None, 0)
        hboxLayout.addLayout(vboxLayout)
        vboxLayout.addWidget(widgets[9])
        vboxLayout.addWidget(widgets[2])
        hboxLayout.addWidget(widgets[7])

        for i in [0, 1, 3, 4, 5, 6]:
            widgets[i].hide()
