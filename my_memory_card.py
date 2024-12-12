#v1.1
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def check_answer():
    if answers[0].isChecked():
        print('Correcto')
        window.score += 1
        window.total += 1
        label_a.setText('Respuesta correcta')
    else:
        print('Incorrecto')
        window.total += 1

        label_a.setText('Respuesta incorrecta')
    print('Estadisticas')
    print('- Preguntas totales', window.total)
    print('- Preguntas correctas', window.score)
    print('Calificacion:', window.score/window.total*100, '%')

def ask(q):
    print('pregunta:', q.question)

    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label_1.setText(q.question)
    label_b.setText(q.question)

def show_result():
    print('click ', button_1.text())
    if button_1.text()=='Responder':
        RadioGroupBox.hide()
        AnsGroupBox.show()

        button_1.setText('Siguiente Pregunta')
        check_answer()
        label_b.setText(answers[0].text())

    elif button_1.text()=='Siguiente Pregunta':
        print(' Siguiente Pregunta')

        next_question()
        RadioGroupBox.show()
        AnsGroupBox.hide()

        button_1.setText('Responder')
        #check_answer()
        
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)

def next_question():
    window.cur_question+=1
    print("",window.cur_question)

    if window.cur_question==len(question_list):
        print("nuevo ciclo")
        window.cur_question=0

    if window.cur_question==0:
        shuffle(question_list)

    ask(question_list[window.cur_question])

app = QApplication([])

window = QWidget()
window.setWindowTitle('Tarjeta de memoria')

layout_V1 = QVBoxLayout()

label_1 = QLabel('¡La pregunta mas dificil del mundo!')

layout_H1 = QHBoxLayout()
layout_H1.addWidget(label_1)

layout_V1.addLayout(layout_H1)


layout_H2 = QHBoxLayout()
RadioGroupBox = QGroupBox('Opciones de respuesta')

rbtn_1 = QRadioButton('Opción 1')
rbtn_2 = QRadioButton('Opción 2')
rbtn_3 = QRadioButton('Opción 3')
rbtn_4 = QRadioButton('Opción 4')

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
layout_H2.addWidget(RadioGroupBox)

AnsGroupBox = QGroupBox('Resultado de prueba')

label_a = QLabel('Verdadero/Falso')
label_b = QLabel('Aquí esta la respuesta')

layout_ans4 = QVBoxLayout()


layout_ans4.addWidget(label_a,alignment=Qt.AlignLeft,stretch=1)
layout_ans4.addWidget(label_b,alignment=Qt.AlignHCenter,stretch=4)


AnsGroupBox.setLayout(layout_ans4)


layout_H2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_V1.addLayout(layout_H2)


button_1 = QPushButton('Responder')
button_1.clicked.connect(show_result)

layout_H3 = QHBoxLayout()
layout_H3.addWidget(button_1)
 
layout_V1.addLayout(layout_H3)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

question_list = []

question_list.append(Question('Como trabajar en un McDonals', 'Chambeando en McDonals', 'No chambeando en McDonals', 'Chambeando en Burguer king', 'No chambeando'))
question_list.append(Question('Como dejar de ser pobre', 'Dejando de ser pobre', 'Seguir siendo pobre', 'Ser mas pobre', 'Ser un poco menos pobre'))
question_list.append(Question('Como Chambear', 'Chambeando', 'No chambeando', 'Buscando chamba', 'Cobrando plata :v'))
question_list.append(Question('Como poner pare en el foltinaiti', 'Poniendo pare', 'Poniendo rampa', 'Poniendo triangulo', 'No poner pare :v'))
question_list.append(Question('Como hacer meguin?', 'Haciendo meguin', 'No haciendo meguin', 'Pelando papas', 'Volviendo tu pais en una potencia mundial'))
question_list.append(Question('Como salir de latam 🤑', 'Saliendo de latam', 'Quedandose en latam', 'llendo a barrancabermeja', 'Durmiendo :v'))
question_list.append(Question('Como comer chicharrón', 'Comiendo chicharron', 'Comiendo tamal', 'No comiendo chicharron', 'Comiendo camaron'))
question_list.append(Question('Como dejar 7 a 0 :v', 'Dejando 7 a 0', 'Dejando 6 a 0', 'No dejando 7 a 0', 'Dejando 0 a 0'))
question_list.append(Question('Como hacer que copia y pega deje de ser manco', 'Dejando de ser manco', 'Dejando que lo deje 7 a 0', 'Poniendo pare cuando respira', 'Comprando tamal'))
question_list.append(Question('Como ser feliz', 'Siendo feliz', 'No siendo feliz', 'Siendo el bicho', 'Perdiendo clasificatoria'))

window.cur_question=-1

window.score = 0
window.total = 0
next_question()

next_question()

window.setLayout(layout_V1)

window.show()
app.exec() 
