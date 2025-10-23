# Video Terminal App

This is a simple video player application that shows educational videos, text content, and includes a built-in terminal. It's designed for learning about computer security and programming topics.

## ⚠️ IMPORTANT WARNING: This is NOT a Streaming App

**Videos are downloaded to your computer first, then played!**

- Each video must be fully downloaded before it can play
- Videos can be large (100MB-200MB each)
- Downloads go to your `Downloads` folder and stay on your computer
- You need enough free space and a good internet connection
- First time playing a video may take several minutes to download
- Once downloaded, videos play quickly on subsequent views

## What This App Does

The app has 4 main sections:

- **Top Left**: Video player that plays educational videos
- **Top Right**: Text content that explains what's in the videos
- **Bottom Left**: List of available videos you can choose from
- **Bottom Right**: Built-in terminal (command line) for practicing commands

## System Requirements

You need a Linux computer with:

- Ubuntu, Debian, or similar Linux distribution
- Internet connection
- **At least 5GB free space on your hard drive** (videos are large and stored locally)

## Step-by-Step Installation

### Step 1: Install Required System Software

Open a terminal and run these commands one by one:

```bash
sudo apt update
sudo apt install -y python3 python3-pip vlc xterm
```

This installs Python, video player software, and terminal emulator.

### Step 2: Install Python Libraries

In the same terminal, go to the app folder and install the required libraries:

```bash
cd /home/altin/Desktop/InfoSec_Course
pip3 install -r requirements.txt
```

## How to Run the App

### Method 1: Using the Launcher Script (Easiest)

1. Open a terminal
2. Go to the app folder:

   ```bash
   cd /home/altin/Desktop/InfoSec_Course
   ```

3. Make the launcher script executable:

   ```bash
   chmod +x run.sh
   ```

4. Run the app:

   ```bash
   ./run.sh
   ```

### Method 2: Direct Python Run

1. Open a terminal
2. Go to the app folder:

   ```bash
   cd /home/altin/Desktop/InfoSec_Course
   ```

3. Run the app:

   ```bash
   python3 main.py
   ```

## How to Use the App

1. When the app opens, you'll see the main window with 4 sections
2. Click on a video in the playlist (bottom left) to select it
3. **The video will download first** (this may take several minutes for large videos)
4. Once downloaded, the video will start playing automatically
5. Use the play/pause button to control playback
6. The text content (top right) will show information about the video
7. The terminal (bottom right) lets you practice commands while watching

## Controls

- **Play/Pause Button**: Click to start or stop the video
- **Seek Slider**: Drag to jump to different parts of the video
- **Volume Slider**: Adjust the sound level
- **Progress Bar**: Shows download progress for videos

## Troubleshooting

### App Won't Start

**Problem**: You see an error when trying to run the app

**Solutions**:

1. Make sure you installed all system requirements:

   ```bash
   sudo apt install -y python3 python3-pip vlc xterm
   ```

2. Install Python libraries:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Try running with Python 3 specifically:

   ```bash
   python3 main.py
   ```

### Video Won't Play

**Problem**: Video downloads but won't play

**Solutions**:

1. Make sure VLC is installed:

   ```bash
   sudo apt install -y vlc
   ```

2. Check if the video file downloaded to your Downloads folder
3. Try restarting the app

### Terminal Not Working

**Problem**: The built-in terminal section is blank or not responding

**Solutions**:

1. Make sure xterm is installed:

   ```bash
   sudo apt install -y xterm
   ```

2. The terminal should work automatically when the app starts

### App Runs But Looks Wrong

**Problem**: Windows don't appear correctly or text is cut off

**Solutions**:

1. Make sure you're running on a Linux desktop (not server)
2. Try resizing the main window
3. Restart the app

### Videos Don't Download

**Problem**: Clicking videos doesn't start download

**Solutions**:

1. Check your internet connection
2. **Make sure you have enough free space (at least 5GB recommended)**
3. Videos download to your Downloads folder automatically
4. **Large videos may take several minutes to download**
5. Watch the progress bar at the bottom to see download status

## Getting Help

If you run into problems:

1. Check the terminal output for error messages
2. Make sure all installation steps were completed
3. Try restarting your computer and running the app again

## What Gets Downloaded

**⚠️ Videos are stored permanently on your computer!**

- Videos are downloaded to your `Downloads` folder and stay there
- Each video can be 100MB-200MB in size
- Text content is also saved to your Downloads folder
- The app remembers what you've downloaded for faster loading next time
- **You can delete downloaded videos from your Downloads folder to free up space**

## Safety Notes

- This app only downloads from the specified GitHub repository
- All downloads go to your Downloads folder
- No personal information is sent anywhere
- The terminal is just for learning - be careful with commands you type
