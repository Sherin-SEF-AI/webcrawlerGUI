import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import requests
from bs4 import BeautifulSoup
import threading
import urllib.parse

class WebCrawler:
    def __init__(self):
        self.urls_to_crawl = []
        self.crawled_urls = set()
        self.pause_flag = threading.Event()
        self.pause_flag.set()
        self.stop_flag = False

    def start_crawling(self, url, depth):
        self.urls_to_crawl.append((url, 0))
        self.stop_flag = False
        thread = threading.Thread(target=self.crawl_website, args=(depth,))
        thread.start()

    def crawl_website(self, max_depth):
        while self.urls_to_crawl and not self.stop_flag:
            self.pause_flag.wait()
            url, depth = self.urls_to_crawl.pop(0)
            if url in self.crawled_urls or depth > max_depth:
                continue
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, 'html.parser')

                base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urllib.parse.urlparse(url))
                links = [urllib.parse.urljoin(base_url, a['href']) for a in soup.find_all('a', href=True)]

                filtered_links = self.filter_links(links, url_filter.get())

                for link in filtered_links:
                    if link not in self.crawled_urls:
                        results_text.insert(tk.END, link + '\n')
                        self.urls_to_crawl.append((link, depth + 1))
                
                self.crawled_urls.add(url)
                status_label.configure(text=f"Status: Crawled {len(self.crawled_urls)} URLs, {len(self.urls_to_crawl)} remaining.")
            except Exception as e:
                results_text.insert(tk.END, f"Error: {str(e)}\n")

        if not self.urls_to_crawl:
            status_label.configure(text="Status: Crawling completed.")
        else:
            status_label.configure(text="Status: Crawling paused.")

    def filter_links(self, links, domain):
        if not domain:
            return links
        return [link for link in links if domain in link]

    def save_results(self, file_type):
        file_path = filedialog.asksaveasfilename(defaultextension=f".{file_type}", filetypes=[(f"{file_type.upper()} files", f"*.{file_type}"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    for line in results_text.get(1.0, tk.END).strip().split('\n'):
                        file.write(line + '\n')
                messagebox.showinfo("Success", "Results saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {str(e)}")

    def pause_crawling(self):
        self.pause_flag.clear()
        status_label.configure(text="Status: Crawling paused.")

    def resume_crawling(self):
        self.pause_flag.set()
        status_label.configure(text="Status: Crawling resumed.")

    def stop_crawling(self):
        self.stop_flag = True
        self.pause_flag.set()
        status_label.configure(text="Status: Crawling stopped.")

def start_crawling():
    url = url_entry.get()
    try:
        depth = int(depth_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for depth.")
        return

    results_text.delete(1.0, tk.END)
    status_label.configure(text="Status: Crawling...")
    web_crawler.start_crawling(url, depth)

def save_results_as_txt():
    web_crawler.save_results('txt')

def save_results_as_csv():
    web_crawler.save_results('csv')

def pause_crawling():
    web_crawler.pause_crawling()

def resume_crawling():
    web_crawler.resume_crawling()

def stop_crawling():
    web_crawler.stop_crawling()

web_crawler = WebCrawler()

app = ctk.CTk()
app.title("Web Crawler")
app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))  # Set the window to full screen

frame = ctk.CTkFrame(app)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# URL Entry
url_frame = ctk.CTkFrame(frame)
url_frame.pack(fill=tk.X, expand=True, pady=(0, 10))

url_label = ctk.CTkLabel(url_frame, text="Enter URL:")
url_label.pack(side=tk.LEFT, padx=(0, 10))

url_entry = ctk.CTkEntry(url_frame, width=400)
url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Depth Entry
depth_frame = ctk.CTkFrame(url_frame)
depth_frame.pack(side=tk.LEFT, padx=(10, 0))

depth_label = ctk.CTkLabel(depth_frame, text="Depth:")
depth_label.pack(side=tk.LEFT)

depth_entry = ctk.CTkEntry(depth_frame, width=50)
depth_entry.pack(side=tk.LEFT)

# Filter Entry
filter_frame = ctk.CTkFrame(frame)
filter_frame.pack(fill=tk.X, expand=True, pady=(0, 10))

filter_label = ctk.CTkLabel(filter_frame, text="Filter by Domain:")
filter_label.pack(side=tk.LEFT)

url_filter = ctk.CTkEntry(filter_frame, width=400)
url_filter.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Control Buttons
button_frame = ctk.CTkFrame(frame)
button_frame.pack(fill=tk.X, expand=True, pady=(10, 5))

crawl_button = ctk.CTkButton(button_frame, text="Crawl", command=start_crawling)
crawl_button.pack(side=tk.LEFT, padx=(0, 5))

pause_button = ctk.CTkButton(button_frame, text="Pause", command=pause_crawling)
pause_button.pack(side=tk.LEFT, padx=(5, 5))

resume_button = ctk.CTkButton(button_frame, text="Resume", command=resume_crawling)
resume_button.pack(side=tk.LEFT, padx=(5, 5))

stop_button = ctk.CTkButton(button_frame, text="Stop", command=stop_crawling)
stop_button.pack(side=tk.LEFT, padx=(5, 5))

save_txt_button = ctk.CTkButton(button_frame, text="Save as TXT", command=save_results_as_txt)
save_txt_button.pack(side=tk.LEFT, padx=(5, 5))

save_csv_button = ctk.CTkButton(button_frame, text="Save as CSV", command=save_results_as_csv)
save_csv_button.pack(side=tk.LEFT, padx=(5, 5))

# Results Text Area
results_frame = ctk.CTkFrame(frame)
results_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 5))

results_text = scrolledtext.ScrolledText(results_frame, wrap=tk.WORD, height=15)
results_text.pack(fill=tk.BOTH, expand=True)

# Status Label
status_frame = ctk.CTkFrame(frame)
status_frame.pack(fill=tk.X, expand=True, pady=(0, 5))

status_label = ctk.CTkLabel(status_frame, text="Status: Ready")
status_label.pack(side=tk.LEFT)

app.mainloop()

