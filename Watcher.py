import sys
import time
import logging
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# from mozaiku import mozaiku
# from gray import gray
# from edge import edge

 
#イベントハンドラ
class ChangeHandler(FileSystemEventHandler):
 
    #ファイルやフォルダが作成された場合
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを作成しました。' % filename)
        #ここで関数を呼び出す
        # mozaiku()
        # gray()
        # edge()
 
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
    print('実行中')
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, current_directory, recursive=True)

    observer.start()
    
    observer.stop()
    observer.join()