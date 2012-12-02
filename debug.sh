#!/bin/sh
cd ..
python -i -c "import sprint; roomba = sprint.Roomba('/dev/ttyAMA0', 115200);"
cd sprint
