# linux.conf.au 2019
Presentation for [Sysadmin miniconf](http://sysadmin.miniconf.org/) at [linux.conf.au 2019](https://linux.conf.au/)

([Online](https://jangroth.github.io/linuxconf2019/) on github.io)

## Talk Abstract

Python is a great language for DevOps tasks. It’s easy to use for automation and offers an end-to-end range of tooling for 
managing infrastructure on-premise and in the cloud. Scripts are quickly implemented and new features easily rolled out. But 
what if complexity grows and all of the sudden you find yourself in a complete mess? How do you add a new feature or fix a 
bug in a script that you struggle to understand because it was written months ago? And do you sometimes see someone else’s 
code that you like but can't always put your finger on the magic ingredient? This talk is aimed at you if you are reasonably 
confident reading Python code and want to discover and improve beyond the basics. I'll provide you with ideas and suggestions 
that will help you stay on top of your coding and will bring it to the next level: Clean code which is easier to understand, 
more functional, testable and beautiful. 

## References and further reading

### Python 3 / venv / pipenv

* [Virtual Environments](https://python-guide-cn.readthedocs.io/en/latest/dev/virtualenvs.html)
* [Pipenv: Python Dev Workflow for Humans](https://pipenv.readthedocs.io/en/latest/)
* [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)
* [Python Application Dependency Management in 2018](https://hynek.me/articles/python-app-deps-2018)

### Conventions / Good Naming / Beautiful Code

* [The Hitchhiker's Guide to Python / Code Style](https://docs.python-guide.org/writing/style/)
* [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)
* [Understanding List Comprehensions in Python 3](https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3)
* [Comprehensions](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html)

### Scope And Classes

* [Introduction to Python Classes](http://introtopython.org/classes.html)

### Using an IDE

Most people I know use either [PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/). The screenshots were taken from PyCharm.

### Language Features

* [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
* Jinja's [custom filters](http://jinja.pocoo.org/docs/2.10/api/#writing-filters)
* Beautiful CLIs with [Click](https://click.palletsprojects.com/en/7.x/) 

## More Python

Some links to resources to see more Python code on a regular base:

### Regular Newsletters
* [Python Weekly](https://www.pythonweekly.com/)
* [PyCoders Weekly](https://pycoders.com/)
* [Python Tricks from Real Python](https://realpython.com/)

### Coding Challenges
* [The Python Challenge](http://www.pythonchallenge.com/)
* [Advent of Code](https://adventofcode.com/) (also look at previous challenges)

## Credits

This presentation uses [reveal.js](https://github.com/hakimel/reveal.js) with these plugins:
* [Elapsed-Time-Bar](https://github.com/tkrkt/reveal.js-elapsed-time-bar) 
* [Badges](https://github.com/ThomasWeinert/reveal-badges) 
  
It's a beautiful framework.

The Python 2.7 countdown comes from [timeanddate.com](https://www.timeanddate.com/clocks/freecountdown.html), inspired by [python clock](https://pythonclock.org/).

The List Comprehension example was taken from [Fluent Python: Clear, Concise, and Effective Programming](http://shop.oreilly.com/product/0636920032519.do) by Luciano Ramalho.