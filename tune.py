from ultralytics import YOLO

# Initialize the YOLO model
model = YOLO("yolo11n.pt")

# Define search space
search_space = {
    "lr0": (1e-5, 1e-1),
    "lrf": (0.01, 1.0)
}

# Tune hyperparameters on COCO8 for 30 epochs
model.tune(
    data= "data.yaml",
    epochs=100,
    iterations=25,
    space=search_space,
)
