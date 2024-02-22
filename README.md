# Original leak
https://github.com/I-S00N/I-S00N

# Anxun-isoon
The iSoon/Anxun leak in a single json file


-   The user identified as `lengmo` is the top sender, with a total of 4981 messages. This indicates that `lengmo` is the most active participant in the conversation.
-   The most frequent communication pair is between `lengmo` and `Shutd0wn`, with `lengmo` sending 4635 messages to `Shutd0wn`. This suggests a significant amount of interaction between these two users.

This data implies a strong communication link between `lengmo` and `Shutd0wn`, potentially indicating a key relationship or hierarchy within the group. `lengmo`'s high level of activity could suggest a leadership or central role in the conversation dynamics.

![image](https://github.com/soufianetahiri/Anxun-isoon/assets/17729335/da21f000-ccce-471c-9fb9-580e821098ee)

**The analysis of working hours by examining the distribution of message times**

    0      279
    1      723
    2     1146
    3     1645
    4     1386
    5      843
    6     1415
    7     1167
    8     1538
    9     1430
    10    1025
    11     742
    12     611
    13     708
    14     441
    15     409
    16     140
    17       6
    18       4
    20       1
    21       2
    22      18
    23      64
    Name: hour, dtype: int64

The distribution of messages per hour shows a pattern that can help infer the working hours. Here's a summary:

-   **Peak Activity Hours:** From the early morning hours around 2 AM, increasing to a peak at 3 AM, and then gradually decreasing after 5 AM. There's another peak starting from 8 AM and extending through 10 AM.
-   **Lower Activity Hours:** Activity significantly drops after 4 PM, with minimal to no messages after 5 PM.

# Initial hot takes
-   https://twitter.com/DE7AULTsec/status/1759388057323618611

-   https://www.malwarebytes.com/blog/news/2024/02/a-first-analysis-of-the-i-soon-data-leak:
Some of the tools that i-Soon used are impressive enough. Some highlights:
    -   Twitter (now X) stealer: Features include obtaining the user’s Twitter email and phone number, real-time monitoring, reading personal messages, and publishing tweets on the user’s behalf.
    -   Custom Remote Access Trojans (RATs) for Windows x64/x86: Features include process/service/registry management, remote shell, keylogging, file access logging, obtaining system information, disconnecting remotely, and uninstallation.
    -   The iOS version of the RAT also claims to authorize and support all iOS device versions without jailbreaking, with features ranging from hardware information, GPS data, contacts, media files, and real-time audio records as an extension. (Note: this part dates back to 2020)
    -   The Android version can dump messages from all popular Chinese chatting apps QQ, WeChat, Telegram, and MoMo and is capable of elevating the system app for persistence against internal recovery.
    -   Portable devices for attacking networks from the inside.
    -   Special equipment for operatives working abroad to establish safe communication.
    -   User lookup database which lists user data including phone number, name, and email, and can be correlated with social media accounts.
    -   Targeted automatic penetration testing scenario framework.
  
# Initial machine translation by @DE7AULTsec
-   https://github.com/soufianetahiri/Anxun-isoon/tree/main/InitialTranslations
