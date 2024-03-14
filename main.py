from logging import _STYLES
import streamlit as st

### Streamlit Code ###

bg = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://wallpapercave.com/wp/wp9326372.jpg");
background-size: cover;
}
</style>
"""

st.markdown(bg, unsafe_allow_html=True)

st.title('Welcome to Treasure Island.')

st.title('Your mission is to find the treasure.')

st.subheader('You are at a crossroad. Where do you want to go?')

second_input = ''
third_input = ''

first_input = st.text_input("Left or Right").lower()
if first_input == "left":
  st.subheader(
      'You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat. Type "swim" to swim across.'
  )

  second_input = st.text_input("Wait or Swim").lower()
  if second_input == 'wait':
    st.subheader(
        'You arrive at the island unharmed. There is a house with 3 doors. 1. Red, 2. Yellow and 3. Blue. Which colour do you choose?'
    )

    third_input = st.text_input("Red, Yellow or Blue").lower()
    if third_input == 'yellow':
      st.success('Hurray!!....You found the treasure!! YOU WIN!!!')

    elif third_input == 'red':
      st.error('It is a room full of fire. Game Over.')

    elif third_input == 'blue':
      st.error('You enter a room of beasts. Game Over.')

    else:
      st.info('Please Provide Red, Blue or Yellow.')

  elif second_input == 'swim':
    st.error('Game Over')

  else:
    st.info('Please Provide Wait or Swim')

elif first_input == 'right':
  st.error('Game Over')

else:
  st.info('Please Provide Left or Right.')
