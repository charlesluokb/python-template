#!/usr/bin/env python3

import os
import requests
import json
from typing import Dict, Any

class App:
    def __init__(self, args: Dict[str, Any]):
        self.arguments = args
        self.var_1 = "variable 1"

    def class_method_1(self, arg1: str, arg2: int = 100) -> None:
        """
        :param arg1: argument one
        :param arg2: argument two, default is 100
        :return:
        """
        print(f"arguments: {self.arguments}")
        print(f"Class method 1 called with arg1: {arg1} and arg2: {arg2}")

def main():
    args = {
        "arg1": "example",
        "arg2": 42
    }

    app_instance = App(args)
    app_instance.class_method_1("test", 200)

if __name__ == "__main__":
    exit(main())
