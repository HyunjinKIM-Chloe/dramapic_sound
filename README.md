# Dramapic Sound Classification AI module
- Predict the label of sounds (Human or not) using pre-trained models.
- Sound input files must be .wav and Models must be .pkl file.

  ## Class
    - There is a total of 5 labels (human, human_voice, life, nature,	song)
    - Human confidence score: "human" + "human_voice"
    - Non-Human confidence score: "life" + "nature" + "song"
    
  ## Requirements

  ### 1. install python dependencies
  ```
  pip install -r requirements.txt
  ```
  ### 2. Create config file in `/config/config.yaml` 
  Example:
  ```yaml
    wav_from_video_path: '../sound_files/wav_from_videos/'
    model_path : 'models/'
    split_wav_path : '../sound_files/wav_cut3s/'
  ```
  ### 3. Create directories
  `../sound_files/wav_from_videos/`
  `../sound_files/wav_cut3s/`
  
  ## How to run
  ### init_sound_features.py
  - Calculate frequencies of sounds
  - For the first time running code, wav files will be stored in `sound_files/`dirs automatically
  - Insert data into DB "sound_features" after calculating
  #### 1. A total video
  ```
  python init_sound_features.py {video_id}
  ```
  #### 2. Part of the video
  ```
  # ex: 2.5 sec to 18.9 sec of video_id 9 (python init_sound_features.py 9 2.5 18.9)
  python init_sound_features.py {video_id} {start_second} {end_second}
  ```
  
  ### init_model_predict.py
  - Predict the label and confidence score of human label
  - Insert data into DB "model_predictions" after predicting
  #### 1. A total video
  ```
  python init_model_predict.py {video_id}
  ```
  #### 2. Part of the video
  ```
  # ex: 2.5 sec to 18.9 sec of video_id 9 (python init_model_predict.py 9 2.5 18.9)
  python init_model_predict.py {video_id} {start_second} {end_second}
  ```
 
