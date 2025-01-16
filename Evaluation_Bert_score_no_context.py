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

answer_llama_1 = """According to his recent game performance data, LeBron James has been putting up incredible numbers with the Los Angeles Lakers. In his most recent games, as shown in his 'RecentGames' list, LeBron has consistently scored over 30 points per game, with a high of 38 points in one of his last two games.
Here are some specific stats from his last few games:
•	January 2nd game against the Portland Trail Blazers: 38 points, 3 rebounds, 8 assists
•	January 3rd game against the Atlanta Hawks: 30 points, 3 rebounds, 8 assists
•	January 5th game against the Houston Rockets: 21 points, 13 rebounds, 9 assists
•	January 7th game against the Dallas Mavericks: 18 points, 10 rebounds, 8 assists
•	January 13th game against the San Antonio Spurs: 18 points, 5 rebounds, 8 assists
These numbers are impressive, especially considering his age and the fact that he's playing in the NBA for a 21st consecutive season. LeBron is consistently putting up strong individual numbers, but it's also worth noting that his team has been struggling overall this season.
In terms of his overall season performance, as shown in his 'SeasonStats', LeBron James has averaged 23.7 points per game, with 8.8 assists and 7.6 rebounds. He's also had a relatively high PER (Player Efficiency Rating) of 0.165.
Overall, LeBron James is performing incredibly well this season, and it's clear that he's still one of the most dominant players in the NBA.
"""
answer_llama_2 = """Based on the latest performance data and LeBron's recent games, I would highly recommend adding him to your team.
LeBron is having an incredible season, consistently scoring around 20-30 points per game and providing a triple-double threat with his assists (8.2) and rebounds (6.6). His recent performances, including a notable 38-point outing against POR on January 2nd, showcase his ability to dominate games on both ends of the court.
Additionally, LeBron's season stats are impressive, with a points average of 23.7 and an assist average of 8.8. He's also been efficient from the field, with a field goal percentage (FG%) of around 50%.
Considering your league settings, I assume you're looking for players who can provide consistent scoring, rebounding, and playmaking capabilities. LeBron fits the bill perfectly.
Before making the move, make sure to check your team's roster constraints and available spaces. If you have a slot open, adding LeBron would be an excellent decision.

"""
answer_llama_3 = """Based on the provided information, LeBron James' recent performance is impressive. Over his last 10 games, he's averaging:
•	25.8 points
•	6.6 rebounds
•	8.2 assists
•	A combined 1.3 steals-plus-blocks
Additionally, his recent performances include:
•	18 points in a game against the SAS on January 13, 2025
•	18 points in a game against DAL on January 7, 2025
•	21 points in a game against HOU on January 5, 2025
•	30 points in a game against ATL on January 3, 2025
•	38 points in a game against POR on January 2, 2025
These numbers indicate that LeBron James is still performing at an elite level, even at the age of 40.

"""
answer_llama_4 = """Nikola Jokić has been consistently impressive this season. His recent games showcase his exceptional all-around skills. Here are some key statistics from his recent performances:
•	In his last game (JAN 14, 2025), against the Dallas Mavericks, he scored 10 points, grabbed 14 rebounds, and chipped in with 10 assists, playing 29 minutes.
•	His previous performance (JAN 12, 2025), also against the Mavericks, saw him score 19 points, grab 18 rebounds, and provide 9 assists, while logging 39 minutes on the court.
•	In his most recent outing (JAN 10, 2025) before those, he recorded an impressive 35 points, along with 12 rebounds and 15 assists over 38 minutes.
Jokić's season statistics are equally remarkable. With 30.6 points per game, 9.9 assists, and 13.2 rebounds, he is one of the top performers in the league. His efficiency metrics also demonstrate his dominance: a field goal percentage (FG%) of .466 and a free throw percentage (FT%) of .783.
Considering these statistics and recent performances, it seems that Nikola Jokić remains an excellent choice for fantasy basketball teams, especially given his consistent scoring and rebounding capabilities, combined with solid assist numbers.
"""
answer_llama_5 = """Whether or not you should add Nikola Jokic to your team depends on various factors, including:
1.	Your team's current roster: Consider the players already on your team and their roles in your lineup. Do you have a center who can provide similar stats to Jokic?
2.	Your fantasy football/scoring settings: Look at your scoring system and consider how Jokic's statistics will fit into it. For example, if he provides strong rebounding, passing, or shooting numbers, they might be valuable in your league.
3.	Jokic's recent performance: Take a look at his recent stats (in the last 7-10 games) to see if he's been consistent and producing the numbers you're looking for.
4.	Injury concerns: Check if Jokic has any known injuries or health issues that could impact his availability for upcoming games.
Assuming you've considered these factors, here are some general pros and cons to help you decide:
Pros:
•	Dominant center: Jokic is a 7-foot center who provides strong rebounding, passing, and scoring numbers.
•	Consistency: He's been one of the top centers in the league for several seasons, providing consistent production.
•	High upside: Jokic has the potential to dominate games on both ends of the floor, making him a valuable addition to any team.
Cons:
•	Dependence on multiple categories: Jokic's fantasy value is tied to multiple categories (rebounding, passing, scoring), which means you'll need to balance his stats with those of other players.
•	Injury concerns: As mentioned earlier, check if Jokic has any known injuries or health issues that could impact his availability.
Overall:
If you're looking for a dominant center who provides strong all-around numbers, Nikola Jokic is definitely worth considering. However, make sure to assess your team's specific needs and consider the pros and cons mentioned above.
"""
answer_llama_6 = """The recent performance of Nikola Jokić can be seen in his statistics and game logs from the 2024-25 NBA season. Here are some key metrics:
PPG (Points Per Game): Jokić has averaged 30.6 points per game, which is one of the highest averages in the league.
RPG (Rebounds Per Game): He has averaged 13.2 rebounds per game, which is also very high and indicative of his versatility as a player.
APG (Assists Per Game): Jokić has averaged 9.9 assists per game, showcasing his exceptional playmaking ability and vision on the court.
Steals: He has an average of 1.67 steals per game, which is impressive for a big man.
Overall, Nikola Jokić's recent performance has been outstanding, with him dominating games on both ends of the floor. His stats are among the best in the league, and he continues to be one of the most valuable players in the NBA.
"""
answer_llama_7 = """Goga Bitadze has been showing some promising signs in his recent games. According to his 'RecentGames' data, he's had a few standout performances with significant rebounding and scoring contributions.
In his last 5 games, Bitadze has averaged around 7-8 points per game, which is relatively consistent for him. His rebounding numbers are particularly impressive, with an average of around 6-7 rebounds per game, showcasing his strength in the paint.
However, it's worth noting that his scoring averages have been somewhat inconsistent throughout the season. He's had stretches where he scores in double digits, but also has games where he struggles to find his rhythm.
Overall, while Bitadze isn't a top-tier player just yet, he shows flashes of potential and could be a solid addition to fantasy lineups if you're looking for a rebounding specialist with some scoring upside.
"""
answer_llama_8 = """Based on the provided data, it seems that Goga Bitadze has been performing reasonably well in his recent games. His last five games have shown some promising numbers:
•	January 5th: 9 points, 11 rebounds
•	January 6th: 6 points, 8 rebounds, and 4 assists
•	January 9th: 15 points, 8 rebounds, and 2 assists
However, we should also consider the overall season statistics for Goga Bitadze:
•	In 23 games this season (from the given data), Goga Bitadze has averaged:
o	9.6 points
o	8.2 rebounds
o	2.4 assists
While his recent performance is encouraging, we need to remember that these numbers can fluctuate from game to game.
Additionally, considering his role on the Orlando Magic team and the overall team performance (28-15), I would caution against picking Goga Bitadze based solely on recent form without more context or a deeper look at the team's overall potential.
Before making a decision, you may want to consider other factors such as:
•	Team injuries and suspensions
•	Upcoming schedule
•	Strength of opponents
Given the current data, I would recommend keeping an eye on Goga Bitadze and monitoring his performance in future games before making any decisions about adding him to your team.
"""
answer_llama_9 = """Goga Bitadze has had a recent stretch of performances that show promise. Here's a breakdown of his last 5 games:
•	January 6, 2025: 4 points, 8 rebounds, 4 assists, and 22 minutes in an Orlando Magic loss to the New York Knicks.
•	January 5, 2025: 9 points, 11 rebounds, 4 assists, and 29 minutes in a Utah Jazz loss to the Orlando Magic.
•	January 4, 2025 (not shown): Unfortunately, I don't have information on this game as it's not shown in the data provided. However, Bitadze has been playing more consistently lately.
Overall, Goga Bitadze has been providing decent production off the bench for his team. He's averaging around 6-8 points and 7-9 rebounds per game over his last three appearances. His assist numbers are also increasing, which could indicate an improvement in his court vision and passing abilities.
Keep in mind that this is just a snapshot of Bitadze's recent performance, and it's essential to consider the context of the team's overall season, as well as any potential injuries or other factors that might impact his production.
"""
answer_llama_10 ="""Based on the provided data, I can give you an overview of the Los Angeles Lakers' performance in their recent games. However, please note that this data is limited to a specific set of dates and opponents.
From the information provided, here's what we can gather:
Recent Performance:
•	The Lakers have played against several teams recently, including the Sacramento Kings, Atlanta Hawks, Miami Heat, Minnesota Timberwolves, Utah Jazz, Portland Trail Blazers, Cleveland Cavaliers, Brooklyn Nets, Boston Celtics, and Phoenix Suns.
•	Their performance has been mixed, with some wins and losses in these games.
Individual Player Performance:
•	LeBron James has been performing well, with high scores in most of his recent games (18-38 points per game).
•	Rui Hachimura has also shown promise, but his scoring averages are slightly lower (9-13 points per game) compared to LeBron.
•	Christian Wood is not playing for the Lakers, so we can't assess his performance.
Team Statistics:
•	The Lakers have had some strong games on offense, with an average of 110-115 points scored per game.
•	On defense, they have struggled at times, allowing opponents to score around 105-110 points per game.
Keep in mind that this data is limited and might not reflect the current season's performance. For a more accurate assessment of the Lakers' overall performance, I would recommend checking recent sports news or official NBA statistics.
"""
answer_llama_11 = ""



