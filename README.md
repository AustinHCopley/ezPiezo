# ezPiezo

## Introduction

My aim here is to classify a chord that is played on a guitar to show the player what the quality of the chord is: major, minor, major 7, minor 7, etc. using a novel approach and extensive experience and knowledge in this domain.

Different chords are made up of different sets of intervals. Each interval has a unique wave formation that gives it a distinct sound. The individual waves and their interactions when played together are what create the tonal difference between types of chords. Because of these ideas, it seemed the proper course of action to sample the vibrations of the instrument being played to determine the chord. Sampling _vibrations_, as opposed to _audio_, was an easy decision. Theoretically, sampling the vibrations on the guitar should be much less susceptible to outside noise and provide superior data for this task and therefore a more refined final product.

This provides the foundation for a really powerful tool in songwriting, composition, transcription, and ear training. **Not everyone who is well-practiced in music knows advanced music theory or even knows how to read music.**
 - If the user wants to explore new chord structures while having instant feedback on what they're playing, they can
 - If the user is writing a song, and they want to immediately write down the chords they come up with, they can
 - If the user is playing with others in a jam-like setting, and they want to articulate what they're playing to their band-mates, they can
 - If the user learns a song by ear, and they want to understand what the chord progression is, they can

## Inspiration

I came to this idea for [a hackathon](https://devpost.com/software/ezpiezo) because I had several different areas that I wanted to explore, and a few of those were music, RaspberryPi/sensors, and machine learning. I realized that those three could be brought together to create a novel way of collecting and classifying musical data. 

I have played music my entire life and I quite enjoy learning about music theory. I often play things by ear or come up with new voicings for chords on the guitar. Sometimes it is not immediately apparent what type of chord I am playing unless I go through all the notes one by one. I figured there must be ways that people have used machine learning to classify chords, but I couldn't find any that used the actual vibration of the instrument to do so.

In the long-run, this project aims to provide someone with an exact chord with all of its alterations and extensions: An ideal use case would show the model differentiating between things like _major 7 add9_, _minor major 7_, _dominant 7 #13_, and _sus4_ or _sus2_. However, the amount of possibilities for chords that this kind of extension brings far exceeds the scope of this project, but I believe this type of problem is solvable to some extent given enough time and effort to really focus on breaking down the intervals in a chord and reconstructing the type of chord from that.

## What it does

The primary structure of the project consists of data creation, labeling, training, validation, and model metrics.

### Data creation

Record voltage from piezo element attached to guitar for 3 seconds while playing a chord, convert analog to digital signal with ADC

### Labeling

Determine the labels from the chord quality for two classification tasks:
#### Binary Classification
 - 0: Major
 - 1: minor

#### Multi-class Classification:
 - 0: Major
 - 1: minor
 - 2: Major 7
 - 3: minor 7

### Models

Mainly focused on a stacked LSTM trained on Fourier-transformed input data. Explored other alternatives like CNN using spectrograms of the data, GRU, and LSTM with attention.

## How we built it

I used a RaspberryPi with a piezo element and an analog-to-digital converter. The [piezo element](https://en.wikipedia.org/wiki/Piezoelectricity) is a type of sensor that generates voltage when mechanical stress or any type of deformation is applied to it, and it can pick up very acute changes like vibrations. I placed the piezo element on the part of the guitar that had the most vibration, essentially an anti-node on the body of the guitar, which I found to be just below the bridge. I sampled 282 chords on the guitar and built different model architectures to classify these chords. I experimented with different transformations to apply to the data but ended up going with a Fourier transform for the LSTM, and spectrograms created from a short-time Fourier transform for the CNN.

## Challenges we ran into

I had quite a bit of difficulty with getting consistent voltage readings from the piezo element, likely due to my less-than-optimal setup.

An issue with creating my own data was that it's very difficult to get a model to generalize when it only sees a limited amount of inputs. Considering I have a limited amount of time due to work and school, and I have only so much finger strength to play hundreds of chords in a row, it just wasn't completely feasible to create the volume of data that machine learning models typically train and test on.

I also had lots of difficulty working with the LSTM, as I've mostly only had experience with CNNs before this project.

## Accomplishments that we're proud of
I'm proud that I was able to complete the entire process all the way from creating the data to tuning different models completely from scratch, and honestly, I'm quite proud that I came up with the concept to begin with and I truly believe in its future potential.

## What we learned
I learned a lot about LSTMs and audio-spectrogram data, Fourier transformations, and different signal-processing techniques. I ended up truly understanding that no matter how much data I had already recorded, more was always better.