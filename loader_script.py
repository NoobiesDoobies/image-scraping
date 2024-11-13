
import instaloader.instaloader as instaloader



loader = instaloader.Instaloader(
    download_videos=False,
    download_comments=False,
    download_geotags=False,
    download_video_thumbnails=False,
    save_metadata=False,

)

loader.login('carlios.e', 'n$bHZsHZjdQ!1_p')

print(f"Logged in as: {loader.test_login()}")



loader.download_hashtag('food', max_count=5, profile_pic=False)