##################################################################################################################################################################################################



answer_gemma_1 = """Player Evaluation: LeBron James
Strengths:
•	Recent performances: averaging 23.7 points, 8.8 assists, and 7.6 rebounds per game.
•	Excellent playmaking: top-5 in assists per game in the NBA.
•	Consistent scoring: 3rd in the league in points per game.
•	Strong rebounder for his position.
Weaknesses:
•	Increased turnovers: averaging 0.165 turnovers per game.
•	Susceptible to occasional injury concerns.
Recommendation:
Pick immediately. LeBron James is playing at an MVP-caliber level and his recent performances are statistically impressive. His leadership and all-around production make him an invaluable asset to any fantasy team. However, be aware of the slight increase in turnovers and potential for minor injuries.
Additional Insights:
•	James' incredible season performance can be attributed to his focus on simplicity and efficiency on the court.
•	His remarkable longevity and consistent production suggest he can maintain his current level of play for the foreseeable future.

"""
answer_gemma_2 = """Recommendation: Pick LeBron James
Reasons:
•	Exceptional Recent Form: LeBron James has averaged 23.7 points, 8.8 assists, and 7.6 rebounds in his recent games, showcasing remarkable consistency and scoring prowess.
•	Peak Performance: Despite 21 seasons in the NBA, LeBron James appears to be reaching his peak, as evidenced by his recent performances and insightful comments on his mindset.
•	Durable and Reliable: Despite his age, LeBron James has maintained remarkable durability, playing all 82 games in the previous two seasons and showing minimal injury concerns.
Considerations:
•	League Format: Ensure your league allows fantasy acquisition of active players.
•	Roster Construction: LeBron James would be a valuable asset regardless of your team's current composition.
Additional Insights:
•	His recent matchups have been relatively favorable, suggesting his production could remain high in the coming games.
•	His leadership and experience will benefit your team both statistically and tactically.
Conclusion:
LeBron James' exceptional performance, peak potential, and remarkable durability make him a highly recommended pick for your fantasy basketball team.
"""
answer_gemma_3 = """LeBron James Player Evaluation:
Recent Performance:
•	Excellent scoring: 23.7 PTS per game in the last season.
•	Consistent play: Averaged 20.3 PTS, 7.6 REB, and 8.8 AST over the past 5 games.
•	Strong shooting: 50.6% FG and 35.3% 3PT in the past 5 games.
Positives:
•	Excellent scorer and playmaker.
•	Strong rebounder for his size.
•	High basketball IQ and leadership qualities.
•	Durable and consistent performer.
Negatives:
•	Increasing turnovers in recent games.
•	Age (39) might be catching up.
Team Dynamics & Schedule:
•	The Lakers have a difficult remaining schedule with several tough opponents.
•	LeBron's recent performances suggest he can handle the challenges.
Recommendation:
Pick LeBron James immediately. His recent scoring and playmaking abilities make him a valuable asset to any fantasy team. While his age is a concern, his consistency and durability suggest he can continue to perform at a high level. Be aware of his increasing turnovers and potential for regression as the season progresses.
Additional Notes:
•	His recent performances suggest he's still one of the best players in the NBA.
•	Despite his age, his leadership and basketball IQ remain invaluable.
•	Monitor his injury status closely.
"""
answer_gemma_4 = """Nikola Jokic is having a phenomenal season, averaging 30.6 points, 9.9 assists, and 13.2 rebounds per game.
Recent performances:
•	Averaging 23.8 points, 9.8 assists, and 12.8 rebounds over the past 4 games.
•	Posted a triple-double with 46 points, 9 rebounds, and 10 assists against the San Antonio Spurs on January 4th.
•	Recorded 35 points, 12 rebounds, and 15 assists against the Brooklyn Nets on January 10th.
Strengths:
•	Excellent playmaking abilities, leading the NBA in assists per game.
•	Skilled scorer with a career-high 58.7% FG%.
•	Strong rebounder and reliable defender.
Considerations:
•	Recent hamstring injury could impact his availability and performance.
•	Team schedule is relatively tough in the next few weeks.
Recommendation:
Pick Nikola Jokic immediately for his exceptional scoring potential, playmaking abilities, and rebounding prowess. His recent injury concern should be monitored, but his long-term value remains high.

"""
answer_gemma_5 = """Should you add Nikola Jokic to your team?
Absolutely! He's one of the best fantasy basketball players in the league and his stats this season are phenomenal.
Here's why you should consider adding him:
•	Dominant Scoring: Averaging 30.6 points per game, Jokic is a consistent and reliable scorer.
•	Elite Playmaking: With 9.9 assists per game, he's a fantastic playmaker who can create scoring opportunities for his teammates.
•	Monster Rebounding: His 13.2 rebounds per game are among the highest in the league.
•	High Usage Rate: With a usage rate of 36.2%, Jokic has the ball in his hands often, leading to increased opportunities for points.
Potential concerns:
•	High Price: He's a high-priced player, but his production justifies the cost.
•	Injury Risk: Like any player, there's a chance of injury, but Jokic has been relatively healthy throughout his career.
Overall:
Nikola Jokic is an exceptional fantasy basketball player with a proven track record of dominant scoring, playmaking, and rebounding. His high price and potential for injury are minor concerns that are outweighed by his immense talent and production.
Recommendation:
Add Nikola Jokic to your team without hesitation.
"""
answer_gemma_6 = """The provided text does not contain any information regarding Nikola Jokic's recent performance, so I am unable to answer this question from the given context."""
answer_gemma_7 = """Goga Bitadze Performance Evaluation
Based on the provided data, Goga Bitadze's recent performances have been inconsistent, with varying minutes and scoring outputs. While his per-game stats look promising (9.6 PTS, 2.4 AST, 8.2 REB), his inconsistency and limited playing time raise concerns.
Positives:
•	Recorded double-double with 15 points and 8 rebounds in a recent game.
•	Averaging 8.2 rebounds per game, suggesting strong rebounding ability.
•	Contributing 2.4 assists per game, indicating some playmaking potential.
Negatives:
•	Scoring output has been inconsistent, with several games scoring below 10 points.
•	Playing time is limited, averaging only 22.5 minutes per game.
•	High turnover rate (PIE of 0.149) suggests vulnerability to committing turnovers.
Recommendations:
•	Consider dropping Bitadze: His inconsistency, limited playing time, and high turnover rate make him a risky option in most fantasy leagues.
•	Wait and hope for improved consistency: If his playing time increases and he sustains his scoring and rebounding averages, he could become a valuable asset.
•	Target other players with better consistency and playing time: There are numerous players available who are performing more reliably and offer greater fantasy potential.
Additional Considerations:
•	Bitadze's matchup against the Orlando Magic on January 12th could be a good opportunity for him to post strong numbers.
•	His fantasy value is likely to remain low until he demonstrates greater consistency and playing time.
Overall:
Goga Bitadze is a risky fantasy option with limited upside at this point. Consider alternatives with better consistency and playing time for your fantasy basketball team.
"""
answer_gemma_8 = """Should you add Goga Bitadze to your team?
Short-Term:
•	Bitadze has averaged 9.6 points, 2.4 assists, and 8.2 rebounds in the past 5 games.
•	He's put up consistent numbers across several games, with multiple double-doubles.
•	His recent performances suggest he's a reliable scorer and rebounder off the bench.
Long-Term:
•	Bitadze's per-game stats are slightly below his career averages, but he's playing more minutes than ever.
•	With a growing role in the team's rotation, his production could potentially increase further.
•	His youth and potential for development make him an intriguing long-term prospect.
Considerations:
•	Bitadze is currently playing for the Orlando Magic, who have one of the worst records in the NBA.
•	His fantasy production may suffer if the team continues to struggle.
•	The Magic have several other young players vying for playing time, which could limit Bitadze's opportunities.
Overall:
Based on his recent performances and long-term potential, Goga Bitadze is a worthwhile addition to your fantasy team. However, keep an eye on his situation with the Magic and their overall team performance.
"""
answer_gemma_9 = """Goga Bitadze's Recent Performance
Based on the provided data, Goga Bitadze has shown consistent, albeit modest, production in his recent games:
•	Points: 8.8 per game in the last 5 games.
•	Rebounds: 8.6 per game in the last 5 games.
•	Assists: 2.8 per game in the last 5 games.
While these numbers are not eye-popping, they suggest that Bitadze is a reliable contributor on the court, especially considering his limited playing time in some games.
Highlights:
•	Scored 15 points in a game on January 9th.
•	Recorded 11 rebounds on January 5th.
•	Averaged 2.8 assists in the last 3 games.
Concerns:
•	Played limited minutes in several games.
•	Scoring efficiency is slightly below his season average.
Overall:
Goga Bitadze is a promising young player with potential for increased production as he gets more opportunities. However, his current performance is more of a role player level.
"""
answer_gemma_10 = ""
answer_gemma_11 = ""






