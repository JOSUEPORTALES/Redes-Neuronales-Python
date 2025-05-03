import re

# 1. Definir un conjunto de documentos (corpus)
# Los documentos son textos de ejemplo donde queremos extraer entidades.
documentos = [
    "Juan y Maria fueron al parque de Central Park para celebrar su aniversario.",
    "Carlos vive en Madrid y le gusta ir al museo del Prado.",
    "Ana y su hermano José viajaron a París para las vacaciones de verano.",
    "El presidente de Estados Unidos, Joe Biden, visitará Europa la próxima semana."
]

# 2. Preprocesar los documentos (convertir todo a minúsculas y eliminar caracteres no deseados)
# Vamos a dividir el texto en palabras y a eliminar signos de puntuación
def preprocesar_documentos(documentos):
    documentos_procesados = []
    for doc in documentos:
        doc = doc.lower()  # Convertir el texto a minúsculas
        doc = re.sub(r'[^a-záéíóúñ\s]', '', doc)  # Eliminar signos de puntuación
        documentos_procesados.append(doc.split())  # Dividir el texto en palabras
    return documentos_procesados

# 3. Definir las listas de posibles entidades (en este ejemplo, usamos nombres comunes y lugares)
# Normalmente, estas entidades se extraen mediante modelos más complejos, pero para este ejemplo, usamos listas simples.
nombres_personas = ["juan", "maria", "carlos", "ana", "jose", "joe", "biden"]
lugares = ["parque", "central park", "madrid", "prado", "paris", "estados unidos", "europa"]

# 4. Función para identificar y extraer las entidades de los documentos
def extraer_entidades(documentos_procesados, nombres_personas, lugares):
    entidades_extraidas = []
    
    # Recorrer cada documento procesado
    for doc in documentos_procesados:
        entidades_doc = {"personas": [], "lugares": []}
        
        # Buscar las entidades de tipo persona
        for palabra in doc:
            if palabra in nombres_personas:
                entidades_doc["personas"].append(palabra)
        
        # Buscar las entidades de tipo lugar (en este caso, buscamos frases como "central park" o "madrid")
        for lugar in lugares:
            if lugar in " ".join(doc):  # Buscar si el lugar aparece en el documento
                entidades_doc["lugares"].append(lugar)
        
        entidades_extraidas.append(entidades_doc)
    
    return entidades_extraidas

# 5. Preprocesar los documentos para eliminar signos de puntuación y convertir a minúsculas
documentos_procesados = preprocesar_documentos(documentos)

# 6. Extraer las entidades de los documentos procesados
entidades = extraer_entidades(documentos_procesados, nombres_personas, lugares)

# 7. Mostrar el resultado de la extracción de información
for i, doc_entidades in enumerate(entidades):
    print(f"Documento {i + 1}:")
    print(f"  Personas: {', '.join(doc_entidades['personas']) if doc_entidades['personas'] else 'Ninguna'}")
    print(f"  Lugares: {', '.join(doc_entidades['lugares']) if doc_entidades['lugares'] else 'Ninguno'}")
    print("-" * 50)
