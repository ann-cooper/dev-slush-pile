Title: Python Resources
Author: AC
Date: 2023-04-03
Tags: resources
Slug: python-resources
Summary: A collection of resources for working in Python


I first put together a Python resources page when I was leading a data engineering department, and this list is an updated and expanded take on that idea. It isn't meant to be comprehensive in any way, but I think it's a starting point for some of the major things that software and data engineers who work in Python need to know.

## Books and blogs
### General
- [Dive Into Python3](https://diveintopython3.net/)
- [Real Python](https://realpython.com/tutorials/basics/)
- [Hynek Schlawack](https://hynek.me/articles/)
- [The Impostor's Handbook](https://bigmachine.io/products/the-imposters-handbook/)

### Topics
- [Architecture Patterns with Python](https://www.oreilly.com/library/view/architecture-patterns-with/9781492052197/)
- [Designing Data-Intensive Applications](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/)
- [Foundations for Architecting Data Solutions](https://www.oreilly.com/library/view/foundations-for-architecting/9781492038733/)
- [Python Testing with Pytest](https://pythontest.com/pytest-book/)

## Podcasts
- [Coding Blocks](https://www.codingblocks.net/)
- [Data Engineering Podcast](https://www.dataengineeringpodcast.com/)
- [Python Bytes](https://pythonbytes.fm/)
- [Software Engineering Daily](https://softwareengineeringdaily.com/)
- [Talk Python to Me](https://talkpython.fm/)
- [Test and Code](https://testandcode.com/)

## Idiomatic Python
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/)
- [A collection of Python best practices posts from Real Python](https://realpython.com/tutorials/best-practices/)

## Style
- [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257](https://www.python.org/dev/peps/pep-0257/)
- [Docstrings styles](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy)

## Data structures
- [Exercises on data structures](https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure.php)
- [On data structures](https://docs.python.org/3/tutorial/datastructures.html)

## Standard library essentials
- [Collections](https://docs.python.org/3/library/collections.html)
- [Itertools](https://docs.python.org/3/library/itertools.html)
- [generators](https://docs.python.org/3/reference/expressions.html#generator-expressions)

## Debugging
- [pdb](https://realpython.com/python-debugging-pdb/)
- [Blog post on debugging approaches](https://ann-cooper.github.io/debugging-thinking.html)

## Object-oriented programming
- [Fluent Python, PyCon 2019](https://www.youtube.com/watch?v=mUu_4k6a5-I)
    - [Repo for the talk](https://github.com/fluentpython/pyob2019)
- [Intro to OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [SOLID principles with Python examples](https://medium.com/@dorela/s-o-l-i-d-principles-explained-in-python-with-examples-3332520b90ff)
- [SOLID cheatsheet](https://www.monterail.com/hubfs/PDF%20content/SOLID_cheatsheet.pdf)

## Functional programming
- [Official docs on functional programming with Python](https://docs.python.org/3/howto/functional.html)
- [Functional Programming learning path](https://realpython.com/learning-paths/functional-programming/)

## Testing
- [Quick tips](https://pybit.es/articles/pytest-tips/) from Pybites.
### Test runners & frameworks
- [Pytest, the Pytest runner can run tests written with unittest](https://docs.pytest.org/en/stable/)

### Unit & Integration testing
- [Fixtures and parametrization](https://realpython.com/pytest-python-testing/)
- [An introduction to testing with a discussion of unit and integration testing](https://realpython.com/python-testing/)

### Other testing approaches
#### Pipeline testing
- [Great Expectations](https://greatexpectations.io/)
#### Property-based testing
- [Hypothesis](https://github.com/HypothesisWorks/hypothesis/tree/master/hypothesis-python)

## Design patterns
- [Pycon AU talk: You Don't Need that](https://www.youtube.com/watch?v=imW-trt0i9I)
- [Design Patterns with Python](https://python-patterns.guide/)

## Memory
- [Official docs on memory management](https://docs.python.org/3/c-api/memory.html)
- [Itamar Turner-Trauring on Memory usage in Python](https://pythonspeed.com/datascience/#memory)
- [Real Python Memory Management article](https://realpython.com/python-memory-management/)


### Formatting and linting
- [Black for code formatting](https://pypi.org/project/black/)
- [Flake8](https://flake8.pycqa.org/en/latest/)

## Libraries and packaging
- [PyPA guidance on packaging](https://packaging.python.org/en/latest/)
- [Distribution options](https://pythonspeed.com/articles/distributing-software/)
- [Flit](https://flit.pypa.io/en/stable/rationale.html)
- [Hatch](https://pederhan.github.io/python-packaging/tools/specialized/hatch/)


### Project structure
- [Flask projects](https://flask.palletsprojects.com/en/2.2.x/tutorial/layout/)
- [Cookiecutter templates](https://www.cookiecutter.io/templates)

### Dependency management
- [pip-tools](https://pip-tools.readthedocs.io/en/latest/index.html)
- [Better Python Dependency Management with pip-tools](https://www.caktusgroup.com/blog/2018/09/18/python-dependency-management-pip-tools/)
- [Poetry](https://python-poetry.org/)

#### Reproducible development environments
- [Tutorial on virtual environments](https://docs.python.org/3/tutorial/venv.html)
- [Venv documentation](https://docs.python.org/3/library/venv.html)
- [Pyenv](https://github.com/pyenv/pyenv)
    - [Pyenv tutorial](https://realpython.com/intro-to-pyenv/)

## Important packages and tools for data-focused engineers

### Exploring data
- [pandas](https://pandas.pydata.org/)
- [polars](https://www.pola.rs/)

### Profiling data
- [ydata-profiling (formerly pandas-profiling)](https://github.com/ydataai/ydata-profiling)

### Visualizations
- [Seaborn](https://seaborn.pydata.org/tutorial.html)
- [Plotly](https://plotly.com/python/)
- [What kind of visualization fits the data?](https://datavizcatalogue.com/search.html)

## Web APIs & related
### Frameworks
- [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
    - [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
    - [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
    - [pytest-flask](https://pytest-flask.readthedocs.io/en/latest/)
- [FastAPI](https://fastapi.tiangolo.com/)

### Data Modeling
- [Sqlalchemy](https://docs.sqlalchemy.org/en/13/)
- [MongoEngine](http://mongoengine.org/)
- [Dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [attrs](https://www.attrs.org/en/stable/examples.html)

### Serialization
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
- [cattrs](https://catt.rs/en/latest/)

### Validation
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [attrs](https://www.attrs.org/en/stable/examples.html)
- [A guide to dataclasses](https://realpython.com/python-data-classes/)

## Learning plans
- [A collection of different learning plans by subject focus](https://realpython.com/learning-paths/)
- [Project ideas](https://www.dataquest.io/blog/python-projects-for-beginners/)
- [Code challenges](https://app.codesignal.com/arcade)
- [Roadmaps](https://roadmap.sh/python)
