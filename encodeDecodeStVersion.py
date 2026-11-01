import ast
import streamlit as st

def encodeString(stringVal):
    prevChar = stringVal[0]
    number = 0
    encodeList = []
    for char in stringVal:
        if char != prevChar:
            if char is not None:
                encodeList.append((prevChar, number))
            number = 1
            prevChar = char
        else:
            number = number + 1

    encodeList.append((prevChar, number))

    return encodeList
    pass

def decodeString(tupleVal):
    decodeStr = ''

    for item in tupleVal:
        decodeStr = decodeStr + (item[0] * item[1])
    return decodeStr

with st.sidebar:
    st.subheader("Welcome to the Ascii Image Encoder and Decoder")
    st.markdown("This app will allow you to encode ASCII images into a copy and paste string and view ASCII art when provided with decode string.")
    st.markdown("")
    st.markdown("")
    st.markdown("This app was created by Cecilia F. as an extension of the Python Essentials Training LinkedIn Course")
    st.markdown("")
    st.markdown("")
    st.markdown("*Side note: It is slow (sorry in advance). Please give it around 20 seconds for small and medium image sizes and longer for large image sizes. If it still doesn't work, go to the three dots at the top right and re-run. Sometimes the result will come up right after you pressed the three dots, so look out!*")
    st.markdown("")
    st.markdown("*I hope you enjoy!*")


st.subheader("Ascii Image Encoder", divider = 'yellow')
stringVal = st.text_area("Paste your ASCII image below!")

if stringVal == '':
    st.text("")
    print("Has not typed anything yet or the user just pressed enter.")
else:
    print(encodeString(stringVal))
    st.text_area("Result", value=encodeString(stringVal), disabled=True)


st.subheader("Ascii Image Decoder", divider="yellow")
tupleVal = st.text_area("Paste your compressed ASCII image string below!")

if tupleVal == '':
    st.text("")
    print("Has not typed anything yet or the user just pressed enter")

else:
    try:
        parsed_tuples = ast.literal_eval(tupleVal)

        if isinstance(parsed_tuples, (list, tuple)):
            decoded_result = decodeString(parsed_tuples)
            st.text_area("Result", value=decoded_result, disabled=True)
        else:
            st.error(
                "Oh no! I do not think you typed in (or lets be real, copy and pasted) a valid encode list sequence. Please try again (not wtih the same sequence, remember the definition of insanity)."
            )
    except (ValueError, SyntaxError):
        st.error(
            "Oh no! Somethink went wrong resulting in a ValueError or a SyntaxError. This was likely cause because you typed in (or lets be real, copy and pasted) text that the system couldn't parse. Please try again (not with the same text, remember the definition of insanity)."
        )
