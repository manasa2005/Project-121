import cv2
import numpy as np

def main():
    # Start video capture
    cap = cv2.VideoCapture(0)  # Change to 1 if using an external webcam

    # Read the image to be shown when the black object gets masked
    image = cv2.imread("path_to_image.jpg")  

    # Resize the image to 640x480
    image = cv2.resize(image, (640, 480))

    # Create arrays for lower and upper bounds of black color
    l_black = np.array([0, 0, 0], dtype=np.uint8)
    u_black = np.array([50, 50, 50], dtype=np.uint8)

    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()

        # Resize the frame to 640x480
        frame = cv2.resize(frame, (640, 480))

        # Create a mask using inRange() function
        mask = cv2.inRange(frame, l_black, u_black)

        # Use np.where() to create the masked image
        masked_image = np.where(mask == 0, frame, image)

        # Show the real video and masked video
        cv2.imshow("Real Video", frame)
        cv2.imshow("Masked Video", masked_image)

        # Break the loop if the user presses "Esc" or "Q"
        if cv2.waitKey(1) & 0xFF in (27, ord('q')):
            break

    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
