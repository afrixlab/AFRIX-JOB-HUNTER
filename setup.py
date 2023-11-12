from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='afrix-job-hunter',
    version='0.1.0',
    url='https://github.com/afrixlabs/afrix-job-hunter',
    author='afrixlabs',
    author_email='Official-support@afrixlabs.me',
    description='Get automatic job updates at your comfort',
    packages=find_packages(),    
    install_requires=required,
    license='AGPL-3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3.6',
    ],
)