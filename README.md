# monografiaProcessamento de Nuvens de Pontos na Identificação de Artefatos Humanos Pictóricos em Abrigos Pré-Históricos

## Sobre o projeto

O presente repositório consiste dos códigos desenvolvidos para o Trabalho de Conclusão de Curso da aluna Gabriela Barion Vidal.

O projeto visa desenvolver um algoritmo que analisará nuvens de ponto de sítios arqueológicos que possuem petróglifos e gerar uma imagem em duas dimensões para servir como painel para artigos científicos futuros e documentação da região. Assim, o presente trabalho irá auxiliar na precisão e automação da documentação de arte rupestre gravada, gerando um modelo bidimensional mais preciso e rápido do que as técnicas manuais utilizadas na arqueologia. O projeto tem como objetivo principal a digitalização do sítio arqueológico presente na cidade de Dourado-SP, que consiste de um paredão com diversas artes rupestres gravadas.

## Executando o projeto
Para conseguir utilizar o projeto em outros trabalhos, é preciso possuir Python 10 e seguir as seguintes etapas:

1. Baixar o repositório
2. Baixar as seguintes bibliotecas em Python:
    * Open3D versão 0.15.1
    * OpenCV
    * NumPy
3. Rodar o seguinte comando: `python main.py -i {path_to_ply_file} -o {name_output_file} -z {zoom_out_value}`

## Desenvolvedora

Gabriela Barion Vidal