<<<<<<< HEAD
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "omar.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
=======
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
>>>>>>> 681e71f2b08535eb092125611d4fd9451fd83640
