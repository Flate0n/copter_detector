import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка аудиофайла
audio_data = 'media_complit_gpt/wav/000.wav'
y, sr = librosa.load(audio_data)
print(type(y), type(sr))

# Вычисление STFT (Short-Time Fourier Transform)
X = librosa.stft(y)
Xdb = librosa.amplitude_to_db(abs(X))

# Построение спектрограммы
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()
plt.title('Spectrogram')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()
