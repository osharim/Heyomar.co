#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "omar.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codlr.settings")
>>>>>>> 96e61d3632b168c9e3ce901fa7154a12e754c9a7

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
