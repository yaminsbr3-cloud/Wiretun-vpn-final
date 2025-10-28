from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.window import Window
import threading
import time

class WireTunVPN(App):
    def __init__(self):
        super().__init__()
        self.is_connected = False
        self.data_used = 0
        Window.size = (350, 600)
        
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(text="WireTun VPN", font_size='24sp', size_hint_y=0.1)
        main_layout.add_widget(title)
        
        self.status = Label(text="🔴 DISCONNECTED", font_size='18sp', size_hint_y=0.1)
        main_layout.add_widget(self.status)
        
        self.progress = ProgressBar(max=100, size_hint_y=0.08)
        main_layout.add_widget(self.progress)
        
        self.connect_btn = Button(text="CONNECT VPN", background_color=(0.2, 0.7, 0.3, 1), 
                                 size_hint_y=0.15, font_size='18sp')
        self.connect_btn.bind(on_press=self.toggle_connection)
        main_layout.add_widget(self.connect_btn)
        
        self.stats_label = Label(text="Data: 0 MB\nSpeed: 0 Mbps", 
                               size_hint_y=0.15, font_size='14sp')
        main_layout.add_widget(self.stats_label)
        
        sites_label = Label(text="Free VPN for Social Media\n• Facebook\n• WhatsApp\n• Twitter\n• Instagram", 
                          size_hint_y=0.3, font_size='14sp')
        main_layout.add_widget(sites_label)
        
        info_label = Label(text="WireTun VPN v1.0\nSecure & Free", 
                          size_hint_y=0.12, font_size='12sp')
        main_layout.add_widget(info_label)
        
        return main_layout
    
    def toggle_connection(self, instance):
        if not self.is_connected:
            self.connect_vpn()
        else:
            self.disconnect_vpn()
    
    def connect_vpn(self):
        self.is_connected = True
        self.connect_btn.text = "DISCONNECT VPN"
        self.connect_btn.background_color = (0.9, 0.2, 0.2, 1)
        self.status.text = "🟡 CONNECTING..."
        self.progress.value = 0
        
        thread = threading.Thread(target=self.connection_process)
        thread.daemon = True
        thread.start()
    
    def disconnect_vpn(self):
        self.is_connected = False
        self.connect_btn.text = "CONNECT VPN"
        self.connect_btn.background_color = (0.2, 0.7, 0.3, 1)
        self.status.text = "🔴 DISCONNECTED"
        self.progress.value = 0
        self.stats_label.text = "Data: 0 MB\nSpeed: 0 Mbps"
    
    def connection_process(self):
        for i in range(101):
            if not self.is_connected:
                return
            Clock.schedule_once(lambda dt, x=i: self.update_progress(x))
            time.sleep(0.02)
        
        if self.is_connected:
            Clock.schedule_once(lambda dt: self.connection_success())
            Clock.schedule_interval(self.update_data_usage, 2)
    
    def update_progress(self, value):
        self.progress.value = value
        self.status.text = f"🟡 CONNECTING... {value}%"
    
    def connection_success(self):
        self.status.text = "🟢 CONNECTED"
        self.stats_label.text = "Data: 0 MB\nSpeed: 25 Mbps"
    
    def update_data_usage(self, dt):
        if self.is_connected:
            self.data_used += 0.05
            speed = 25
            self.stats_label.text = f"Data: {self.data_used:.1f} MB\nSpeed: {speed} Mbps"

if __name__ == '__main__':
    WireTunVPN().run()
