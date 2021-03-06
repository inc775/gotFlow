from setuptools import setup, find_packages

setup(
    name='gotFlow',
    author='Adam Maxwell',
    version='1.0',
    author_email='catalyst256@gmail.com',
    description='Netflow transforms for Maltego',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
