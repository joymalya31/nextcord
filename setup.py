from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
filename = 'nextcord/__init__.py'
with open(filename, 'r') as f:
    match = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if match is None:
        raise ValueError(f'"__version__" not found in {filename}')
    version = match.group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

readme = ''
with open('README.rst') as f:
    readme = f.read()

tests_require = [
    "python-dotenv"
]

extras_require = {
    'voice': ['PyNaCl>=1.3.0,<1.5'],
    'docs': [
        'sphinx==4.0.2',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
    ],
    'speed': [
        'orjson>=3.5.4',
    ],
    'test': tests_require,
}

packages = [
    'nextcord',
    'nextcord.types',
    'nextcord.ui',
    'nextcord.webhook',
    'nextcord.ext.commands',
    'nextcord.ext.tasks',
]

setup(name='nextcord',
      author='tag-epic & Rapptz',
      url='https://github.com/nextcord/nextcord',
      project_urls={
          "Documentation": "https://nextcord.readthedocs.io/en/latest/",
          "Issue tracker": "https://github.com/nextcord/nextcord/issues",
      },
      version=version,
      packages=packages,
      license='MIT',
      description='A Python wrapper for the Discord API forked from discord.py',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=requirements,
      tests_require=tests_require,
      extras_require=extras_require,
      python_requires='>=3.8.0',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
          'Typing :: Typed',
      ]
      )
