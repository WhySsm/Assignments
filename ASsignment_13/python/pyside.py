from PySide6.QtWidgets import*
from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtUiTools import QUiLoader



class Sajjad(QMainWindow):
    def __init__(self) :
        super().__init__()
        loader = QUiLoader()
        self.my_ui=loader.load("mmain.ui")
        #self.my_ui.output.setStyleSheet("background-image: url('bg.jpg');")
        self.my_ui.show()
        self.my_ui.zerobutton.clicked.connect(self.press_0)
        self.my_ui.onebutton.clicked.connect(self.press_1)
        self.my_ui.twobutton.clicked.connect(self.press_2)
        self.my_ui.threebutton.clicked.connect(self.press_3)
        self.my_ui.fourbutton.clicked.connect(self.press_4)
        self.my_ui.fivebutton.clicked.connect(self.press_5)
        self.my_ui.sixbutton.clicked.connect(self.press_6)
        self.my_ui.sevenbutton.clicked.connect(self.press_7)
        self.my_ui.eightbutton.clicked.connect(self.press_8)
        self.my_ui.ninebutton.clicked.connect(self.press_9)
        self.my_ui.addbutton.clicked.connect(self.press_add)
        self.my_ui.minusbutton.clicked.connect(self.press_minus)
        self.my_ui.multiplybutton.clicked.connect(self.press_mult)
        self.my_ui.dividebutton.clicked.connect(self.press_divide)
        self.my_ui.equalbutton.clicked.connect(self.press_equal)
        self.my_ui.cbutton.clicked.connect(self.press_clear)
    def press_0(self):
        if self.my_ui.output2.text()=='0':
            pass
        else:
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"0"}')

    def press_1(self):
        if self.my_ui.output2.text()=='0':
            self.my_ui.output2.setText("")
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"1"}')
        else:
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"1"}')
    
    def press_2(self):
        if self.my_ui.output2.text()=='0':
            self.my_ui.output2.setText("")
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"2"}')
        else:
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"2"}')
         


    def press_3(self):
        
        if self.my_ui.output2.text()=='0':
            self.my_ui.output2.setText("")
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"3"}')
        else:
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"3"}')



    def press_4(self):
        
        if self.my_ui.output2.text()=='0':
            self.my_ui.output2.setText("")
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"4"}')
        else:
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"4"}')


    def press_5(self):
        
        if self.my_ui.output2.text()=='0':
            self.my_ui.output2.setText("")
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"5"}')
        else:
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"5"}')


    def press_6(self):
        
        if self.my_ui.output2.text()=='0':
            self.my_ui.output2.setText("")
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"6"}')
        else:
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"6"}')


    def press_7(self):
        
        if self.my_ui.output2.text()=='0':
            self.my_ui.output2.setText("")
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"7"}')
        else:
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"7"}')

    def press_8(self):
        
        if self.my_ui.output2.text()=='0':
            self.my_ui.output2.setText("")
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"8"}')
        else:
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"8"}')

    def press_9(self):
        
        if self.my_ui.output2.text()=='0':
            self.my_ui.output2.setText("")
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"9"}')
        else:
            self.my_ui.output2.setText(f'{self.my_ui.output2.text()}{"9"}')

    def press_add(self):
        #x=['+','-','÷','×']
        if self.my_ui.output2.text()!='0':
            st=self.my_ui.output2.text()
            self.my_ui.output2.setText("")
            if self.my_ui.output.text()=='':
                self.my_ui.output.setText(f'{str(st)}{"+"}')
                st=self.my_ui.output.text()
            elif self.my_ui.output.text()!='0' and ('+'  in self.my_ui.output.text() or '-'  in self.my_ui.output.text() or
             '÷'  in self.my_ui.output.text() or '×'  in self.my_ui.output.text()) and '='not in self.my_ui.output.text() :
                st=self.my_ui.output.text()+st
                if '÷'  in st:
                    st=st.replace('÷','/')
                if'×' in st:
                    st=st.replace('×','*')
                result=eval(st)
                self.my_ui.output.setText(f'{str(result)}{"+"}')
            elif '=' in self.my_ui.output.text():
                self.my_ui.output.setText(f'{str(st)}{"+"}')
        #'-'  not in self.my_ui.output.text() and '÷'  not in self.my_ui.output.text() and '×'  not in self.my_ui.output.text()):
        #    self.my_ui.output.setText(f'{self.my_ui.output.text()}{"+"}')
        #elif self.my_ui.output.text()!='0' and ('+'  in self.my_ui.output.text() or 
        #'-'  in self.my_ui.output.text() or '÷'  in self.my_ui.output.text() or '×'  in self.my_ui.output.text()):
        #    st= self.my_ui.output.text()
        #    if '÷'  in st:
        #        st=st.replace('÷','/')
        #    if'×' in st:
        #        st=st.replace('×','*')
        #    result=eval(st)
        #    self.my_ui.output.setText(f'{str(result)}{"+"}')

    def press_minus(self):
        if self.my_ui.output2.text()!='0':
            st=self.my_ui.output2.text()
            self.my_ui.output2.setText("")
            if self.my_ui.output.text()=='':
                self.my_ui.output.setText(f'{str(st)}{"-"}')
                st=self.my_ui.output.text()
            elif self.my_ui.output.text()!='0' and ('+'  in self.my_ui.output.text() or '-'  in self.my_ui.output.text() or
             '÷'  in self.my_ui.output.text() or '×'  in self.my_ui.output.text())and '=' not in self.my_ui.output.text():
                st=self.my_ui.output.text()+st
                if '÷'  in st:
                    st=st.replace('÷','/')
                if'×' in st:
                    st=st.replace('×','*')
                result=eval(st)
                self.my_ui.output.setText(f'{str(result)}{"-"}')
            elif '=' in self.my_ui.output.text():
                self.my_ui.output.setText(f'{str(st)}{"+"}')
        #if self.my_ui.output.text()!='0'  and ('+'  not in self.my_ui.output.text() and 
        #'-'  not in self.my_ui.output.text() and '÷'  not in self.my_ui.output.text() and '×'  not in self.my_ui.output.text()):
        #    self.my_ui.output.setText(f'{self.my_ui.output.text()}{"-"}')
        #elif self.my_ui.output.text()!='0' and ('+'  in self.my_ui.output.text() or 
        #'-'  in self.my_ui.output.text() or '÷'  in self.my_ui.output.text() or '×'  in self.my_ui.output.text()):
        #    st= self.my_ui.output.text()
        #    if '÷'  in st:
        #        st=st.replace('÷','/')
        #    if'×' in st:
        #        st=st.replace('×','*')
        #    result=eval(st)
        #    self.my_ui.output.setText(f'{str(result)}{"-"}')
    def press_mult(self):
        if self.my_ui.output2.text()!='0':
            st=self.my_ui.output2.text()
            self.my_ui.output2.setText("")
            if self.my_ui.output.text()=='':
                self.my_ui.output.setText(f'{str(st)}{"×"}')
                st=self.my_ui.output.text()
            elif self.my_ui.output.text()!='0' and ('+'  in self.my_ui.output.text() or '-'  in self.my_ui.output.text() or
             '÷'  in self.my_ui.output.text() or '×'  in self.my_ui.output.text())and '=' not in self.my_ui.output.text():
                st=self.my_ui.output.text()+st
                if '÷'  in st:
                    st=st.replace('÷','/')
                if'×' in st:
                    st=st.replace('×','*')
                result=eval(st)
                self.my_ui.output.setText(f'{str(result)}{"×"}')
            elif '=' in self.my_ui.output.text():
                self.my_ui.output.setText(f'{str(st)}{"+"}')
       #if self.my_ui.output.text()!='0'  and ('+'  not in self.my_ui.output.text() and 
        #'-'  not in self.my_ui.output.text() and '÷'  not in self.my_ui.output.text() and '×'  not in self.my_ui.output.text()):
        #    self.my_ui.output.setText(f'{self.my_ui.output.text()}{"×"}')
       #elif self.my_ui.output.text()!='0' and ('+'  in self.my_ui.output.text() or 
       # '-'  in self.my_ui.output.text() or '÷'  in self.my_ui.output.text() or '×'  in self.my_ui.output.text()):
        #    st= self.my_ui.output.text()
       #     if '÷'  in st:
       #         st=st.replace('÷','/')
       #     if'×' in st:
       #         st=st.replace('×','*')
        #    result=eval(st)
        #    self.my_ui.output.setText(f'{str(result)}{"×"}')

    def press_divide(self):
        if self.my_ui.output2.text()!='0':
            st=self.my_ui.output2.text()
            self.my_ui.output2.setText("")
            if self.my_ui.output.text()=='':
                self.my_ui.output.setText(f'{str(st)}{"÷"}')
                st=self.my_ui.output.text()
            elif self.my_ui.output.text()!='0' and ('+'  in self.my_ui.output.text() or '-'  in self.my_ui.output.text() or
             '÷'  in self.my_ui.output.text() or '×'  in self.my_ui.output.text())and '=' not in self.my_ui.output.text():
                st=self.my_ui.output.text()+st
                if '÷'  in st:
                    st=st.replace('÷','/')
                if'×' in st:
                    st=st.replace('×','*')
                result=eval(st)
                self.my_ui.output.setText(f'{str(result)}{"÷"}')
            elif '=' in self.my_ui.output.text():
                self.my_ui.output.setText(f'{str(st)}{"+"}')

        #if self.my_ui.output.text()!='0'  and ('+'  not in self.my_ui.output.text() and 
        #'-'  not in self.my_ui.output.text() and '÷'  not in self.my_ui.output.text() and '×'  not in self.my_ui.output.text()):
        #    self.my_ui.output.setText(f'{self.my_ui.output.text()}{"÷"}')
        #elif self.my_ui.output.text()!='0' and ('+'  in self.my_ui.output.text() or 
        #'-'  in self.my_ui.output.text() or '÷'  in self.my_ui.output.text() or '×'  in self.my_ui.output.text()):
        #    st= self.my_ui.output.text()
        #    if '÷'  in st:
        #        st=st.replace('÷','/')
        #    if'×' in st:
        #       st=st.replace('×','*')
        #    result=eval(st)
        #    self.my_ui.output.setText(f'{str(result)}{"÷"}')
    
    def press_equal(self):
        if self.my_ui.output2.text()!='0':
            st=self.my_ui.output2.text()
            if self.my_ui.output.text()!='0' and ('+'  in self.my_ui.output.text() or '-'  in self.my_ui.output.text() or
             '÷'  in self.my_ui.output.text() or '×'  in self.my_ui.output.text()):
                st=self.my_ui.output.text()+st
                if '÷'  in st:
                    st=st.replace('÷','/')
                if'×' in st:
                    st=st.replace('×','*')
                result=eval(st)
                if '/'  in st:
                    st=st.replace('/','÷')
                self.my_ui.output.setText(f'{str(st)}{"="}')
                self.my_ui.output2.setText(str(result))
       # st= self.my_ui.output.text()
        #if '×'  in st:
       #     st=st.replace('×','*')
       # if '÷'  in st:
        #        st=st.replace('÷','/')    
       # result=eval(st)
        #self.my_ui.output.setText(str(result))
    
    def press_clear(self):
         self.my_ui.output2.setText("0")            
         self.my_ui.output.setText("") 
app= QApplication([])
my_window=Sajjad()
app.exec()



