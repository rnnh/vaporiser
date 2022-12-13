![vaporiser](assets/logo.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/rnnh/vaporiser)
![GitHub licence](https://img.shields.io/github/license/rnnh/vaporiser)
![Code style: Black](https://img.shields.io/badge/code%20style-black-black)
[![Test Python Environment](https://github.com/rnnh/vaporiser/actions/workflows/test-venv.yml/badge.svg)](https://github.com/rnnh/vaporiser/actions/workflows/test-venv.yml)

<a href='https://ko-fi.com/rnn_h' target='_blank'><img height='30' style='border:0px;height:30px;' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' />

[ｖａｐｏｒｉｓｅｒ](https://github.com/rnnh/vaporiser) is a Python script that creates a vaporwave (slowed, with reverb) remix of a given MP3 file, with the option of playing over a looped GIF as a video.
It applies audio effects to an input MP3 file, and writes the result to a new MP3 file.
If a GIF is given in the command, an MP4 video file of the GIF on repeat for the duration of the remix is also created.
Vaporiser can apply the following audio effects:

- Speed shift
- Pitch shift
- Reverb
- Lowpass filter
- Bass boost
- Gain adjustment
- Out Of Phase Stereo (karaoke) effect
- Phaser effect
- Tremolo effect
- Compand

See [usage](#usage) for details of available effects.

# Contents

- [System requirements](#system-requirements)
- [Setup instructions](#setup-instructions)
- [Usage](#usage)

# System requirements

## Required software

- [Python](https://www.python.org/) 3.10 or higher
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

## Installing Python 3.10 and venv on Ubuntu

```bash
$ sudo apt install python3.10
$ sudo apt-get install python3.10-venv
```

# Setup instructions

## Clone the repo

```bash
$ git clone https://github.com/rnnh/vaporiser.git
$ cd vaporiser/
```

## Create a virtual environment

```bash
/vaporiser$ python3.10 -m venv env
/vaporiser$ source env/bin/activate
```

## Install required packages

```bash
(env) /vaporiser$ pip install --upgrade pip
(env) /vaporiser$ pip install -r requirements.txt
```

## Optional: Make script executable

Making the script executable will allow it to be called from the command line using `$ ./vaporiser.py` instead of `$ python vaporiser.py` when the virtual environment is active.

```bash
(env) $ chmod +x vaporiser.py
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
                    [-p PITCH_SHIFT] [-l LOWPASS_CUTOFF] [-b BASS_BOOST]
                    [-ga GAIN_DB] [-op] [-ph] [-tr] [-co] [-nr] [-g GIF_FILE]
                    [-sb]

Creates a vaporwave (slowed, with reverb) remix of a given MP3 file, with
multiple audio effects available, and the option of playing over a looped GIF
as a video.

options:
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

  -b BASS_BOOST, --bass BASS_BOOST
                        Add a bass boost effect (e.g. --bass 3). (default:
                        None)
  -ga GAIN_DB, --gain GAIN_DB
                        Applies gain (dB). (default: None)
  -op, --oops           Applies Out Of Phase Stereo effect. This is sometimes
                        known as the ‘karaoke’ effect as it often has the
                        effect of removing most or all of the vocals from a
                        recording. (default: False)
  -ph, --phaser         Enable phaser effect. (default: False)
  -tr, --tremolo        Enable tremolo effect. (default: False)
  -co, --compand        Enable compand, which compresses the dynamic range of
                        the audio. (default: False)
  -nr, --noreverb       Disables reverb. (default: False)

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
