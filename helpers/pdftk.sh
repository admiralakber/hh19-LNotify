#!/bin/bash

sudo docker run -v $(pwd):/workdir -w /workdir --rm -it agileek/pdftk $@