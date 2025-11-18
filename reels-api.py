import instaloader

def download_instagram_video(url):
    # Initialize the Instaloader object
    L = instaloader.Instaloader()

    # Download the post
    try:
        post = instaloader.Post.from_shortcode(L.context, url.split('/')[-2])
    except Exception as e:
        print(f"Error: {e}")
        return

    # Check if the post contains a video
    if post.is_video:
        # Download the video
        L.download_post(post, target=post.owner_username)

        # Print success message
        print(f"Video downloaded successfully from {url}")

        # Print path to save it in case we need to find it later.
        print(f'The video is saved here: {L.context.save_metadata_filename()}')

    else:
        print("The provided URL does not contain a video.")

if __name__ == "__main__":
    # Example usage
    url = input("Enter the Instagram post URL: ")
    download_instagram_video(url)
