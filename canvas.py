from PySide import QtGui, QtCore
from draw_line import DrawLine


class Canvas(QtGui.QWidget):

    def __init__(self):
        super(Canvas, self).__init__()
        self.currentImg = None
        self.buf = None  # buffer is what repaint use
        self.paintTool = DrawLine()
        self.current_location = QtCore.QPoint(20, 40)
        self.initUI()
        self.repaint()

    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)
        self.currentImg = QtGui.QPixmap('lenna.tif')
        self.buf = self.currentImg.copy()

        self.setLayout(hbox)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Lenna')

    def mousePressEvent(self, e):
        self.paintTool.begin(self.buf, e.pos())

    def mouseMoveEvent(self, e):
        if self.paintTool.isBegin:
            self.buf = self.paintTool.process(e.pos())
            self.repaint()

    def mouseReleaseEvent(self, e):
        self.paintTool.end()
        # always separate buffer and currentImg
        self.currentImg = self.buf.copy()
        self.repaint()

    def paintEvent(self, e):
        if self.buf is not None:
            p = QtGui.QPainter(self)
            p.drawPixmap(self.buf.rect(), self.buf, self.buf.rect())
