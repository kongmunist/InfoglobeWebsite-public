# 2/11/2025 Update: This repo for archival purposes and contains old code for my Infoglobe website. Due to various security reasons I cannot publish the up-to-date repo, but for emotional reasons I needed to publish this project. The website may not run as-is, and the updated Arduino code can be found on my website. 


# Interactive Infoglobe Website

## Introduction
The Interactive Infoglobe is a project made using a modded Caller ID system and the internet. Simply by visiting our website at [bit.ly/andyball](bit.ly/andyball), any internet user may send a message directly to a spinning LED display situated in Andy's current abode, where it will appear along with 3 other messages, the time, and the date in a rotating queue. 

![https://twitter.com/i/status/1557860334047617024](igt2_tolife.jpg)

Some kind and funny messages I've received are documented in [this twitter thread](https://twitter.com/oldestasian/status/1557780763583471617)

## Motivation
In a lot of ways, Infoglobe messages are like emails or SMS — async, text-based messages. But it's still a little bit weird to email your friends, and I wouldn't want to mix up work messages with those of friends and family. So we need a new medium. 

I'm also a big fan of writing letters with my friends because I really enjoy how tangible the medium is. Even if you do not read it immediately, you cannot help but see its existence in your mailbox or on your desk. But it takes a lot of effort to write and send a letter, so short messages usually do not get this treatment. Ideally, something digital could accomplish the same. 

The cross-section of these two ideas is the Interactive Infoglobe. Physical, asynchronous messages that can be sent as easily as a text, but show up in the real, physical world. 

## Hardware Setup
I've written up the details of how to make your own modded Infoglobe in a series of blog posts, you can find them here: [part 1](https://andykong.org/blog/infoglobetutorial1/) and [part 2](https://andykong.org/blog/infoglobetutorial2/). Completing the hardware stuff requires some prying, screwdriving, and soldering. It also requires an Olympia Infoglobe; they can usually be found looking for new homes on eBay.

## Firmware
The firmware running on the Infoglobe microcontroller can be found in the `arduinostuff/` directory. It should work cold-turkey, given you input your SSID details before uploading it onto your hardware. More details can be found in blog post [part 3](https://andykong.org/blog/infoglobetutorial3/), which is mainly about the software setup.


## Comments/Suggestions?
Please feel free to send them on my Infoglobe at [bit.ly/andyball](bit.ly/andyball), or my email at (check my [CV](https://andykong.org/static/AndyKongCV.pdf))!
