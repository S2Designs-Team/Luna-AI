from setuptools import setup, find_packages

# Leggi i pacchetti da requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name            ='Luna-AI',
    version         ='0.1.0',
    packages        =find_packages(),
    install_requires=requirements,
    # Specifica se il progetto utilizza Python 3.x
    python_requires ='>=3.10',
    # Altri metadati opzionali
    author          ='㊙️anonimo㊙️',
    author_email    ='',
    description     ='Progetto di intelligenza artificiale Luna-AI',   #
    url             ='https://github.com/Phobetor1999/LUNA-AI',        # Aggiorna con il link corretto
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: OS Independent',
    ],
)