![vaporiser](assets/logo.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/rnnh/vaporiser)

# [Vaporiser](https://github.com/rnnh/vaporiser)

Vaporiser is a Python script that creates a ｖａｐｏｒｗａｖｅ (slowed and reverb) remix of a given MP3 file, with the option of playing over a looped GIF as a video.
It adds reverb, applies a low-pass filter, slows down, and pitches down an input MP3 file.
The result is written to a new MP3 file, and if a GIF is given in the command, an MP4 video file of the GIF on repeat for the duration of the remix is also created.
The speed, pitch and low-pass filter cutoff can be controlled with the `--speed`, `--pitch` and `--lowpass` arguments (this is optional, default parameters are provided).

# Contents

- [System requirements](#system-requirements)
- [Setup instructions](#setup-instructions)
- [Usage](#usage)

# System requirements

- Python 3.6.9 or higher
- [Sound eXchange (SoX)](http://sox.sourceforge.net/)
- [libsox-fmt-mp3 for SoX MP3 support](https://pkgs.org/download/libsox-fmt-mp3)

SoX and libson-fmt-mp3 can be installed with the following commands:

```bash
$ sudo apt install sox
$ sudo apt-get install libsox-fmt-mp3
```

Required Python modules are given in [requirements.txt](requirements.txt).

# Setup instructions

## Clone the repo

```bash
$ git clone https://github.com/rnnh/vaporiser.git
$ cd vaporiser/
```

## Create a virtual environment

```bash
$ virtualenv env
$ source env/bin/activate
```

## Install required packages

```bash
(env) $ pip install -r requirements.txt
```

# Usage

## Example

Vaporiser can be used to create a remix of the file `audio_file.mp3` with the following command:

```bash
$ python vaporiser.py --audio audio_file.mp3
```

The remixed audio will be written to the file `audio_file_vaporised.mp3`.
By default, `_vaporised` is added to the end of the output filename, unless an output filename is specified using the `--output` argument.

## Help text

```bash
$ python vaporiser.py --help
```

```
usage: vaporiser.py [-h] [-g GIF_FILE] [-o OUTPUT_NAME] [-s SPEED_RATIO]
                    [-p PITCH_SHIFT] [-l LOWPASS_CUTOFF] -a AUDIO_INPUT

Creates a vaporwave (slowed and reverb) remix of a given MP3 file, with the
option of playing over a looped GIF as a video.

optional arguments:
  -h, --help            show this help message and exit
  -g GIF_FILE, --gif GIF_FILE
                        Input GIF file to loop. Without a GIF, only an MP3 is
                        created. With a GIF, an MP4 video is also created.
                        (default: None)
  -o OUTPUT_NAME, --output OUTPUT_NAME
                        Name of output file. (default: None)
  -s SPEED_RATIO, --speed SPEED_RATIO
                        Ratio of new playback speed to old speed. (default:
                        0.85)
  -p PITCH_SHIFT, --pitch PITCH_SHIFT
                        Pitch shift (100ths of a semitone). (default: -50)
  -l LOWPASS_CUTOFF, --lowpass LOWPASS_CUTOFF
                        Cutoff for lowpass filter (Hz). (default: 3500)

required arguments:
  -a AUDIO_INPUT, --audio AUDIO_INPUT
                        Input audio file to vaporise (.mp3) (default: None)
```
