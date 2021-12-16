![vaporiser](assets/logo.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/rnnh/vaporiser)
![GitHub](https://img.shields.io/github/license/rnnh/vaporiser)

[ｖａｐｏｒｉｓｅｒ](https://github.com/rnnh/vaporiser) is a Python script that creates a vaporwave (slowed, with reverb) remix of a given MP3 file, with the option of playing over a looped GIF as a video.
It adds reverb, applies a low-pass filter, slows down, and pitches down an input MP3 file.
The result is written to a new MP3 file, and if a GIF is given in the command, an MP4 video file of the GIF on repeat for the duration of the remix is also created.
The speed, pitch and low-pass filter cutoff can be controlled with the `--speed`, `--pitch` and `--lowpass` arguments (these are optional, default parameters are provided).
See [usage](#usage) for a full list of available effects.

# Contents

- [System requirements](#system-requirements)
- [Setup instructions](#setup-instructions)
- [Usage](#usage)

# System requirements

## Required software

- [Python](https://www.python.org/) 3.6.9 or higher
- Python modules in [requirements.txt](requirements.txt)
- [Sound eXchange (SoX)](http://sox.sourceforge.net/)
- [libsox-fmt-mp3 for SoX MP3 support](https://pkgs.org/download/libsox-fmt-mp3)
- A UNIX operating system (Linux or macOS)

## Using vaporiser on Windows

This project is written to be used through a UNIX (Linux or Mac with macOS Mojave or later) operating system (OS).
If you are using Windows, you can use this project on a Linux OS (e.g. [Ubuntu](https://ubuntu.com/)) through either:

- [Windows Subsytem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/about)
- [A virtual machine](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox)

## Installing SoX

SoX and libson-fmt-mp3 can be installed with the following commands:

```bash
$ sudo apt install sox
$ sudo apt-get install libsox-fmt-mp3
```

# Setup instructions

## Clone the repo

```bash
$ git clone https://github.com/rnnh/vaporiser.git
$ cd vaporiser/
```

## Create a virtual environment

```bash
/vaporiser$ virtualenv env
/vaporiser$ source env/bin/activate
```

## Install required packages

```bash
(env) /vaporiser$ pip install -r requirements.txt
```

# Usage

## Example

Vaporiser can be used to create a remix of the file `audio_file.mp3` with the following command:

```bash
$ python vaporiser.py --audio audio_file.mp3
```

The remixed audio will be written to the file `audio_file_vaporised.mp3`.
By default, `_vaporised` is added to the end of the output filenames, unless an output filename is specified using the `--output` argument.

## Help text

```bash
$ python vaporiser.py --help
```

```
usage: vaporiser.py [-h] [-o OUTPUT_NAME] -a AUDIO_INPUT [-s SPEED_RATIO]
                    [-p PITCH_SHIFT] [-l LOWPASS_CUTOFF] [-tr] [-ph]
                    [-ga GAIN_DB] [-co] [-g GIF_FILE] [-sb]

Creates a vaporwave (slowed, with reverb) remix of a given MP3 file, with the
option of playing over a looped GIF as a video.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_NAME, --output OUTPUT_NAME
                        Name of output file(s), instead of audio file name
                        with the addition of '_vaporised'. (default: None)

required arguments:
  -a AUDIO_INPUT, --audio AUDIO_INPUT
                        Input audio file to vaporise (.mp3) (default: None)

audio arguments:
  these arguments control audio effects that will be applied by default

  -s SPEED_RATIO, --speed SPEED_RATIO
                        Ratio of new playback speed to old speed. (default:
                        0.75)
  -p PITCH_SHIFT, --pitch PITCH_SHIFT
                        Pitch shift (100ths of a semitone). (default: -75)
  -l LOWPASS_CUTOFF, --lowpass LOWPASS_CUTOFF
                        Cutoff for lowpass filter (Hz). (default: 3500)

extra audio arguments:
  these arguments control extra, optional audio effects

  -tr, --tremolo        Enable tremolo effect. (default: False)
  -ph, --phaser         Enable phaser effect. (default: False)
  -ga GAIN_DB, --gain GAIN_DB
                        Applies gain (dB). (default: None)
  -co, --compand        Enable compand, which compresses the dynamic range of
                        the audio. (default: False)

video arguments:
  optional arguments, result in an MP4 video output in addition to the MP3
  audio

  -g GIF_FILE, --gif GIF_FILE
                        Input GIF file to loop. Without a GIF, only an MP3 is
                        created. With a GIF, an MP4 video is also created.
                        (default: None)
  -sb, --sobel          Applies a Sobel filter to video output. (default:
                        False)
```
