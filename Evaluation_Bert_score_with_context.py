import torch
from bert_score import score



##################################################################################################################################################################################################


reference_answer_1 = """LeBron James has been performing at an elite level during the 2024-2025 NBA season, continuing to defy age and impress with his all-around game. As of January 2025, LeBron has been averaging over 25 points, 8 rebounds, and 7 assists per game, showcasing his versatility and leadership on the court. He has maintained his ability to impact the game in multiple ways, from scoring and playmaking to rebounding and defense. Notably, LeBron recently recorded his fourth consecutive triple-double, underlining his exceptional court vision and high basketball IQ.
At 39 years old, LeBron remains one of the league’s most efficient players, and his performance has been pivotal in keeping the Los Angeles Lakers competitive in the highly contested Western Conference. His mindset this season has been centered around maintaining peak physical condition and focusing on team success, which has helped him stay consistent and continue performing at a top-tier level. His leadership and ability to elevate teammates have been crucial in the Lakers' successes so far this season.
"""
reference_answer_2 = """LeBron James remains one of the best players in the NBA, continuing to deliver exceptional performances well into his 40s. As of January 2025, LeBron is averaging over 25 points, 8 rebounds, and 7 assists per game, showcasing his all-around game and ability to influence every facet of the court. His high basketball IQ and leadership have made him indispensable to the Los Angeles Lakers, and his ability to play at an MVP level at age 40 is a testament to his exceptional longevity and conditioning. He has recently recorded his fourth consecutive triple-double and continues to perform at an elite level, including highlight-worthy dunks and key plays, which make him a reliable asset for any fantasy team.
However, there are a few considerations before adding him to your roster. LeBron's age means that he could face rest days or moments of reduced performance later in the season, especially as the Lakers aim to manage his workload. Additionally, his personal life has recently been in the spotlight due to some allegations, but these have not affected his on-court performance. If you value consistency, high output across multiple categories, and leadership, LeBron James is still an excellent choice for your fantasy team, especially if you're looking for a player who can contribute in scoring, assists, and rebounds.
"""
reference_answer_3 = """LeBron James has been playing at an elite level during the 2024-2025 NBA season, continuing to defy expectations as he approaches his 40th birthday. As of January 2025, LeBron is averaging over 25 points, 8 rebounds, and 7 assists per game, demonstrating his versatility and ability to impact the game in multiple ways. He has been especially impressive in recent games, recording his fourth consecutive triple-double, showcasing his all-around skills and ability to contribute across scoring, playmaking, and rebounding.
Despite being 39 years old, LeBron remains one of the top performers in the league. His exceptional longevity and fitness have allowed him to maintain a high level of performance, and his leadership has been instrumental in the Los Angeles Lakers' competitive success in the Western Conference. Off the court, LeBron has opened up about his mindset for the season, focusing on maintaining peak physical condition and staying mentally sharp to continue elevating his game.
"""
reference_answer_4 = """Nikola Jokić has been performing at an exceptional level during the 2024-2025 NBA season for the Denver Nuggets. As of January 2025, he is averaging 30.6 points, 13.2 rebounds, and 9.9 assists per game. His contributions have been crucial to the Nuggets' success, with Jokić leading the team in both scoring and playmaking.
In addition to his impressive stats, Jokić has maintained an efficient shooting line with 57.1% from the field, 38% from three-point range, and 81.6% from the free-throw line. His all-around game has been a key factor in Denver's strong season, and his performance continues to solidify his position as one of the top players in the league.
Jokić’s ability to impact the game in multiple facets—scoring, rebounding, and playmaking—along with his efficiency, makes him one of the most valuable players in the NBA.
"""
reference_answer_5 = """Nikola Jokić is undoubtedly one of the top players in the NBA, with impressive stats across the board. His ability to contribute in multiple areas—scoring, rebounding, and playmaking—makes him a highly valuable asset for any fantasy basketball team. In his recent games, he has consistently delivered strong performances, such as a triple-double with 35 points, 12 rebounds, and 15 assists against the Brooklyn Nets on January 10, 2025.
However, Jokić's status for the game on January 14, 2025, is listed as "questionable" due to illness, which could be a risk for your fantasy team if you're looking for immediate results. It's worth considering this factor, especially with other potential injuries in the Denver Nuggets roster (e.g., Jamal Murray, Aaron Gordon). If Jokić plays, his performances are typically top-tier, and he has a good track record against the Dallas Mavericks.
If you're able to monitor his status before the game and confirm he's active, adding him to your team would be a solid decision given his overall consistency and upside. Just be cautious about his health status leading up to game time.
"""
reference_answer_6 = """Nikola Jokić's recent performances for the Denver Nuggets have been impressive. In his most recent game on January 13, 2025, the Nuggets defeated the Dallas Mavericks 118-99.
Here are some of his season stats for the 2023-24 NBA season:
•	Points per game (PPG): 28.7
•	Rebounds per game (RPG): 13.4
•	Assists per game (APG): 8.7
•	Field Goal Percentage (FG%): 53.1%
•	Three-Point Percentage (3P%): 24.4%
•	Free Throw Percentage (FT%): 69.8%
•	True Shooting Percentage (TS%): 62.5%
For the 2024-25 season, he is currently averaging 30.6 points per game (PPG), 13.2 rebounds per game (RPG), and 9.9 assists per game (APG). Jokić continues to be one of the best all-around players in the league, maintaining an efficient scoring rate and a high level of playmaking.
His performance has placed the Nuggets in a strong position with a 24-15 record, ranking them 3rd in the Western Conference.
"""
reference_answer_7 = """Goga Bitadze is currently listed as questionable for the Orlando Magic's upcoming game against the Milwaukee Bucks on January 17, 2025, due to a hip injury. Bitadze left Sunday's game against the Philadelphia 76ers early and did not participate in Tuesday's practice. His status is considered day-to-day, and if he is unable to play, Jonathan Isaac may step into a larger role.
In terms of his recent performance, while exact stats were not provided in the update, Bitadze's injury has limited his availability. If healthy, he typically contributes as a reserve big man, providing depth to the Magic's frontcourt. However, his current injury status may impact his immediate playing time and production.
"""
reference_answer_8 = """Given Goga Bitadze's current injury status, where he's listed as questionable with a hip contusion, adding him to your team may be risky at the moment. His day-to-day status suggests uncertainty around his availability for upcoming games, and if he remains sidelined, it could affect your team's performance.
If you need immediate contributions and can't afford the potential uncertainty, it might be better to wait until he returns to full health. However, if you have an open roster spot and are looking for a longer-term potential add once he's healthy, he could be a solid depth piece, especially if you need frontcourt support.
Keep an eye on his status leading up to game time and consider how it fits with your team’s needs and available roster space. If he misses time, Jonathan Isaac might be a better short-term option for the Magic's frontcourt.
"""
reference_answer_9 = """Goga Bitadze's recent performance has been impacted by an injury. He left Sunday's game against the 76ers early due to a right hip contusion and did not practice on Tuesday, which has led to him being listed as questionable for Wednesday's game against the Bucks. While his recent play before the injury isn't fully detailed, the injury status suggests that his availability and impact on the court are uncertain for the near future.
If Bitadze misses games, Jonathan Isaac could be in line for more playing time, which might affect Bitadze's role on the team in the short term. Keep an eye on his recovery and availability before considering him for your fantasy team.
"""
reference_answer_10 = """The Los Angeles Lakers are currently experiencing a bit of a rough patch in the NBA regular season. After a strong start, their recent performances have faltered. They are 20-17, sitting in 7th place in the Western Conference as of January 2025. Notably, there have been some postponed games due to external factors like wildfires in Los Angeles, affecting their rhythm.
In terms of individual performances, Austin Reaves has been a notable contributor, including a recent double-double against the Spurs with 12 points, five rebounds, and eight assists, though he struggled with shooting in that game. The Lakers have faced challenges but remain a competitive team in the standings.
"""
reference_answer_11 = """The Orlando Magic are currently navigating through some injury challenges but remain a competitive team in the NBA. Franz Wagner, a key player for the team, has been out due to a torn right oblique. He is expected to return once he is back in game shape. Before the injury, Wagner was performing impressively, recently scoring 35 points in a win against the 76ers, and contributing consistently in other games with strong scoring performances.
The team’s overall performance has been solid, with the Magic having managed notable victories, such as a win against Brooklyn. However, their momentum has been affected by the absence of key players like Wagner, and their injury recovery will be crucial for their continued success this season.
"""


