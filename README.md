# BigIPCookie
Python script to easily verify the F5 BIG-IP Cookie Remote Information Disclosure vulnerability.
This script takes the F5 BIG-IP cookies and converts them to the corresponding IP address. 

## Motivation

I originally created this project just to practice writing python, but I wish to improve it so that it will also serve me better at work. 

## Installation

[Download](https://github.com/sgtalpha/BigIPCookie/archive/master.zip) the ipCookie.py script.

## Usage
```shell
usage: ipCookie.py [-h] [-c COOKIE]

optional arguments:
  -h, --help  show this help message and exit
  -c COOKIE   Specify the F5 BIG IP Cookie value
```
1: Obtain the F5 BIG-IP Cookie from the website you are testing

2: Run the script with the following command, replacing the brackets with the F5 BIG-IP cookie
```shell
python ipCookie.py -c [Cookie]
```
Example: 
```shell
python ipCookie.py -c 574728384.20480.0000
```
