#  Weekend Tracker Probability Analysis Using Naive Bayes Formula
# Group7 - Floremonte, Licatan, Dandin
Predicting weekend Sentiments of my Peers in University of Southern Mindanao (USM) using Naïve Bayes Formula:
P(y | X) = P(y) × P(x₁ | y) × P(x₂ | y) × ... × P(xₙ | y)
We aim to determine the probability of a student experiencing a "Great" or "Terrible" weekend based on four categorical features: Worship Service Attendance, Location, Academic Load, and Financial Status.

# Form used to gather data from the respondents: 
  https://docs.google.com/forms/d/1qYgGbGJ1hYi4iBRYf0QrXdZeU8izCmuVRikidRifiLs/edit

# Raw Data Collected from the Participants

![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/94838a3c9bc60e1768048b2088ea3cac6d3af883/screenshots%20of%20data%20tables/raw%20data.png)

# Features Used to Calculate the Probability

### Worship Services
![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/744b94ade03f49f853776293a12ed76992c624ce/screenshots%20of%20data%20tables/worship%20data.png)

![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/0d4ee5ada86fbfd7a5e06a7bca0317cb80e345f9/form/charts%20from%20forms/Worship%20pie%20chart.png)

### Location
![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/744b94ade03f49f853776293a12ed76992c624ce/screenshots%20of%20data%20tables/location%20data.png)

![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/0d4ee5ada86fbfd7a5e06a7bca0317cb80e345f9/form/charts%20from%20forms/Location%20pie%20chart.png)

### Academic Load
![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/744b94ade03f49f853776293a12ed76992c624ce/screenshots%20of%20data%20tables/academic%20data.png)

![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/0d4ee5ada86fbfd7a5e06a7bca0317cb80e345f9/form/charts%20from%20forms/Academic%20load.png)

### Financials
![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/744b94ade03f49f853776293a12ed76992c624ce/screenshots%20of%20data%20tables/financials%20data.png)

![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/0d4ee5ada86fbfd7a5e06a7bca0317cb80e345f9/form/charts%20from%20forms/Financial.png)

# Overall Probability Calculated of P(yes) and P(no) for Both Scenarios

![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/744b94ade03f49f853776293a12ed76992c624ce/screenshots%20of%20data%20tables/overall%20calculation%20of%20data.png)

![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/0d4ee5ada86fbfd7a5e06a7bca0317cb80e345f9/form/charts%20from%20forms/Label%20(Great%20or%20Terrible)%20chart.png)

# Naive Bayes - Likelihood, Priors and Final Posteriors

![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/5e4e757fb7877074897987cef849b7ad755e707c/bar_chart.png)

# Summary
Data used in this model was collected from 14 participants. The overall outcome was perfectly balanced, providing an equal baseline for both classes:
•	Prior Probability of a Great Weekend: 7/14 (50%)
•	Prior Probability of a Terrible Weekend: 7/14 (50%)

The following table displays the conditional probabilities for each feature:

![Alt text](https://github.com/Cloyd-glitch/Group7-Weekend-Tracker-Probability-Analysis-Using-Naive-Bayes-Formula/blob/d9c36384e5df0cadc2c81f42532e2eb5e0ba3472/screenshots%20of%20data%20tables/condtional%20tables%20for%20all%20features.png)

To verify the model, we calculated the final subsequent probabilities for two distinct hypothetical scenarios using the data gathered above.
In the first scenario, the data used was the data from the “Yes” or “all positive” students—my peers, who attended worship service, stayed in their hometown, had a heavy academic load, and was financially stable. The concluded probability was P(Great): 0.031; P(Terrible): 0.006, therefore the prediction is Great Weekend for 0.031 is greater than 0.006.
Meanwhile the second scenario for the “No” or “Negative” student; did not attend worship service, stayed in their boarding house, had a light/non-academic load, and was broke/tipid mode, showed a different conclusion or prediction. P(Great): 0.004; P(Terrible): 0.049 which is greater than the former and predicting my peers having a terrible Weekend.
The Naive Bayes model successfully identified key patterns in the data. Financial Status proved to be the strongest predictor; students who were financially stable were significantly more likely to report a "Great" weekend (5/7) compared to a "Terrible" one (1/7). Interestingly, Location had an equal probability distribution (5/7 for Hometown across both outcomes), indicating it was not a primary deciding factor for this specific group.


