import os
import librosa
import librosa.display
import numpy as np  # Import NumPy
import matplotlib.pyplot as plt
import soundfile as sf

# Конвертация .mp3 в .wav
def convert_mp3_to_wav(input_file, output_file):
    y, sr = librosa.load(input_file, sr=None)
    sf.write(output_file, y, sr)

# Построение спектрограммы аудиофайла
def plot_audio_spectrogram(wav_file, output_plot_file):
    y, sr = librosa.load(wav_file, sr=None)

    # Вычисление спектрограммы
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    # Построение графика
    plt.figure(figsize=(12, 6))
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f"Spectrogram for {os.path.basename(wav_file)}")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.savefig(output_plot_file)
    plt.close()

# Обработка всех .mp3 файлов в папке
def process_audio_files_in_folder(input_folder, wav_output_folder, plot_output_folder):
    os.makedirs(wav_output_folder, exist_ok=True)
    os.makedirs(plot_output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            mp3_file = os.path.join(input_folder, filename)
            wav_file = os.path.join(wav_output_folder, filename.replace(".mp3", ".wav"))
            plot_file = os.path.join(plot_output_folder, filename.replace(".mp3", ".png"))

            convert_mp3_to_wav(mp3_file, wav_file)
            plot_audio_spectrogram(wav_file, plot_file)
            print(f"Processed {filename}")

# Пример использования
input_folder = 'media'
wav_output_folder = 'media/media_complit_gpt/wav'
plot_output_folder = 'media/media_complit_gpt/image'

process_audio_files_in_folder(input_folder, wav_output_folder, plot_output_folder)
