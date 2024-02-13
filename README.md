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
After importing the data into R, a few additional data sanity check and cleaning steps were taken before visualising the data. 
1.	Column Removal: The 'favouriteCount' column, containing only NA values, and the 'definition' column were removed from the dataset as they were deemed non-essential for the analysis. <br>
![image](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/603fe19d-f0b8-43b3-bf7f-82e96721cc7a)

2. Video Categorization: To enhance analysis, a new column named 'member' was added to categorize each video based on its title. Initially, a lookup table dataframe was created to facilitate sustainable categorization of member names. Using pattern matching with the grepl function, member names were extracted from video titles. Videos with multiple member names were categorized as "Group", those with no member names as "Other", and if a single unique member name was identified, it was assigned to the 'member' column.
![image](https://github.com/Kfkyyian1/bangtantv_exploration/assets/146427900/7a6f313a-4fc6-44a0-8bc1-d2c256a38b09)

3. Data Export: The cleaned dataset was exported to a CSV file to ensure data integrity and safekeeping for future analysis.
<br>
These steps ensured the dataset's readiness for visualization and analysis, streamlining the project's progression.

# Exploratory Analysis



