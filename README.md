SUDOKU-Agenda es una aplicación web diseñada para facilitar la programación de citas en nuestra academia de reforzamiento académico. La aplicación permite a los usuarios seleccionar y reservar horarios para clases de reforzamiento. Además, cuenta con scripts adicionales para enviar correos de confirmación y registrar la información en Google Sheets.

Características:
    Agendamiento de citas: Los usuarios pueden ver la disponibilidad y reservar horarios para clases.
    Confirmación por correo electrónico: Un script en Python envía correos de confirmación a los usuarios después de reservar una cita.
    Registro en Google Sheets: Otro script en Python registra la información de las citas en una hoja de cálculo de Google Sheets para llevar un control detallado.
Tecnologías Utilizadas:
    Frontend y Backend: Streamlit, Python
    Base de Datos: Google Sheets (a través de la API)
Librerías Adicionales:
    Envío de correos: smtplib
    Google Sheets: gspread==6.1.2
    Streamlit: streamlit==1.35.0
    Menú de opciones en Streamlit: streamlit_option_menu==0.3.13
Instalación y Configuración
Prerrequisitos
    Python 3.x
    Pip
    Acceso a una cuenta de Google para usar la API de Google Sheets
    Credenciales para el servidor de correo electrónico
