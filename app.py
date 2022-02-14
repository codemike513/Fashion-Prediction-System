import streamlit as st
from classify import predict
from PIL import Image


def main():

    st.markdown("<h1 style='text-align: center; color: white;'>Fashion Prediction System</h1>",
                unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Made By - Mihir Pesswani</h1>",
                unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload an Image", type=[
                                     "jpg", "png", "jpeg", "jiff"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)
        label = predict(image, 'keras_model.h5')
        if label == 0:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Prediction -> Dress</h1>", unsafe_allow_html=True)
        elif label == 1:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Prediction -> LongSleeve</h1>", unsafe_allow_html=True)
        elif label == 2:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Prediction -> Cap</h1> border-style: solid; border-color: red;", unsafe_allow_html=True)
        elif label == 3:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Prediction -> Outwear</h1>", unsafe_allow_html=True)
        elif label == 4:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Prediction -> Shirt</h1>", unsafe_allow_html=True)
        elif label == 5:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Prediction -> Pant</h1>", unsafe_allow_html=True)
        elif label == 6:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Prediction -> T-Shirt</h1>", unsafe_allow_html=True)
        elif label == 7:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Prediction -> Shoes</h1>", unsafe_allow_html=True)
        elif label == 8:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Prediction -> Shorts</h1>", unsafe_allow_html=True)
        elif label == 9:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Prediction -> Skirt</h1>", unsafe_allow_html=True)
        else:
            st.markdown(
                "<h1 style='text-align: center; color: #fafafa;'>Upload a Suitable Image</h1>", unsafe_allow_html=True)

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .reportview-container .main {background-color: #0e1117;}
            .reportview-container p {color: white;}
            .reportview-container h1:first-child {color: white}
            .main {background-color: #0e1117;}
            .Widget>label {color: #fafafa}
            .streamlit-button.primary-button {background-color: #131720; border-color: #131720}
            .streamlit-button {color: #fafafa;}
            .div {color: black}
            .st-bk {color: #fafafa;}
            .st-bo {color: #b6b9c9;}
            .st-bd {background-color: #31333f;}
            .st-bh {color: #fafafa}
            .reportview-container h1 {color: white}
            
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