##################################################################################################################################################################################################

answer_llama_1 = """LeBron James has been putting up incredible performances lately! According to his recent game data, he's averaging:
•	30 points per game
•	7.6 rebounds per game
•	8.8 assists per game
•	1.4 steals per game
•	0.9 blocks per game
In his most recent games, he's shown no signs of slowing down, putting up 38 points, 3 rebounds, and 8 assists in a recent game against the Portland Trail Blazers.
His advanced statistics also indicate that he's playing at an elite level, with a true shooting percentage of 58.5% and a player efficiency rating (PER) of 28.4, which is among the highest in the league this season.
It seems like LeBron James is still in top form, making him a great pickup for fantasy basketball owners!
"""
answer_llama_2 = """Based on the information provided, Lebron James is having a strong season with the Los Angeles Lakers. His recent performances have been impressive, with high scores in multiple categories such as points and assists.

However, without knowing more about your specific fantasy basketball league settings, roster structure, and current team situation, it's difficult to give a definitive answer.

That being said, Lebron James is generally considered a reliable and consistent performer in the NBA, so adding him to your team could be a good idea if:

You have space available on your roster
Your team needs more scoring or playmaking power
You're looking for a player with a strong track record of performance
It's worth considering the following factors before making a decision:

His current salary and cap hit in your fantasy league
The team's upcoming schedule and potential matchups against teams that might be able to contain him
Any other players on your roster who could be impacted by Lebron's addition (e.g., if you already have a strong scoring option, adding Lebron might not provide enough additional value)
If you're unsure, I can try to help you analyze the situation further or provide more information about Lebron James' fantasy basketball prospects.
"""
answer_llama_3 = """Based on the provided data, Lebron James' recent performances are impressive. Here's a summary:
•	In his last 4 games (January 2-7), he has averaged:
o	26.5 points per game
o	8.3 assists per game
o	6.8 rebounds per game
o	32 minutes of playing time per game
•	Specifically, in each of these games, he has scored at least 18 points, with a high of 30 points in one game.
•	He has also shown consistent shooting percentages, including:
o	FG%: 48.1%
o	3PT%: 35.7%
o	FT%: 84.2%
Overall, Lebron James' recent performance is strong, with high scoring averages and consistent playmaking and rebounding. He seems to be in top form, which makes him a great choice for fantasy basketball owners.
"""
answer_llama_4 = """Based on the provided data, I can see that Nikola Jokic's performance is being highlighted alongside other players in a boxscore-style format. However, there is no explicit information about his individual stats or overall performance.
That being said, I can suggest some possible ways to get an idea of how Nikola Jokic is performing:
1.	Check the latest NBA news and updates: Websites like ESPN, NBA.com, or sports news outlets often provide up-to-date information on player performances, including statistics, injuries, and other relevant details.
2.	Look for recent games' boxscores: You can search online for the most recent boxscores of Nikola Jokic's games, which will provide you with his individual stats, such as points, rebounds, assists, and others.
If you'd like to know more about Nikola Jokic's performance or get a general idea of how he's doing this season, I can try to provide some additional context based on publicly available information.
"""
answer_llama_5 = """Based on the provided information, it's difficult to make a definitive recommendation. However, I can offer some insights.
Nikola Jokic is having an incredible season with high points (23.4), assists (8.1), and rebounds (10.5) per game for the Denver Nuggets. His consistent production makes him a desirable player in fantasy basketball.
Considering his team dynamics, schedule, and opponent matchups, Jokic's performance should continue to be strong. The Nuggets have a favorable schedule ahead, with several games against weaker teams, which could boost his statistics.
In terms of your specific league settings, if you're playing a points-based scoring system, Jokic's scoring abilities might be appealing. However, if you're using a category-based system that emphasizes rebounding or assists, he might not be the top pick for you.
Given the current information and considering it might be limited, I would recommend adding Nikola Jokic to your team if:
1.	You have space in your roster for another player.
2.	Your league settings prioritize points scoring.
3.	You're looking for a consistent performer with strong statistics.
However, if you're on a tight budget or prefer to focus on other players, it's essential to evaluate your team's overall needs and make an informed decision based on your specific situation.
Would you like me to help you assess your team's current roster and recommend alternative players?
"""
answer_llama_6 = """Based on the provided data, I can provide some insights into Nikola Jokic's recent performance.
Nikola Jokic has been playing well lately, with a strong recent stretch. However, I don't have specific game-by-game statistics or performance metrics to share.
From the content source, we know that Victor Wembanyama (who is likely a player on Jokic's team) had a line of 8.0 points, 7.9 rebounds, and 6.7 assists against Lauri Markkanen (of the UTA Jazz) and Malik Beasley (of the DET Pistons). This suggests that Nikola Jokic has been playing well, but I don't have exact numbers to confirm this.
To get a better sense of Jokic's recent performance, I would recommend checking a reliable source such as NBA.com, ESPN, or a fantasy basketball website for up-to-date statistics and analysis.
"""
answer_llama_7 = """I don't have any information on Goga Bitadze's performance. The provided data only includes LeBron James, Nikola Jokic, and some team statistics for other players, but it does not include Goga Bitadze. If you're looking for more up-to-date information on Goga Bitadze's performance, I recommend checking the latest NBA stats or a reliable sports website."""
answer_llama_8 = """Based on the provided information, it appears that you may want to consider adding Goga Bitadze to your team. Here's why:
•	His recent performance is quite impressive: with 8.0 points per game, he's showing signs of a resurgence in his season.
•	The player mentions that Victor Wembanyama (SAS) has 8.0 points, and Lauri Markkanen (UTA) has 7.9 points, indicating that Bitadze is competing with top players for scoring opportunities.
However, I would like to know more about your team's current situation before making a definitive recommendation. Could you please provide some context about your team, such as:
•	Your current roster composition
•	Your team's scoring and rebounding needs
•	The scoring categories in your fantasy league (e.g., points, rebounds, etc.)
With this information, I can provide a more tailored advice on whether adding Goga Bitadze to your team is a good idea
"""
answer_llama_9 = """I don't have any information on Goga Bitadze's recent performance. The provided data only includes statistics and news articles about LeBron James, Nikola Jokic, Victor Wembanyama, Lauri Markkanen, Malik Beasley, Anthony Edwards, Tyler Herro, Damian Lillard, and other players, but not Goga Bitadze. If you're looking for information on Goga Bitadze's performance, I recommend checking the latest NBA statistics or sports news websites."""
answer_llama_10 ="""Based on the information provided, I can only find data on LeBron James' recent performances with the Los Angeles Lakers. However, it appears that he is having a strong season.
According to his recent game statistics (January 13, 2025), LeBron James had 18 points, 5 rebounds, and 8 assists in a game against the San Antonio Spurs. His performance on January 7, 2025, was also impressive, with 18 points, 10 rebounds, and 8 assists in a game against the Dallas Mavericks.
However, I couldn't find any information on the overall team performance of the Los Angeles Lakers. If you're looking for more specific information on their current standing or recent results, I'd be happy to try and help you find that information.
"""
answer_llama_11 = """I couldn't find any information about the Orlando Magic's performance in the data provided. The data only includes information about LeBron James and his recent performances, as well as some player stats for other teams (SAS, UTA, DET, MIA, and MIL). It does not include any information about the Orlando Magic.
However, I can suggest checking a reliable sports website or news source for information about the Orlando Magic's current performance. They should have up-to-date information on their recent games, standings, and statistics.
"""



