from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

# Database setup
MyBookstore = sqlite3.connect("bookstore.db")
cursbook = MyBookstore.cursor()
cursbook.execute('''
CREATE TABLE IF NOT EXISTS books(
    QUANTITY REAL,
    TITLE TEXT,
    AUTHOR TEXT,
    PRICE REAL
);''')

cursbook.execute('''
INSERT INTO books(QUANTITY, TITLE, AUTHOR, PRICE) VALUES 
(20, "think python", "a dowrry", 450),
(10, "java", "oak", 500),
(30, "c", "pops", 430);''')

MyBookstore.commit()
MyBookstore.close()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(615, 420)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 90, 101, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 200, 91, 31))
        self.label_2.setObjectName("label_2")
        self.bookname = QtWidgets.QLineEdit(Form)
        self.bookname.setGeometry(QtCore.QRect(170, 100, 151, 31))
        self.bookname.setObjectName("bookname")
        self.quantity = QtWidgets.QLineEdit(Form)
        self.quantity.setGeometry(QtCore.QRect(170, 200, 151, 31))
        self.quantity.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.quantity.setObjectName("quantity")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 260, 55, 16))
        self.label_4.setObjectName("label_4")
        self.findprice = QtWidgets.QPushButton(Form)
        self.findprice.setGeometry(QtCore.QRect(340, 100, 101, 28))
        self.findprice.setObjectName("findprice")
        self.findtotal = QtWidgets.QPushButton(Form)
        self.findtotal.setGeometry(QtCore.QRect(340, 200, 93, 28))
        self.findtotal.setObjectName("findtotal")
        self.total = QtWidgets.QLabel(Form)
        self.total.setGeometry(QtCore.QRect(160, 260, 55, 16))
        self.total.setObjectName("total")
        self.bookprice = QtWidgets.QLabel(Form)
        self.bookprice.setGeometry(QtCore.QRect(150, 140, 55, 16))
        self.bookprice.setObjectName("bookprice")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(90, 170, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Form)
        
        # Connect buttons to functions
        self.findprice.clicked.connect(self.find_price)
        self.findtotal.clicked.connect(self.calculate_total)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Book Name:"))
        self.label_2.setText(_translate("Form", "Quantity:"))
        self.bookname.setText(_translate("Form", ""))
        self.quantity.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "Price:"))
        self.label_4.setText(_translate("Form", "Total:"))
        self.findprice.setText(_translate("Form", "Find Price"))
        self.findtotal.setText(_translate("Form", "Find Total"))
        self.total.setText(_translate("Form", "rs. 0"))
        self.bookprice.setText(_translate("Form", "rs. 0"))
    
    def find_price(self):
        # Get the book name from the input field
        book_name = self.bookname.text()
        MyBookstore = sqlite3.connect("bookstore.db")
        cursbook = MyBookstore.cursor()
        
        cursbook.execute('SELECT * FROM books WHERE TITLE = ?;', (book_name,))
        record = cursbook.fetchone()
        
        MyBookstore.close()
        
        if record:
            price = int(record[3])
            self.bookprice.setText(f"rs. {price}")
        else:
            self.bookprice.setText("rs. 0")

    def calculate_total(self):
        # Get the book price from the label
        price_text = self.bookprice.text().replace("rs. ", "")
        
        try:
            price = int(price_text)
        except ValueError:
            self.total.setText("Invalid Price")
            return
        
        # Get the quantity from the input field
        try:
            quantity = int(self.quantity.text())
        except ValueError:
            self.total.setText("Invalid Quantity")
            return
        
        # Calculate the total
        total = price * quantity
        
        # Update the total label
        self.total.setText(f"rs. {total}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
