import librosa
import soundfile as sf  # для сохранения аудиофайла с новой частотой дискретизации

# Загрузка аудиофайла
audio_data = 'media_complit_gpt/wav/001.wav'
y, sr = librosa.load(audio_data, sr=None)  # Загрузка с неопределённым sr (будет использован оригинальный sr)

# Увеличение частоты дискретизации до 48000 Гц
target_sr = 48000
y_resampled = librosa.resample(y, sr, target_sr)

# Сохранение аудиофайла с новой частотой дискретизации
output_file = 'resampled_audio.wav'
sf.write(output_file, y_resampled, target_sr)

print(f"Частота дискретизации до: {sr} Гц")
print(f"Частота дискретизации после: {target_sr} Гц")
print(f"Длительность аудио: {len(y) / sr} секунд")
