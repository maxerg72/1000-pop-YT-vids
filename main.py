import pandas as pd
import numpy as np

videos = pd.read_csv("YT_vids_1000.csv")
videos.rename(columns={"Video": "video", "Video views": "video_views", "Likes": "likes", "Dislikes":"dislikes", "Category":"category"}, inplace=True)
videos['video_views'] = videos['video_views'].replace({',': ''}, regex=True).astype(int)
videos['likes'] = videos['likes'].replace({',': ''}, regex=True).astype(int)
videos["dislikes"] = videos.dislikes.apply(lambda x: str(x).replace(",", ""))
videos["dislikes"] = videos.dislikes.apply(lambda x: x.replace("nan", "0"))
videos["dislikes"] = videos.dislikes.astype(int)

#print("SUMMARY STATISTICS FOR THE DATASET")
#print(videos.describe())