import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def start_recognition():
    model = Model("model")  # Place Vosk model folder here
    rec = KaldiRecognizer(model, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000,
                           dtype='int16', channels=1, callback=callback):
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                yield result.get("text", "")
            else:
                partial = json.loads(rec.PartialResult())
                yield partial.get("partial", "")
