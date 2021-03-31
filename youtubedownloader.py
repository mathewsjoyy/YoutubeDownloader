from pytube import YouTube
import tkinter as tk
from playsound import playsound

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 120
WINDOW_TITLE = "YouTube Video Downloader"
BUTTON_CLICK_SOUND = "clicks.wav" # Make sure its in .wav format

class YoutubeDownloader:

    def __init__(self):
        # Define the format of the GUI
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(WINDOW_WIDTH,WINDOW_HEIGHT))
        self.window.configure(bg="#FF0000")
        self.window.title(WINDOW_TITLE)
        self.window.iconbitmap("youtube.ico")
        
        # Create Labels
        self.link_label = tk.Label(self.window, text = "Download Link", width = 15)
        self.link_label.grid(column = 0, row = 0) # Puts in top left 
        self.name_label = tk.Label(self.window, text = "Save File As..", width = 15)
        self.name_label.grid(column = 0, row = 1) # Puts in top left 1 down 
        self.path_label = tk.Label(self.window, text = "Save File Path", width = 15)
        self.path_label.grid(column = 0, row = 2) # Puts in top left 2 down 
        self.ext_label = tk.Label(self.window, text = "File Extension", width = 15)
        self.ext_label.grid(column = 0, row = 3) # Puts in top left 3 down
        
        # Create Entry Paths
        self.link_entry = tk.Entry(master = self.window, width = 65)
        self.link_entry.grid(column = 1, row = 0)
        self.name_entry = tk.Entry(master = self.window, width = 65)
        self.name_entry.grid(column = 1, row = 1)
        self.path_entry = tk.Entry(master = self.window, width = 65)
        self.path_entry.grid(column = 1, row = 2)
        self.ext_entry = tk.Entry(master = self.window, width = 65)
        self.ext_entry.grid(column = 1, row = 3)
        
        # Create Download Button 
        self.download_button = tk.Button(self.window, text = "Download", command = self.__get_link)
        self.download_button.grid(column = 1, row = 4)
        
        return
    
    # We use (__) private methods so it can only be called within the class
    def __downloader(self, link, save_path = "", save_name = "", extension = ".mp4"):
        playsound(BUTTON_CLICK_SOUND)
        yt = YouTube(link)
        # Get First video with file extension .mp4 (default) with highest resolution and with audio and video
        yt_stream = yt.streams.filter(progressive=True, file_extension = extension).order_by("resolution").desc().first()
        yt_stream.download(output_path = save_path, filename = save_name)
        
    def __get_link(self):
        link = self.link_entry.get()
        path = self.path_entry.get()
        name = self.name_entry.get()
        ext = self.ext_entry.get()
        
        self.__downloader(link, path, name, ext)
        return
        
    
    # Method to run the tkinter main   
    def run_app(self):
        self.window.mainloop()
        return

# Call the main functionailty 
if __name__ == "__main__":
    app = YoutubeDownloader()
    app.run_app()
        
        
        