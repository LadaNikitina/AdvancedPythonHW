FROM python:3

RUN apt-get update && apt-get install -y texlive-full

ENV TEXINPUTS=.:$TEXINPUTS

WORKDIR /app
COPY . /app

CMD ["pdflatex", "pip_table_image_tex_example.tex"]