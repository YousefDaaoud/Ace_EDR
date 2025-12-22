from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from core.logger import log_info
import time

class FileMonitorHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            log_info(f"File created: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            log_info(f"File modified: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            log_info(f"File deleted: {event.src_path}")

def start_file_monitor(path):
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    log_info(f"Started file monitoring on: {path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
