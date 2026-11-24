from abc import ABC, abstractmethod
 
class Observer(ABC):
    @abstractmethod
    def update(self, event): ...
class Subject:
    def __init__(self):
        self._observers = []
 
    def attach(self, observer):
        self._observers.append(observer)
 
    def detach(self, observer):
        self._observers.remove(observer)
 
    def notify(self):
        for o in self._observers:
            o.update(self)
            
class Event(Subject):
    """ConcreteSubject: holds the state."""
    def __init__(self, title, status="scheduled"):
        super().__init__()
        self.title = title
        self._status = status        # subjectState
 
    def get_state(self):
        return self._status
 
    def set_status(self, new_status):
        self._status = new_status
        self.notify()   # state changed: tell everyone
class EmailObserver(Observer):
    def update(self, event):
        print("[email]", event.title,
              "is now", event.get_state())
 
class DashboardObserver(Observer):
    def update(self, event):
        print("[dashboard]", event.title,
              event.get_state().upper())
class PushObserver(Observer):
    def update(self, event):
        print("[push]", event.title,
              event.get_state())

 
hackathon = Event("CSE Club Hackathon")
hackathon.attach(EmailObserver())
hackathon.attach(DashboardObserver())
hackathon.set_status("cancelled")
hackathon.attach(PushObserver())
hackathon.set_status("moved to Hall B")

