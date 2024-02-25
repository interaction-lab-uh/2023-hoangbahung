import cv2

def extract_frames(input_video_path, output_folder):
    # Open the video file
    video_capture = cv2.VideoCapture(input_video_path)

    # Check if the video file is opened successfully
    if not video_capture.isOpened():
        print("Error: Unable to open the video file.")
        return

    frame_count = 0

    # Loop through the video frames
    while True:
        # Read the next frame from the video
        ret, frame = video_capture.read()

        # If the frame is not read successfully, it means we reached the end of the video
        if not ret:
            break

        # Save the frame to the output folder
        frame_count += 1
        output_path = f"{output_folder}/frame_{frame_count:04d}.jpg"
        cv2.imwrite(output_path, frame)

    # Release the video capture object and close the video file
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 'input_video_path' with the path to your video file.
    # Replace 'output_folder' with the folder where you want to save the frames.
    input_video_path = "./ant_video/panic.mov"
    output_folder = "./frame_2"

    
    extract_frames(input_video_path, output_folder)
