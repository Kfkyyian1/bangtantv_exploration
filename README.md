![bts](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/3b97556d-88ab-42a0-b923-8c0b16752061)
# Overview & Background
This project delves into the official YouTube channel of BTS called [BANGTANTV](https://www.youtube.com/@BTS), a globally acclaimed K-pop group sensation with a vast international fanbase. Despite primarily featuring songs in Korean and English, BTS has garnered immense popularity worldwide. Each member of the group brings a distinct talent and persona, contributing uniquely to the group's success. The project seeks to analyze the channel dynamics and performance of  videos, shedding light on the viewership as well as engagement patterns associated with each member. 

_As a fan of Jungkook, I found his latest album "Golden" particularly intriguing, as it showcased a departure from his usual persona, unveiling a more nuanced musical style. It is fascinating to explore whether other ARMYs (BTS’s Fanbase) share similar biases and how they reflect in viewership trends._

# Summary of Key Findings
**1.	**Member Performance Analysis:****
- Jungkook emerges as the top contributor with the highest count of uploaded videos, views, and likes.
- V stands out with significant engagement despite a lower count of uploaded videos.
- Jimin secures the third position across major metrics, reflecting consistent viewer engagement.
- Jin excels in fostering audience interaction, evidenced by the highest count of comments.
- SUGA and RM maintain substantial presence and impact with their content, while J-Hope contributes consistently.
  
**2.	Video Duration and Views:** <br>
Most views fall within the 200 to 500-second mark, indicating sustained engagement with longer content such as music videos and behind-the-scenes footage.

**3. Published Day Impact:**<br>
Thursday, Friday, and Sunday emerge as optimal days for video uploads, garnering higher viewership.
  
**4. Publishing Patterns Heatmap:**<br>
The heatmap reveals peak viewing times, with Thursday and Friday afternoons, along with Sunday mornings, attracting the highest views.

**5. Violin Plot Analysis:**
- The majority of videos across all members fall within the 0-300 seconds duration range.
- SUGA stands out with a considerable number of shorter videos, suggesting a unique content strategy.

# Data Extraction
The data extraction was done by leveraging the YouTube API and BTS's channel ID ('UCLkAepWjdylmXSltofFvsYQ'). Download the code from _"bts_youtube_api_external.py"_ file.

The first task was to retrieve essential statistics about the channel. Through a custom function, 'get_channel_stats', key metrics were extracted such as subscriber count, total views, and video count. BTS's channel has an extensive repository of 2424 videos **(as of 26 December 2023)**. However, the default behavior of the code only yielded 5 video IDs. To remedy this, a pagination loop was implemented with page tokens, ensuring the retrieval of all 2424 video IDs associated with BTS's channel.

With the video IDs in hand, detailed information was collected about each video. Employing another custom function, 'get_video_details', metadata was retrieved encompassing titles, descriptions, view counts, likes, comments, and more for every video in the dataset. This process culminated in the creation of the final dictionary named 'video_df'. Spanning a breadth of insights, 'video_df' contains a comprehensive overview of BTS's YouTube channel, enabling nuanced analysis of viewer engagement, content performance, and publishing trends.

# Data Preparation
With the raw dataset, a few data cleaning steps were conducted. Download the code from _"bts_youtube_api_external.py"_ file.
1.	Handling Null Values: The dataset underwent a null value check, revealing an empty 'favouriteCount' column.
2.	Data Type Correction: To ensure consistency and facilitate numerical operations, columns such as 'viewCount', 'likeCount', 'favouriteCount', and 'commentCount' were converted from their original format to numeric.
3.	Publish Day Extraction: A new column, 'publishDayName', was introduced to denote the day of the week when each video was published. This involved converting the 'publishedAt' column to datetime objects, allowing for the extraction of the corresponding day of the week.
4.	Duration Standardization: Video durations, initially represented in a string format (e.g., PT2M25S), were standardized to seconds. This transformation was achieved using the isodate module, resulting in the creation of a new column named 'durationSecs' to express video durations uniformly.
Upon completion of these data preprocessing steps, the refined dataset was exported to a CSV format, ensuring compatibility with R for subsequent visualization and analysis tasks. 

# Data Cleaning & Video Categorization in R
After importing the data into R, a few additional data sanity check and cleaning steps were taken before visualising the data. Download the code from _"bts_youtube_external.Rmd"_ file.
1.	Column Removal: The 'favouriteCount' column, containing only NA values, and the 'definition' column were removed from the dataset as they were deemed non-essential for the analysis. <br>
![image](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/603fe19d-f0b8-43b3-bf7f-82e96721cc7a)

2. Video Categorization: To enhance analysis, a new column named 'member' was added to categorize each video based on its title. Initially, a lookup table dataframe was created to facilitate sustainable categorization of member names. Using pattern matching with the grepl function, member names were extracted from video titles. Videos with multiple member names were categorized as "Group", those with no member names as "Other", and if a single unique member name was identified, it was assigned to the 'member' column.
![image](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/fe6afd06-6ec1-4cdc-8a94-736f18468204)

3. Data Export: The cleaned dataset was exported to a CSV file to ensure data integrity and safekeeping for future analysis.
<br>
These steps ensured the dataset's readiness for visualization and analysis, streamlining the project's progression.

# Exploratory Analysis
## Bar Plot: Total Video Views and Likes By BTS Member
![1-Total Video Views and Likes by BTS Member](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/475cdf58-c3bd-42e4-b7c4-2b028247eb67)
![1-Summary Data-Screenshot 2024-02-13 at 2 00 04 PM](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/36fdb83e-447e-4c23-b6d9-ae77c51c576f) <br>
Based on the barplot and summary dataframe above (arranged by total views in descending order), we can observe that:
1.	Jungkook (JK) emerges as the highest contributor, boasting the highest count of uploaded videos, along with commanding the top position in both total views and likes. This indicates not only a consistent output of content but also a significant and engaged audience.
2.	V stands out prominently as the second-highest contributor in terms of total views, likes, and comments. Remarkably, V achieves this with a comparatively lower count of uploaded videos, underscoring the exceptional engagement and impact of each video.
3.	Jimin secures the third position across all major metrics—total views, likes, and comments. This consistency suggests a substantial and engaged viewership, contributing to the overall success of the channel.
4.	Jin, while maintaining a competitive position in terms of total views and likes, particularly excels in fostering audience interaction as evidenced by the highest count of comments among all members. This reflects a strong community engagement around Jin's content, emphasizing the qualitative aspect of audience participation.
5.	SUGA has a substantial number of videos and total views, indicating a significant presence on the platform.
6.	RM, despite having fewer videos compared to some other members, has a respectable total views count, showcasing a strong impact with each video.
7.	J-Hope maintains a consistent performance across total views, likes, and comments, contributing significantly to the overall engagement.

These observations highlight the diverse contributions of each member, with some excelling in specific metrics, while others demonstrate a balance across multiple aspects of audience interaction.

## Scatter Plot: Video Duration vs Total Video Views
![2-Video Duration vs Video Views](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/a2ca8358-9b98-44b3-abb0-caa1cd189c76)

The scatter plot highlights a concentration of views occurring between the 200 to 500-second mark (3.3 to 8.3 minutes). This trend aligns with the expectation that fans often engage with longer content, including music videos and behind-the-scenes footage, which are likely to capture their sustained interest and attention. 

## Bar Plot: Total Video Views By Published Day
![3 - Total Video Views By Published Day](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/ac01afa8-de22-4f9c-b74c-4c3a4838da66)

The bar plot illustrates the distribution of total video views based on the day of the week when the videos were published. Each bar represents a specific day of the week, ranging from Monday to Sunday. The height of each bar indicates the cumulative number of views garnered by videos published on that day. The plot identifies that Thursday, Friday, and Sunday are optimal days to publish videos for higher viewership. 

## Publishing Patterns: Day & Hour Heatmap by Total Views
![4-Publishing Patterns- Day and Hour Heatmap by Views](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/04d24bdc-fa81-4c58-903b-03df5c24d526)
This heatmap of publishing patterns was created to understand the optimal timing of postings on each day:
- Monday: 3PM
- Tuesday: 12PM
- Wednesday: 10AM <br>
- **Thursday: 3PM (highest views)** 
- **Friday: 1PM (highest views)** 
- Saturday: 10AM
- **Sunday: 10AM (highest views)**

## Violin Plot: Video Duration by BTS Member
![5-Video Duration Distribution by Member](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/aac76cb0-c8c3-42d7-9875-b29d98da28dc)

The plot shows a predominant trend where the majority of videos across all members fall within the 0-300 seconds duration range. Interestingly, a closer examination indicates that SUGA stands out with a considerable number of videos, particularly concentrated below the 150 seconds mark, distinguishing his content from other members. This observation suggests a potential stylistic or content preference specific to SUGA's video production strategy.

# Conclusion
Based on the exploratory analysis conducted, several insights emerge regarding the performance and audience engagement of BTS's YouTube channel:
1.	**Member Contribution Analysis:** Jungkook (JK) emerges as the highest contributor, leading in both total views and likes, showcasing a consistent content output and engaged audience. V stands out with significant impact despite fewer uploaded videos, highlighting exceptional engagement. 
2.	**Content Duration and Engagement:** The scatter plot illustrates a concentration of views between 200 to 500 seconds, indicating a preference for longer content such as music videos and behind-the-scenes footage. This aligns with audience expectations for engaging and immersive content experiences.
3.	**Optimal Publishing Days:** Analysis of total video views by published day reveals that Thursday, Friday, and Sunday are optimal days for video uploads, attracting higher viewership. This insight provides valuable guidance for content scheduling and audience engagement strategies.
4.	**Publishing Patterns:** The heatmap highlights optimal publishing times across different days, with Thursday and Friday afternoons, along with Sunday mornings, garnering the highest views. This detailed understanding of publishing patterns enables strategic content planning and audience outreach.
5.	**Video Duration Trends:** The violin plot underscores a predominant trend where most videos across all members fall within the 0-300 seconds duration range. Notably, SUGA's content stands out with a significant number of shorter videos, suggesting a unique stylistic approach or content preference specific to his production strategy. <br>
<br>
Overall, these findings offer valuable insights into BTS's YouTube channel dynamics, highlighting member contributions, audience engagement patterns, and strategic considerations for content creation and distribution. 

# Reference
- Thu Vu data analytics. (2022, January 22). YouTube API for Python: How to create a unique Data Portfolio Project [Video]. YouTube. https://www.youtube.com/watch?v=D56_Cx36oGY
- BTS (방탄소년단) (2023, June 9). [Image] Facebook. https://www.facebook.com/photo/?fbid=858730148944371&set=a.282831103200948

