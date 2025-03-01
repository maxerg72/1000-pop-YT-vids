import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset with pandas
videos = pd.read_csv("YT_vids_1000.csv")

#dataset cleaning
videos.rename(columns={"Video": "video", "Video views": "video_views", "Likes": "likes", "Dislikes":"dislikes", "Category":"category"}, inplace=True)
videos['video_views'] = videos['video_views'].replace({',': ''}, regex=True).astype(int)
videos['likes'] = videos['likes'].replace({',': ''}, regex=True).astype(int)
videos["dislikes"] = videos.dislikes.apply(lambda x: str(x).replace(",", ""))
videos["dislikes"] = videos.dislikes.apply(lambda x: x.replace("nan", "0")).astype(int)


#prints a summary (max, median, mean for the columns)
print("SUMMARY STATISTICS FOR THE DATASET")
print(videos.describe())



#1: Finding out the most present category
categories = videos.groupby("category").video.count().reset_index()
print(categories)
plt.pie(categories.video, labels=categories.category, autopct='%1.2f%%', textprops={'fontsize':7})
plt.title("Video categories")
plt.show()


#2: Analyzing likes, dislikes and views of certain categories
categories_likes_dislikes = videos[["category", "likes", "dislikes", "video_views"]]
music_likes_dislikes = categories_likes_dislikes[categories_likes_dislikes.category == "Music"]
nonmusic_likes_dislikes = categories_likes_dislikes[categories_likes_dislikes.category != "Music"]

#Creating scatterplot to see if there is correlation between views and likes in music videos
sns.scatterplot(data=music_likes_dislikes, x=music_likes_dislikes.video_views, y=music_likes_dislikes.likes)
plt.yscale("log")
plt.xscale("log")
plt.title("VIEWS TO LIKES RATIO")
plt.show()
plt.clf()

#Creating scatterplot to see if there is correlation between views and dislikes in music videos
sns.scatterplot(data=music_likes_dislikes, x=music_likes_dislikes.video_views, y=music_likes_dislikes.dislikes)
plt.yscale("log")
plt.xscale("log")
plt.title("VIEWS TO DISLIKES RATIO")
plt.show()
plt.clf()