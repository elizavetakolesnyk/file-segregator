from setuptools import setup

setup(
    name='clean_folder',
    version='1.0',  # ??????
    description='Folder sorting app by Python',
    author='Liza Kolesnyk',
    author_email='liza_kolesnyk@gmail.com',
    # url=
    # license=
    # classifiers=
    packages=['clean_folder'],
    include_package_data=True,
    entry_points={'console_scripts': [
        'clean-folder=clean_folder.clean:main']}

)
