#!/bin/bash

python setup.py bdist_wheel sdist
twine upload dist/wiraconcha-$1-py3-none-any.whl