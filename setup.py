from setuptools import find_packages, setup
setup(
    name='coeficienteDevanecimento_GlobalLib',
    packages=find_packages(),
    version='0.1.0',
    description='gerador de coeficiente global de desvanecimento',
    author='Yuri Pedro dos Santos',
    author_email='yurisantosypds@gmail.com',
    install_requires=['numpy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)