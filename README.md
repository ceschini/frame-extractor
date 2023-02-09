# Frame Extractor

Simple frame extractor using openCV. Extract frames from videos by specifying seconds, minutes or time interval.

## Installation

In order to install the application, python3 and virtualenv package must be installed. Bellow are the steps to install these pre-requisites, setting up a virtual environment and installing required packages.

```python3
    pip install -r requirements.txt
```

Even though it can be installed in the global python environment, it is prefferable to install it in a virtual environment as follows:

1. Install ```virtualenv``` if you don't already have it.

    ```pip install virtualenv```

2. Create a new virtual environment via the ```virtualenv``` package.

```virtualenv .venv```

3.Install python packages requirements.

```pip install -r requirements.txt```

## Usage

There are two main ways of using this script. You can simply call it and specify its parameters, as shown below, or you can call the interactive command-line interface (CLI), by using the ```-cli``` flag.

### Running the script directly

```bash
python frame_extractor.py  -f <filename> -s <seconds> -m <minutes> -i <interval>
```

In order to run, please take notice of the four positional parameters.

* **-f**, **--filename**: local filename or full filepath
* **-s**, **--seconds**: Exact second for frame extracted
* **-m**, **--minutes**: Exact minute for frame extracted
* **-i**, **--interval**: Interval in seconds (ex: 5-6)

### Running the command-line interface

```bash
python frame_extractor.py -cli
```

By executing with the ```-cli```, the main loop started, and you are greeted by the interface, which will follow you step-by-step on the frame extracting process.

## Contact

For questions and sugestions, you can [reach me at Zulip](https://chat.pixforcemaps.com/#narrow/pm-with/18-lucas.ceschini), or [e-mail me](mailto:lucas.ceschini@pixforce.ai).
***

Lucas Ceschini, Feb 7, 2023.
