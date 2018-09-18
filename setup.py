from setuptools import setup

with open('README.rst') as file:
	long_description = file.read()

setup(
	name='botblocker',
	version='1.0.2',
	author='Yan Orestes',
	author_email='yan.orestes@alura.com.br',
	packages=['botblocker'],
	description='Python script to identify and block your bot followers on Twitter',
	long_description=long_description,
	url='https://github.com/yanorestes/botblocker',
	download_url='https://github.com/yanorestes/botblocker/archive/1.0.2.zip',
	license='MIT',
	keywords='twitter bot blocker tweepy botometer',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Natural Language :: Portuguese (Brazilian)',
		'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Topic :: Internet',
	],
	python_requires='>= 3.4',
	entry_points={
		'console_scripts':['botblocker=botblocker.__init__:main']
	},
	install_requires=[
          'tweepy',
          'botometer',
          'huepy',
    ],
)