##
# @file ecu.py
# @brief Exception.
# @details None.
# @author Calm
# @date 2023-05-13
# @version v1.0.0
# @copyright Calm
#

class DatLenErr(Exception):
    def __init__(self):
        super().__init__("DatLenErr")

class DatFmtErr(Exception):
    def __init__(self):
        super().__init__("DatFmtErr")
