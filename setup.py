#!/usr/bin/python3

from setuptools import setup

setup(
    name = 'alidns',
    version = '2018.3.17',
    keywords = ('aliyun', 'dns'),
    author = 'luoyeah',
    author_email = '1403287193@qq.com',
    url = 'https://github.com/luoyeah/alidns',
    license = 'GPLv3',
    description = 'aliyun dns service tools',
    long_description = 'aliyun dns service tools',
    include_package_data = True,
    packages = [
        'alidns'
    ],
    platforms = 'any',
    install_requires = [
        'aliyun-python-sdk-core-v3>=2.5.2',
        'aliyun-python-sdk-alidns>=2.0.7'
    ],
    entry_points = {
        'console_scripts':[
            'alidns = alidns.alidns:main'
        ]
    }
)
