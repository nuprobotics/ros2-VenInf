from setuptools import find_packages, setup
from glob import glob


package_name = 'task03'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + "/launch", ['launch/task03.launch']),
        ('share/' + package_name + "/config", ['config/task03.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ilia Nechaev',
    maintainer_email='ilia.nechaev@jetbrains.com',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = task03.service:main',
        ],
    },
)
