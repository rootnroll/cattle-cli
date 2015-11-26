from setuptools import setup


setup(
    name='cattle',
    version='0.5.2',
    py_modules=['cattle'],
    url='https://github.com/cattleio/cattle-cli',
    license='MIT Style',
    author='Darren Shepherd',
    author_email='darren.s.shepherd@gmail.com',
    description='Python API and CLI for Cattle',
    install_requires=['gdapi-python==0.5.2'],
    entry_points={
        'console_scripts': [
            'cattle = cattle:_main'
        ]
    }
)
