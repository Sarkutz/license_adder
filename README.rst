
#############
License Adder
#############

*Add the specified license to the top of every file*.


*****
Usage
*****

- Place the license, that you want to insert in each file, in a file named
  :file:`lic.txt` in the current folder.

- Run :file:`add_license.py` providing the name of the file, in which you want
  to add the license, at the argument. ::

     python license-adder/license_adder/add_license.py test/resource/test.py

  If you want to modify multiple files, use the :command:`find` command. ::

     cat test/resource/test.*

     find . -type d \( -path '*license_adder*' -o -path '*log*' -o -path '*.git*' \) -prune -o  \
         -type f \( -name '*.py' -o -name '*.scala' \) -exec python license_adder/add_license.py '{}' \;

     cat test/resource/test.*

