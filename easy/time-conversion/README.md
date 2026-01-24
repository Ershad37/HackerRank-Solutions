# Description
This program converts a 12-hour AM/PM time format into a 24-hour military time format.
It handles special cases for midnight (12 AM) and noon (12 PM) correctly.
# Problem Statement
Given a time string s in 12-hour format (hh:mm:ssAM or hh:mm:ssPM), convert it to 24-hour format (HH:MM:SS).
Rules:
12:00:00AM → 00:00:00
12:00:00PM → 12:00:00
All other hours are converted according to AM/PM rules.
Example:
Input: "07:05:45PM"
Output: "19:05:45"
