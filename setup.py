from setuptools import setup

setup(
    name='realex-client',
    version='0.8.0',
    packages=['realexpayments'],
    url='https://github.com/viniciuschiele/realex-client',
    license='MIT',
    author='Vinicius Chiele',
    author_email='vinicius.chiele@gmail.com',
    description='Python interface to Realex Payments',
    keywords=['realex', 'payments', 'api', 'client'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)