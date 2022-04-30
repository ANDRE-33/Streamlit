import numpy as np
import streamlit as st
from PIL import Image
from ClassOCR import ReadTextFromImage
import mysql.connector 

def initializeConnection():
    return mysql.connector.connect(**st.secrets["mysql"])
conn=initializeConnection()
@st.experimental_memo(ttl=600)
def runQuery(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
rows=runQuery(f"SELECT p.nom,p.postnom,p.prenom,p.adresse,v.designation,v.matricule FROM avoirvoiture a",
"INNER JOIN proprietaire p on p.codeProp=a.codeProprio",
"INNER JOIN voiture v on v.codeVoiture=a.codeVoiture where v.matricule='{resultat}'")

for row in rows:
    st.write(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}")


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


