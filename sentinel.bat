@echo off
set SENTINEL_DEBUG=
rem set SENTINEL_DEBUG=1

rem uncomment next line to run sentinel every minute
rem python main.py

rem or program a windows shedule to run sentinel.py each couple of minutes
python bin/sentinel.py
