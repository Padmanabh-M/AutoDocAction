#!/bin/bash
cd docs/
printf 'n\n\nDocForFabric\n\nPaddy\n\n1\n\n' | sphinx-quickstart
cd ..
cp ./index.rst ./conf.py ./docs
sphinx-apidoc -o docs .
rm docs/conf.rst
cd docs/
make html
