#Simple Youtube Song Download Script Made By github.com/Wasabixy

from pytube import YouTube

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ") #Youtube Song URL 
    output_path = input("Enter the output directory path to save the audio: ") #Path You want to save your song / OR / Leave Empty

    download_audio(video_url, output_path)
