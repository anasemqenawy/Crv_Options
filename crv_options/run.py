import importlib

import crv_options.main as main

importlib.reload(main)

from crv_options.main import CurveOptionsMain

if __name__ == "__main__":
    try:
        global _main_
        _main_.close()
        _main_.deleteLater()

    except:
        pass
    _main_ = CurveOptionsMain()
    _main_.show()
