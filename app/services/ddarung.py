from app.models.ddarung import DDarung
import pandas as pd

class DDarungService:
    
    ddarung = DDarung()
    
    def preprocess(self, path, train, test) -> object:
        model = self.ddarung
        this = model.context
        this.train = model.from_csv(path, train)
        this.test = model.from_csv(path, test)
    
    def submit(self, path, train, test):
        this = self.preprocess(path, train, test)
        count  = 0
        pd.Dataframe({'id': this.id, 'count':count})
        