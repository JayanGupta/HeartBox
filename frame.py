import cv2


def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        

        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        
        frame_count += 1
    
    cap.release()


def process_video(video_path):
   
    output_folder = "frames"
    os.makedirs(output_folder, exist_ok=True)
    

    extract_frames(video_path, output_folder)
    

    for filename in os.listdir(output_folder):
        frame_path = os.path.join(output_folder, filename)
        predicted_class = predict_ecg_class(frame_path)
        print(f"Frame {filename}: Predicted class: {predicted_class}")
    
    


video_path = "path/to/video.mp4"
process_video(video_path)