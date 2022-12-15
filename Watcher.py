import sys
import time
import logging
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
 
#イベントハンドラ
class ChangeHandler(FileSystemEventHandler):
 
    #ファイルやフォルダが作成された場合
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを作成しました。' % filename)
        #ここで関数に引数としてfilenameを送る？
        print(filename)
 
    #ファイルやフォルダが更新された場合
    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        # print('%sを変更しました。' % filename)
 
    #ファイルやフォルダが移動された場合
    def on_moved(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        # print('%sを移動しました。' % filename)
 
    #ファイルやフォルダが削除された場合
    def on_deleted(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        # print('%sを削除しました。' % filename)
 

def watcher():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, current_directory, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()