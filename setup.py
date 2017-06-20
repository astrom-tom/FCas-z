from setuptools import setup

setup(
        name='cosmo_at_z',                      
        version='1.0',                          
        scripts=['cosmo_at_z'],                  
        description='Cosmology at redshift z',
        author='Romain THOMAS',
        author_email='the.spartan.proj@gmail.com',
        url = 'https://github.com/astrom-tom/spartan_cosmo'
        packages=['cosmospartan']
        install_requires=['numpy', 'scipy', 'decimal']
     )

