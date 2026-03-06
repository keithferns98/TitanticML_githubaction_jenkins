from pydantic import BaseModel


class TitanicRequest(BaseModel):
    name: str
    pclass: int
    sex: str
    age: float
    sibsp: int
    parch: int
    fare: float
    embarked: str

    def to_model_input(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Embarked": self.embarked,
            "Fare": self.fare,
            "Parch": self.parch,
            "Pclass": self.pclass,
            "Sex": self.sex,
            "SibSp": self.sibsp,
        }
