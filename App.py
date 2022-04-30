import numpy as np
import streamlit as st
from PIL import Image
from ClassOCR import ReadTextFromImage
from matplotlib import pyplot as plt



# main app
if __name__=="__main__":
    st.title("License Plate Recognition")
    st.markdown("Upload picture for recognition")
    
    image=st.file_uploader(label="Upload picture...",type=['png','jpg','jpeg'])
    # imageUrl=image.name
    if image is not None:
        input_image=Image.open(image)
        with st.spinner("Uploaded"):
            resultat=ReadTextFromImage(str(image.name))
            st.image(input_image)
        st.success(resultat)
    else:
        st.write("Upload An image")
    st.caption("CRES IA/Projet fin de Module")


