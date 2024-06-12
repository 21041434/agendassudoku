import streamlit as st
from streamlit_option_menu import option_menu
from enviar_correo import enviar
import re
from google_sheets import GoogleSheets
import uuid


##FRONTEND
page_title = "SUDOKU"
page_icon = "📚" 
layout = "centered"

horas = ["16:00","17:00","18:00","19:00"]
materias = ["Matematicas","Español","Ingles","Fisica","Quimica","CENEVAL","Otro... (Especificar en notas)",]

document = "Gestion_sudoku"
sheet = "Reservas"
credentials = st.secrets["google"]["credentials_google"]



def validar_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True
    else:
        return False

def generate_uuid():
    return str(uuid.uuid4())




st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)


st.title("SUDOKU")
st.image("assets/sudoku.jpg", caption=("REFORZANDO TUS CONOCIMIENTOS")) 


selected = option_menu(menu_title=None, options=["Reservar","Materias","Detalles"], 
                        icons=["calendar-date", "journals", "clipboard-minus"],

                        orientation="horizontal") 


if selected == "Detalles":
    st.subheader("Dirección 📍")
    st.text("Fuente de Cantos #418 - Fracc. Las Funtes")
    st.markdown("""<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3643.5564154373074!2d-104.6155591!3d24.0467028!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x869bb7a97dbb4657%3A0x80facab57446a07!2sFuente%20de%20Cantos%20418%2C%20Las%20Fuentes%2C%2034220%20Durango%2C%20Dgo.!5e0!3m2!1ses-419!2smx!4v1717991662364!5m2!1ses-419!2smx" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""", unsafe_allow_html=True)
    st.markdown("""<iframe src="https://www.google.com/maps/embed?pb=!4v1717992194441!6m8!1m7!1suOP9KH4IF-EwkotSvfzV8A!2m2!1d24.04678423868657!2d-104.6156675734958!3f112.41069411220789!4f-6.5140040354368125!5f0.7820865974627469" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""", unsafe_allow_html=True) 
    st.subheader("Horarios 🕓")
    dia, hora, = st.columns(2)
    dia.text("Lunes a viernes excepto días festivos")
    hora.text("16:00 - 20:00")

    st.subheader("Contacto")
    wp, inst, fb, = st.columns(3)
    wp.markdown("[WhatsApp](https://w.app/SUDOKU)")
    inst.markdown("[Facebook](https://www.facebook.com/escueladereforzamiento?mibextid=ZbWKwL)")
    fb.markdown("[Instagram](https://www.instagram.com/sudoku_dgo?igsh=MW52YWx5ZjA3OTV3ag==)")

if selected == "Materias":
    st.subheader("Matematicas & CENEVAL\nAlberto Gonzalez")
    st.image("assets/alberto.jpg", caption="Estudiante Ing. Informatica y profesor suplente")
    st.subheader("Español & Ingles\nAngelica Ontiveros")
    st.image("assets/angelica.jpeg", caption="Lic. en lenguas extranjeras y profesora")
    st.subheader("Fisica & Quimica\nSandra Uviña")
    st.image("assets/sandra.jpeg", caption="Ing. Logistica y profesora")

if selected == "Reservar":
    st.subheader("Reservar")
    c1, c2 = st.columns(2)
    nombre = c1.text_input("Nombre del alumn@*", placeholder=("Nombre"))
    email = c2.text_input("Tu email*", placeholder=("Email"))
    fecha = c1.date_input("Fecha")   
    hora = c2._selectbox("Hora", horas)
    materia = c1.selectbox("Materia",materias)
    notas = c2.text_area("Notas", placeholder=("Notas adicionales, especificaciones, etc..."))
    boton_enviar = st.button("Reservar")

##BACKEND
    if boton_enviar:
        with st.spinner("Reservando..."):
            if nombre =="":
                st.warning("El nombre es obligatorio")
            elif email=="":
                st.warning("El email es obligatorio")
            elif not validar_email(email):
                st.warning("El email no es valido")    
            else:
                uid = generate_uuid()
                data = [[nombre, email, str(fecha), hora, materia, notas, uid]]
                gs = GoogleSheets(credentials, document, sheet)
                range = gs.get_last_row_range()
                gs.write_data(range, data)
                enviar(email, nombre, fecha, hora, materia)
                st.success("Su pasantia ha sido reservada de forma exitosa.")
