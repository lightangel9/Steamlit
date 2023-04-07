from apps.Predictions import Predictions
from apps.Dataset import Dataset
from apps.RefCode import RefCode

app = MultiApp()

# Add all your application here
app.add_app("Predictions", Predictions.app)
app.add_app("Dataset", Dataset.app)
app.add_app("RefCode", RefCode.app)
app.run()
