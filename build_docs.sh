#!/bin/bash

rm -r ./docs/*
pdoc --force --html --output-dir ./docs xenodiffusionscope
mv ./docs/xenodiffusionscope/* ./docs/
rm -r ./docs/xenodiffusionscope

echo "Docs built with pdoc3!"