##################################################################################################################################################################################################



answer_gemma_1 = """Player Evaluation: LeBron James
Strengths:
•	Excellent scoring average: 23.7 PTS per game
•	Consistent playmaker: 8.8 AST per game
•	Strong rebounder: 7.6 REB per game
•	Excellent all-around stats: PIE of 0.165
Weaknesses:
•	Increased turnovers: 1.6 TO per game
•	Susceptible to injuries: 3 games missed in the past month
Recent Performance:
•	Averaging 25 points, 8 assists, and 7 rebounds per game in the past 5 games.
•	Put up a season-high 38 points in a game against the Portland Trail Blazers.
Factors to Consider:
•	LeBron James' age (39) and potential for decline
•	Lakers' tough schedule with many games against strong opponents
•	Increasing injury risk
Recommendation:
Pick LeBron James immediately.
While his recent injury risk is concerning, LeBron James' recent performances and overall statistics make him one of the most valuable players in fantasy basketball. His scoring potential and all-around skillset are unmatched by many other players. However, be sure to monitor his injury situation before making a final decision.
Data-Driven Insights:
•	LeBron James has averaged 28.1 points, 8.6 assists, and 7.9 rebounds per game in the past 3 seasons.
•	He has recorded a triple-double in 10 of the past 15 games.
•	His current PTS per game is the highest of his career.
"""
answer_gemma_2 = """Recommendation: Pick LeBron James immediately.
Reasons:
•	Exceptional Recent Performances: LeBron James has averaged 23.7 points, 8.8 assists, and 7.6 rebounds per game in the current season, showcasing remarkable consistency and dominance.
•	Elite Scoring Potential: His recent performances demonstrate his ability to consistently score points, averaging 30.8 points in the last 5 games.
•	Sustained Longevity: Across his 21-year career, LeBron James has maintained an exceptional level of play, showing no signs of decline.
•	High Value for Fantasy Teams: In leagues with points-based scoring, LeBron James is a guaranteed double-double machine, making him an invaluable asset.
Additional Considerations:
•	His recent matchups have been relatively favorable, contributing to his impressive scoring numbers. However, his upcoming opponents are also strong, suggesting his scoring potential may remain high.
•	While his age might be a concern for some, his exceptional skills and mental fortitude suggest he can continue to perform at a high level.
Conclusion:
LeBron James' combination of exceptional performance, sustained longevity, and high fantasy value makes him an optimal pick for your team. Given his recent dominance and sustained scoring potential, he is likely to remain one of the most valuable players in your league.
"""
answer_gemma_3 = """Player Evaluation: LeBron James
Recent Performance:
•	Averaging 23.7 points, 8.8 assists, and 7.6 rebounds per game this season.
•	Posted impressive stat lines in recent games: 38 points, 3 rebounds, 8 assists vs. Portland; 30 points, 3 rebounds, 8 assists vs. Atlanta; 21 points, 13 rebounds, 9 assists vs. Houston.
Positives:
•	Exceptional scoring ability with elite FG% and FT%.
•	Consistent playmaking and high assist numbers.
•	Excellent rebounder for his size.
•	Strong leadership and team presence.
Negatives:
•	Increased turnovers this season (2.7 per game).
•	Age (39) may be a concern for long-term durability.
Recommendation:
Pick him immediately!
While his turnovers are slightly concerning, LeBron James' overall performance, leadership qualities, and recent production make him an invaluable asset to any fantasy basketball team. His ability to contribute in multiple statistical categories and lead his team makes him a safe and reliable pick.
"""
answer_gemma_4 = """Player Evaluation: LeBron James
Strengths:
•	Recent scoring output: 23.7 PTS in 2024-25.
•	Consistent playmaking: 8.8 AST per game.
•	Strong rebounding: 7.6 REB per game.
•	Excellent free-throw shooting: 84.7% FT.
Weaknesses:
•	Increased turnovers: 3.0 TO per game.
•	Susceptible to injury: 3 recent games with minutes limitations.
Recent Performance:
•	5 games averaging 23.8 PTS, 7.8 REB, 8.8 AST, and 32.8 MPG.
•	Put up a season-high 38 PTS in a recent game.
Analysis:
LeBron James is currently playing at an elite level and should be considered a top fantasy basketball option. His recent performances, combined with his consistent playmaking and rebounding, make him a valuable asset. However, his increased turnovers and injury concerns should be monitored.
Recommendation:
Keep LeBron James in your starting lineup for his current production and potential. Be aware of his injury risk and manage his minutes accordingly.
Additional Notes:
•	The provided text does not contain any information regarding Nikola Jokic's performance.
•	This evaluation is based on the information available in the provided sources.
"""
answer_gemma_5 = """Recommendation: Consider dropping Nikola Jokic from your team.
Reasoning:
While LeBron James has indeed been having a phenomenal season, suggesting that he has reached his peak is inaccurate. However, this analysis reveals crucial information about Jokic's performance in comparison to LeBron James:
•	Points: LeBron James is averaging 23.7 points per game, while Jokic is averaging 23.8 points per game.
•	Efficiency: LeBron James has a Player Efficiency Index (PIE) of 0.165, while Jokic has a PIE of 1.330.
•	Advanced Stats: LeBron James leads in assists per game (8.8) compared to Jokic (8.7), but Jokic dominates in rebounds per game (11.8) and blocks per game (2.4).
Considerations:
•	Your league's scoring categories and team needs should be factored in. If your league prioritizes assists or rebounds, Jokic's value might be higher.
•	LeBron James' recent performances are undoubtedly impressive, but his season-long stats still fall slightly behind Jokic's.
Conclusion:
While LeBron James' performance this season is undoubtedly remarkable, the available data suggests that Nikola Jokic remains the superior fantasy basketball player based on his overall production and advanced stats. Given LeBron James' consistency and recent remarkable performances, dropping Jokic might be a viable option if your team needs other positions more.
"""
answer_gemma_6 = """Player Evaluation: LeBron James
Strengths:
•	Averaging 23.7 PTS, 8.8 AST, and 7.6 REB per game this season
•	Played 36+ minutes in every game this month
•	Put up 38 PTS in a recent game against Portland
•	Excellent playmaking abilities with 8.8 AST per game
Weaknesses:
•	Struggles with turnovers (4.3 TO per game)
•	Below-average shooting percentages (48.3% FG%, 35.7% 3PT%)
Recent Performance:
•	4 solid games in a row, averaging 24 PTS, 8 AST, and 8 REB
•	Played with heightened efficiency in the past week (FG% of 50%)
Recommendation: Pick LeBron James immediately. His recent performances and overall statistics suggest he's a valuable asset for your fantasy team. While his turnovers are a concern, his scoring, playmaking, and rebounding abilities outweigh that risk.
Additional Notes:
•	LeBron James' workload and minutes might be slightly reduced with the return of Anthony Davis. This could slightly impact his fantasy production.
•	Consider his upcoming matchup against the Minnesota Timberwolves, who are allowing the 8th most points per game to opponents. This could be another opportunity for LeBron to continue his impressive scoring streak.

"""
answer_gemma_7 = """Player Evaluation: LeBron James
Strengths:
•	Exceptional scoring: 23.7 PTS per game this season.
•	Elite playmaking: 8.8 AST per game.
•	Solid rebounding: 7.6 REB per game.
•	High basketball IQ: Excellent passer and teammate.
•	Durable: Played all 48 games this season (as of January 14th).
Weaknesses:
•	Increased turnovers: 3.6 TO per game this season (career high).
•	Shooting efficiency concerns: 48.9% FG and 35.6% 3P in the last month.
Recent Performance:
•	Averaging 26.5 PTS, 8.8 AST, and 7.8 REB in the last 5 games.
•	Recorded his 19th career triple-double in the last game against the Nuggets.
Fantasy Impact:
LeBron James is an automatic starting point in most leagues due to his elite stats and consistent production. However, his recent turnovers and shooting inefficiency might slightly impact his fantasy production.
Recommendations:
•	Consider dropping him if:
o	You are in a points-per-game league and his turnovers become a significant issue.
o	You have other players with better shooting percentages and offensive upside.
•	Continue drafting him if:
o	You are in a category-based league where his assists and rebounds are valuable.
o	You believe his shooting efficiency will improve and he returns to his dominant scoring form.
Additional Considerations:
•	Goga Bitadze's performance has been inconsistent this season, averaging 5.8 PTS and 3.8 REB per game. He has shown flashes of potential, but remains a limited offensive player.
"""
answer_gemma_8 = """Recommendation: Avoid Goga Bitadze
Reasoning:
While LeBron James' recent performances are indeed remarkable, his recommendation for Goga Bitadze doesn't align with his comments. LeBron James emphasizes maintaining a balanced approach and prioritizing team success over individual accolades. Considering Bitadze's limited playing time and inconsistent production, it's unlikely he's a key factor in the Lakers' success.
Data Points:
•	Bitadze has averaged just 10.8 minutes per game this season, significantly less than LeBron James' 34.6 minutes.
•	His scoring average is a mere 4.5 points per game, significantly lower than LeBron James' 23.7 points per game.
•	His recent performances haven't shown significant improvement in these areas.
Therefore, based on LeBron James' mindset and the available data, there's little reason to believe adding Bitadze would contribute meaningfully to your fantasy basketball team.
"""
answer_gemma_9 = """I do not have access to real-time information or current player performance data, so I am unable to provide any information regarding Goga Bitadze's recent performance. For the most up-to-date information, please check reputable sports news sources or the official NBA website."""
answer_gemma_10 = """Player Evaluation: LeBron James
Strengths:
•	Consistent scoring: Averaging 23.7 points per game this season.
•	Excellent playmaking: 8.8 assists per game.
•	Strong rebounding: 7.6 rebounds per game.
•	High shooting efficiency: 52.8% FG and 35.4% 3PT.
Weaknesses:
•	Increased turnovers: 5.8 turnovers per game.
•	Susceptible to injuries: Missed 4 games this season due to injury.
Recent Performance:
•	Averaging 24.8 points, 8.8 assists, and 7.8 rebounds in the last 5 games.
•	Put up a season-high 38 points against the Portland Trail Blazers on January 2nd.
Fantasy Implications:
Pick:
•	LeBron James' combination of scoring, playmaking, and rebounding makes him an invaluable asset in most fantasy leagues.
•	His high FG% and 3PT% suggest he can consistently put points on the board.
•	His recent performances indicate he's playing at an elite level.
Considerations:
•	His increased turnovers may slightly impact his fantasy production.
•	His injury risk should be monitored.
Overall Recommendation:
Pick LeBron James immediately for his exceptional scoring potential, playmaking abilities, and overall dominance on the court.
"""
answer_gemma_11 = """Player Evaluation: LeBron James
Strengths:
•	Consistent scoring: averaging 23.7 points per game this season
•	Excellent playmaking: 8.8 assists per game
•	Strong rebounding: 7.6 rebounds per game
•	Excellent minutes per game: 35.6
Weaknesses:
•	Increased turnovers: 4.3 turnovers per game this season (career-high)
•	Lower free throw percentage: 73.6% this season (career-low)
Recent Performance:
•	Averaging 24.8 points, 8.2 assists, and 7.8 rebounds in the last 5 games.
•	Put up a season-high 38 points against the Portland Trail Blazers on January 2nd.
Verdict:
LeBron James is still one of the best players in the NBA despite his recent turnover and FT struggles. His incredible scoring, playmaking, and rebounding make him a valuable asset for fantasy teams. However, his increased turnovers and lower FT% are concerning and should be monitored.
Recommendation:
Keep LeBron James in your fantasy team for his overall production and potential to overcome his recent struggles.
"""






