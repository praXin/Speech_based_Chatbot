from watson_developer_cloud import SpeechToTextV1
import json
import StringIO
import pyaudio
import wave
import os
import re

stt = SpeechToTextV1(username="c473f7e9-97c7-4e6a-a7e1-9120265ec996", password="yl0juKEXpGI0")


CHUNK = 128 # The size of each audio chunk coming from the input device.
FORMAT = pyaudio.paInt16 # Should not be changed, as this format is best for speech recognition.
RATE = 16000 # Speech recognition only works well with this rate.  Don't change unless your microphone demands it.
RECORD_SECONDS = 5 # Number of seconds to record, can be changed.
WAVE_OUTPUT_FILENAME = "output.wav"


def find_device(p, tags):
    device_index = None
    for i in range(p.get_device_count()):
        devinfo = p.get_device_info_by_index(i)
        #print("Device %d: %s" % (i, devinfo["name"]))

        for keyword in tags:
            if keyword in devinfo["name"].lower():
                #print("Found an input: device %d - %s"%(i, devinfo["name"]))
                device_index = i
                return device_index

    if device_index is None:
        print("No preferred input found; using default input device.")

    return device_index

def save_audio(WAVE_OUTPUT_FILENAME):
    """
    Stream audio from an input device and save it.
    """
    p = pyaudio.PyAudio()

    device = find_device(p, ["input", "mic", "audio"])
    device_info = p.get_device_info_by_index(device)
    channels = int(device_info['maxInputChannels'])

    stream = p.open(
        format=FORMAT,
        channels=channels,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
        input_device_index=device
    )

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording\n")

    stream.stop_stream()
    stream.close()

    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def SpeechToText():
    save_audio(WAVE_OUTPUT_FILENAME)



    audio_file = open("output.wav", "rb")
    a=""
    b=""
    a = json.dumps(stt.recognize(audio_file, content_type="audio/wav"), indent=2)
    c=0
    buf = StringIO.StringIO(a)
    for i in range(1,7):
        b = buf.readline()
    a = buf.readline()
    b = re.split(': ',a)
    return b[1]
