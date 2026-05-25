# Módulo XII - Arquitecturas Multimodales

Este repositorio contiene las prácticas del Módulo XII sobre arquitecturas multimodales. La práctica principal incluida explora técnicas de generación de descripciones automáticas de imágenes (image captioning) usando modelos basados en Transformers.

## Estructura del repositorio

- `Practica_1/`: Carpeta con la práctica de image captioning.
  - `main.ipynb`: Notebook principal que implementa y compara diferentes arquitecturas.
  - `captions_blip.csv`: Resultados de captions generados con BLIP.
  - `captions_clip.csv`: Resultados de captions seleccionados con CLIP.
  - `captions_transformer.csv`: Resultados de captions generados con un modelo ViT+GPT2.
  - `comparacion_captions.csv`: Comparación de resultados entre los diferentes métodos.
  - `imagenes_practica/`: Imágenes utilizadas en la práctica.

## Objetivo

El objetivo de esta práctica es comparar tres enfoques para generar o seleccionar descripciones de imágenes:

1. Modelo `ViT + GPT-2` para generación directa de texto.
2. Modelo `BLIP` para generación de captions condicionales.
3. Modelo `CLIP` para selección del caption más relevante entre candidatos.

## Requisitos

Para ejecutar el notebook se requieren los siguientes paquetes de Python:

- `torch`
- `torchvision`
- `transformers`
- `Pillow`
- `matplotlib`
- `pandas`
- `numpy`
- `sentencepiece`

## Uso

1. Abre `Practica_1/main.ipynb` en Jupyter Notebook o JupyterLab.
2. Ejecuta las celdas de instalación de paquetes y carga de librerías.
3. Ejecuta la sección de carga de imágenes y luego cada bloque de modelo.
4. Revisa los resultados generados en los archivos CSV.

## Documentación adicional

Consulta `Practica_1/README.md` para una guía detallada de la práctica, explicación de cada arquitectura y recomendaciones de uso.

## Notas

- El notebook detecta si hay GPU disponible y usa `cuda` cuando está presente.
- Los resultados se guardan en archivos CSV que pueden abrirse con Excel, pandas o cualquier editor de texto.

