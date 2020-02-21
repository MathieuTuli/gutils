from setuptools import setup, find_namespace_packages
from glob import glob

setup(
    name='matutils',
    use_scm_version=True,
    packages=find_namespace_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/mathieutuli/matutils',
    python_requires='~=3.7',
    install_requires=[
    ],
    dependency_links=[
    ],
    setup_requires=[
        'setuptools_scm',  # for git-based versioning
    ],
    # DO NOT do tests_require; just call pytest or python -m pytest.
    license='License :: Other/Proprietary License',
    author='Mathieu Tuli',
    author_email='tuli.mathieu@gmail.com',
    description='Utility API for various python libraries',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: Other/Proprietary License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3',
    ],
    scripts=glob('bin/*'),
)
