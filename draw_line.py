from PySide import QtCore, QtGui


class DrawLine(QtCore.QObject):

    def __init__(self):
        super(DrawLine, self)
        self.drawPen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        self.drawPen.setWidth(1)

        self.startPoint = None

        self.target = None
        self.buf = None
        self.bufferPainter = QtGui.QPainter()

        self.isBegin = False

    def begin(self, dst, newPoint):
        self.isBegin = True
        self.target = dst
        if self.startPoint is None:
            self.startPoint = newPoint

    def process(self, newPoint):
        if not self.isBegin:
            return

        # end the painter and reset the target
        if self.bufferPainter.isActive():
            self.bufferPainter.end()
        self.buf = self.target.copy()

        self.bufferPainter.begin(self.buf)
        self.bufferPainter.setPen(self.drawPen)
        self.bufferPainter.drawLine(self.startPoint, newPoint)
        return self.buf

    def end(self):
        if self.bufferPainter.isActive():
            self.bufferPainter.end()
        self.startPoint = None
        self.target = None
        self.buf = None
        self.isBegin = False
