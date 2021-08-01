# ci-template

Get your Github Python CI up and running quick with this clone-and-forget template.

## Usage

```
$ git clone https://github.com/Graeme22/ci-template.git
```

Modify the names as you see fit!
Make sure to also set repository secrets:
- PYPI_USERNAME
- PYPI_PASSWORD

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

Creating a virtualenv for development:
```
$ make venv
$ source env/bin/activate
```

...after building the environment, will need to install the package: 

```
$ make install
```

It's usually a good idea to make sure you're passing tests locally before submitting a PR:
```
$ make test
```
