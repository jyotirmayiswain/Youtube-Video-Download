from pytube.__main__ import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *
import os

font = ('verdana', 20)
file_size = 0
iconPath = os.path.join(os.path.join(os.getcwd(), "img"), "youtube_PNG5.png")


#on complete
def completeDownload(stream=None, file_path=None):

    print("download complete")
    showinfo("Message", "File has been downloaded")
    downloadBtn['text'] = "Download Video"
    downloadBtn['state'] = "active"
    urlField.delete[0, END]


#on progress
def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = (( file_size - bytes_remaining ) / file_size) * 100
    downloadBtn['text'] = "{:00.0f}%  downloaded".format(percent)


#download function
def startDownload(url):

    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return
    try:
        yt = YouTube(url)
        st = yt.streams.first()
        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path_to_save)

    except Exception as e:
        print(e)
        print("Something Went wrong...Try again")


# will be called on button click
def btnclicked():
    try:
        downloadBtn['text'] = "Please Wait"
        downloadBtn['state'] = 'disabled'

        url = urlField.get()

        if url == '':
            return None
        print(url)

        thread = Thread(target=startDownload, args=(url,))
        thread.start()

    except Exception as e:
        print(e)


#gui coding
root = Tk()
root.title("My Youtube downloader")
root.iconbitmap(iconPath)

#main icon
file = PhotoImage(file=iconPath)
headingIcon = Label(root, image=file)
headingIcon.pack(side=TOP, pady=3)

#making url
urlField = Entry(root, font=font, justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
urlField.focus()

#download button
downloadBtn=Button(root, text="Download Video", font=font, relief='ridge', command=btnclicked)
downloadBtn.pack(side=TOP, pady=20)

# Starting the main GUI loop
root.mainloop()