#!/usr/bin/env python

# Loading modules
from pysndfx import AudioEffectsChain
import moviepy.editor as movedit
import argparse
import datetime
import sys
import re

# Parsing for command line arguments
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description = "Creates a vaporwave (slowed, with reverb) remix of a given \
    MP3 file, with the option of playing over a looped GIF as a video.")

parser.add_argument("-o", "--output",
                    dest = "output_name",
                    help = "Name of output file(s), instead of audio file name \
                    with the addition of '_vaporised'.",
                    type = str)

required_arguments = parser.add_argument_group("required arguments")

required_arguments.add_argument("-a", "--audio",
                                dest = "audio_input",
                                help = "Input audio file to vaporise (.mp3)",
                                type = str,
                                required = True)

audio_arguments = parser.add_argument_group("audio arguments",
                                            "these arguments control audio \
                                            effects that will be applied by \
                                            default")

audio_arguments.add_argument("-s", "--speed",
                    dest = "speed_ratio",
                    help = "Ratio of new playback speed to old speed.",
                    type = float,
                    default = 0.75)

audio_arguments.add_argument("-p", "--pitch",
                    dest = "pitch_shift",
                    help = "Pitch shift (100ths of a semitone).",
                    type = float,
                    default = -75)

audio_arguments.add_argument("-l", "--lowpass",
                    dest = "lowpass_cutoff",
                    help = "Cutoff for lowpass filter (Hz).",
                    type = int,
                    default = 3500)

audio_arguments_optional = parser.add_argument_group("extra audio arguments",
                                                     "these arguments control \
                                                     extra, optional audio \
                                                     effects")

audio_arguments_optional.add_argument("-tr", "--tremolo",
                                      dest = "tremolo",
                                      help = "Enable tremolo effect.",
                                      action = "store_true")

audio_arguments_optional.add_argument("-ph", "--phaser",
                                      dest = "phaser",
                                      help = "Enable phaser effect.",
                                      action = "store_true")

audio_arguments_optional.add_argument("-ga", "--gain",
                                      dest = "gain_db",
                                      help = "Applies gain (dB).",
                                      type = int,
                                      default = None)

audio_arguments_optional.add_argument("-co", "--compand",
                                      dest = "compand",
                                      help = "Enable compand, which compresses \
                                      the dynamic range of the audio.",
                                      action = "store_true")

video_arguments = parser.add_argument_group("video arguments",
                                            "optional arguments, result in an \
                                            MP4 video output in addition to \
                                            the MP3 audio")

video_arguments.add_argument("-g", "--gif",
                    dest = "gif_file",
                    help = "Input GIF file to loop. Without a GIF, only an MP3 \
                    is created. With a GIF, an MP4 video is also created.",
                    type = str)

args = parser.parse_args()

# Setting name of output file
if args.output_name is None:
    # If no output name is given, add "_vaporised" to input audio file name
    audio_input_string = re.sub(".mp3", "", str(args.audio_input))
    audio_output = audio_input_string + "_vaporised.mp3"
    video_output = audio_input_string + "_vaporised.mp4"
else:
    # Otherwise, use the output file name given via the command line
    output_string = re.sub(".mp3", "", str(args.output_name))
    output_string = re.sub(".mp4", "", str(output_string))
    audio_output = output_string + ".mp3"
    video_output = output_string + ".mp4"
    if args.audio_input == args.output_name:
        print("ERROR: Input and output name are identical")
        sys.exit()

# Creating audio effects chain function
fx = (
    AudioEffectsChain()
    .pitch(args.pitch_shift)
)

# Adds tremolo effect to the audio effects chain
if args.tremolo:
    fx = fx.tremolo(freq = 500, depth = 50)

# Adds a phaser to the audio effects chain
if args.phaser:
    # fx.phaser(gain_in, gain_out, delay, decay, speed)
    fx = fx.phaser(0.9, 0.8, 2, 0.2, 0.5)
    
# Applies gain to the audio effects chain
if args.gain_db is not None:
    fx = fx.gain(db = args.gain_db)
    
# Applies compand to the audio effects chain
if args.compand:
    fx = fx.compand()

# Adding reverb, lowpass filter, speed alteration to audio effects chain
fx = fx.speed(args.speed_ratio)\
    .lowpass(args.lowpass_cutoff)\
    .reverb()

# Applying audio effects
fx(args.audio_input, audio_output)

# Create video if a GIF file is provided
if args.gif_file is None:
    # If no GIF is provided, exit here
    print("Script finished at", datetime.datetime.now().strftime('%H:%M:%S'))
    print("Vaporised MP3 file (audio):", audio_output)
    sys.exit()
else:
    # If a GIF is provided, loop it for the length of the vaporised audio file
    mp3_movedit = movedit.AudioFileClip(audio_output)
    gif_movedit = movedit.VideoFileClip(args.gif_file)
    number_of_loops = float(mp3_movedit.duration / gif_movedit.duration)
    gif_looped = gif_movedit.loop(number_of_loops)
    gif_looped_with_audio = gif_looped.set_audio(mp3_movedit)
    gif_looped_with_audio.write_videofile(video_output)
    print("Script finished at", datetime.datetime.now().strftime('%H:%M:%S'))
    print("Vaporised MP3 file (audio):", audio_output)
    print("Vaporised MP4 file (video):", video_output)
