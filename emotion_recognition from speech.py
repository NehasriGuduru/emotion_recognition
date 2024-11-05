#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install tensorflow')


# In[2]:


get_ipython().system('pip install librosa')


# In[3]:


get_ipython().system('pip install librosa matplotlib')


# In[4]:


get_ipython().system('pip install resampy')


# In[5]:


import os


# In[6]:


# Define the path where the RAVDESS dataset is extracted
dataset_path = r'C:\Users\HP\emotion\archive (3)\Actor_10'


# In[7]:


# List all files in the directory
all_files = os.listdir(dataset_path)
print("All files in directory:")
print(all_files)


# In[8]:


# Count the number of .wav files
wav_files = [f for f in all_files if f.endswith('.wav')]
print(f"\nNumber of .wav files: {len(wav_files)}")
print("List of .wav files:")
print(wav_files)


# In[9]:


# Print the first few .wav filenames for inspection
if wav_files:
    print("Sample .wav file names:")
    for file in wav_files[:5]:  # Show the first 5 files
        print(file)
else:
    print("No .wav files found in the directory.")


# In[10]:


# Initialize lists to hold file paths and labels
file_paths = []
labels = []


# In[11]:


# Example of different emotion label parsing (update according to your filenames)
label_map = {
    '01': 'neutral',
    '02': 'calm',
    '03': 'happy',
    '04': 'sad',
    '05': 'angry',
    '06': 'fearful',
    '07': 'disgust',
    '08': 'surprised'
}


# In[12]:


# Loop through the dataset and collect file paths and corresponding emotion labels
for filename in wav_files:
    print(f"Processing file: {filename}") 
    parts = filename.split('-')  
    print(f"Filename parts: {parts}") 
    if len(parts) >= 3:  
        emotion_code = parts[2]  
        label = label_map.get(emotion_code)
        if label:  
            file_paths.append(os.path.join(dataset_path, filename))
            labels.append(label)


# In[15]:


import pandas as pd
# Create a DataFrame
data_df = pd.DataFrame({'file_path': file_paths, 'label': labels})

# Display the resulting DataFrame
print(data_df)  


# In[16]:


from IPython.display import Audio, display

#Define the path to your audio file 
audio_path = r'C:\Users\HP\emotion\archive (3)\Actor_10\03-01-01-01-01-01-10.wav'

#Set the sample rate
sr = 22050

#Display the audio

display(Audio(filename=audio_path, rate=sr))


# In[18]:


import librosa
import matplotlib.pyplot as plt

# Define the path to your audio file
audio_file_path =r'C:\Users\HP\emotion\archive (3)\Actor_10\03-01-01-01-01-01-10.wav'

# Load the audio file
y, sr = librosa.load(audio_file_path, sr=None) 
# Create a time axis in seconds
time = librosa.times_like(y, sr=sr)

# Plot the waveform
plt.figure(figsize=(14, 5))
plt.plot(time, y)
plt.title('Waveform of Audio')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, max(time))
plt.grid()
plt.show()


# In[ ]:




