import json
import numpy as np
import onnxruntime as ort
import cv2

# Load the LaTeX symbol mappings from keys.json
with open("keys.json", "r", encoding="utf-8") as f:
    latex_map = json.load(f)

# Convert keys to integers for proper indexing
latex_map = {int(k): v for k, v in latex_map.items()}

# Load the ONNX model
session = ort.InferenceSession("model.onnx")

def preprocess_image(image_path):
    """ Preprocess the image for model input. """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (128, 32))  # Resize to model input shape
    image = image.astype(np.float32) / 255.0  # Normalize
    image = np.expand_dims(image, axis=(0, 1))  # Add batch & channel dimensions
    return image

def predict_math_expression(image_path):
    """ Run inference and convert model output to LaTeX expression. """
    image = preprocess_image(image_path)
    
    # Run inference
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    raw_output = session.run([output_name], {input_name: image})[0]
    
    # Get predicted indices
    predicted_indices = np.argmax(raw_output, axis=-1).flatten()

    # Map indices to LaTeX symbols
    predicted_latex = ''.join([latex_map.get(idx, '?') for idx in predicted_indices if idx in latex_map])

    return predicted_latex

if __name__ == "__main__":
    image_path = "captured_equation.jpg"
    latex_expression = predict_math_expression(image_path)
    print(f"Predicted LaTeX Expression:\n{latex_expression}")
