"""
Warning
--

Warning sound

---------------------
Author: Shota Arai
Date: 2024/08/28

2025/01/22: If not SOUND_DEVICE, print "sounddevice is not installed."
"""

SOUND_DEVICE = False
try:
    import sounddevice as sd
    try:
        import numpy as np
    except ImportError:
        raise ImportError("numpy is not installed.")
    SOUND_DEVICE = True
    SAMPLE_RATE = 44100
    sd.default.samplerate = SAMPLE_RATE

except ImportError:
    SOUND_DEVICE = False


class Warning:
    def __init__(self) -> None:
        self.playing = False
        if not SOUND_DEVICE:
            print("sounddevice is not installed.")

    def __call__(self, frequency: list[float], second: list[float], volume: float = 1, message: str | None = None) -> None:
        if message is not None:
            print(message)
        if SOUND_DEVICE:
            assert len(frequency) == len(second), "The length of frequency and second must be the same."
            try:
                total_sec = sum(second)
                t = np.linspace(0, total_sec, int(total_sec * SAMPLE_RATE))
                data = np.zeros_like(t)
                i = 0
                for j in range(len(frequency)):
                    for tt in range(int(second[j] * SAMPLE_RATE)):
                        assert i < total_sec * SAMPLE_RATE, "The length of t is not enough."
                        data[i] = volume * np.sin(2 * np.pi * frequency[j] * t[i])
                        i += 1
                sd.play(data, loop=True, blocking=True)
                self.playing = True
            except Exception:
                self.playing = False

    def stop(self) -> None:
        if SOUND_DEVICE and self.playing:
            sd.stop()
            self.playing = False

    def __del__(self) -> None:
        if SOUND_DEVICE and self.playing:
            sd.stop()
            self.playing = False


if __name__ == "__main__":
    w = Warning()
    w([880, 440], [0.1, 0.1], 1, "This is a test.")
