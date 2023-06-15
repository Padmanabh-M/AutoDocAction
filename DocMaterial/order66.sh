#!/bin/bash
cd docs/
printf 'n\n\nDocForFabric\n\nPaddy\n\n1\n\n' | sphinx-quickstart
cd ..
cp ./DocMaterial/index.rst ./DocMaterial/conf.py ./docs
sphinx-apidoc -o docs .
rm docs/conf.rst docs/crawler.rst
cd docs/
make html
