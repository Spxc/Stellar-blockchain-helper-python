from setuptools import setup

setup(name='stellar_blockchain_helper',
      version='0.1',
      description='Simple Stellar helper util',
      url='https://github.com/Spxc/Stellar-blockchain-helper-python',
      author='Spxc',
      author_email='noreply@email.com',
      license='MIT',
      packages=['stellar_sdk'],
      install_requires=[
          'stellar_sdk',
      ],
      zip_safe=False)