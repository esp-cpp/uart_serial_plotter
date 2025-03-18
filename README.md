# uart_serial_plotter

This project provides [pyqtgraph](https://www.pyqtgraph.org/) based applications for real-time plotting and analysis of timeseries data

## Features
- Fast, real-time plotting of time series data
- Plot timeseries data received over UART
- Plot timeseries data read from CSV file
- Dynamically change the serial port being monitored
- Detect new USB devices connected to system and automatically update available serial ports
  - Currently only implemented for Windows
- Export the plot / scane to PNG, SVG, CSV etc.
- Load previously exported CSV files of plot / scene
- Zoom into parts of the plot, reset the view, export/screenshot select portions of the plot
- Reset the connected device using DTR/RTS hardware flow control
  - Tested on ESP32

## Setup

``` console
brew install qt5
brew install pyqt5
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Creating an Installer

``` console
source env/bin/activate
python -m pyinstaller --clean src/uart_serial_plotter.spec 
```

## Quick Start

```console
source env/bin/activate
python src/main.py
```


## Notes:

* For M1 Macs, you can either run the MacOS release or, if you are developing / would like to run source, you may need to follow the instructions here to use a python environment within rosetta: https://stackoverflow.com/questions/65901162/how-can-i-run-pyqt5-on-my-mac-with-m1chip
* If you have issues, maybe look a [this stackoverflow](https://stackoverflow.com/questions/70961915/error-while-installing-pytq5-with-pip-preparing-metadata-pyproject-toml-did-n)
