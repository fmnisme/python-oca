# -*- coding: UTF-8 -*-


class OpenNebulaException(Exception):
    def __init__(self, data, return_code):
        self.return_code = return_code
        super(OpenNebulaException, self).__init__(data)
