[![Discord](https://img.shields.io/discord/492624619149459458.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.com/invite/eMJ5yjyJVM)
[![downloads](https://img.shields.io/github/downloads/marmarachain/marmara-connector/total?color=brightgreen&style=plastic)]()
![last commit](https://img.shields.io/github/last-commit/marmarachain/marmara-connector?color=blue)
[![issues](https://img.shields.io/github/issues/marmarachain/marmara-connector?color=yellow)](https://github.com/marmarachain/marmara-connector/issues)
![language](https://img.shields.io/github/languages/top/marmarachain/marmara-connector)
![twitter](https://img.shields.io/twitter/follow/marmarachain?label=marmarachain&style=social)

![MarmaraCreditLoops Logo](https://raw.githubusercontent.com/marmarachain/marmara/master/MCL-Logo.png "Marmara Credit Loops Logo")

## Marmara Connector
Marmara Connector is an easy to use GUI application for installing Marmara Chain and conducting credit loops on your local machine or on a remote server. 

The app is designed to handle Marmara Credit loop operations as well as wallet operations.

The local platform is either Linux, Windows or MacOS based OS. The remote platform is Linux based OS.

The developed platform establishes a connection to a remote platform through SSH technology.

For more detailed information on creating Marmara credit loops, kindly refer to [Making Marmara Credit Loops](https://github.com/marmarachain/marmara/wiki/How-to-make-Marmara-Credit-Loops?). 

## Features
- Enables installing Marmara Chain on a remote server or local virtual machine,
- Send/receive MCL transactions,
- Enables making Marmara Credit Loops and managing them on a single interface without having to know the commands.

## Getting Started

- To install/download Marmara Connector, follow the [Marmara Connector Installation Guidelines](https://github.com/marmarachain/marmara-connector/wiki).
- For development purposes, follow the [Developer Guidelines for Marmara Connector](https://github.com/marmarachain/marmara-connector/wiki/Getting-Started-with-Marmara-Connector-Development).

### Development

sudo apt install python3.10 python3.10-dev python3.10-venv

Create a virtual environment:
```
python3.10 -m venv myvenv
```
You can install pyQt5 and PyInstaller using pip:
```
pip3 install pyQt5 PyInstaller
```

If you experience problems packaging the app, then update your PyInstaller and hooks package the latest versions using

```
pip3 install --upgrade PyInstaller pyinstaller-hooks-contrib
```

To run the PyInstaller build:

```
pyinstaller marmara-connector.spec
```

To compile our resources.qrc file to a Python file named resources_rc.py we can use:
```
pyrcc5 resources.qrc -o resources_rc.py
```

## Contact
- B. Gültekin Çetiner [![twitter](https://img.shields.io/twitter/follow/drcetiner?style=social)](https://twitter.com/drcetiner )

Contribution Workflow
---
Contributions to the development of this software are very welcomed. Here is the basic flow for a contribution:

1. Fork this project to your account.
2. Create a branch for the change you intend to make.
3. Make your changes to your fork.
4. Send a pull request, PR, from your fork’s branch to our `development` branch.

Important Notice
---
Marmara Connector is experimental and a work-in-progress. Use at your own risk. 
 
License
---
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
