from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
	name='matrix_vector',
	version='0.1.2',
	description='A python package for matrices and vectors operations.',
	url='https://github.com/Guldjan/matrix_vector',
	author='Guldjan Kupen',
	author_email='guldjan.kupen@gmail.com',
	license='MIT',
	packages=['matrix_vector'],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)