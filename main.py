#1. Survived — обозначает, выжил данный пассажир или нет (0 для умерших, 1 для выживших);
#2. Pclass — класс пассажира (1 — высший, 2 — средний, 3 — низший);
#3. Name — имя;
#4. Sex — пол;
#5. Age — возраст;
#6. SibSp — количество братьев, сестер, сводных братьев, сводных сестер, супругов на борту
#титаника;
#7. Parch — количество родителей, детей (в том числе приемных) на борту титаника;
#8. Ticket — номер билета;
#9. Fare — плата за проезд;
#10. Cabin — каюта;
#11. Embarked — порт посадки (C — Шербур; Q — Квинстаун; S — Саутгемптон).
import matplotlib.pyplot as plt
import streamlit as st

with (open('data.csv','r') as file):
  a_0 = 0
  a_1 = 0
  b_0 = 0
  b_1 = 0
  c_0 = 0
  c_1 = 0
  for lines in file:
      data = lines.split(',')
      if data[1] == '1' and data[12].strip() == 'C':
          a_1 += 1
      elif data[1] == '0' and data[12].strip() == 'C':
          a_0 += 1
      elif data[1] == '1' and data[12].strip() == 'Q':
          b_1 += 1
      elif data[1] == '0' and data[12].strip() == 'Q':
          b_0 += 1
      elif data[1] == '1' and data[12].strip() == 'S':
          c_1 += 1
      elif data[1] == '0' and data[12].strip() == 'S':
          c_0 += 1

print("C - спасенных/погибших: ", a_1, "/", a_0)
print("Q - спасенных/погибших: ", b_1, "/", b_0)
print("S - спасенных/погибших: ", c_1, "/", c_0)

import streamlit as st

# Вывод изображения
st.image('titanic.jpg')

# Вывод результатов
st.header('Данные пассажиров Титаника')
st.write('2. Подсчитать число спасенных и погибших для указанного пункта посадки')

# Выбор пункта посадки
selected_port = st.selectbox('Пункт посадки:', ['выбрать', 'Шербур', 'Квинстаун', 'Саутгемптон'])

# Отображение результатов в зависимости от выбранного пункта посадки
if selected_port == 'Шербур':
    st.write(f"C - спасенных/погибших: {a_1} / {a_0}")
elif selected_port == 'Квинстаун':
    st.write(f"Q - спасенных/погибших: {b_1} / {b_0}")
elif selected_port == 'Саутгемптон':
    st.write(f"S - спасенных/погибших: {c_1} / {c_0}")

fig, ax = plt.subplots(figsize=(8, 3))
ports = ['Шербур', 'Квинстаун', 'Саутгемптон']
saved = [a_1, b_1, c_1]
lost = [a_0, b_0, c_0]
ax.bar(ports, saved, label='Спасенные')
ax.bar(ports, lost, bottom=saved, label='Погибшие')
ax.set_ylabel('Количество')
ax.set_title('Количество спасенных и погибших по пунктам посадки')
ax.legend()
st.pyplot(fig)



