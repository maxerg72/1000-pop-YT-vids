# 📊DATA ANALYSIS | 1000 Most popular YouTube videos
This project works with the dataset <strong>"Most popular 1000 Youtube videos"</strong> from <a href="https://www.kaggle.com/datasets/samithsachidanandan/most-popular-1000-youtube-videos?phase=FinishSSORegistration&returnUrl=%2Fdatasets%2Fsamithsachidanandan%2Fmost-popular-1000-youtube-videos%2Fversions%2F1%3Fresource%3Ddownload&SSORegistrationToken=CfDJ8AuLNK2TuwVNoq0UgqCcqcYFrvoQ1_gpuSj8UBlKg_2JcBQheD7VuCeMPm6HAvTiY_pV_t9XG8J_DWvmyTEOweuCMGoyDLgNa638LJnp3KiU4qe6h6so7Dt24-WRq5Bmj7JaOQu-YVKuZcM7moKJHSWQTdVP6DGXSGDrEUqq8EBqNThE3an4Ff5ZpEMQXVhT16iqTUu3URrKZ6F5Sjh5gLgoSYtDFR-Wmp_X-XXI-KE21A1WhkebIIr75jEXk47K8SNzOl61JcOb0SX9rD7mkjAntnk7Ny3OTzMO5xRKhMQmGNfGItWAlvg4GmovRiSylsY8jdCfygKppSBMujJCq40&DisplayName=Maximili%C3%A1n+Cenkner">Kaggle.</a>
<h2>What Did I analyze?</h2>
<ol>
  <li>Which category represents the largest part in the dataset?;</li>
  <li>Do the videos from this categories tend to have more likes/dislikes as their views increase?</li>
</ol>

<h2>🔴Required tools🔴</h2>
<ul>
  <li>
    <strong>🐍Python 3.12</strong>
  </li>
  <li>
    <strong>💻Newest version of Pandas, Seaborn and MatPlotLib libraries</strong>
  </li>
</ul>

<h2>📊Analysis results📊</h2>

<h3>1. The most represented category</h3>
<img src="Visualizations/video_categories.png" alt="Pie chart visualization showing proportions of each category">

<br>
  From the pie chart visualization, we can clearly see that "Music" category leads the way with around 44% of the dataset categories being "Music". 

<h3>2. Analysis of the most represented (likes, dislikes, views)</h3>
<img src="Visualizations/views_likes_ratio-music.png" alt="Scatterplot visualization, which shows the ratio between views and likes in the music category"><img src="Visualizations/views_dislikes_ratio-music.png" alt="Scatterplot visualization, which shows the ratio between views and likes in the music category">
  
  By using scatterplot visualizations, I answered the question whether like/dislike counts tend to increase with video views in the "Music" category. In both scatterplots, we can clearly see the strong positive correlation between variables. 
