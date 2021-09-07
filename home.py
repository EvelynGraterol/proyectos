import streamlit as st
import pandas as pd

def app():
    st.title('PROYECTO FINAL DE DATA MINING')
    #st.write('Grupo 2')
    st.header ("MODELO DE PREDICCIÖN DE WEB MALICIOSO") 
    st.subheader ('Descripción del problema')
    st.write("""El proyecto consiste en evaluar diferentes modelos de clasificación para predecir sitios web maliciosos y benignos, en función de la capa de aplicación y las características de la red""")


    
    html_temp = """
    <ol>Descripcion de las variables:</ol>
    <li>URL: es la identificación anónima de la URL analizada en el estudio</li>
    <li>URL_LENGTH: es la cantidad de caracteres en la URL</li>
    <li>NÚMERO DE CARACTERES ESPECIALES : es el número de caracteres especiales identificados en la URL, tales como, “/”, “%”, “#”, “&”, “. "," = "</li>
    <li>CHARSET: es un valor categórico y su significado es el estándar de codificación de caracteres (también llamado juego de caracteres).</li>
    <li>SERVIDOR: es un valor categórico y su significado es el sistema operativo del servidor obtenido de la respuesta del paquete.</li>
    <li>CONTENT_LENGTH: representa el tamaño del contenido del encabezado HTTP. </li>
    <li>WHOIS_COUNTRY: es una variable categórica, sus valores son los países que obtuvimos de la respuesta del servidor (específicamente, nuestro script usó la API de Whois). </li>
    <li>WHOIS_STATEPRO: es una variable categórica, sus valores son los estados que obtuvimos de la respuesta del servidor (específicamente, nuestro script usó la API de Whois). </li>
    <li>WHOIS_REGDATE: Whois proporciona la fecha de registro del servidor, por lo que esta variable tiene valores de fecha con formato DD / MM / AAAA HH: MM </li>
    <li>FECHA DE ACTUALIZACIÓN DE WHOIS : A través del Whois obtuvimos la última fecha de actualización del servidor analizado
    INTERCAMBIO DE CONVERSACIÓN TCP : Esta variable es el número de paquetes TCP intercambiados entre el servidor y nuestro cliente honeypot  </li>
    <li>DIST REMOTE TCP_PORT: es el número de puertos detectados y diferentes a TCP </li>
    <li>REMOTE_IPS: esta variable tiene el número total de IP conectadas al honeypot </li>
    <li>APP_BYTES: este es el número de bytes transferidos </li>
    <li>PAQUETES DE APLICACIONES FUENTE : paquetes enviados desde el honeypot al servidor </li>
    <li>REMOTO APP PAQUETES: los paquetes recibidos desde el servidor </li>
    <li>APP_PACKETS: este es el número total de paquetes IP generados durante la comunicación entre el honeypot y el servidor </li>
    <li>TIEMPOS DE CONSULTA DNS : este es el número de paquetes DNS generados durante la comunicación entre el honeypot y el servidor </li>
    <li>TIPO: esta es una variable categórica, sus valores representan el tipo de página web analizada, específicamente, 1 es para sitios web maliciosos y 0 es para sitios web benignos</li>"""
    st.markdown(html_temp,unsafe_allow_html=True)




    #carga del dataset
    data = pd.read_csv("dataset.csv")


    data.isnull().sum()
    if st.checkbox('Cantidad de nulos'):
        st.write(data.isnull().sum())

    #if st.checkbox('Heatmap de datos transformados'):
        #im_o = Image.open("heat.PNG")
        #st.image(im_o, width=600)
    
    if st.checkbox('Tipos de datos originales'):
        st.write(data.dtypes)



    #normalizacion de los nombres de las columnas
    data.columns = map(str.lower, data.columns)
    #normalizacion de los datos 
    data = data.apply(lambda x: x.astype(str).str.lower())
    #correción de datos nulos
    data.fillna(0, inplace=True)
    data.content_length.replace({'nan':'0.0'}, inplace=True)
    data.dns_query_times.replace({'nan':'0.0'}, inplace=True)

    if st.checkbox('Observacion total de los datos'):
        st.dataframe(data.head(10))



    #conversion de las variables de objeto de tipo numerico a int
    data['content_length'] = data['content_length'].astype(float).astype(int) 
    data['dns_query_times'] = data['dns_query_times'].astype(float).astype(int)

    #conversion de las variables de objeto a int
    data['url_length'] = data['url_length'].astype(int)
    data['number_special_characters'] = data['number_special_characters'].astype(int)
    data['tcp_conversation_exchange'] = data['tcp_conversation_exchange'].astype(int)
    data['dist_remote_tcp_port'] = data['dist_remote_tcp_port'].astype(int)
    data['remote_ips'] = data['remote_ips'].astype(int)
    data['app_bytes'] = data['app_bytes'].astype(int) 
    data['source_app_packets'] = data['source_app_packets'].astype(int) 
    data['remote_app_packets'] = data['remote_app_packets'].astype(int) 
    data['source_app_bytes'] = data['source_app_bytes'].astype(int)
    data['remote_app_bytes'] = data['remote_app_bytes'].astype(int)
    data['app_packets'] = data['app_packets'].astype(int)
    #transformacion de la variable objetivo
    data['type'] = data['type'].astype(int)

    if st.checkbox('Tipos de datos transformados'):
        st.write(data.dtypes)


    #if st.checkbox('Heatmap de datos transformados'):
        #im_ = Image.open("heat_no.PNG")
        #st.image(im_, width=600)


    #cantidad de datos
    f = data.shape[0]
    c = data.shape[1]

    if st.checkbox('Cantidad de filas y columnas'):
        st.write('Numero de filas:{}'.format(f))
        st.write('Numero de columnas:{}'.format(c))



    #verificacion de balance la variable target (TYPE)
    #La variable target sera (sitio web malicioso) 1 - yes, 0 - no)

    y = data.groupby('type').size()[0]
    n = data.groupby('type').size()[1]
    p1 = round((n*100)/(f))
    p2 = round(100-p1)

    if st.checkbox('Número de observaciones por tipo de etiqueta'):
        st.write(print(''))
    #st.write('Número de observaciones con la etiqueta 0 (no):{}'.format(y))
    #st.write('Número de observaciones con la etiqueta 1 (yes):{}'.format(n))
        st.write('Porcentaje de las clase minoritaria(1):{}%'.format(p1))
        st.write('Porcentaje de la clase mayoritaria(0):{}%'.format(p2))