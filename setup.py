from distutils.core import setup

setup(
    name="django-useful-enums",
    packages=["usefulenums"],
    version="1.0",
    description="A useful enumeration / choice library for Django.",
    author="Graham Binns",
    author_email="graham@outcoded.dev",
    url="https://github.com/grahambinns/django-useful-enums",
    download_url=(
      "https://github.com/grahambinns/django-useful-enums/archive/1.0.tar.gz"),
    keywords=["django", "choices", "enumerations"],
    classifiers=[],
    install_requires=[
      "stringcase",
    ]
)
