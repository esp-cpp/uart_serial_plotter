import pyqtgraph as pg


class Plot(object):
    def __init__(self, header=None, data=None):

        self.traces = dict()
        self.data = dict()
        self.trace_names = []
        self.canvas = pg.PlotWidget()
        self.plot = None
        self.canvas.showGrid(x=True, y=True, alpha=0.4)
        self.canvas.getAxis("left").setTextPen("w")
        self.canvas.getAxis("bottom").setTextPen("w")
        self.plot_item = self.canvas.getPlotItem()

        if header:
            self.set_header(header)
        if data:
            self.set_data(data)

        self.legend = self.canvas.addLegend()

    def get_pen(self, index):
        return pg.mkPen(index, len(self.trace_names))

    def set_header(self, header_names):
        self.trace_names = header_names
        # the first trace is the x axis, so take it out and use it to set the x
        # axis label
        self.plot_item.setLabel("bottom", text=self.trace_names[0])
        for i, name in enumerate(self.trace_names[1:]):
            if name in self.traces:
                pass
            else:
                self.traces[name] = self.canvas.plot(
                    pen=self.get_pen(i),
                    name=name,
                )

    def update_data(self, data):
        for name in self.trace_names:
            # initialize the data for this trace
            if name not in self.data:
                self.data[name] = {"x": [], "y": []}

        for row in data:
            time = row[0]
            # skip the first value (since we assume it is time)
            for i in range(1, len(self.trace_names)):
                self.data[self.trace_names[i]]["x"].append(time)
                self.data[self.trace_names[i]]["y"].append(row[i])

        # now actually plot the data
        for i, name in enumerate(self.trace_names[1:]):
            self.set_plotdata(name, self.data[name]["x"], self.data[name]["y"])

    def update_raw(self, data):
        for name in self.trace_names:
            # initialize the data for this trace
            if name not in self.data:
                self.data[name] = {"x": [], "y": []}

        for row in data:
            print("row len: {}".format(len(row)))
            for i in range(1, len(self.trace_names)):
                print("updating data for {} - {}".format(i, self.trace_names[i]))
                self.data[self.trace_names[i]]["x"].append(row[i*2])
                self.data[self.trace_names[i]]["y"].append(row[i*2+1])

        # now actually plot the data
        for i, name in enumerate(self.trace_names[1:]):
            self.set_plotdata(name, self.data[name]["x"], self.data[name]["y"])

    def set_plotdata(self, name, data_x, data_y):
        if name in self.traces:
            self.traces[name].setData(data_x, data_y)
        else:
            self.traces[name] = self.canvas.plot(
                pen=self.get_pen(len(self.trace_names)),
                name=name,
            )
