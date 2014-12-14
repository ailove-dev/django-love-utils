from distutils.core import setup

setup(
    name='django-love-utils',
    version='0.1',
    url='https://github.com/ailove-dev/django-love-utils',
    license='MIT',
    author='Ailove',
    author_email='ailove@ailove.com',
    description='Utils for django project',
    packages=['love_utils'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'django>=1.5',
    ],
    tests_require=['Django'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)