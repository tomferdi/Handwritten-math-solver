import cv2
import math_recognition

def capture_from_webcam():
    cap = cv2.VideoCapture(0)
    print("Press 's' to capture an image. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break

        cv2.imshow("Webcam", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):  # Capture image
            image_path = "captured_equation.jpg"
            cv2.imwrite(image_path, frame)
            print("Image saved as captured_equation.jpg")
            cap.release()
            cv2.destroyAllWindows()
            
            # Predict equation from selected region
            latex_expr = math_recognition.predict_math_expression(image_path)
            if latex_expr:
                print("\nPredicted LaTeX Expression:\n", latex_expr)
            return

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    print("Select Input Type:")
    print("1. PDF File")
    print("2. Webcam Capture")
    choice = input("Enter choice (1 or 2): ")

    if choice == "2":
        capture_from_webcam()
    else:
        print("PDF processing not implemented yet.")

if __name__ == "__main__":
    main()