##################################################################################################################################################################################################


answer_mistral_1 = """Based on the provided data and recent performances, LeBron James is having a strong season for the Los Angeles Lakers. In the last five games, his averages are: 27.4 points, 8.2 assists, 7.6 rebounds, and a Player Impact Estimate (PIE) of 0.165. This level of performance makes him a valuable asset in fantasy basketball leagues, especially in categories such as points, assists, and PIE.
Considering his recent performances and the context provided about his mindset and focus, I would recommend considering adding LeBron James to your roster if he is available. His consistent production and commitment to improving his game make him an attractive option for fantasy basketball success.
"""
answer_mistral_2 = """Based on the impressive statistics and consistent performance from LeBron James, adding him to your team would significantly boost your roster. His scoring potential (23.7 PTS/G), assist average (8.8 AST/G), and strong rebounding abilities (7.6 REB/G) make him a valuable asset in most fantasy leagues.
However, it's essential to consider your team needs and the availability of other players on the waiver wire before making the decision to add James. If he is available and fits within your roster structure, I would highly recommend adding him immediately for his standout performance this season.
Keep in mind that while LeBron's recent performances have been exceptional, it's important to also consider opponent matchups, injuries, and team dynamics moving forward. Injury reports should be closely monitored to ensure he remains healthy throughout the rest of the NBA season.
"""
answer_mistral_3 = """Based on the provided data and additional sources, it appears that Lebron James has been putting up strong performances recently for the Los Angeles Lakers. His season stats show an average of 23.7 points per game (PTS), 8.8 assists per game (AST), and 7.6 rebounds per game (REB) over the 2024-25 season, with several notable games including scoring 18, 18, 21, 30, and 38 points in his last five matches.
Given this recent performance and impressive statistics, it would be advisable for fantasy basketball players to consider picking LeBron James, especially if they need a boost in points, assists, or rebounds in their league. However, it's essential to evaluate the specific needs of your team and the league settings when making a decision on adding him to your roster.
Keep in mind that while Lebron James has been performing well recently, it's crucial to monitor his injury status as he could be at risk for some minor injuries due to his aggressive playing style. By staying updated with any potential injuries or changes in his role within the team, you can make informed decisions on when to start and sit him in your lineup.
Overall, considering Lebron James' impressive performance this season and his potential to continue dominating games, he is a valuable addition for fantasy basketball players looking to improve their roster. Just remember to weigh the specific needs of your team and the league settings before making any decisions on picking or dropping players.
"""
answer_mistral_4 = """Nikola Jokic has been consistently performing well this season with the Denver Nuggets, averaging 27 points, 13 rebounds, and 9 assists per game in the given timeframe. His recent statistics show that he's been scoring at a high rate and contributing significantly to his team's success. Given his consistent performance, advanced basketball statistics (e.g., field goal percentage), and team role as one of the key players for the Nuggets, Nikola Jokic is a strong pickup in most fantasy leagues due to his high scoring potential.
For context, make sure to consider your league settings and needs, as well as the roster structure. In terms of matchups, Jokic often faces tough opponents, so it's essential to analyze upcoming schedules before making a move. If there are other players with similar or better performance available on the waiver wire, compare their statistics and team roles before deciding which player is a better fit for your fantasy roster.
"""
answer_mistral_5 = """Based on the data provided, Nikola Jokic (PLAYER_ID: 2075) is having a fantastic season with impressive statistics across multiple categories. His average points (PTS: 26.1), rebounds (REB: 13.8), and assists (AST: 9.6) make him a valuable asset in almost any fantasy league setting.
LeBron James (PLAYER_ID: 2544), on the other hand, has also been performing exceptionally well this season, with an average of 23.7 points, 7.6 rebounds, and 8.8 assists per game. However, considering the depth of his position, it might be more beneficial to prioritize adding a player in a different position, especially if you need help elsewhere on your roster.
Considering the data available for both players and their respective positions, I would recommend adding Nikola Jokic (PLAYER_ID: 2075) to your team due to his well-rounded performance and consistent production throughout the season so far. This recommendation is based on a points-based fantasy league, but it may vary depending on your specific league settings and team needs.
Remember that player performances can change over the course of the season due to various factors such as injuries, trades, or changes in team dynamics. Keep monitoring the situation and adjust your roster accordingly to maximize your chances of success in your fantasy basketball league. Good luck!
"""
answer_mistral_6 = """Based on the provided data, Nikola Jokic's recent performance has been impressive. In the five games listed, he averaged 21 points, 8 assists, and 7 rebounds per game. His minutes played ranged from 30 to 36 minutes in each game, indicating a consistent role within his team.
Regarding LeBron James, his recent performance has also been noteworthy, as he averaged 25 points, 8 assists, and 7 rebounds per game over the five games provided. However, it's important to note that each player's context within their respective teams, schedules, and matchups should be taken into account when making fantasy basketball decisions.
In this situation, both players are performing well, but your choice between them might depend on your specific league settings, team needs, and roster structure. For example, if you need more points or rebounds, LeBron James may be the better option due to his higher averages in those categories. If you're looking for more assists, Jokic could be a stronger choice. It's essential to consider all factors when making decisions for your fantasy team.
"""
answer_mistral_7 = """Based on the provided data, Goga Bitadze does not have any recent performance data for the given time frame (2024-25 season). However, it's important to note that advanced basketball statistics such as points, rebounds, assists, steals, blocks, turnovers, field goal percentage (FG%), and free throw percentage (FT%) are crucial in assessing a player's performance.
For Goga Bitadze, we can analyze his season stats: PTS - 6.4, AST - 1.5, REB - 3.9, FG% - 0.517, FT% - 0.732. These numbers suggest that he has been contributing modestly in the statistical categories relevant to fantasy basketball leagues.
To get a better understanding of his performance and potential value for your fantasy team, I recommend keeping an eye on his recent games and updates regarding his role within his team. It's also essential to consider factors such as injuries, schedule, and opponent matchups when making decisions in fantasy basketball.
In conclusion, if you are looking for a consistent contributor across multiple categories, Goga Bitadze might not be the best option at this time due to limited recent performance data. However, it's important to monitor his development throughout the season for potential opportunities.
"""
answer_mistral_8 = """Based on the data provided, LeBron James is having a strong season with impressive statistics across multiple categories. However, since you've asked about adding Goga Bitadze to your team, let's analyze that player instead.
Goga Bitadze plays center for the Indiana Pacers and has averaged 6.2 points, 5.3 rebounds, and 1.3 assists per game this season (as of January 14th, 2025). Given that you didn't provide specific information about your fantasy league, I will provide a general recommendation:
It depends on the structure of your league and your team needs. If your league emphasizes categories such as rebounds and blocks, Bitadze could be a valuable addition due to his solid rebounding numbers and potential for blocks. However, if your league is points-based or focuses more on assists, steals, or 3-point percentage, there might be other players who would contribute more to your team's success.
In this case, I recommend considering the strengths of both players (LeBron James and Goga Bitadze) in relation to your league settings and team needs before making a decision on whether to add Goga Bitadze to your roster. If you need assistance with finding suitable alternatives or want help tailoring this advice for your specific league, feel free to ask!
"""
answer_mistral_9 = """Based on the data provided, Goga Bitadze has not been included in the given players. However, if we analyze his recent games based on the format and context you've specified:
Goga Bitadze has had a relatively consistent role in the Indiana Pacers, averaging around 10 minutes per game over the past few games. His stat line includes an average of 3 points, 4 rebounds, and 0.5 assists. However, his field goal percentage (FG%) is quite low at about 38%, which suggests room for improvement in this area.
In terms of advanced statistics such as blocks and steals, Bitadze does not contribute significantly to those categories. Given these numbers and the limited playing time he receives, I would advise you to look for other options if you are searching for a player who can provide a consistent statistical impact.
However, it's important to consider league settings, team needs, and roster structure when making recommendations in a fantasy basketball context. If Bitadze fits well with your team's requirements and there is limited availability on the waiver wire, he could be an option for short-term value. Keep monitoring his playing time and performance to determine whether he can contribute positively to your team in the long run.
"""
answer_mistral_10 = ""
answer_mistral_11 = """The Orlando Magic have been struggling this season, currently holding a record of 12 wins and 30 losses. In the context of fantasy basketball, facing teams with poor records such as the Magic can often result in increased opportunities for players to accumulate points and statistics. However, it's essential to consider whether LeBron James is more likely to shine against a struggling team like Orlando, given his track record of performing well regardless of opponent strength.
In your league settings, if points are a significant scoring category, you might want to consider adding LeBron James to your roster for this matchup due to his impressive scoring potential. On the other hand, if assists or rebounds are heavily weighted in your league, you may need to evaluate other options as well.
LeBron James' recent performance has been outstanding, averaging 23.7 points, 8.8 assists, and 7.6 rebounds per game this season. While his playing time remains consistent, there's always a risk of injury or rest days, so it's crucial to monitor his status closely.
Considering all factors, adding LeBron James to your roster for the upcoming matchup against Orlando could provide an excellent short-term boost. Just remember to keep an eye on his playing time and any potential injuries.
"""








##################################################################################################################################################################################################




def compute_bertscore(reference_answer, model_answer_llama, model_answer_gemma, model_answer_mistral):
    # Vergleiche Modellantwort Llama mit Referenzantwort
    P_llama, R_llama, F1_llama = score([answer_llama_11], [reference_answer_11], lang="de")
    print(f"Modell Llama F1-Score: {F1_llama.mean().item():.4f}")

    # Vergleiche Modellantwort Gemma mit Referenzantwort
    P_gemma, R_gemma, F1_gemma = score([answer_gemma_11], [reference_answer_11], lang="de")
    print(f"Modell Gemma F1-Score: {F1_gemma.mean().item():.4f}")

    # Vergleiche Modellantwort Mistral mit Referenzantwort
    P_mistral, R_mistral, F1_mistral = score([answer_mistral_11], [reference_answer_11], lang="de")
    print(f"Modell Mistral F1-Score: {F1_mistral.mean().item():.4f}")



# Führen Sie den BERTScore-Vergleich durch
compute_bertscore(reference_answer_11,answer_llama_11, answer_gemma_11, answer_mistral_11)