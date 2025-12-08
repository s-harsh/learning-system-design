"""
Day 9: Observer Pattern Demo
Scenario: YouTube Channel Subscription System.
Multiple users subscribe to a channel and get notified when a new video is uploaded.
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. Observer Interface (The Subscriber)
# ==========================================
class Observer(ABC):
    @abstractmethod
    def update(self, channel_name: str, video_title: str):
        pass

# ==========================================
# 2. Concrete Observers (The Users)
# ==========================================
class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, channel_name: str, video_title: str):
        print(f"🔔 Hey {self.name}, {channel_name} just uploaded: '{video_title}'")

class AnalyticsTracker(Observer):
    def update(self, channel_name: str, video_title: str):
        print(f"📈 [Analytics]: Logging upload event for {channel_name} -> {video_title}")

# ==========================================
# 3. The Subject (The YouTuber)
# ==========================================
class YouTubeChannel:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self._subscribers = []  # List of Observers
        self.videos = []

    def subscribe(self, observer: Observer):
        print(f"➕ {getattr(observer, 'name', 'System')} subscribed to {self.channel_name}.")
        self._subscribers.append(observer)

    def unsubscribe(self, observer: Observer):
        print(f"➖ {getattr(observer, 'name', 'System')} unsubscribed.")
        self._subscribers.remove(observer)

    def upload_video(self, video_title):
        print(f"\n🎥 Uploading '{video_title}'...")
        self.videos.append(video_title)
        self.notify_subscribers(video_title)

    def notify_subscribers(self, video_title):
        print("--- Notifying Subscribers ---")
        for sub in self._subscribers:
            sub.update(self.channel_name, video_title)
        print("-----------------------------")

# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("--- Observer Pattern Demo: YouTube ---\n")

    # 1. Create Channel
    tech_channel = YouTubeChannel("Tech Explainers")

    # 2. Create Users
    alice = Subscriber("Alice")
    bob = Subscriber("Bob")
    analytics = AnalyticsTracker()

    # 3. Subscribe
    tech_channel.subscribe(alice)
    tech_channel.subscribe(bob)
    tech_channel.subscribe(analytics)

    # 4. Action: Upload Video
    tech_channel.upload_video("Observer Pattern Design Deep Dive")

    # 5. One user leaves
    tech_channel.unsubscribe(bob)

    # 6. Action: Another Upload
    tech_channel.upload_video("Strategy Pattern in 5 Minutes")
