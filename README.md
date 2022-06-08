# FOCS

FOCS is an open-source python data science project which simulates Formula One weekend sessions completely with every internal and external odds. You are feel free to seek and use it.

In order, you have to install additional packages at below to work with this repository.

```bash
pip install pandas
```

```bash
pip install numpy
```

## Version
Latest Version: Formula One 2022 Season

### How Is It Works?

Well, FOCS algorithm is a little bit complicated but not that complicated to can not explain. First of all we have 3 base of data seperated into src folder named 'manufacturers.xlsx', 'drivers.xlsx' and 'DB2022.py'. DB2022 includes tyre and circuit informations stored into python classes to use that information to create objects with several functions that we are going to give it to as a parameter for each driver for prevent same laptimes by different drivers. After that, manufacturers and drivers excel table includes informations of the current grid. In 'main.py' file includes base algorithm of 2 part process. Function takes one parameter which is the name of the circuit. With that way you can arrange races wherever you want. Circuit names listed in 'DB2022.py'. When we get to the 2 part process, it is qualifying and races. If you wanna just dive into it, you'll find a lot more exicting things.

## License

MIT Licence Included.

## Maintainer

Emir Yarkin Yaman
[GitHub](https://github.com/Weinoose) & [PyPi](https://pypi.org/user/Weinoose/)
