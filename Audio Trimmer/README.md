## Audio Trimmer
A simple CLI for trimming audio from any video written in python.

## Usage
### Trimming
```$ py main.py --start_frame=123 --video="video_file_path" --audio="audio_file_path"```
  - `--start_frame` takes the frame number from the video to start trimming from **(required)**.
  - `--video` takes the file path to the video file **(required)**.
  - `--audio` takes the file path to the audio file pre extracted from the video **(required)**.
  - `--end_frame` takes the last frame of the video (defaults to `None` i.e it'll trim the audio from `--start_frame` to the end.) **(optional)**.
### Help
```$ py main.py [-h] --help```

## Dependencies
  - FFmpeg.\
    Make sure it is installed and is in your `PATH` variable. [More here](https://www.wikihow.com/Install-FFmpeg-on-Windows).
  - VapourSynth.\
    Instructions on how to [install](https://github.com/vapoursynth/vapoursynth).
  - Acsuite.\
    ```$ pip3 install acsuite-orangechannel```
  - Argparse.\
    ```$ pip3 install argparse```
