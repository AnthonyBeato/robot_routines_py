from setuptools import find_packages, setup

package_name = 'robot_routines_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anthony',
    maintainer_email='axba0001@ce.pucmm.edu.do',
    description='Paquete para crear y ejecutar rutinas en el robot',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'routine_node = robot_routines_py.routine_node:main',
        ],
    },
)
