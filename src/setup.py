import setuptools

setuptools.setup(
    name="opt2",
    version="0.0.1",
    author="Equipo",
    description="Método numérico que resuelva problemas de optimización convexa de pequeña escala.",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy>=1.21.0'
        ],
    python_requires=">=3.7.3",
)
