# uart_serial_plotter

This project provides [pyqtgraph](https://www.pyqtgraph.org/) based applications for real-time plotting and analysis of timeseries data

## Features
- Fast, real-time plotting of time series data
- Plot timeseries data received over UART
- Plot timeseries data read from CSV file
- Dynamically change the serial port being monitored
- Export the plot / scane to PNG, SVG, CSV etc.
- Load previously exported CSV files of plot / scene
- Zoom into parts of the plot, reset the view, export/screenshot select portions of the plot

## Quick Start

Install dependencies and run `main.py`

```console
foo@bar:~$ pip install -r requirements.txt
foo@bar:~$ python main.py
```

![image](https://raw.githubusercontent.com/appliedinnovation/uart_serial_plotter/master/images/demo_02.png?token=ACAPAK2Y4RQ3FMUBJVFKLHLBR5PPM)