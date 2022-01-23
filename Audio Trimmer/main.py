import argparse
import vapoursynth as vs
from acsuite import eztrim

def main():
    parser = argparse.ArgumentParser(description = "A simple command line utility for trimming audio losslessly.")
    parser.add_argument("-e", "--end_frame", type = int, nargs = 1, metavar = "end_frame", default = None, help = "last frame of audio for trimmed audio.")
    
    required_args = parser.add_argument_group("required named arguments")
    required_args.add_argument("-s", "--start_frame", type = int, nargs = 1, metavar = "start_frame", default = None, help = "frame of audio to start trimming from.", required = True)
    required_args.add_argument("-v", "--video", type = str, nargs = 1, metavar = "video_file ", default = None, help = "file path for the video file.", required = True)
    required_args.add_argument("-a", "--audio", type = str, nargs = 1, metavar = "audio_file", default = None, help = "file path for the audio file.", required = True)

    args = parser.parse_args()
    
    core = vs.core

    _end_frame = args.end_frame[0] if args.end_frame else None
    _start_frame = args.start_frame[0]
    video_file, audio_file = args.video[0], args.audio[0]

    src = core.lsmas.LWLibavSource(video_file)
    eztrim(src, [(_start_frame, _end_frame)], audio_file)

if __name__ == "__main__":
    main()