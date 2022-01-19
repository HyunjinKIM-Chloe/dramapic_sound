import model_predict as mp
import access_db as db
import os
import sys
import shutil

mmp = mp.ModelPredict()
sql = db.Query()
cursor, engine, db = sql.connect_sql()

if __name__ == '__main__':
    try:
        arg1 = int(sys.argv[1])
        mmp.mp4_to_wav(arg1)
        mmp.cut_song_by_msec(arg1)
        try:
            arg2 = sys.argv[2]
            arg3 = sys.argv[3]
            freq_df = mmp.save_frequency_df(video_id=arg1, start=int(arg2), end=int(arg3))
            sql.save_sql(engine, freq_df, 'sound_features', 'append')

        except:
            freq_df = mmp.save_frequency_df(video_id=arg1)
            sql.save_sql(engine, freq_df, 'sound_features', 'append')

        print(f"id-{arg1} video: {len(freq_df)} rows INSERT COMPLETED!")
        print("Local saved wav files will be deleted soon.")
        os.remove(f"{mmp.wav_from_video_path}{arg1}.wav")
        shutil.rmtree(f"{mmp.split_wav_path}{arg1}")
        print(f"Deleted {arg1} wav temporary files.")

    except:
        print("Please check video_id!")
