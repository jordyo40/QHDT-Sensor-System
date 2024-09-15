<<<<<<< HEAD
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="config.yaml", epochs=1)  # train the model
=======
from Website.__init__ import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 11940536b3a7be12396edcc3975a52a5726f0c32
