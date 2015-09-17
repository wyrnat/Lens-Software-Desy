'''
Created on 02.07.2015

@author: Woehnert
'''

class Observable(object):
    '''
    An Observable informs its Observer about changes.
    '''


    def __init__(self):
        """
        Initialize the class parameter 'observer'
        """
        self.observer = None
    
    def registerObserver(self, observer):
        """
        let the observer set himself
        @param observer: An Object which desire to observe the Observable
        """
        self.observer = observer
        
    def informObserver(self, reason):
        """
        calls an observer specified method and transmit the reason
        @param reason: Information contributed to the Observer
        """
        if self.observer != None:
            self.observer.observableChanged(reason)
        