import os
import imageio

def create_video(image_folder, video_name, fps=24):
    images = []
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            file_path = os.path.join(image_folder, filename)
            images.append(imageio.imread(file_path))

    with imageio.get_writer(video_name, fps=fps) as writer:
        for image in images:
            writer.append_data(image)

if __name__ == "__main__":
    # Set the path to your image folder and the desired video name
    image_folder_path = "D:\dent_detection\Dhristi\dent detection\depth_array_output_cropped_images"
    output_video_name = "depth_array_output_cropped_images_output_video.mp4"
    # Call the function to create the video
    create_video(image_folder_path, output_video_name)

    print(f"Video '{output_video_name}' created successfully.")


