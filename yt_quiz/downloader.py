import yt_dlp

def download_audio(youtube_url, output_path="downloads/temp.mp3"):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/temp.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")
    
    return filename