from setuptools import setup,find_namespace_packages

setup(name='personal-assistant',
      version='1.0',
      description='Personal Assistant',
      url='https://github.com/VolodymyrKoz/Personal-Assistant-HW1',
      author='VolodymyrKoz',
      packages=find_namespace_packages(),
      entry_points = {'console_scripts': ['assistantdc=personal_assistant.main:main'],},
      install_requires=['colored==2.2.4', 'prompt-toolkit==3.0.43', 'wcwidth==0.2.13'],
      )