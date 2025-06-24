import numpy as np
import platform
import asyncio
from scipy.io.wavfile import write

# Parameters
sample_rate = 44100  # Hz
duration = 30  # 5 minutes in seconds
carrier_freq_left = 100  # Hz
beat_freq = 40  # Hz
carrier_freq_right = carrier_freq_left + beat_freq  # 240 Hz


async def generate_binaural_beats():
    # Generate time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generate left and right channel signals
    left_channel = 0.5 * np.sin(2 * np.pi * carrier_freq_left * t)
    right_channel = 0.5 * np.sin(2 * np.pi * carrier_freq_right * t)

    # Combine into stereo signal
    stereo_signal = np.stack((left_channel, right_channel), axis=1)

    # Normalize to 16-bit PCM range
    stereo_signal = np.int16(stereo_signal * 32767)

    # Save as WAV file (simulated for Pyodide compatibility)
    # In a browser, this would trigger a download or play directly
    write("binaural_beats_40hz.wav", sample_rate, stereo_signal)

    print("Generated 40 Hz binaural beats (5 minutes)")


async def main():
    await generate_binaural_beats()


if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())
