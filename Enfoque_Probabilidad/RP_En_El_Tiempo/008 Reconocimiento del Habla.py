import speech_recognition as sr

# Creamos un reconocedor de voz
reconocedor = sr.Recognizer()

# Usamos el microfono como fuente de audio
with sr.Microphone() as fuente_audio:
    print("Habla algo (esperando entrada de voz)...")
    
    # Ajustamos el reconocedor al ruido ambiente
    reconocedor.adjust_for_ambient_noise(fuente_audio)

    # Escuchamos la entrada del usuario
    audio_entrada = reconocedor.listen(fuente_audio)

    try:
        # Intentamos reconocer el texto usando Google Speech Recognition
        texto = reconocedor.recognize_google(audio_entrada, language="es-ES")
        print("Texto reconocido:", texto)

    except sr.UnknownValueError:
        # Si no se pudo entender el audio
        print("No se pudo entender el audio.")
        
    except sr.RequestError as e:
        # Si hubo un problema con la conexion al servicio de Google
        print("Error al conectarse al servicio de reconocimiento:", str(e))