##################################################################################################################################################################################################


answer_mistral_1 = """Based on the data provided, LeBron James is having an excellent season with the Los Angeles Lakers, averaging 23.7 points, 8.8 assists, and 7.6 rebounds per game. His recent performance shows he has been consistently delivering impressive numbers, scoring in the range of 18 to 38 points in his last five games.
LeBron's Player Impact Estimate (PIE) of 0.165 indicates that he contributes significantly to winning basketball games. His field goal percentage, although not provided in the data, is typically above average. With these statistics and considering his team role, I would recommend adding LeBron James to your fantasy basketball roster for his high potential to contribute across multiple categories.
If you have any specific league settings or team needs, feel free to share them so that I can tailor my advice accordingly.
"""
answer_mistral_2 = """Based on the data and context provided, it appears that LeBron James is currently performing exceptionally well for the Los Angeles Lakers in the 2024-25 NBA season. He consistently averages around 23.7 points per game (PTS), 8.8 assists per game (AST), and 7.6 rebounds per game (REB). These numbers demonstrate a strong all-around performance, making him an attractive addition to any fantasy basketball team.
However, it's essential to consider your team needs and league settings when deciding whether or not to pick up LeBron James. If you need help in the scoring categories that he excels in (PTS, AST, REB), then picking him immediately would be a strategic move for his strong potential contributions.
It's also worth noting that LeBron James' schedule and opponent matchups could impact his performance short-term. Be sure to monitor any changes to the Lakers' upcoming games, as certain opponents may present challenging matchups for him. Additionally, consider the long-term value of adding LeBron James to your team, given his proven track record of consistency over a 21-year career.
In summary, based on his recent performance and career longevity, I recommend adding LeBron James to your team if you have an immediate need in scoring categories where he excels or if you see long-term value in his consistent contributions. Just keep an eye on the Lakers' schedule for any potential challenging matchups that could affect his short-term performance.
"""
answer_mistral_3 = """Based on the provided data, Lebron James has been consistently delivering strong performances for the Los Angeles Lakers this NBA season. He averages 23.7 points, 7.6 rebounds, and 8.8 assists per game (as of the season statistics given).
Recently, his scoring average ranges from 18 to 38 points in five games, with an average of around 26 points per game. This is a solid contribution in any fantasy league setting. In addition, he maintains high efficiency with his field goal percentage (FG%) and free throw percentage (FT%).
Overall, considering James' strong recent performance and consistent contributions across multiple statistical categories, I would recommend adding him to your roster if possible, especially given the short-term value he provides for a potential fantasy playoff push. However, make sure to assess your team needs and league settings before making any final decisions.
"""
answer_mistral_4 = """Based on the provided data, Nikola Jokić is currently performing exceptionally well in the 2024-25 season. His average points (30.6), assists (9.9), and rebounds (13.2) per game are impressive, as is his Player Impact Estimate (PIE) of 0.21, which suggests his overall contribution to the team is significant.
In terms of recent performance, Jokić has been consistent with double-doubles in four out of the last five games, and a triple-double in one game. His minutes played have varied slightly, but he's shown resilience and adaptability by maintaining high productivity across different game lengths.
While it is essential to keep an eye on injury reports, Jokić has no reported injuries at this time. Given his current form, I would recommend keeping or acquiring Nikola Jokić for your fantasy basketball team due to his consistent scoring potential and versatile skillset.

"""
answer_mistral_5 = """To answer your question, it is essential to consider several factors when deciding whether or not to add a player like Nikola Jokic to your fantasy basketball team. Here's a breakdown of some key aspects that you should look at:
1.	Player performance: Check out Nikola Jokic's average stats and consistency over the season, as well as his recent form. Look at his per-game averages for points, rebounds, assists, steals, blocks, and field goal percentage to determine whether he is a valuable addition to your team.
2.	Team context: Factor in how Nikola Jokic's team is performing this season, as well as their schedule going forward. If the Denver Nuggets have a favorable schedule with multiple games against poor defensive teams, then Jokic could potentially put up big numbers.
3.	Player value on the waiver wire: Consider which other players are available on your league's waiver wire or free agency list. It might not be worth adding Jokic if there is another player with similar stats but a lower price tag or better schedule.
4.	Your team needs and roster construction: Look at the current makeup of your team and identify any positions where you are weak or have excess depth. If adding Nikola Jokic would help address one of these issues, then it might be worth adding him to your team. However, if you already have a surplus of centers or forwards, it may not make sense to add another one.
5.	Injuries and potential drop-offs: Check if there are any players on your roster who could potentially miss games due to injury or other reasons. If so, adding Nikola Jokic as a replacement player makes more sense.
6.	Player upside and long-term potential: Assess whether Nikola Jokic has shown signs of improvement over the season or if he is capable of reaching new heights in terms of production. A player with high upside can provide significant value to your team in the long run.
"""
answer_mistral_6 = """Nikola Jokic's recent performance can be summarized as follows:
•	In the last 10 games, Jokic has averaged 30.6 points, 13.2 rebounds, and 9.4 assists per game.
•	During this period, his FanDuel Fantasy Points average is approximately 58.2 points per game.
•	His team, the Denver Nuggets, has won 7 out of their last 10 games.
"""
answer_mistral_7 = """Based on the provided data, Goga Bitadze has shown some inconsistency in his recent games. However, he has had a good stretch where he scored 15 points and grabbed 8 rebounds against the Minnesota Timberwolves (Jan 09, 2025), indicating his potential when given more playing time.
In the current season, Bitadze is averaging 9.6 points per game (PTS) with 8.2 rebounds per game (REB), 2.4 assists per game (AST), and a player efficiency rating (PIE) of 0.149. These numbers are decent for a center but may not be enough to significantly contribute to fantasy teams in most leagues, especially if points are heavily weighted.
However, considering his recent performance and potential upside due to increased playing time, Goga Bitadze could be worth picking up as a bench player or streaming option in deeper fantasy basketball leagues, provided there aren't better alternatives available on the waiver wire.
If your league is points-based and team needs are focused on other categories, you might want to avoid adding Bitadze to your roster unless he consistently performs well or sees increased minutes. Always remember to keep an eye on his playing time and production as the season progresses.
"""
answer_mistral_8 = """Based on the data provided, it seems that Goga Bitadze has had a mix of performances recently, with some games where he scores in single digits and others where he contributes significantly more. In the last five games, his average points per game is around 15.2, rebounds are 8.4, and assists are 2.6.
While these statistics can be beneficial, it's also important to consider other factors such as playing time, matchups, and role within the team. As of now, Goga Bitadze appears to be a viable option off the bench for the Orlando Magic and could potentially provide some value to your fantasy basketball team.
However, I would recommend monitoring his performance closely in upcoming games, particularly against weaker opponents or in favorable matchups, before making a decision on adding him to your roster. Keep in mind that consistent playing time is crucial for any player's success and stability within a lineup. Make sure Goga Bitadze continues to receive significant minutes from his coach before making the final call on whether to add him to your team or not.
"""
answer_mistral_9 = """Based on the data provided, Goga Bitadze has been averaging 9.6 points, 8.2 rebounds, and 2.4 assists per game for the season. In his last five games, he scored an average of 10 points, grabbed around 8 rebounds, and dished out about 2 assists per game, while playing an average of 25 minutes per contest.
In terms of individual games, his most recent one was on January 13, 2025, where he scored 4 points with 2 rebounds in a loss against the San Antonio Spurs. Prior to that, he played against the Philadelphia 76ers on January 12, 2025, scoring 4 points and pulling down 2 rebounds in a victory. Before that, he had a 15-point, 8-rebound performance against the Milwaukee Bucks (January 10), followed by an 11-point, 8-rebound effort in a win over the New York Knicks (January 6) and a 9-point, 11-rebound game versus the Utah Jazz (January 5). In his previous match, he scored 12 points with 4 rebounds against the Houston Rockets on January 3.
Overall, Goga Bitadze appears to be contributing consistently across various statistical categories for his team, with a slight decrease in scoring compared to his season average in his last two games.
"""
answer_mistral_10 = ""
answer_mistral_11 = ""








##################################################################################################################################################################################################




def compute_bertscore(reference_answer, model_answer_llama, model_answer_gemma, model_answer_mistral):
    # Vergleiche Modellantwort Llama mit Referenzantwort
    P_llama, R_llama, F1_llama = score([answer_llama_10], [reference_answer_10], lang="de")
    print(f"Modell Llama F1-Score: {F1_llama.mean().item():.4f}")

    # Vergleiche Modellantwort Gemma mit Referenzantwort
    P_gemma, R_gemma, F1_gemma = score([answer_gemma_10], [reference_answer_10], lang="de")
    print(f"Modell Gemma F1-Score: {F1_gemma.mean().item():.4f}")

    # Vergleiche Modellantwort Mistral mit Referenzantwort
    P_mistral, R_mistral, F1_mistral = score([answer_mistral_10], [reference_answer_10], lang="de")
    print(f"Modell Mistral F1-Score: {F1_mistral.mean().item():.4f}")



# Führen Sie den BERTScore-Vergleich durch
compute_bertscore(reference_answer_10, answer_llama_10, answer_gemma_10, answer_mistral_10)