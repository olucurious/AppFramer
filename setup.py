from setuptools import setup
import sys, os

__url__ = 'https://github.com/olucurious/pyfcm'

__version__ = '1.0.0'

if sys.argv[-1] == 'publish':
    os.system("git tag -a %s -m 'v%s'" % (__version__, __version__))
    os.system("python setup.py sdist bdist_wheel upload -r pypi")
    os.system("git push --tags")
    sys.exit()

setup(
    name="appframer",
    version=__version__,
    description="AppFramer helps to reduce the pain of putting your app screenshots in various device frames.",
    url=__url__,
    author="Emmanuel Adegbite",
    author_email="olucurious@gmail.com",
    license='MIT License',
    packages=["appframer"],
    entry_points="""
             [console_scripts]
             appframer = appframer.app:main
        """,
    install_requires=[
        'Pillow',
        'six>=1.10.0',
    ],
    package_data={'appframer': ['fonts/*', 'devices/*']},
    include_package_data=True,
    zip_safe=False,
    keywords='ios, android, screenshot, app frame, screenshot framer, itunes assets, googleplay assets',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
