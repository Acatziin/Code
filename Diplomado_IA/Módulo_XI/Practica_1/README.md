# Práctica 1: Image Captioning con arquitecturas multimodales

Este documento describe la práctica de image captioning realizada en `Practica_1/main.ipynb`.

## Objetivo

Comparar diferentes enfoques para generar o seleccionar descripciones de imágenes:

- Generación automática con un modelo `ViT + GPT-2`.
- Generación automática con un modelo `BLIP`.
- Selección de la mejor descripción con un modelo `CLIP`.

## Contenido de `main.ipynb`

1. Instalación de dependencias necesarias.
2. Carga de una imagen de prueba y visualización.
3. Configuración de dispositivo (`cuda` o CPU).
4. Definición y carga del modelo `nlpconnect/vit-gpt2-image-captioning`.
5. Generación de captions usando un enfoque Transformer básico.
6. Definición y carga del modelo `Salesforce/blip-image-captioning-base`.
7. Generación de captions usando BLIP.
8. Definición y carga del modelo `openai/clip-vit-base-patch32`.
9. Uso de CLIP para seleccionar entre captions candidatos.
10. Guardado de resultados en archivos CSV para comparación.

## Archivos generados

- `captions_transformer.csv`: Captions generados con el modelo ViT+GPT2.
- `captions_blip.csv`: Captions generados con BLIP.
- `captions_clip.csv`: Resultado de la selección de captions candidatos usando CLIP.
- `comparacion_captions.csv`: Comparación conjunta de los resultados de los tres métodos.

## Cómo ejecutar

1. Abre `Practica_1/main.ipynb` en Jupyter Notebook o JupyterLab.
2. Ejecuta la primera celda para instalar dependencias (si es necesario).
3. Ejecuta las celdas una por una en el orden presentado.
4. Observa las descripciones generadas y los archivos CSV resultantes.

## Descripción de las arquitecturas

### 1. ViT + GPT-2

- Usa un encoder de visión (`ViT`) para extraer características de la imagen.
- Un decoder basado en `GPT-2` genera texto a partir de dichas características.
- Es un enfoque de generación directa de captions.

### 2. BLIP

- Modelo diseñado específicamente para tareas de VQA y captioning.
- Genera captions condicionales sobre la imagen usando un pipeline de procesamiento propio.
- Permite obtener descripciones más naturales y coherentes.

### 3. CLIP

- No genera texto directamente.
- Evalúa la similitud entre la imagen y un conjunto de captions candidatos.
- Selecciona el caption más relevante de la lista dada.

## Recomendaciones

- Si tienes GPU, ejecuta el notebook con `cuda` para acelerar el procesamiento.
- Ajusta los captions candidatos de CLIP según el dominio de las imágenes.
- Compara los resultados de los archivos CSV y analiza cuál método produce descripciones más precisas.

## Notas finales

Esta práctica sirve para entender cómo diferentes arquitecturas multimodales abordan el problema de describir imágenes. La comparación entre generación directa y selección por similitud es útil para evaluar fuerza y limitaciones de cada estrategia.
