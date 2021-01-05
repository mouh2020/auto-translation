from setuptools import setup
from setuptools import find_namespace_packages
from setuptools import find_packages
#README file :
with open("README.md","r") as readme_handle :
    long_descriptions=readme_handle.read()
setup(
    name="auto_translation",
    author="Mohammed BADI",
    author_email="badimohammed2019@gmail.com",
    version="0.1.5",
    description="A simple python library used to translate and speak a given text from the user with Google Translation using user's Chrome browser. ",
    long_description=long_descriptions,
    long_description_content_type="text/markdown",
    url="https://github.com/mouh2020/auto-translation",
    install_requires=['selenium==3.141.0',
                      'chromedriver-binary-auto==0.1'],
    keywords=['translation','traduction','translate','speech','voice','google translation','languages'],
    packages=find_namespace_packages(include=['auto_browser','auto_browser.*']),
    classifiers=[
        'Intended Audience :: Education',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat'
    ],
)


